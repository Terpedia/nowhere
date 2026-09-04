# Is absinthe psychedelic? A Terpedia evidence map of psychedelic biochemistry, absinthe chemistry, and competing mechanisms

**Working manuscript — 3 September 2026**

## Abstract

Absinthe is often described as a hallucinogenic or psychedelic drink, but the biochemical basis of that description has not been established. We evaluated the claim using Terpedia's evidence-oriented knowledge-base workflow. First, we defined a classic serotonergic psychedelic as a compound or preparation with centrally relevant 5-HT2A agonism or activation and reproducible alteration of perception, cognition, or self-experience at plausible human exposure. We then mapped the absinthe compounds recorded in Terpedia's Functional Flavors profile and repository GC–MS certificate of analysis against that framework, while separating volatile observations, nonvolatile botanical constituents, ethanol, receptor pharmacology, toxicology, and historical narrative. The inventory is dominated by trans-anethole in the repository COA, with fenchone and thujones as additional reported constituents. Direct evidence supports thujone as a concentration-dependent GABA-A channel antagonist/convulsant, not as a 5-HT2A psychedelic. Human psychedelic evidence for psilocybin provides a useful positive-control standard: plasma psilocin, cerebral 5-HT2A occupancy, and subjective intensity covary in controlled volunteers. On the current evidence, absinthe is psychoactive and potentially toxic, but it is not established as a classic psychedelic. A preparation-level psychedelic claim remains untested rather than disproved; the decisive next study is a chemically characterized, ethanol-matched, blinded experiment coupled to receptor, pharmacokinetic, and subjective-effect measurements.

**Keywords:** absinthe; thujone; 5-HT2A; GABA-A; psychedelic; ethanol; Terpedia; phytochemistry

## 1. Introduction

Absinthe is a distilled alcoholic beverage traditionally associated with grand wormwood (*Artemisia absinthium*), green anise (*Pimpinella anisum*), and Florence fennel (*Foeniculum vulgare*), with coloring botanicals such as petit wormwood, hyssop, and lemon balm. Its ritual, intense aroma, louche, and nineteenth-century cultural history generated a persistent claim that it produces effects qualitatively different from ordinary alcohol. Historical reports grouped euphoria, sharpened perception, hallucinations, insomnia, confusion, and convulsions under “absinthism.” Those reports are clinically and pharmacologically heterogeneous: hallucination, delirium, withdrawal, alcohol intoxication, adulterants, and seizure are not interchangeable endpoints.

The modern question is therefore narrower: does absinthe meet the biochemical and phenomenological meaning of a classic psychedelic? The answer cannot be inferred from a compound being natural, psychoactive, CNS-active, or associated with hallucinations. It requires identity-resolved exposure, a mechanism relevant to psychedelic phenomenology, and controlled human evidence.

## 2. Definitions and biochemical framework

Classic serotonergic psychedelics include psilocybin/psilocin, LSD, and mescaline. Across this class, agonism or partial agonism at cortical serotonin 5-HT2A receptors is the most reproducible mechanistic anchor, although receptor activation is necessary rather than sufficient for the full subjective state. 5-HT2A is a G-protein-coupled receptor expressed prominently on cortical pyramidal neurons. Activation can engage Gq/11-linked phospholipase C signaling, intracellular calcium mobilization, excitability changes, and downstream circuit effects. Other serotonin receptors, glutamatergic signaling, network dynamics, learning, expectation, and set and setting contribute to the final experience.

The appropriate evidence ladder is:

1. **Identity:** exact structure, stereochemistry, salt/protonation state, and preparation are resolved.
2. **Target pharmacology:** binding and functional assays show 5-HT2A activity, with concentration-response data and selectivity context.
3. **Brain exposure:** active parent or metabolite reaches the CNS at concentrations plausibly produced by the preparation.
4. **Phenomenology:** controlled human administration produces reproducible changes in perception, cognition, or self-experience.
5. **Causality:** an antagonist, comparator, or dose-response relationship supports the proposed mechanism.

Psilocybin illustrates the standard. In a controlled human PET study, oral psilocybin produced dose-related 5-HT2A occupancy through its active metabolite psilocin; plasma psilocin, occupancy, and subjective psychedelic intensity were closely associated. This is materially stronger than a molecule merely appearing in a plant or sharing a broad “psychoactive” label.

## 3. Terpedia-centered methods

### 3.1 Sources and entity handling

