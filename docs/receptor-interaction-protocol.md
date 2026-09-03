# Terpene–neural receptor interaction protocol

## Question

Which neural receptors are plausibly engaged by absinthe terpenes, and what kind of evidence supports each interaction?

## Terpedia route

The current source map identifies two SAIR BigQuery projections:

- `terpedia_raw.sair_structures` — structure-level records with protein, SMILES, assay, potency, pIC50, docking/structure fields, and provenance.
- `terpedia_raw.sair_protein_terpene_interactions` — protein/SMILES interaction aggregates.

The public tabular API's `sair` search currently exposes `sair_structures`. Name searches for thujone, anethole, fenchone, linalool, myrcene, and limonene returned zero rows. This is not evidence of no interaction: SAIR must be joined by canonicalized structure/SMILES or a stable molecular identifier.

## Required workflow

1. Resolve each absinthe molecule at isomer level using the GCP `supernatural2` records and retain InChIKey/SMILES.
2. Canonicalize the exact structure without merging stereoisomers.
3. Join the structure to SAIR by canonical SMILES or InChIKey where present.
4. Attach the receptor/protein identifier, assay type, potency/pIC50, source release, manifest URI, hash, and ingestion run.
5. Classify the result as direct functional assay, binding assay, curated interaction, docking/structure prediction, or unresolved.
6. Compare observed or predicted targets against a prespecified panel: HTR2A (5-HT2A), HTR3A (5-HT3A), GABA-A subunits, CNR1 (CB1), TRPA1, and other targets returned by the join.
7. Treat docking scores and target-fishing labels as hypothesis-generating only. They cannot establish affinity, agonism/antagonism, CNS exposure, or psychedelic phenomenology.

## Minimum evidence table

| Field | Why it is required |
|---|---|
| exact molecule | Prevents generic-name and stereoisomer errors |
| protein stable ID | Prevents target-name collisions |
| assay and endpoint | Distinguishes binding from functional activity |
| potency and units | Enables exposure comparison |
| preparation/route | Prevents neat-compound-to-beverage extrapolation |
| source release and manifest | Makes the result reproducible |
| evidence class | Prevents predictions from being presented as experiments |

## Current live-search result

Terpedia's unified search returned a `5-hydroxytryptamine receptor 2A` record (`protein:CDBP02043`) and GABA receptor records, including `protein:CDBP03419` (GABA-A beta-2), plus Cellosaurus assay-cell records for HTR2A. These are target and assay-resource records, not evidence that any absinthe terpene interacts with those receptors. The initial SAIR name searches and this distinction are recorded in the working session notes.

## SAIR retrieval checkpoint (2026-09-03)

The SandboxAQ release object `gs://sandboxaq-sair/sair.parquet` was retrieved and read with DuckDB. Its schema includes `protein`, `sequence`, `SMILES`, `srcSMILES`, `source`, `description`, `potency`, `assay`, `pIC50`, and docking/model-quality fields; the inspected object contains 8,803,710 rows. RDKit canonicalization of seven resolved absinthe structures across 18,145 chemically compatible candidate rows produced zero isomeric and zero non-isomeric matches. This does not establish biological absence: alternate structure representations, release coverage, and the Terpedia-promoted `protein_terpene_interactions.csv` projection still require checking. See `data/sair-canonical-join-results.csv` and `data/sair-release-metadata.json` for the reproducibility record.
