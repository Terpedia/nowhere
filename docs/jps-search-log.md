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
| Citation chasing | References and cited-by links from the retained primary/review papers | Historical toxicology, controlled human effects, and compound pharmacology | 10 external scientific papers |

## Eligibility rules

Retain a source if it directly addresses the 5-HT2A psychedelic mechanism, absinthe composition or historical toxicology, receptor pharmacology of an inventory constituent, or controlled human effects relevant to the classification question. Exclude unsourced web claims, compound-presence claims without analytical or pharmacological context, and endpoints that cannot distinguish psychedelic phenomenology from intoxication, delirium, seizure, or general CNS effects.

## Accounting boundary

The current bibliography contains 12 retained sources: two Terpedia artifacts and 10 external scientific papers. The project does not report a database-wide number of records screened, duplicate records, or per-paper exclusion counts because the Paperpile and citation-chasing stages were not executed as a registered systematic search. The 29-compound inventory, 19-target comparator panel, eight evidence-qualified interaction rows, and 684 structure-target coverage rows are separate entity-specific outputs, not sequential PRISMA stages.
