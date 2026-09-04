# Initial absinthe–human terpene receptor interactome

## Scope

This is an evidence-qualified network, not a target-fishing result. Nodes are exact or explicitly unresolved absinthe compounds and human neural or sensory-neural receptor systems. Edges preserve whether the source reports direct binding, functional activity, a preclinical modulation result, or only an unresolved hypothesis.

## Current network

```mermaid
graph LR
  AT[alpha-thujone] -->|direct binding + electrophysiology; GABA-A blockade| GABA[GABA-A receptor complex]
  BT[beta-thujone] -->|direct binding; beta-specific potency unresolved| GABA
  TA[trans-anethole] -->|functional agonism; TRPA1 assay| TRPA1[TRPA1]
  LI[linalool] -->|preclinical GABA-A-relevant modulation| GABA
  AT -.->|5-HT2A edge unestablished| HTR2A[HTR2A / 5-HT2A]
  TA -.->|5-HT2A edge unestablished| HTR2A
  FE[fenchone] -.->|receptor edge unresolved| GABA
  PC[pinocamphone] -.->|receptor edge unresolved| GABA
```

## Interpretation

The network contains two materially different biological stories. Thujones have direct evidence for GABA-A channel modulation and toxicological excitation, while trans-anethole has direct evidence at the sensory-neural TRPA1 receptor. Linalool has preclinical GABA-A-relevant literature but requires exact-isomer and concentration reconciliation. None of these edges establishes classic psychedelic pharmacology. The HTR2A dashed edges are unresolved tests, not negative assay results.

## Limitations

SAIR name and exact-SMILES searches returned no rows for the tested absinthe compounds through the public tabular API, even though the broader Terpedia KB returned HTR2A and GABA receptor target records. The SandboxAQ `sair.parquet` contains 8,803,710 rows and was queried with DuckDB over authenticated HTTP ranges. The content-addressed Terpedia interaction projection contains 1,489 rows, 397 protein IDs, and 907 unique structures. RDKit canonicalization across 35 unique compound-SMILES records representing 28 inventory compounds yielded zero isomeric or non-isomeric matches in the projection. The full parquet query, using an explicit Terpedia-to-UniProt protein crosswalk, scanned 136,025 rows for 19 human targets and yielded 665 compound-target rows with zero matches. This remains a release-level join result because one inventory name still lacks a uniquely adjudicated Terpedia structure and SAIR may contain a different structure representation or missing compound. Direct BigQuery querying remains unavailable to the current account. Therefore, the network is a transparent first release: it includes literature-supported edges and records the SAIR join result rather than treating missing annotation as biological absence. Results are in `data/sair-expanded-join-summary.csv`, `data/sair-19-target-parquet-join.csv`, and `data/terpedia-resolved-structure-records.csv`; retrieval and schema metadata are in `data/sair-release-metadata.json`.

## Next analysis

Obtain the SAIR interaction CSV or a read-only BigQuery role, canonicalize all exact GCP SMILES, join by structure, and append assay endpoint, potency, units, protein ID, source release, manifest URI, and hash. Rank edges only after separating direct assays from docking and target-prediction records. Then compare estimated human plasma or brain exposure with assay concentrations.
