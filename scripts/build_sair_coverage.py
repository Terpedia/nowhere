#!/usr/bin/env python3
"""Build an explicit compound-by-human-target SAIR coverage matrix."""

import argparse
import csv
from pathlib import Path

try:
    from rdkit import Chem
except ImportError:  # pragma: no cover - dependency is environment-specific
    Chem = None


def canonical(smiles, isomeric=True):
    if Chem is None:
        raise SystemExit("build_sair_coverage.py requires rdkit")
    molecule = Chem.MolFromSmiles(smiles or "")
    return Chem.MolToSmiles(molecule, canonical=True, isomericSmiles=isomeric) if molecule else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--structures", type=Path, required=True)
    parser.add_argument("--panel", type=Path, required=True)
    parser.add_argument("--crosswalk", type=Path, default=Path(__file__).parents[1] / "data" / "sair-protein-crosswalk.csv")
    parser.add_argument("--interactions", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if Chem is None:
        raise SystemExit("build_sair_coverage.py requires rdkit")

    with args.structures.open(newline="") as handle:
        structures = []
        seen_structures = set()
        for row in csv.DictReader(handle):
            key = (row.get("inventory_compound", row.get("compound", "")), row.get("smiles", ""))
            if key not in seen_structures:
                seen_structures.add(key)
                structures.append(row)
    with args.panel.open(newline="") as handle:
        panel = list(csv.DictReader(handle))
    with args.crosswalk.open(newline="") as handle:
        crosswalk = {row["target"]: row["sair_protein_id"] for row in csv.DictReader(handle)}
    with args.interactions.open(newline="") as handle:
        interactions = list(csv.DictReader(handle))

    indexed = {}
    for row in interactions:
        iso = canonical(row.get("SMILES"), True)
        noniso = canonical(row.get("SMILES"), False)
        if iso:
            indexed.setdefault((row.get("protein", ""), iso), []).append(row)
        if noniso:
            indexed.setdefault((row.get("protein", ""), noniso, "noniso"), []).append(row)

    fields = [
        "compound", "structure_identifier", "compound_smiles", "target",
        "receptor_record_id", "sair_protein_id", "system", "target_source_release",
        "sair_interaction_rows_scanned", "isomeric_match_count",
        "nonisomeric_match_count", "join_status", "interpretation",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for structure in structures:
            compound = structure.get("inventory_compound") or structure.get("compound", "")
            identifier = structure.get("terpedia_id") or structure.get("structure_identifier", "")
            smiles = structure.get("smiles", "")
            iso = canonical(smiles, True)
            noniso = canonical(smiles, False)
            for target in panel:
                terp_protein = target.get("terpedia_record") or target.get("receptor_record_id", "")
                protein = crosswalk.get(target.get("target", ""), "")
                exact = indexed.get((protein, iso), [])
                connectivity = [
                    row for row in indexed.get((protein, noniso, "noniso"), [])
                    if canonical(row.get("SMILES"), True) != iso
                ]
                status = "isomeric_match" if exact else "connectivity_only_match" if connectivity else "no_join_found"
                writer.writerow({
                    "compound": compound,
                    "structure_identifier": identifier,
                    "compound_smiles": smiles,
                    "target": target.get("target", ""),
                    "receptor_record_id": terp_protein,
                    "sair_protein_id": protein,
                    "system": target.get("system", ""),
                    "target_source_release": target.get("source_release", ""),
                    "sair_interaction_rows_scanned": len(interactions),
                    "isomeric_match_count": len(exact),
                    "nonisomeric_match_count": len(connectivity),
                    "join_status": status,
                    "interpretation": "Inspect SAIR assay fields before biological interpretation" if exact or connectivity else "No structure join in supplied SAIR projection; not biological absence",
                })
    print(f"wrote {len(structures) * len(panel)} compound-target rows to {args.output}")


if __name__ == "__main__":
    main()
