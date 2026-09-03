#!/usr/bin/env python3
"""Join resolved Terpedia structures to the SAIR structure parquet.

The parquet is intentionally queried in DuckDB rather than loaded into pandas.
Matching is performed with RDKit canonical isomeric SMILES, followed by a
non-isomeric comparison that records connectivity-only matches separately.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

try:
    import duckdb
    from rdkit import Chem
except ImportError:  # pragma: no cover - dependency is environment-specific
    duckdb = None
    Chem = None


def canonical(smiles: str, isomeric: bool) -> str | None:
    if Chem is None:
        raise SystemExit("join_sair_parquet.py requires duckdb and rdkit")
    molecule = Chem.MolFromSmiles(smiles or "")
    if molecule is None:
        return None
    return Chem.MolToSmiles(molecule, isomericSmiles=isomeric)


def read_targets(structures_path: Path, panel_path: Path) -> tuple[dict[str, dict[str, str]], set[str]]:
    structures: list[dict[str, str]] = []
    with structures_path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            smiles = row.get("smiles", "").strip()
            compound = row.get("inventory_compound", row.get("compound", "")).strip()
            if smiles and compound:
                structures.append({
                    "compound": compound,
                    "smiles": smiles,
                    "isomeric": canonical(smiles, True) or "",
                    "nonisomeric": canonical(smiles, False) or "",
                })

    targets: dict[str, dict[str, str]] = {}
    proteins: set[str] = set()
    with panel_path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            protein = row.get("terpedia_record", row.get("receptor_record_id", "")).strip()
            if not protein:
                continue
            proteins.add(protein)
            for structure in structures:
                target_key = protein + "\t" + structure["compound"] + "\t" + structure["smiles"]
                targets[target_key] = {"protein": protein, **structure}
    return targets, proteins


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--structures", type=Path, required=True)
    parser.add_argument("--panel", type=Path, required=True)
    parser.add_argument("--parquet", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if duckdb is None or Chem is None:
        raise SystemExit("join_sair_parquet.py requires duckdb and rdkit")

    targets, proteins = read_targets(args.structures, args.panel)
    if not targets:
        raise SystemExit("no usable target structures found")

    connection = duckdb.connect()
    try:
        columns = connection.execute(
            "DESCRIBE SELECT * FROM read_parquet(?)", [str(args.parquet)]
        ).fetchall()
        names = {row[0] for row in columns}
        required = {"protein", "SMILES"}
        missing = required - names
        if missing:
            raise SystemExit(f"SAIR parquet is missing columns: {sorted(missing)}")

        placeholders = ",".join("?" for _ in proteins)
        query = (
            "SELECT protein, SMILES FROM read_parquet(?) "
            f"WHERE protein IN ({placeholders}) AND SMILES IS NOT NULL"
        )
        rows = connection.execute(query, [str(args.parquet), *sorted(proteins)]).fetchall()
    finally:
        connection.close()

    matched_isomeric: defaultdict[str, list[str]] = defaultdict(list)
    matched_nonisomeric: defaultdict[str, list[str]] = defaultdict(list)
    candidate_rows = defaultdict(int)
    for protein, smiles in rows:
        key = str(protein)
        candidate_rows[key] += 1
        iso = canonical(str(smiles), True)
        noniso = canonical(str(smiles), False)
        if not iso or not noniso:
            continue
        for target_key, target in targets.items():
            if target["protein"] != key:
                continue
            if iso == target["isomeric"]:
                matched_isomeric[target_key].append(str(smiles))
            elif noniso == target["nonisomeric"]:
                matched_nonisomeric[target_key].append(str(smiles))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        fields = [
            "compound", "receptor_record_id", "target_smiles",
            "compatible_sair_rows", "isomeric_match_rows",
            "nonisomeric_match_rows", "join_status",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for target_key, target in sorted(targets.items()):
            iso_count = len(matched_isomeric[target_key])
            noniso_count = len(matched_nonisomeric[target_key])
            status = "isomeric_match" if iso_count else (
                "connectivity_only_match" if noniso_count else "no_match"
            )
            writer.writerow({
                "compound": target["compound"],
                "receptor_record_id": target["protein"],
                "target_smiles": target["smiles"],
                "compatible_sair_rows": candidate_rows[target["protein"]],
                "isomeric_match_rows": iso_count,
                "nonisomeric_match_rows": noniso_count,
                "join_status": status,
            })

    print(f"queried {len(rows)} SAIR rows for {len(proteins)} protein targets")
    print(f"wrote {len(targets)} compound-target join rows to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
