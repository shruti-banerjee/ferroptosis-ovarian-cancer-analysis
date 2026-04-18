# Ferroptosis Hub Genes & Apoptosis in Ovarian Cancer
### MSc Bioinformatics Dissertation | Pondicherry University | May 2024

**Author:** Shruti Banerjee (Reg. No. 22378042)  
**Supervisor:** Dr. Basant K. Tiwary, Professor, Department of Bioinformatics  
**Degree:** Master of Science in Bioinformatics  

---

## Overview

Ovarian cancer has one of the highest mortality rates among gynaecological malignancies, largely due to late-stage diagnosis and resistance to standard chemotherapy. This study investigates the molecular crosstalk between two distinct cell death pathways — **ferroptosis** and **apoptosis** — to identify potential therapeutic targets in ovarian cancer.

**Key finding:** From 7,862 differentially expressed genes, two critical ferroptosis hub genes — **CDKN1A** and **GDF15** — were identified as co-expressed with apoptosis genes and associated with multiple carcinogenic pathways.

---

## Pipeline Overview

```
Raw RNA-Seq Data (ENA SRA)
        ↓
Quality Control (FastQC + Trimmomatic)
        ↓
Alignment to Reference Genome (HISAT2)
        ↓
Transcriptome Assembly (StringTie)
        ↓
Differential Gene Expression (DESeq2 in R)
        ↓
PPI Network Construction (STRING + Cytoscape)
        ↓
Gene Co-expression Network (PSYCH package in R)
        ↓
Functional Enrichment Analysis (DAVID / KEGG)
        ↓
Hub Gene Identification → CDKN1A & GDF15
```

---

## Dataset

| Parameter | Diseased Samples | Control Samples |
|---|---|---|
| Bioproject | PRJNA1005317 | PRJNA578440 |
| Organism | *Homo sapiens* | *Homo sapiens* |
| Assay type | RNA-Seq | RNA-Seq |
| Platform | Illumina HiSeq 300 | Illumina HiSeq 300 |
| Library layout | Paired | Paired |
| Samples after QC | 5 | 6 |
| Alignment score | 95–98% | 96–97% |

Samples with alignment scores below 60% (SRR25637208, SRR25637224) were excluded from downstream analysis.

---

## Tools & Technologies

**Bioinformatics Pipeline**

