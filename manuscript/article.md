# Is absinthe a different kind of drunk—and is it psychedelic? A critical Terpedia evidence map of ethanol, thujone, and 5-HT2A pharmacology

**Working manuscript — 3 September 2026**

## Abstract

Absinthe is often described as producing a qualitatively different intoxication from ordinary spirits, sometimes escalating to a claim that it is psychedelic. The biochemical basis of either claim has not been established. We evaluated the claim using Terpedia's evidence-oriented knowledge-base workflow. We used an operational definition of a classic serotonergic psychedelic requiring a plausible 5-HT2A-centered mechanism, plausible human exposure, and reproducible controlled human changes in perception, cognition, or self-experience; receptor activity alone was not treated as sufficient. We then mapped the absinthe compounds recorded in Terpedia's Functional Flavors profile and repository GC–MS certificate of analysis against that framework, while separating volatile observations, nonvolatile botanical constituents, ethanol, receptor pharmacology, toxicology, and historical narrative. The inventory is dominated by trans-anethole in the repository COA, with fenchone and thujones as additional reported constituents. Direct evidence supports alpha-thujone, and mixed/isomer-qualified evidence supports the thujone fraction, as GABA-A channel antagonists/convulsant toxicology candidates—not as 5-HT2A psychedelics. Human psychedelic evidence for psilocybin provides a useful positive-control standard: plasma psilocin, cerebral 5-HT2A occupancy, and subjective intensity covary in controlled volunteers. On the current evidence, an ethanol-containing absinthe preparation has established intoxicating effects and plausible toxicological/sensory-neural modifiers, but it is not established as a classic psychedelic. A preparation-level psychedelic claim remains untested rather than disproved; the decisive next study is a chemically characterized, ethanol-matched, blinded experiment coupled to receptor, pharmacokinetic, and subjective-effect measurements.

**Keywords:** absinthe; thujone; 5-HT2A; GABA-A; psychedelic; ethanol; Terpedia; phytochemistry

## 1. Introduction

Absinthe is a distilled alcoholic beverage traditionally associated with grand wormwood (*Artemisia absinthium*), green anise (*Pimpinella anisum*), and Florence fennel (*Foeniculum vulgare*), with coloring botanicals such as petit wormwood, hyssop, and lemon balm. Its ritual, intense aroma, louche, and nineteenth-century cultural history generated a persistent claim that it produces effects qualitatively different from ordinary alcohol. Historical reports grouped euphoria, sharpened perception, hallucinations, insomnia, confusion, and convulsions under “absinthism.” Those reports are clinically and pharmacologically heterogeneous: hallucination, delirium, withdrawal, alcohol intoxication, adulterants, and seizure are not interchangeable endpoints.

The primary question is whether absinthe produces a reproducibly different intoxication profile from an ethanol-matched spirit. A secondary question is whether any difference has a classic serotonergic psychedelic mechanism. Neither question can be answered from a compound being natural, psychoactive, CNS-active, or associated with hallucinations. The first requires preparation-matched human behavioral and subjective data; the second additionally requires identity-resolved exposure, a relevant mechanism, and controlled psychedelic phenomenology. In this review, “different” means a reproducible between-preparation difference in validated subjective domains, cognitive or motor performance, physiological effects, or time course after matching ethanol dose and administration conditions—not merely a distinctive aroma, ritual, expectation, or isolated historical report.

## 2. Definitions and biochemical framework

Classic serotonergic psychedelics include psilocybin/psilocin, LSD, and mescaline. Across this class, agonism or partial agonism at cortical serotonin 5-HT2A receptors is the most reproducible mechanistic anchor, although receptor activation is necessary rather than sufficient for the full subjective state (González-Maeso et al., 2007; Nichols, 2016). 5-HT2A is a G-protein-coupled receptor expressed prominently on cortical pyramidal neurons. Activation can engage Gq/11-linked phospholipase C signaling, intracellular calcium mobilization, excitability changes, and downstream circuit effects. Other serotonin receptors, glutamatergic signaling, network dynamics, learning, expectation, and set and setting contribute to the final experience.

The appropriate evidence ladder is:

1. **Identity:** exact structure, stereochemistry, salt/protonation state, and preparation are resolved.
2. **Target pharmacology:** binding and functional assays show 5-HT2A activity, with concentration-response data and selectivity context.
3. **Brain exposure:** active parent or metabolite reaches the CNS at concentrations plausibly produced by the preparation.
4. **Phenomenology:** controlled human administration produces reproducible changes in perception, cognition, or self-experience.
5. **Causality:** an antagonist, comparator, or dose-response relationship supports the proposed mechanism.