The primary project source is the Terpedia KB, documented as a GCP-backed biochemical system with ChEBI, PubChem, Rhea, natural-product, essential-oil, and literature datasets. The current Cloud Run API in project `terpedia-489015` was queried on 2026-09-03 using the documented Secret Manager key and tabular-search route. Searches in the `supernatural2` projection resolved stereochemical records for thujone, anethole, fenchone, and linalool; the returned release, ingestion run, manifest URI, source object, and SHA-256 are preserved in `data/gcp-kb-refresh-2026-09-03.json`. The local Terpedia source artifacts were used to establish the starting inventory: `functional-flavors/absinthe.html` and `functional-flavors/absinthe-coa.html`. Psychedelic comparator literature was located in Terpedia's Paperpile export and checked against primary or review articles.

Chemical records were kept separate when the source distinguishes stereoisomers or geometric isomers. The inventory also separates volatile COA observations from absinthin, artabsin, and rosmarinic acid, which the Terpedia profile lists but which are not represented in the volatile COA table.

### 3.2 Evidence coding

Each claim is coded as observed in a Terpedia artifact, directly characterized in a primary experiment, mechanistically supported, or unestablished. A GC–MS library match is chemical-identification evidence for the analyzed sample; it is not receptor or phenomenology evidence. A connected biochemical graph path is a testable hypothesis, not proof of in vivo production or human pharmacology.

### 3.3 Structure-first receptor interactome

We prespecified a five-target comparator panel (HTR2A, HTR3A, GABRB2, TRPA1, and CNR1) and expanded it to 19 Terpedia-linked human neural/CNS target records spanning serotonin, GABA-A, dopamine, opioid, cholinergic, cannabinoid, sensory-channel, glutamatergic, and transporter systems. Stable Terpedia protein record IDs, source releases, URLs, and content hashes are retained in the panel tables. The target panel is a comparator universe, not evidence of interaction.

Resolved Terpedia structures were joined to the recovered SAIR interaction projection by RDKit canonical isomeric SMILES, with a second non-isomeric check used to detect connectivity-only matches. The projection contains 1,489 rows, 397 protein IDs, and 907 unique structures. Thirty-four unique compound-SMILES records representing 27 inventory compounds were scanned; no isomeric or non-isomeric matches were found. The full SAIR parquet was then queried remotely for the 19-target human panel after mapping Terpedia protein records to UniProt accessions; 136,025 compatible protein rows yielded 646 compound-target rows and zero matches. These database results are reported as “no join found,” not as evidence of receptor inactivity. Literature-supported edges were retained separately in an evidence-qualified interactome, with direct binding/functional assay results distinguished from preclinical candidates and unresolved 5-HT2A tests. Reported beverage concentrations were attached as exposure context, never substituted for plasma or brain concentrations. Full procedures and source checks are in `docs/receptor-interaction-protocol.md`, `docs/identity-resolution.md`, and the `data/` tables.

## 4. Absinthe molecular inventory

The repository COA describes a Swiss-style absinthe verte analyzed by HS-SPME/GC–MS. It reports 27 identified volatile entries, 91.2% total identified area, and 8.8% unidentified peaks. The dominant reported constituent is trans-anethole at 72.4 area% and 868.8 mg/L. Fenchone is reported at 8.7 area% and 104.4 mg/L. Alpha- and beta-thujone are reported at 14.4 and 7.2 mg/L, respectively, for a combined 21.6 mg/L. These values are repository observations, not independent measurements generated for this study.

The high trans-anethole signal is consistent with the sensory and physical identity of anise-rich absinthe, including the louche. It does not imply psychedelic pharmacology. The thujones are chemically and toxicologically more relevant to the historical claim, but their presence likewise does not establish a psychedelic mechanism. Fenchone, pinocamphone, isopinocamphone, camphor, linalool, and other minor volatiles broaden the possible CNS pharmacology, while nonvolatile constituents may be extracted during coloring or remain absent from the distilled fraction. Finished-beverage composition can therefore vary with cultivar, chemotype, recipe, distillation, coloring, storage, and analytical method.

## 5. Candidate mechanisms

### 5.1 Thujones

The strongest direct mechanistic evidence in the absinthe literature concerns alpha-thujone and beta-thujone at the GABA-A receptor picrotoxin/convulsant site. The foundational PNAS work reported competitive inhibition of a radiolabeled convulsant ligand and reversible blockade of GABA-A chloride currents, with alpha-thujone more active than beta-thujone in the reported binding assay. The associated phenotype is reduced inhibitory neurotransmission and, at sufficiently high exposure, excitation and convulsions. This is a toxicological/analeptic mechanism, not evidence of 5-HT2A agonism.