![HISAT2](https://img.shields.io/badge/HISAT2-v2.2.1-brightgreen?style=flat)
![StringTie](https://img.shields.io/badge/StringTie-v2.1.7-brightgreen?style=flat)
![FastQC](https://img.shields.io/badge/FastQC-v0.73-brightgreen?style=flat)
![Galaxy](https://img.shields.io/badge/Galaxy-usegalaxy.org-blue?style=flat)

**Statistical Analysis & Visualisation**

![R](https://img.shields.io/badge/R-276DC3?style=flat&logo=r&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![DESeq2](https://img.shields.io/badge/DESeq2-Bioconductor-brightgreen?style=flat)

**Network Analysis**

![STRING](https://img.shields.io/badge/STRING-v11.5-orange?style=flat)
![Cytoscape](https://img.shields.io/badge/Cytoscape-NetworkAnalyzer-orange?style=flat)
![GeneMania](https://img.shields.io/badge/GeneMania-interaction-orange?style=flat)

**Databases**

![TCGA](https://img.shields.io/badge/TCGA-genomics-red?style=flat)
![Ensembl](https://img.shields.io/badge/Ensembl-GRCh38.13-red?style=flat)
![NCBI](https://img.shields.io/badge/NCBI-SRA-red?style=flat)
![DAVID](https://img.shields.io/badge/DAVID-enrichment-red?style=flat)

---

## Results

### 1. Differential Gene Expression

| Filter | Gene Count |
|---|---|
| Total DEGs identified | 7,862 |
| Significant (p < 0.05) | 8,002 |
| Highly significant (p < 0.01) | 6,577 |
| Ferroptosis + Apoptosis genes filtered | 289 |

### 2. PPI Network Statistics

| Network | Nodes | Interactions |
|---|---|---|
| All DEGs | 236 | 886 |
| Ferroptosis genes | 174 | 1,469 |
| Co-expressed hub genes | 12 | 25 |

### 3. Ferroptosis Hub Gene Rankings (PPI Network)

| Rank | Gene | Pathway Role |
|---|---|---|
| 1 | TP53 | Tumour suppressor, apoptosis regulator |
| 2 | HIF1A | Hypoxia response, ferroptosis modulator |
| 3 | EGFR | Cell proliferation signalling |
| 4 | IL6 | Inflammatory signalling |
| 4 | STAT3 | Oncogenic transcription factor |
| 6 | PARP1 | DNA repair, apoptosis |
| 7 | GPX4 | Key ferroptosis regulator |
| 8 | SIRT1 | Metabolic regulation |
| 8 | MTOR | Cell growth and survival |
| 8 | NFE2L2 | Oxidative stress response |

### 4. Co-expressed Ferroptosis–Apoptosis Hub Genes

Four ferroptosis genes were found co-expressed with apoptosis genes in both positive and negative correlation networks:

| Gene | Type | Interactions | Role |
|---|---|---|---|
| **CDKN1A (p21)** | Ferroptosis | 23 | Cell cycle arrest at G1; tumour suppressor; mediates p53 response |
| **GDF15** | Ferroptosis | 10 | Stress-induced cytokine; involved in cancer progression |
| CISD2 | Ferroptosis | — | Iron-sulphur cluster protein; mitochondrial function |
| NUPR1 | Ferroptosis | — | Stress-response gene; linked to ferroptosis resistance |

**CDKN1A and GDF15 were selected as key hub genes** due to their high interaction degrees.

### 5. KEGG Pathway Enrichment

| Pathway | Key Genes Involved |
|---|---|
| Pathways in cancer | CDKN1A, JUN, CYCS, CKS1B |
| Colorectal cancer | CDKN1A, JUN, CYCS |
| Small cell lung cancer | CDKN1A, CYCS, CKS1B |
| Renal cell carcinoma | CDKN1A, JUN |
| **Platinum drug resistance** | **CDKN1A, CYCS** |
| **p53 signalling pathway** | **CDKN1A, CYCS** |
| Human T-cell leukemia virus 1 | FOSL1, CDKN1A, JUN |

The platinum drug resistance pathway is particularly significant — CDKN1A's involvement suggests a mechanistic link between ferroptosis and cisplatin resistance in ovarian cancer, which is a major clinical challenge.

---

## Data Visualisations

Reproducible charts generated from thesis data using Python and R.  
See [`visualizations.py`](./visualizations.py) and [`visualizations.R`](./visualizations.R).

### Sample count through the QC pipeline
![QC Pipeline](charts/chart1_qc_pipeline.png)

### HISAT2 alignment scores — diseased vs control
![Alignment Scores](charts/chart2_alignment_scores.png)

### Hub gene interaction degrees — co-expressed network
![Hub Gene Degrees](charts/chart3_hub_gene_degrees.png)

### KEGG pathway gene involvement
![KEGG Pathways](charts/chart4_kegg_pathways.png)

### DEG filtering funnel
![DEG Funnel](charts/chart5_deg_funnel.png)

---

## Repository Structure

```
ferroptosis-ovarian-cancer-analysis/
├── README.md                  ← this file
├── visualizations.py          ← Python charts (Matplotlib + NumPy)
├── visualizations.R           ← R charts (ggplot2)
├── charts/                    ← generated PNG outputs
│   ├── chart1_qc_pipeline.png
│   ├── chart2_alignment_scores.png
│   ├── chart3_hub_gene_degrees.png
│   ├── chart4_kegg_pathways.png
│   └── chart5_deg_funnel.png
└── thesis/
    └── thesis_shruti_banerjee.pdf   ← full dissertation
```

---

## How to Reproduce the Visualisations

**Python (requires matplotlib, numpy, pandas):**
```bash
pip install matplotlib numpy pandas
python visualizations.py
```

**R (requires ggplot2):**
```r
install.packages("ggplot2")
Rscript visualizations.R
```

Charts will be saved to the `charts/` folder.

---

## Key Biological Insights

**Why does this matter clinically?**

- Ovarian cancer frequently develops **resistance to cisplatin**, the standard chemotherapy. CDKN1A's involvement in the platinum drug resistance pathway suggests ferroptosis induction could be a strategy to **resensitise resistant tumours**.
- **GPX4**, ranked 7th in hub gene interaction, is the primary guardian against ferroptotic cell death. Its differential expression in ovarian cancer cells makes it a promising drug target.
- The **p53–CDKN1A axis** is central to both ferroptosis delay and apoptosis induction, revealing a shared regulatory point between the two pathways.
- Ferroptosis inducers (erastin, RSL3) combined with TRAIL-based apoptosis induction show **synergistic anti-tumour effects** — a potential combination therapy avenue.

---

## Conclusion

This study identified **CDKN1A and GDF15** as key ferroptosis hub genes with co-regulatory roles in apoptosis in ovarian cancer. Their involvement in pathways including platinum drug resistance and p53 signalling opens avenues for novel combination therapies that target both cell death mechanisms simultaneously.

---

## Citation

Banerjee, S. (2024). *Identification of ferroptosis-related hub genes and their potential relation with apoptosis in Ovarian Cancer.* MSc Dissertation, Department of Bioinformatics, Pondicherry University, Puducherry.

---

## Contact

**Shruti Banerjee**  
📧 banerjee.shruti1306@gmail.com  
🔗 [GitHub Profile](https://github.com/shruti-banerjee)
