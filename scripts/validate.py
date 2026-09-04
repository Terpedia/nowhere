#!/usr/bin/env python3
"""Small integrity check for the initial Absinthe research tables."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    with (ROOT / "data" / name).open(newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        for row_number, row in enumerate(rows, start=2):
            assert len(row) == len(reader.fieldnames), f"malformed CSV row {row_number}"
        return rows

compounds = read("absinthe-compounds.csv")
framework = read("psychedelic-framework.csv")
identifiers = read("terpedia-identifiers.csv")
interactome = read("receptor-interactome.csv")
modulation_map = read("psychedelic-modulation-map.csv")
panel = read("receptor-target-panel.csv")
expanded_panel = read("human-neural-receptor-panel.csv")
resolved_structures = read("terpedia-resolved-structure-records.csv")
identity_audit = read("terpedia-identity-audit.csv")
unresolved_aliases = read("terpedia-unresolved-aliases.csv")
expanded_join = read("sair-expanded-join-summary.csv")
crosswalk = read("sair-protein-crosswalk.csv")
full_panel_join = read("sair-19-target-parquet-join.csv")
projection_coverage = read("sair-human-panel-coverage.csv")
panel_evidence = read("sair-human-panel-evidence-summary.csv")
source_evidence = read("source-level-evidence.csv")
manifest = json.loads((ROOT / "data" / "reproducibility-manifest.json").read_text())
notebook = json.loads((ROOT / "notebooks" / "absinthe_terpedia_analysis.ipynb").read_text())

for relative_path, expected_sha256 in manifest["sha256"].items():
    actual_sha256 = hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()
    assert actual_sha256 == expected_sha256, f"manifest hash mismatch: {relative_path}"

assert len(compounds) >= 20, "compound inventory unexpectedly short"
assert len({row["compound"] for row in compounds}) == len(compounds), "duplicate compound"
for row in compounds:
    assert row["compound"] and row["terpedia_observation"] and row["status"]
    if row["reported_area_pct"] and row["reported_area_pct"] != "trace":
        assert float(row["reported_area_pct"]) >= 0
assert {"primary target", "brain exposure", "phenomenology", "classification"} <= {
    row["criterion"] for row in framework
}
assert {"thujone", "limonene", "linalool"} <= {row["terpedia_label"] for row in identifiers}
assert {"alpha-thujone", "trans-anethole", "linalool", "absinthin"} <= {row["compound"] for row in interactome}
assert len(modulation_map) == len(compounds)
assert {row["compound"] for row in modulation_map} == {row["compound"] for row in compounds}
assert {row["modulation_level"] for row in modulation_map} <= {
    "directly characterized", "isomer-qualified", "preclinical candidate", "unresolved", "unestablished", "unassessed"
}
assert {row["evidence_status"] for row in modulation_map} >= {
    "supported for GABA-A and TAS2R14; HTR2A unestablished", "supported for TRPA1; HTR2A unestablished",
    "supported for TAS2R46; HTR2A unestablished", "candidate", "unresolved", "unassessed"
}
assert sum(row["modulation_level"] == "directly characterized" for row in modulation_map) == 3
assert sum(row["modulation_level"] == "isomer-qualified" for row in modulation_map) == 1
assert sum(row["modulation_level"] == "unassessed" for row in modulation_map) == 2
assert {"direct binding and functional electrophysiology", "no qualifying interaction located"} <= {
    row["evidence_class"] for row in interactome
}
assert all(row["reported_concentration_mg_L"] for row in interactome)
assert all(row["target_resolution"] for row in interactome)
assert any(row["receptor_record_id"] == "protein:CDBP04867" for row in interactome)
assert {"HTR2A", "HTR3A", "GABRB2", "TRPA1", "CNR1"} <= {row["target"] for row in panel}
assert all(row["terpedia_record"].startswith("protein:") for row in panel)
assert len(expanded_panel) >= 15
assert all(row["terpedia_record"].startswith("protein:") for row in expanded_panel)
assert len(resolved_structures) >= 15
assert all(
    (row["terpedia_id"].startswith("SN") or row["terpedia_id"].startswith("CDB") or row["terpedia_id"].startswith("JEA"))
    and row["inchi_key"] and row["smiles"]
    for row in resolved_structures
)
assert all(
    row["source_object_uri"].endswith("supernatural2/full_data_download.csv")
    or row["source_object_uri"].startswith("https://cannabisdatabase.ca/compounds/")
    or row["source_object_uri"].endswith("essoildb/v1.0/info_c.tsv")
    for row in resolved_structures
)
assert len(identity_audit) == len(compounds)
assert {row["inventory_compound"] for row in identity_audit} == {row["compound"] for row in compounds}
assert any(row["identity_status"] == "stereoisomer family matched" for row in identity_audit)
assert len(unresolved_aliases) == 2
assert all(row["terpedia_record"] for row in unresolved_aliases)
assert all(row["structure_available"] == "yes" for row in unresolved_aliases)
assert len(expanded_join) == 27
assert all(row["join_status"] == "no_match" for row in expanded_join)
assert all(row["interaction_rows_scanned"] == "1489" for row in expanded_join)
assert len(crosswalk) == len(expanded_panel)
assert {row["target"] for row in crosswalk} == {row["target"] for row in expanded_panel}
assert all(row["sair_protein_id"] and row["organism"] == "Homo sapiens" for row in crosswalk)
assert len(full_panel_join) == 684
assert len({row["compound"] for row in full_panel_join}) == 29
assert len({row["target"] for row in full_panel_join}) == 19
assert all(row["join_status"] == "no_match" for row in full_panel_join)
assert all(row["sair_protein_id"] for row in full_panel_join)
assert len(projection_coverage) == 684
assert len({row["compound"] for row in projection_coverage}) == 29
assert len({row["target"] for row in projection_coverage}) == 19
assert all(row["join_status"] == "no_join_found" for row in projection_coverage)
assert all(row["sair_protein_id"] for row in projection_coverage)
assert len(panel_evidence) == 19
assert {row["target"] for row in panel_evidence} == {row["target"] for row in expanded_panel}
assert all(row["source_object"] == "gs://sandboxaq-sair/sair.parquet" for row in panel_evidence)
assert sum(int(row["parquet_rows"]) for row in panel_evidence) == 136025
assert len(source_evidence) == 18
assert {row["source_id"] for row in source_evidence} == {"T1", "T2", "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10", "A1", "H1", "A2", "G1", "G2", "G3"}
assert all(row["source"] and row["principal_result"] and row["primary_limitation"] for row in source_evidence)
assert manifest["release_date"] == "2026-09-03"
assert len(manifest["sha256"]) == 13
assert notebook["nbformat"] == 4
assert len(notebook["cells"]) >= 10
assert sum(cell["cell_type"] == "code" for cell in notebook["cells"]) >= 5
assert any("Terpedia" in "".join(cell.get("source", [])) for cell in notebook["cells"])
print(f"validated {len(compounds)} compounds, {len(framework)} framework criteria, {len(identifiers)} identifiers, {len(panel)} primary and {len(expanded_panel)} expanded receptor targets, and {len(interactome)} interaction edges")
