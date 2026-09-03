#!/usr/bin/env python3
"""Join exact absinthe structures to a SAIR protein/SMILES CSV.

Requires RDKit. A no_match row means that the supplied SAIR release contained
no canonical structure match; it is not a biological negative.
"""
import argparse
import csv

from rdkit import Chem


def canonical(smiles, isomeric=True):
    molecule = Chem.MolFromSmiles(smiles or "")
    if molecule is None:
        return None
    return Chem.MolToSmiles(molecule, canonical=True, isomericSmiles=isomeric)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--targets", required=True, help="CSV with compound, structure_identifier, and smiles")
    parser.add_argument("--interactions", required=True, help="SAIR CSV with protein and SMILES columns")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    with open(args.targets, newline="") as handle:
        targets = list(csv.DictReader(handle))
    with open(args.interactions, newline="") as handle:
        interactions = list(csv.DictReader(handle))

    output = []
    for target in targets:
        target_iso = canonical(target["smiles"], True)
        target_noniso = canonical(target["smiles"], False)
        iso_matches = []
        noniso_matches = []
        for interaction in interactions:
            interaction_iso = canonical(interaction.get("SMILES"), True)
            interaction_noniso = canonical(interaction.get("SMILES"), False)
            if interaction_iso == target_iso:
                iso_matches.append(interaction)
            if interaction_noniso == target_noniso:
                noniso_matches.append(interaction)

        output.append({
            "compound": target["compound"],
            "structure_identifier": target["structure_identifier"],
            "smiles": target["smiles"],
            "canonical_smiles": target_iso,
            "interaction_rows_scanned": len(interactions),
            "isomeric_match_count": len(iso_matches),
            "nonisomeric_match_count": len(noniso_matches),
            "matched_proteins": ";".join(sorted({row.get("protein", "") for row in iso_matches if row.get("protein")})),
            "join_status": "matched" if iso_matches else "no_match",
            "interpretation": "Structure match only; inspect assay fields before biological interpretation" if iso_matches else "No canonical structure match in supplied SAIR release; not biological absence",
        })

    fields = list(output[0]) if output else ["compound", "join_status"]
    with open(args.output, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)


if __name__ == "__main__":
    main()