Psilocybin illustrates the standard. In a controlled human PET study, oral psilocybin produced dose-related 5-HT2A occupancy through its active metabolite psilocin; plasma psilocin, occupancy, and subjective psychedelic intensity were closely associated (Madsen et al., 2019). This is materially stronger than a molecule merely appearing in a plant or sharing a broad “psychoactive” label.

## 3. Terpedia-centered methods

### 3.1 Sources and entity handling

The primary project source is the Terpedia KB, documented as a GCP-backed biochemical system with ChEBI, PubChem, Rhea, natural-product, essential-oil, and literature datasets. The current Cloud Run API in project `terpedia-489015` was queried on 2026-09-03 using the documented authenticated tabular-search route. The external literature component was targeted and citation-chained rather than systematic; this paper therefore makes no claim of exhaustive literature retrieval. Searches in the `supernatural2` projection resolved stereochemical records for thujone, anethole, fenchone, and linalool; the returned release, ingestion run, manifest URI, source object, and SHA-256 are preserved in `data/gcp-kb-refresh-2026-09-03.json`. The local Terpedia source artifacts were used to establish the starting inventory: `functional-flavors/absinthe.html` and `functional-flavors/absinthe-coa.html`. Psychedelic comparator literature was located in Terpedia's Paperpile export and checked against primary or review articles.

Chemical records were kept separate when the source distinguishes stereoisomers or geometric isomers. The inventory also separates volatile COA observations from absinthin, artabsin, and rosmarinic acid, which the Terpedia profile lists but which are not represented in the volatile COA table.

### 3.2 Evidence coding

Each claim is coded as observed in a Terpedia artifact, directly characterized in a primary experiment, mechanistically supported, or unestablished. A GC–MS library match is chemical-identification evidence for the analyzed sample; it is not receptor or phenomenology evidence. A connected biochemical graph path is a testable hypothesis, not proof of in vivo production or human pharmacology.

### 3.3 Literature search and selection

This article is a critical review and evidence map, not a registered systematic review or meta-analysis. To make the selection process auditable, we provide a structured evidence-selection summary. Terpedia source artifacts supplied the preparation-level inventory and knowledge-base records. Psychedelic neurobiology, thujone pharmacology, absinthe history, human thujone effects, linalool, and trans-anethole were identified through the Terpedia Paperpile export, citation chasing, and targeted searches of primary or authoritative review literature. Sources were retained when they addressed the 5-HT2A psychedelic mechanism, absinthe composition or historical toxicology, receptor pharmacology of an inventory constituent, or controlled human effects relevant to the classification question. Unsourced web claims and compound-presence claims without analytical or pharmacological context were excluded.

The evidence-selection summary is intentionally entity-specific: two local Terpedia preparation artifacts support the inventory; one curated 29-compound inventory is analyzed; 19 Terpedia-linked human target records define the comparator panel; 10 compound–target rows are retained in the evidence-qualified map; and 18 references are retained in the bibliography, comprising two Terpedia artifacts, 10 external scientific papers, two peer-reviewed physiology reviews, two TAS2R pharmacology papers, one historical essay, and one authoritative assessment report. Because the discovery export and citation-chasing steps were not run as a reproducible database-wide systematic search, the number of records screened and excluded at those stages is not claimed. This limitation is deliberate and is why the paper is presented as a critical review rather than a systematic review. The exact search log and source-level evidence table are provided in `docs/jps-search-log.md` and `data/source-level-evidence.csv`. The computational methods and tabulated results are reproducible in `notebooks/absinthe_terpedia_analysis.ipynb`, which reads versioned Terpedia snapshots and exposes an optional read-only authenticated API confirmation cell.

### 3.4 Structure-first compound–human-target evidence map

We prespecified a five-target comparator panel (HTR2A, HTR3A, GABRB2, TRPA1, and CNR1) and expanded it to 19 Terpedia-linked human neural/CNS target records spanning serotonin, GABA-A, dopamine, opioid, cholinergic, cannabinoid, sensory-channel, glutamatergic, and transporter systems. Stable Terpedia protein record IDs, source releases, URLs, and content hashes are retained in the panel tables. This is a human-target comparator panel, not a claim that every pharmacology result is human or that the panel is an interactome. The target panel is a comparator universe, not evidence of interaction.

