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

## Mixture-level modulation interpretation

Across the full 29-compound inventory, the evidence tiers are:

| Tier | Inventory members | What may be modulated | Boundary |
|---|---|---|---|
| Directly characterized | alpha-thujone, beta-thujone, trans-anethole | GABA-A inhibitory tone/excitability; TRPA1 sensory signaling | These are non-5-HT2A mechanisms; beta-thujone-specific potency and preparation-level effects remain incomplete |
| Preclinical candidate | linalool | GABA-A-relevant inhibitory tone | Direction, exact isomer, potency, metabolism, and CNS exposure remain unresolved |
| Unresolved comparator | fenchone, pinocamphone | Possible GABA-A-linked neurotoxicity | A comparator hypothesis is not an observed receptor interaction |
| No qualifying edge located | 20 volatile inventory entries, excluding the tiers above | Unknown | A no-join or literature gap is not evidence of biological inactivity |
| Unassessed nonvolatile fraction | absinthin, artabsin, rosmarinic acid | Unknown | These were listed in the Terpedia profile but were not resolved in the volatile receptor map |

The corresponding one-row-per-inventory-compound assignments are in `data/psychedelic-modulation-map.csv`. The map is intended to answer “what might modulate?” at the level justified by the evidence: thujones may alter inhibitory tone and arousal, trans-anethole may alter sensory signaling, and linalool may be an inhibitory-tone modifier. It does not support claims of additivity, synergy, brain exposure, or a classic psychedelic state. No inventory compound has a supported direct HTR2A edge; the alpha-thujone and trans-anethole HTR2A rows are unresolved target tests only.

## Limitations

SAIR name and exact-SMILES searches returned no rows for the tested absinthe compounds through the public tabular API, even though the broader Terpedia KB returned HTR2A and GABA receptor target records. The SandboxAQ `sair.parquet` contains 8,803,710 rows and was queried with DuckDB over authenticated HTTP ranges. The content-addressed Terpedia interaction projection contains 1,489 rows, 397 protein IDs, and 907 unique structures. RDKit canonicalization across 36 unique compound-SMILES records representing all 29 inventory compounds yielded zero isomeric or non-isomeric matches in the projection. The full parquet query, using an explicit Terpedia-to-UniProt protein crosswalk, scanned 136,025 rows for 19 human targets and yielded 684 compound-target rows with zero matches. The trans-sabinyl acetate SMILES is explicitly a supplemental crosswalk keyed to a Terpedia systematic name because the native EssoilDB row has no structure field. This remains a release-level join result because gamma-himachalene still lacks sample-specific stereoisomer assignment and SAIR may contain a different structure representation or missing compound. Direct BigQuery querying remains unavailable to the current account. Therefore, the network is a transparent first release: it includes literature-supported edges and records the SAIR join result rather than treating missing annotation as biological absence. Results are in `data/sair-expanded-join-summary.csv`, `data/sair-19-target-parquet-join.csv`, and `data/terpedia-resolved-structure-records.csv`; retrieval and schema metadata are in `data/sair-release-metadata.json`.

## Next analysis

Obtain the SAIR interaction CSV or a read-only BigQuery role, canonicalize all exact GCP SMILES, join by structure, and append assay endpoint, potency, units, protein ID, source release, manifest URI, and hash. Rank edges only after separating direct assays from docking and target-prediction records. Then compare estimated human plasma or brain exposure with assay concentrations.
