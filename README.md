# Is Terpedia's absinthe psychedelic?

Working repository for a journal paper on whether absinthe should be described as a psychedelic, using Terpedia's compound, analytical, and biomedical records.

## Working position

The project does not assume that absinthe is psychedelic. It will test the claim against an operational framework derived from psychedelic neurobiology and against the compounds Terpedia associates with absinthe. The main alternatives are classic serotonergic activity; ethanol and non-5-HT2A CNS effects; expectation, dose, and preparation effects; and a psychoactive mixture that does not meet a psychedelic definition.

## Repository map

- `manuscript/outline.md` — paper question, hypotheses, methods, and planned sections.
- `data/absinthe-compounds.csv` — compound inventory transcribed from Terpedia's absinthe COA and botanical attribution page.
- `data/psychedelic-framework.csv` — operational criteria and comparator molecules for the literature review.
- `docs/evidence-boundaries.md` — evidence taxonomy and rules for separating observation from inference.
- `docs/receptor-interaction-protocol.md` — structure-first workflow for mapping absinthe terpenes to neural receptors.
- `data/receptor-target-panel.csv` — initial prespecified receptor panel.
- `scripts/validate.py` — lightweight integrity checks for the data tables.

## Terpedia source artifacts

- `../functional-flavors/absinthe.html` — botanical/compound profile and biological-interaction claims.
- `../functional-flavors/absinthe-coa.html` — repository COA record for a Swiss-style absinthe verte; HS-SPME/GC-MS description, marker attribution, and reported concentrations.
- `../terport/Paperpile - References - Nov 2.csv` — Terpedia reference export, including psychedelic neurobiology and human psilocybin/5-HT2A occupancy records.
- `../kb/` — biochemical knowledge-base implementation and Terport integration notes.

## Provenance note

The COA is a Terpedia artifact, not a newly generated measurement for this paper. Its values are treated as repository-reported analytical observations pending raw chromatograms, standards, calibration data, sample identity, and independent replication. A graph edge, compound page, or name match is not evidence of psychedelic activity.

## First local check

```bash
python3 scripts/validate.py
```