Resolved Terpedia structures were joined to the recovered SAIR interaction projection by RDKit canonical isomeric SMILES, with a second non-isomeric check used to detect connectivity-only matches. The projection contains 1,489 rows, 397 protein IDs, and 907 unique structures. Thirty-six unique compound-SMILES records representing all 29 inventory compounds were scanned; no isomeric or non-isomeric matches were found. The full SAIR parquet was then queried remotely for the 19-target human panel after mapping Terpedia protein records to UniProt accessions; 136,025 compatible protein rows generated 684 structure–target combinations (36 resolved structure records × 19 targets), with zero exact structure matches. The trans-sabinyl acetate SMILES is explicitly a supplemental crosswalk keyed to a Terpedia systematic name because the native EssoilDB row has no structure field. These database results are reported as “no join found,” not as evidence of receptor inactivity. Literature-supported edges were retained separately in an evidence-qualified map, with direct binding/functional assay results distinguished from preclinical candidates and unresolved 5-HT2A tests. Reported beverage concentrations were attached as exposure context, never substituted for plasma or brain concentrations. Full procedures and source checks are in `docs/receptor-interaction-protocol.md`, `docs/identity-resolution.md`, and the `data/` tables.

**Figure 1.** Evidence-qualified absinthe modulation map (`manuscript/figure-1-evidence-map.mmd`). **Table 1.** Curated absinthe inventory and preparation-level exposure context (`data/absinthe-compounds.csv`). **Table 2.** Evidence-qualified human-target edges (`data/receptor-interactome.csv`). **Supplementary Table S1.** Full 29-compound modulation assignments (`data/psychedelic-modulation-map.csv`).

## 4. Absinthe molecular inventory

The repository COA is a provisional, repository-provided analytical artifact describing one Swiss-style absinthe verte analyzed by HS-SPME/GC–MS (Terpedia, n.d.-a, n.d.-b). Its table lists 27 identified volatile rows and reports a summary total of 91.2 area% with 8.8% unidentified peaks. The curated study inventory contains 26 of those volatile rows plus three nonvolatile profile entries; p-cymene (CAS 99-87-6) is presently excluded pending identity-resolution reconciliation. The displayed source-row values sum differently because of rounding or source-table inconsistency, so the source-reported total is retained rather than recomputed. The dominant reported constituent is trans-anethole at 72.4 area% and 868.8 mg/L. Fenchone is reported at 8.7 area% and 104.4 mg/L. Alpha- and beta-thujone are reported at 14.4 and 7.2 mg/L, respectively, for a combined 21.6 mg/L. These values are repository observations, not independent measurements generated for this study.

The high trans-anethole signal is consistent with the sensory and physical identity of anise-rich absinthe, including the louche. It does not imply psychedelic pharmacology. The thujones are chemically and toxicologically more relevant to the historical claim, but their presence likewise does not establish a psychedelic mechanism. Fenchone, pinocamphone, isopinocamphone, camphor, linalool, and other minor volatiles broaden the possible CNS pharmacology, while nonvolatile constituents may be extracted during coloring or remain absent from the distilled fraction. Finished-beverage composition can therefore vary with cultivar, chemotype, recipe, distillation, coloring, storage, and analytical method.

## 5. Candidate mechanisms

### 5.1 Thujones

The strongest direct mechanistic evidence in the absinthe literature concerns alpha-thujone at the GABA-A receptor picrotoxin/convulsant site; evidence for beta-thujone is more limited and isomer-qualified. The foundational PNAS work reported competitive inhibition of a radiolabeled convulsant ligand and reversible blockade of GABA-A chloride currents. In that study, alpha-thujone had an [3H]EBOB-binding IC50 of 13 ± 4 μM and a GABA-current IC50 of approximately 21 μM; beta-thujone had an [3H]EBOB-binding IC50 of 29 ± 8 μM, making the beta-isomer less potent in that binding assay (Höld et al., 2000; Olsen, 2000). The associated phenotype is reduced inhibitory neurotransmission and, at sufficiently high exposure, excitation and convulsions. These findings support toxicological mechanism, not a psychedelic phenotype. This is a toxicological/analeptic mechanism, not evidence of 5-HT2A agonism.

Thujone is also rapidly metabolized in experimental systems, producing hydroxylated and dehydrogenated metabolites. Thus, even a positive in vitro result would require parent/metabolite exposure matching before it could explain a beverage-level effect. Modern toxicological assessments describe human dose uncertainty and emphasize dose-dependent neurotoxicity. A seizure or delirium pathway should not be relabeled psychedelic merely because historical accounts used the word hallucination.

### 5.2 Fenchone and pinocamphone

Terpedia's absinthe record associates fenchone with Florence fennel and pinocamphone/isopinocamphone with hyssop. These monoterpene ketones are reasonable safety and non-5-HT2A comparator targets because concentrated essential oils can be neuroactive and convulsant. However, the presence of a compound, or even evidence of toxicity at high concentration, does not satisfy the 5-HT2A, brain-exposure, and controlled-phenomenology criteria. These molecules deserve a receptor-panel and exposure study, not a psychedelic label.

