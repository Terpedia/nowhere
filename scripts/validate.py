#!/usr/bin/env python3
"""Small integrity check for the initial Absinthe research tables."""
import csv
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
panel = read("receptor-target-panel.csv")

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
assert {"alpha-thujone", "trans-anethole", "linalool"} <= {row["compound"] for row in interactome}
assert {"direct binding and functional electrophysiology", "no qualifying interaction located"} <= {
    row["evidence_class"] for row in interactome
}
assert {"HTR2A", "HTR3A", "GABRB2", "TRPA1", "CNR1"} <= {row["target"] for row in panel}
assert all(row["terpedia_record"].startswith("protein:") for row in panel)
print(f"validated {len(compounds)} compounds, {len(framework)} framework criteria, {len(identifiers)} identifiers, {len(panel)} receptor targets, and {len(interactome)} interaction edges")
