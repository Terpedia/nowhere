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

assert len(compounds) >= 20, "compound inventory unexpectedly short"
assert len({row["compound"] for row in compounds}) == len(compounds), "duplicate compound"
for row in compounds:
    assert row["compound"] and row["terpedia_observation"] and row["status"]
    if row["reported_area_pct"] and row["reported_area_pct"] != "trace":
        assert float(row["reported_area_pct"]) >= 0
assert {"primary target", "brain exposure", "phenomenology", "classification"} <= {
    row["criterion"] for row in framework
}
print(f"validated {len(compounds)} compounds and {len(framework)} framework criteria")