### 5.3 Anetholes, linalool, and other volatiles

Trans-anethole is the dominant reported volatile in the repository COA. Terpedia's compound record emphasizes aroma, metabolism, and preclinical pharmacology rather than 5-HT2A agonism. A primary study reports selective, nonelectrophilic agonism of human TRPA1 by trans-anethole (Memon et al., 2019). Linalool has preclinical GABA-A-relevant literature (Höld et al., 2017), but that is not equivalent to a classic psychedelic mechanism. Estragole and methyleugenol raise toxicological questions; limonene, pinene, myrcene, cineole, aldehydes, and sesquiterpenes contribute to a chemically complex mixture. The correct conclusion for this group is not “inactive,” but “no established classic psychedelic evidence in the current Terpedia record.”

### 5.4 Mixture-level modulation map

The complete 29-compound map separates plausible modifiers from compounds that are merely present in the analytical inventory. Alpha-thujone has direct functional GABA-A evidence, the thujone fraction has mixed/isomer-qualified binding evidence, and trans-anethole has functional TRPA1 evidence. Linalool is a preclinical GABA-A-relevant candidate. Fenchone and pinocamphone remain safety-oriented GABA-A comparators, while the remaining volatile entries have no qualifying compound–receptor edge in the inspected Terpedia and SAIR releases. The nonvolatile entries absinthin, artabsin, and rosmarinic acid remain unassessed in this receptor map.

This is the relevant modulation hypothesis for the psychedelic question: alpha-thujone and the thujone fraction could reduce inhibitory tone and alter arousal or salience; linalool could, if the reported preclinical activity survives exact-isomer and exposure testing, shift inhibitory tone in the opposite direction; and trans-anethole could change sensory input through TRPA1. These effects could make an ethanol-containing mixture feel different without supplying the cortical 5-HT2A mechanism used to classify classic serotonergic psychedelics. They must not be described as additive or synergistic: the current data contain no mixture experiment, brain-exposure measurements, or component-resolved concentration–response model.

No supported direct 5-HT2A edge was located for an inventory compound in the searched Terpedia/SAIR releases and retained literature. Alpha-thujone and trans-anethole are recorded as unresolved HTR2A tests, not as negative results. Accordingly, the map supports a testable hypothesis of non-5-HT2A modulation—especially inhibitory tone, sensory signaling, ethanol interaction, and toxicological excitation—but does not support a psychedelic classification. The machine-readable assignments, including the 23 compounds with no qualifying edge or no receptor assessment, are in `data/psychedelic-modulation-map.csv`.

### 5.5 Receptors and neural functions implicated by the current map

The current evidence does not support the statement that absinthe “stimulates” a single psychedelic receptor. It supports a small set of compound–target hypotheses with different evidence levels and physiological functions:

| Compound or fraction | Target | Normal function | Evidence in the absinthe analysis | Interpretive boundary |
|---|---|---|---|---|
| Alpha-thujone | GABA-A receptor picrotoxin/convulsant site | GABA-A receptors are ligand-gated chloride channels that generally reduce neuronal excitability when activated; their activity shapes inhibition, arousal, motor control, and seizure threshold | Direct binding and electrophysiology support channel blockade/modulation (Höld et al., 2000; Olsen, 2000) | Reduced inhibitory tone could contribute to excitation, disinhibition, or toxicity; this is not 5-HT2A psychedelic pharmacology |
| Alpha-thujone | TAS2R14 | TAS2R14 is a broadly tuned bitter-chemosensory GPCR; activation can signal through heterotrimeric G proteins and intracellular calcium pathways | Functional expression studies identify (-)-alpha-thujone as a human TAS2R14 ligand (Behrens et al., 2004) | Supports bitterness and chemosensory signaling; it does not establish a gut-specific effect, CNS activity, or psychedelic mechanism |
| Beta-thujone | GABA-A receptor picrotoxin/convulsant site | Same inhibitory receptor system | Mixed-isomer binding evidence; beta-specific functional potency remains incompletely resolved (Höld et al., 2000) | Isomer-qualified evidence, not a fully characterized beta-thujone human mechanism |
| Trans-anethole | TRPA1 | TRPA1 is a nonselective cation channel involved in chemical sensing, irritation, nociception, and sensory-neural signaling | Functional agonism at recombinant human TRPA1 and cellular systems (Memon et al., 2019) | May alter sensory input or oral/trigeminal experience; TRPA1 activity does not establish altered consciousness or a psychedelic state |
| Linalool and metabolites | GABA-A-relevant sites | GABA-A signaling regulates inhibitory tone and network excitability | Preclinical modulation has been reported, but exact isomer, direction, potency, and CNS exposure remain unresolved (Höld et al., 2017) | Candidate modifier only; do not infer activity from linalool concentration in the COA |
| Absinthin | TAS2R46 | TAS2R46 is a bitter-chemosensory GPCR expressed in oral and extraoral tissues; downstream signaling can alter cellular calcium responses | Absinthin is a characterized human TAS2R46 agonist in cellular studies (Talmon et al., 2019) | This is the strongest direct GI-relevant ligand evidence in the current inventory, but absinthin concentration and absorption in the analyzed beverage are unknown |
| Fenchone and pinocamphone | GABA-A comparator system | Inhibitory signaling and seizure threshold | Included as safety-oriented comparators; compound-resolved receptor interactions remain unresolved | Neurotoxicity is a hypothesis requiring direct assay, not evidence of psychedelic action |
| Alpha-thujone and trans-anethole | HTR2A (5-HT2A) | Cortical 5-HT2A signaling contributes to psychedelic phenomenology when activated by established psychedelics | No qualifying direct edge located in the searched Terpedia/SAIR releases and retained literature | The result is unresolved, not proof of inactivity; no absinthe constituent currently supplies the paper’s 5-HT2A criterion |

