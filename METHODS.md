# Methods

Detailed technical methods for the analysis described in this repository.  
Full methodology is available in the [thesis PDF](./thesis_shruti_banerjee.pdf).

---

## 1. Data Collection

**Source:** European Nucleotide Archive (ENA) Sequence Read Archive (SRA)  
**Access:** https://www.ebi.ac.uk/ena/browser/

| Bioproject | Type | Samples | Sequencing |
|---|---|---|---|
| PRJNA1005317 | Diseased (BRCA1/2 ovarian cancer) | 15 | Illumina HiSeq 300, Paired-end |
| PRJNA578440 | Healthy control | 10 | Illumina HiSeq 300, Paired-end |

Data was retrieved as `.fastq` files using the SRA toolkit. Severely diseased cancerous samples with BRCA1/2 mutations were specifically selected.

---

## 2. Quality Control

**Tool:** FastQC v0.73  
**Platform:** Galaxy (usegalaxy.org, usegalaxy.eu)

Parameters assessed:
- Per tile sequence quality
- Per sequence GC content
- Sequence duplication levels
- Overrepresented sequences
- Adapter content

**Outcome:** 15 diseased samples reduced to 7; 10 control samples reduced to 6 after QC.

**Pre-processing:** Trimmomatic — adapter trimming and low-quality read removal.

---

## 3. Alignment to Reference Genome

**Tool:** HISAT2 v2.2.1+galaxy0  
**Reference genome:** ENSEMBL GRCh38.13 (Fasta + GTF primary assembly)

Settings:
- Strand information: Unstranded
- Input: Paired-end FastQ files
- Output: BAM files with alignment scores

**Threshold:** Samples with alignment score < 80% were excluded.  
**Outcome:** 2 diseased samples excluded (SRR25637208: 42.36%, SRR25637224: 56.23%).  
**Final dataset:** 5 diseased + 6 control samples.

---

## 4. Genome-Guided Transcriptome Assembly

**Tool:** StringTie v2.1.7+galaxy1  
**Sorting:** SAMtools sort v2.0.3

StringTie settings:
```
Input options:          Short reads
Strand information:     Unstranded
Reference file:         ENSEMBL GTF (GRCh38.13)
Reference transcripts:  Yes (reference-based assembly)
Output:                 Gene abundance (GTF), gene count, transcript count
```

For novel transcript discovery, "Use Reference Transcripts only" was set to NO.  
Gene counts were merged using the "Column merge" tool in Galaxy.

---

## 5. Differential Gene Expression Analysis

**Tool:** DESeq2 (Bioconductor R package)  
**Environment:** R programming within Windows + Galaxy GUI

Gene IDs for DEGs were identified using **Ensembl BioMart**:
```
Database:  Ensembl Genes 106
Dataset:   Human genes (GRCh38.13)
Filters:   Gene ID list (DEGs)
Attributes: Gene Stable ID, Gene Name, Gene Type
```

Only protein-coding genes were retained for downstream analysis.

**Results:**
- Total DEGs (with reference GTF): 7,862
- Significant (p < 0.05): 8,002
- Highly significant (p < 0.01): 6,577

---

## 6. Protein–Protein Interaction Network

**Tool:** STRING v11.5 (https://string-db.org)  
**Visualisation:** Cytoscape with NetworkAnalyzer plugin v4.5.0

PPI interactions were derived from:
- Genomic context prediction
- High-throughput lab experiments
- Co-expression data
- Automated text mining
- Known pathway databases

A total of **289 ferroptosis + apoptosis DEGs** were filtered using log2 fold-change and p-value thresholds and submitted to STRING.

**Network results:**
- All DEGs: 236 nodes, 886 interactions
- Ferroptosis DEGs: 174 nodes, 1,469 interactions
- Hub gene network: 12 nodes, 25 interactions

---

## 7. Gene Co-expression Network

**Tool:** PSYCH package in R  
**Method:** Pearson's correlation coefficient

Genes with statistically significant pairwise correlations were identified. Both positive and negative co-expression networks were constructed and visualised in Cytoscape.

**Network composition:**
- Positive network: 223 apoptosis genes + 7 ferroptosis genes (230 total)
- Negative network: 143 apoptosis genes + 7 ferroptosis genes (150 total)

**Hub gene selection:** Genes with the highest interaction degree were cross-referenced with PPI results. Four ferroptosis genes were found co-expressed with apoptosis genes in both networks: CDKN1A, GDF15, CISD2, NUPR1. CDKN1A (23 interactions) and GDF15 (10 interactions) were selected as key candidates.

---

## 8. Functional Enrichment Analysis

**Tool:** DAVID v6.8 (https://david.ncifcrf.gov)  
**Database:** KEGG pathway enrichment

Co-expressed hub genes were submitted to DAVID for functional annotation and KEGG pathway mapping. Pathways regulated by both ferroptosis and apoptosis co-expressed genes were identified.

**Significant pathways identified:**

| Pathway | Genes | Clinical Relevance |
|---|---|---|
| Platinum drug resistance | CDKN1A, CYCS | Direct relevance to cisplatin resistance in OC |
| p53 signalling pathway | CDKN1A, CYCS | Central tumour suppressor axis |
| Pathways in cancer | CDKN1A, JUN, CYCS, CKS1B | Pan-cancer relevance |
| Colorectal cancer | CDKN1A, JUN, CYCS | Cross-cancer validation |
| Small cell lung cancer | CDKN1A, CYCS, CKS1B | Cross-cancer validation |
| Renal cell carcinoma | CDKN1A, JUN | Cross-cancer validation |
| HTLV-1 infection | FOSL1, CDKN1A, JUN | Viral oncogenesis |

---

## 9. Visualisation (Reproducible)

All downstream visualisations were generated independently from thesis data using:

| Script | Language | Charts |
|---|---|---|
| `thesis_visualizations_fixed.py` | Python 3 (Matplotlib, NumPy) | 5 charts |
| `thesis_visualizations.R` | R (ggplot2, ggalluvial) | 3 charts (lollipop, alluvial, stacked bar) |
| `notebooks/ferroptosis_analysis.ipynb` | Python 3 (Jupyter) | Interactive notebook |

---

## Software Versions Summary

| Tool | Version | Purpose |
|---|---|---|
| FastQC | 0.73+galaxy0 | Quality control |
| Trimmomatic | — | Read trimming |
| HISAT2 | 2.2.1+galaxy0 | Genome alignment |
| SAMtools sort | 2.0.3 | BAM sorting |
| StringTie | 2.1.7+galaxy1 | Transcriptome assembly |
| DESeq2 | Bioconductor | Differential expression |
| Ensembl BioMart | GRCh38.13 | Gene ID mapping |
| STRING | 11.5 | PPI network |
| Cytoscape | — | Network visualisation |
| NetworkAnalyzer | 4.5.0 | Network metrics |
| PSYCH (R) | — | Co-expression network |
| DAVID | 6.8 | Pathway enrichment |
| Galaxy | usegalaxy.org/eu | Pipeline execution |
| Python | 3.9+ | Data visualisation |
| R | 4.x | Statistical analysis |
| ggplot2 | — | R visualisation |
| ggalluvial | — | Alluvial diagrams |

---

*For questions about methodology, contact: banerjee.shruti1306@gmail.com*
