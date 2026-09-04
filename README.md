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
- `data/human-neural-receptor-panel.csv` — expanded 19-target Terpedia panel; the five-target file remains the narrow primary comparator set.
- `data/sair-protein-crosswalk.csv` — explicit Terpedia protein-record to UniProt accession crosswalk used for the SAIR parquet.
- `data/sair-19-target-parquet-join.csv` — complete 19-target parquet join result (646 compound-target rows).
- `data/sair-human-panel-coverage.csv` — namespace-correct 19-target interaction-projection coverage matrix (646 compound-target rows).
- `data/sair-human-panel-evidence-summary.csv` — SAIR assay/potency/pIC50/docking-field availability by human target.
- `data/receptor-interactome.csv` — initial evidence-qualified compound–receptor edges.
- `data/sair-release-metadata.json` — SAIR parquet retrieval, schema, row-count, and structure-join checkpoint.
- `data/sair-canonical-join-results.csv` — seven-target canonical and non-isomeric join results, including the 18,145-row compatible-candidate scan.
- `data/sair-expanded-join-summary.csv` — complete SAIR interaction-projection join summary for all resolved structure records.
- `data/terpedia-resolved-structure-records.csv` — exact structure records recovered from the full Terpedia SuperNatural II export; unresolved inventory names remain separate.
- `data/terpedia-identity-audit.csv` — full 29-compound identity audit, including source-label discrepancies and unresolved stereochemistry.
- `docs/identity-resolution.md` — identity-resolution rules and the boundary between supplemental lookup and Terpedia adjudication.
- `manuscript/receptor-interactome-report.md` — network visualization, interpretation, and limitations.
- `scripts/validate.py` — lightweight integrity checks for the data tables.
- `scripts/join_sair_interactions.py` — reproducible RDKit canonical-structure join against the Terpedia SAIR interaction CSV.
- `scripts/join_sair_parquet.py` — reproducible DuckDB/RDKit compound-by-panel join against the full SAIR structure parquet.
- `scripts/build_sair_coverage.py` — explicit compound-by-human-target coverage matrix for the SAIR interaction projection.

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