This functional view explains why the phrase “absinthe stimulates receptors” is too imprecise. The best-supported effects point toward inhibitory-tone disruption and sensory modulation, while the defining psychedelic target remains unestablished. The table also prevents a common category error: receptor function describes what a target normally does, whereas a beverage-level claim requires compound-specific potency, unbound exposure, metabolism, mixture context, and human phenotype.

### 5.6 Gastrointestinal chemosensing, appetite, and digestion

The traditional “digestif” reputation of wormwood and absinthe warrants a gastrointestinal mechanism section (Terpedia, n.d.-a), but it should not be conflated with psychedelic pharmacology. Human gastrointestinal mucosa expresses bitter taste GPCRs (TAS2Rs) on enteroendocrine and other epithelial cells. Bitter-ligand stimulation can alter intracellular calcium signaling and the release of gut peptides such as cholecystokinin (CCK), GLP-1, PYY, and ghrelin; these signals can influence gastric emptying, motility, satiation, nutrient handling, and gut–brain communication (Sternini & Rozengurt, 2025). The direction and magnitude of these effects depend on receptor subtype, ligand, dose, gut location, and species.

| GI-relevant receptor, channel, or downstream pathway | Function | Relationship to absinthe |
|---|---|---|
| TAS2R bitter taste receptors | Detect bitter compounds in the mouth and gut; can regulate enteroendocrine secretion, motility, gastric emptying, appetite, and epithelial defense | Alpha-thujone–TAS2R14 and absinthin–TAS2R46 are supported by ligand/receptor studies (Behrens et al., 2004; Talmon et al., 2019); preparation-level gut exposure and effects remain unestablished |
| TRPA1 | Chemosensory cation channel involved in irritant, visceral-sensory, and nociceptive signaling | Trans-anethole directly activates recombinant human TRPA1 (Memon et al., 2019); this supports sensory-neural activity, but does not establish a gut-specific effect after drinking absinthe |
| 5-HT3A | Ligand-gated serotonin channel on enteric and vagal pathways involved in nausea, emesis, visceral sensation, and motility | Included in the Terpedia human comparator panel, but no qualifying absinthe-constituent interaction was located |
| CCK, GLP-1, PYY, and ghrelin signaling | Hormonal outputs that coordinate satiation, gastric emptying, motility, and energy intake | These are candidate downstream readouts of bitter-gut sensing, not evidence that an absinthe constituent directly activates their receptors |

This framework modifies the interpretation of “absinthe helps appetite or digestion.” Bitter taste and ethanol-related sensory/contextual effects could influence cephalic-phase responses, gastric sensation, and meal behavior, while TAS2R signaling is a plausible gut mechanism. However, the current data do not show that the analyzed preparation activates a particular human TAS2R, increases digestive secretion, improves digestion, or produces a reproducible appetite effect. The dominant trans-anethole signal should therefore not be used as a proxy for a proven digestive receptor mechanism, and any future study should measure gastric emptying, gut hormones, nausea, appetite, and motility alongside CNS endpoints.

#### General ligand–protein evidence versus TAS2R-specific evidence