Thujone is also rapidly metabolized in experimental systems, producing hydroxylated and dehydrogenated metabolites. Thus, even a positive in vitro result would require parent/metabolite exposure matching before it could explain a beverage-level effect. Modern toxicological assessments describe human dose uncertainty and emphasize dose-dependent neurotoxicity. A seizure or delirium pathway should not be relabeled psychedelic merely because historical accounts used the word hallucination.

### 5.2 Fenchone and pinocamphone

Terpedia's absinthe record associates fenchone with Florence fennel and pinocamphone/isopinocamphone with hyssop. These monoterpene ketones are reasonable safety and non-5-HT2A comparator targets because concentrated essential oils can be neuroactive and convulsant. However, the presence of a compound, or even evidence of toxicity at high concentration, does not satisfy the 5-HT2A, brain-exposure, and controlled-phenomenology criteria. These molecules deserve a receptor-panel and exposure study, not a psychedelic label.

### 5.3 Anetholes, linalool, and other volatiles

Trans-anethole is the dominant reported volatile in the repository COA. Terpedia's compound record emphasizes aroma, metabolism, and preclinical pharmacology rather than 5-HT2A agonism. Linalool has preclinical CNS and GABA-A-relevant literature, but that is not equivalent to a classic psychedelic mechanism. Estragole and methyleugenol raise toxicological questions; limonene, pinene, myrcene, cineole, aldehydes, and sesquiterpenes contribute to a chemically complex mixture. The correct conclusion for this group is not “inactive,” but “no established classic psychedelic evidence in the current Terpedia record.”

### 5.4 Ethanol and preparation context

Ethanol is not a minor confounder: it is the beverage matrix and produces dose-dependent intoxication, disinhibition, sedation, memory impairment, and, with chronic exposure or withdrawal, severe neuropsychiatric effects. Absinthe effects must therefore be compared with an ethanol-matched spirit and, ideally, a botanical-matched alcohol-free or de-aromatized control. The louche changes dispersion and sensory expectation, but a visible colloidal transition is not a pharmacological assay.

## 6. Historical claims and causal interpretation

Historical reviews conclude that nineteenth-century “absinthism” mixed chronic alcohol misuse with reports of seizures, hallucinations, and mental deterioration, and that wormwood oil is far more convulsant than properly manufactured absinthe. Later chemical analyses also challenged exaggerated assumptions about historical thujone concentrations. These reviews do not prove that no absinthe preparation can alter perception. They do show why historical anecdotes cannot identify a receptor mechanism or quantify dose.

One directly relevant human study did test absinthe-like drinks under matched alcohol conditions. Dettling and colleagues administered drinks containing identical alcohol amounts but 0, 10, or 100 mg/L thujone to 25 healthy volunteers and measured attention and mood. The high-thujone condition impaired peripheral attention and temporarily counteracted alcohol's anxiolytic effect; the low-thujone condition did not show those effects. This supports a dose-dependent interaction between thujone and alcohol-related CNS effects, but the endpoints were attention and mood, not validated psychedelic phenomenology, and the study did not establish 5-HT2A involvement.

The phrase “absinthe is psychedelic” compresses at least three distinct claims: that the drink is subjectively different from other spirits; that it can cause hallucination or perceptual alteration; and that it does so through a classic psychedelic mechanism. The first may be plausible because of ethanol dose, aroma, ritual, expectation, and minor constituents. The second remains preparation- and dose-dependent. The third is not established by the current evidence map.

## 7. Synthesis

| Claim | Current status | Evidence boundary |
|---|---|---|
| Absinthe contains multiple botanical volatiles | Observed in Terpedia artifact | One repository COA; independent replication needed |
| The recorded preparation contains thujones | Observed in Terpedia artifact | Reported alpha + beta = 21.6 mg/L; raw analytical files unavailable |
| Alpha-thujone can inhibit GABA-A receptor function | Directly characterized | Strong mechanism for excitation/convulsant toxicology |
| Absinthe constituents activate 5-HT2A at human-relevant exposure | Unestablished | No complete compound-resolved receptor/exposure dataset located |
| Absinthe produces a reproducible classic psychedelic state | Unestablished | A human matched-alcohol thujone study measured attention/mood, not psychedelic phenomenology |
| Historical absinthism proves a psychedelic mechanism | Not supported | Historical symptom reports are non-specific and confounded |
| Resolved absinthe structures have SAIR projection or full-parquet matches | No match found in the inspected releases | 34 unique compound-SMILES records representing 27 inventory compounds; 646 human-panel compound-target rows; no isomeric or connectivity-only match; not biological absence |
| Absinthe terpene–receptor edges are all experimentally established | Not supported | The network separates direct assays, preclinical modulation, candidate hypotheses, and unresolved target tests |

