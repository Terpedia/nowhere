# JPS review search and evidence-selection log

## Review design

This is a critical review and evidence map, not a registered systematic review. The log records the reproducible discovery routes used for the current manuscript. Search and selection date: 2026-09-03. The Terpedia KB release and local snapshots are content-addressed in `data/gcp-kb-refresh-2026-09-03.json` and `data/reproducibility-manifest.json`.

## Discovery routes

| Route | Exact query or selection rule | Purpose | Retained output |
|---|---|---|---|
| Terpedia local preparation profile | `functional-flavors/absinthe.html` | Botanical context, listed constituents, historical and biological claims | 1 preparation profile |
| Terpedia local COA | `functional-flavors/absinthe-coa.html` | HS-SPME/GC–MS inventory and reported concentration/area values | 1 COA artifact; 27 source volatile rows |
| Terpedia GCP tabular search | `thujone`, `anethole`, `fenchone`, `linalool`; source `supernatural2` | Exact structures, stereochemistry, release and ingestion provenance | Selected Terpedia records preserved in the dated refresh JSON |
| Terpedia Paperpile export | Records relevant to `psychedelic`, `5-HT2A`, `psilocybin`, `absinthe`, `thujone`, `GABA-A`, `linalool`, and `anethole` | Comparator neurobiology and linked primary literature | Bibliography candidates |
| Citation chasing and authoritative background | References and cited-by links from the retained primary/review papers; peer-reviewed alcohol-neurobiology and GI physiology reviews; EMA assessment report | Historical toxicology, controlled human effects, compound pharmacology, ethanol pathways, human absinthe exposure context, and gut chemosensing | 10 external scientific papers plus two peer-reviewed physiology reviews and one authoritative assessment report |
| Historical/cultural primary source | Crowley, “Absinthe: The Green Goddess,” *The International* 12(2), 1918 | Establish the cultural myth and subjective vocabulary around absinthe | 1 historical essay; interpreted as cultural testimony, not pharmacological evidence |
| GI/TAS2R literature | `TAS2R`, bitter taste, appetite, digestion, gastric emptying, gut hormones, absinthin, alpha-thujone | Define the digestive/appetite mechanism and assess constituent-specific bitter-receptor pharmacology | Human TAS2R14 ligand evidence for alpha-thujone and TAS2R46 agonist evidence for absinthin retained; preparation-level exposure remains unresolved |

## Eligibility rules

Retain a source if it directly addresses the 5-HT2A psychedelic mechanism, absinthe composition or historical toxicology, receptor pharmacology of an inventory constituent, or controlled human effects relevant to the classification question. Exclude unsourced web claims, compound-presence claims without analytical or pharmacological context, and endpoints that cannot distinguish psychedelic phenomenology from intoxication, delirium, seizure, or general CNS effects.

## Accounting boundary

The current bibliography contains 18 retained sources: two Terpedia artifacts, 10 external scientific papers, two peer-reviewed physiology reviews, two TAS2R pharmacology papers, one historical essay, and one authoritative assessment report. The project does not report a database-wide number of records screened, duplicate records, or per-paper exclusion counts because the Paperpile and citation-chasing stages were not executed as a registered systematic search. The 29-compound inventory, 19-target comparator panel, 10 evidence-qualified interaction rows, and 684 structure-target coverage combinations are separate entity-specific outputs, not sequential PRISMA stages. The 684 combinations represent 36 resolved structure records crossed with 19 targets, not 684 independent biological observations.