These are distinct analytical questions. A general ligand–protein result means that a compound is associated with a protein target in a database, or that an assay reports binding or functional modulation. A TAS2R result is narrower: it requires an identity-resolved absinthe ligand, a named human bitter-receptor subtype, and a direct binding or functional assay at a concentration relevant to the consumed preparation. A ligand can be chemically plausible, bitter, or biologically active without being a TAS2R ligand. Conversely, a TAS2R interaction would support gastrointestinal chemosensing but would not establish CNS penetration, altered consciousness, or psychedelic activity.

The current Terpedia/SAIR panel did not include TAS2Rs, so its structure-search output cannot provide a database-level positive or negative result for this receptor family. The literature-qualified map now includes alpha-thujone–TAS2R14 and absinthin–TAS2R46 edges, alongside the direct trans-anethole–TRPA1 edge and direct or isomer-qualified thujone–GABA-A evidence. These TAS2R edges establish ligand/receptor pharmacology, not the concentration, absorption, gut distribution, or human appetite effect of the analyzed beverage. TAS2Rs should still be added as a dedicated GI target family in the next Terpedia query and assay pass.

### 5.7 Ethanol and preparation context

Ethanol is not a minor confounder: it is the beverage matrix and produces dose-dependent intoxication, disinhibition, sedation, memory impairment, and, with chronic exposure or withdrawal, severe neuropsychiatric effects. Acute ethanol effects are concentration-, brain-region-, receptor-subtype-, and exposure-state-dependent rather than reducible to one receptor action. At the synaptic level, ethanol can enhance selected GABA-A-mediated inhibitory signaling and inhibit NMDA-type glutamatergic signaling; at the circuit level, it alters cerebellar and hippocampal processing, prefrontal control, and mesolimbic reward signaling. Ethanol-associated dopamine release in the ventral tegmental area–nucleus accumbens pathway, together with opioid, endocannabinoid, and stress-system modulation, can change reward, salience, anxiety, and behavioral control (Abrahao et al., 2017). These pathways explain why an absinthe experience may differ from a nonalcoholic botanical preparation without providing a 5-HT2A psychedelic mechanism. Absinthe effects must therefore be compared with an ethanol-matched spirit and, ideally, a botanical-matched alcohol-free or de-aromatized control. The louche changes dispersion and sensory expectation, but a visible colloidal transition is not a pharmacological assay.

## 6. Historical claims and causal interpretation

Historical reviews conclude that nineteenth-century “absinthism” mixed chronic alcohol misuse with reports of seizures, hallucinations, and mental deterioration, and that wormwood oil is far more convulsant than properly manufactured absinthe (Lachenmeier et al., 2006; Pelkonen et al., 2013). Later chemical analyses also challenged exaggerated assumptions about historical thujone concentrations. These reviews do not prove that no absinthe preparation can alter perception. They do show why historical anecdotes cannot identify a receptor mechanism or quantify dose.

The cultural record nevertheless contains explicit testimony that absinthe was understood as more than ordinary drinking. In “Absinthe: The Green Goddess,” first published in *The International* in 1918, Aleister Crowley describes absinthe through the language of mystery, cult, inspiration, and altered meaning, asking what makes it a “separate cult” (Crowley, 1918). This is useful evidence for the existence and vocabulary of the myth—not evidence that Crowley’s reported or implied effects were pharmacologically specific. A small human exposure report later summarized by the European Medicines Agency provides a contrasting observation: two subjects consumed 110 mL of absinthe containing an estimated 3.85 mg thujone; blood alcohol exceeded 1 g/L, thujone was below the assay detection limit, and the described signs were ordinary alcohol intoxication rather than hallucination (European Medicines Agency, n.d.). The sample is too small and the protocol too limited to exclude unusual effects, but it does not provide positive evidence for a robust psychedelic syndrome.

One directly relevant human study did test absinthe-like drinks under matched alcohol conditions. Dettling and colleagues administered drinks containing identical alcohol amounts but 0, 10, or 100 mg/L thujone to 25 healthy volunteers and measured attention and mood (Dettling et al., 2004). The high-thujone condition impaired peripheral attention and temporarily counteracted alcohol's anxiolytic effect; the low-thujone condition did not show those effects. This supports a dose-dependent interaction between thujone and alcohol-related CNS effects, but the endpoints were attention and mood, not validated psychedelic phenomenology, and the study did not establish 5-HT2A involvement.

The phrase “absinthe is a different drunk” compresses at least three distinct claims: that the drink produces a reproducibly different intoxication profile from an ethanol-matched spirit; that it can cause hallucination or perceptual alteration; and that any such difference arises through a classic psychedelic mechanism. The first may be plausible because of ethanol dose, aroma, ritual, expectation, and minor constituents. The second remains preparation- and dose-dependent. The third is not established by the current evidence map.