### Conclusion

On the Terpedia evidence currently assembled, absinthe should be classified as an alcoholic botanical mixture with psychoactive and toxicological potential, not as an established classic psychedelic. The central negative result is evidentiary rather than metaphysical: the project found strong GABA-A/toxicology evidence for thujone and a chemically complex beverage record, but not the joined chain of 5-HT2A agonism, plausible CNS exposure, controlled psychedelic phenomenology, and causal antagonism required for the stronger label. A preparation-level psychedelic effect remains a falsifiable hypothesis, especially for unusual recipes or adulterated products, but it cannot be inferred from thujone, anethole, historical reputation, or a GC–MS peak.

## 8. Limitations and next experiments

The COA lacks raw chromatograms, reference-standard traces, calibration files, bottle identity, alcohol-by-volume confirmation, and independent replication. Terpedia's authenticated public API and content-addressed SAIR interaction projection were queried, but direct BigQuery access and the full SAIR structure-parquet join remain operationally separate from the public projection. Several compounds still have ambiguous stereoisomer assignment or source-label discrepancies, and one inventory name lacks a Terpedia structure match. Literature coverage is a first-pass map rather than a systematic review with registered search strings and dual screening.

The smallest decisive experimental program is:

1. Independently analyze multiple absinthe preparations by validated GC–MS/LC–MS, including ethanol, alpha/beta-thujone, anethole isomers, fenchone, pinocamphones, and nonvolatile fractions.
2. Test exact compounds and realistic mixtures in a functional 5-HT2A assay plus a broader receptor panel, with concentration-response curves and cytotoxicity controls.
3. Measure parent and metabolite plasma exposure after a controlled, ethically approved, ethanol-matched administration; do not extrapolate from neat-compound doses.
4. Run a preregistered, blinded human study with validated subjective psychedelic scales, cognition, perception, autonomic measures, and a comparator spirit. Include a 5-HT2A antagonist arm only if scientifically and ethically justified.
5. Treat seizures, delirium, or severe intoxication as adverse toxicological outcomes, not as positive psychedelic endpoints.

## References

1. Terpedia. *Absinthe: Herbal Ingredients & Bioactive Compounds*. Local source artifact: `../functional-flavors/absinthe.html`.
2. Terpedia. *GC-MS Certificate of Analysis — Absinthe (Traditional Verte)*. Local source artifact: `../functional-flavors/absinthe-coa.html`.
3. Nichols DE. Psychedelics. *Pharmacol Rev*. 2016;68:264–355. https://doi.org/10.1124/pr.115.011478
4. Madsen MK, et al. Psychedelic effects of psilocybin correlate with serotonin 2A receptor occupancy and plasma psilocin levels. *Neuropsychopharmacology*. 2019;44:1328–1334. https://pmc.ncbi.nlm.nih.gov/articles/PMC6785028/
5. González-Maeso J, et al. Hallucinogens recruit specific cortical 5-HT2A receptor-mediated signaling pathways. *Neuron*. 2007;53:439–452. https://doi.org/10.1016/j.neuron.2007.01.008
6. Höld KM, et al. Alpha-thujone: GABA-A receptor modulation and metabolic detoxification. *PNAS*. 2000;97:3826–3831. https://pmc.ncbi.nlm.nih.gov/articles/PMC18101/
7. Olsen RW. Absinthe and gamma-aminobutyric acid receptors. *PNAS*. 2000;97:4417–4418. https://pmc.ncbi.nlm.nih.gov/articles/PMC34311/
8. Lachenmeier DW, et al. Absinthism: a fictitious 19th century syndrome with present impact. *Subst Abuse Treat Prev Policy*. 2006;1:14. https://pmc.ncbi.nlm.nih.gov/articles/PMC1475830/
9. Pelkonen O, Abass K, Wiesner J. Thujone and thujone-containing herbal medicinal and botanical products: toxicological assessment. *Regul Toxicol Pharmacol*. 2013;65:100–107. https://pubmed.ncbi.nlm.nih.gov/23201408/
10. Dettling A, et al. Absinthe: attention performance and mood under the influence of thujone. *J Stud Alcohol*. 2004;65:573–581. https://pubmed.ncbi.nlm.nih.gov/15536765/