## 7. Synthesis

| Claim | Current status | Evidence boundary |
|---|---|---|
| Absinthe contains multiple botanical volatiles | Observed in Terpedia artifact | One repository COA; independent replication needed |
| The recorded preparation contains thujones | Observed in Terpedia artifact | Reported alpha + beta = 21.6 mg/L; raw analytical files unavailable |
| Alpha-thujone can inhibit GABA-A receptor function | Directly characterized | Strong mechanism for excitation/convulsant toxicology |
| Absinthe constituents activate 5-HT2A at human-relevant exposure | Unestablished | No complete compound-resolved receptor/exposure dataset located |
| Absinthe produces a reproducibly different intoxication profile from an ethanol-matched spirit | Unestablished | The available human study measured attention/mood under matched alcohol, not a comprehensive subjective intoxication profile |
| Absinthe produces a reproducible classic psychedelic state | Unestablished | A human matched-alcohol thujone study measured attention/mood, not psychedelic phenomenology |
| Historical absinthism proves a psychedelic mechanism | Not supported | Historical symptom reports are non-specific and confounded |
| Crowley’s essay proves absinthe is pharmacologically psychedelic | Not supported | It documents the cultural myth and subjective vocabulary, not controlled exposure, receptor pharmacology, or causal mechanism |
| Alpha-thujone and absinthin interact with human TAS2Rs | Directly characterized ligand evidence | Alpha-thujone–TAS2R14 and absinthin–TAS2R46 are supported in heterologous/cellular studies; beverage-level exposure and GI phenotype remain unknown |
| Absinthe activates GI bitter receptors and improves appetite or digestion | Unestablished | TAS2R biology provides plausibility, but no preparation-level receptor, gut-hormone, motility, or appetite study was located |
| Resolved absinthe structures have SAIR projection or full-parquet matches | No match found in the inspected releases | 36 unique compound-SMILES records representing all 29 inventory compounds; 684 structure–target combinations; no isomeric or connectivity-only match; not biological absence |
| Absinthe terpene–target edges are all experimentally established | Not supported | The map separates direct assays, preclinical modulation, candidate hypotheses, and unresolved target tests |
| The 29-compound mixture may contain non-5-HT2A modulators | Plausible but unquantified | Supported GABA-A and TRPA1 edges, a linalool candidate, and unresolved comparators do not establish direction, synergy, CNS exposure, or psychedelic action |

### Conclusion

On the Terpedia evidence currently assembled, absinthe should be classified as an ethanol-containing botanical mixture with established intoxicating effects and incompletely characterized modifiers. The available evidence does not establish that it produces a reproducibly different intoxication profile from an ethanol-matched spirit, and it does not establish a classic psychedelic mechanism. The central negative result is evidentiary rather than metaphysical: the project found strong GABA-A/toxicology evidence for thujone and a chemically complex beverage record, but not the joined chain of a distinct preparation-level subjective phenotype, 5-HT2A agonism, plausible CNS exposure, and causal antagonism required for the stronger claims. A preparation-level psychedelic effect remains a falsifiable hypothesis, especially for unusual recipes or adulterated products, but it cannot be inferred from thujone, anethole, historical reputation, or a GC–MS peak.

## 8. Limitations and next experiments

The COA lacks raw chromatograms, reference-standard traces, calibration files, bottle identity, alcohol-by-volume confirmation, and independent replication. Terpedia's authenticated public API and content-addressed SAIR interaction projection were queried, while the full SAIR structure parquet was queried remotely through its published object. Several compounds still have ambiguous stereoisomer assignment or source-label discrepancies; trans-sabinyl acetate is represented through an explicitly supplemental structure crosswalk rather than a native EssoilDB structure field. Its reported bottle concentrations cannot be compared directly with receptor-assay concentrations: serving volume, absorbed dose, bioavailability, metabolism, protein binding, unbound plasma exposure, and brain distribution are unknown. The complete preparation also cannot be classified from this volatile-focused record because the listed nonvolatile fraction was not chemically resolved or pharmacologically screened. Literature coverage is a first-pass map rather than a systematic review with registered search strings and dual screening.

The smallest decisive experimental program is:

1. Independently analyze multiple absinthe preparations by validated GC–MS/LC–MS, including ethanol, alpha/beta-thujone, anethole isomers, fenchone, pinocamphones, and nonvolatile fractions.
2. Test exact compounds and realistic mixtures in a functional 5-HT2A assay plus a broader receptor panel, with concentration-response curves and cytotoxicity controls.
3. Measure parent and metabolite plasma exposure after a controlled, ethically approved, ethanol-matched administration; do not extrapolate from neat-compound doses.
4. Run a preregistered, blinded human study with validated subjective psychedelic scales, cognition, perception, autonomic measures, and a comparator spirit. Include a 5-HT2A antagonist arm only if scientifically and ethically justified.
5. Treat seizures, delirium, or severe intoxication as adverse toxicological outcomes, not as positive psychedelic endpoints.

## References

Abrahao, K. P., Salinas, A. G., & Lovinger, D. M. (2017). Alcohol and the brain: Neuronal molecular targets, synapses, and circuits. *Neuron, 96*, 1223–1238. https://doi.org/10.1016/j.neuron.2017.10.032

Behrens, M., Brockhoff, A., Kühn, C., Bufe, B., Winnig, M., & Meyerhof, W. (2004). The human taste receptor hTAS2R14 responds to a variety of different bitter compounds. *Biochemical and Biophysical Research Communications, 319*, 479–485. https://doi.org/10.1016/j.bbrc.2004.05.019

Crowley, A. (1918). Absinthe: The green goddess. *The International, 12*(2). https://hermetic.com/crowley/international/xii/2/absinthe-the-green-goddess

Dettling, A., et al. (2004). Absinthe: Attention performance and mood under the influence of thujone. *Journal of Studies on Alcohol, 65*, 573–581. https://pubmed.ncbi.nlm.nih.gov/15536765/

European Medicines Agency. (n.d.). *Assessment report on Artemisia absinthium L., herba*. https://www.ema.europa.eu/en/documents/herbal-report/final-assessment-report-artemisia-absinthium-l-herba_en.pdf

González-Maeso, J., et al. (2007). Hallucinogens recruit specific cortical 5-HT2A receptor-mediated signaling pathways. *Neuron, 53*, 439–452. https://doi.org/10.1016/j.neuron.2007.01.008

Höld, K. M., et al. (2000). Alpha-thujone: GABA-A receptor modulation and metabolic detoxification. *Proceedings of the National Academy of Sciences, 97*, 3826–3831. https://pmc.ncbi.nlm.nih.gov/articles/PMC18101/

Höld, K. M., et al. (2017). Metabolic products of linalool and modulation of GABA-A receptors. *Frontiers in Chemistry, 5*, 46. https://pmc.ncbi.nlm.nih.gov/articles/PMC5478857/

Lachenmeier, D. W., et al. (2006). Absinthism: A fictitious 19th century syndrome with present impact. *Substance Abuse Treatment, Prevention, and Policy, 1*, 14. https://pmc.ncbi.nlm.nih.gov/articles/PMC1475830/

Madsen, M. K., et al. (2019). Psychedelic effects of psilocybin correlate with serotonin 2A receptor occupancy and plasma psilocin levels. *Neuropsychopharmacology, 44*, 1328–1334. https://pmc.ncbi.nlm.nih.gov/articles/PMC6785028/

Memon, T., et al. (2019). trans-Anethole of fennel oil is a selective and nonelectrophilic agonist of the TRPA1 ion channel. *Molecular Pharmacology, 95*, 433–441. https://pmc.ncbi.nlm.nih.gov/articles/PMC6408737/

Nichols, D. E. (2016). Psychedelics. *Pharmacological Reviews, 68*, 264–355. https://doi.org/10.1124/pr.115.011478

Olsen, R. W. (2000). Absinthe and gamma-aminobutyric acid receptors. *Proceedings of the National Academy of Sciences, 97*, 4417–4418. https://pmc.ncbi.nlm.nih.gov/articles/PMC34311/

Pelkonen, O., Abass, K., & Wiesner, J. (2013). Thujone and thujone-containing herbal medicinal and botanical products: Toxicological assessment. *Regulatory Toxicology and Pharmacology, 65*, 100–107. https://pubmed.ncbi.nlm.nih.gov/23201408/

Sternini, C., & Rozengurt, E. (2025). Bitter taste receptors as sensors of gut luminal contents. *Nature Reviews Gastroenterology & Hepatology, 22*, 39–53. https://doi.org/10.1038/s41575-024-01005-z

Talmon, M., et al. (2019). Absinthin, an agonist of the bitter taste receptor hTAS2R46, uncovers an ER-to-mitochondria Ca2+–shuttling event. *Journal of Biological Chemistry, 294*, 12472–12482. https://doi.org/10.1074/jbc.RA119.007763

Terpedia. (n.d.-a). *Absinthe: Herbal ingredients & bioactive compounds* [Terpedia source artifact].

Terpedia. (n.d.-b). *GC-MS certificate of analysis: Absinthe traditional verte* [Terpedia source artifact].
