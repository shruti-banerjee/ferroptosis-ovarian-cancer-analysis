# Visualizations — Ferroptosis Hub Genes & Apoptosis in Ovarian Cancer
# MSc Bioinformatics Dissertation, Pondicherry University (2024)
# Author: Shruti Banerjee
#
# Run: Rscript visualizations.R
# Output: PNG files saved to charts/ folder
# Requirements: install.packages(c("ggplot2", "dplyr"))

library(ggplot2)

dir.create("charts", showWarnings = FALSE)

source_note <- "Source: Banerjee S. (2024). MSc Dissertation, Pondicherry University."
PURPLE <- "#534AB7"
TEAL   <- "#1D9E75"
CORAL  <- "#D85A30"
AMBER  <- "#BA7517"
GRAY   <- "#888780"

theme_thesis <- theme_minimal(base_size = 12) +
  theme(
    plot.title    = element_text(size = 12, face = "bold", margin = margin(b = 8)),
    plot.subtitle = element_text(size = 10, color = "gray40"),
    plot.caption  = element_text(size = 8,  color = "gray50", hjust = 1),
    panel.grid.major.x = element_blank(),
    panel.grid.minor   = element_blank(),
    axis.title    = element_text(size = 11),
    legend.position = "bottom"
  )


# ── Chart R1: Hub gene degrees (ggplot2 version) ──────────────────────────────

hub_data <- data.frame(
  gene   = c("CDKN1A", "JUN", "CCL2", "GDF15", "BTG2",
             "FOSL1",  "IER3", "CYCS", "HSPA1B", "S100A11"),
  degree = c(23, 18, 15, 10, 8, 8, 8, 8, 5, 4),
  type   = c("Ferroptosis", "Apoptosis", "Apoptosis", "Ferroptosis", "Apoptosis",
             "Apoptosis", "Apoptosis", "Apoptosis", "Apoptosis", "Apoptosis")
)
hub_data$gene <- factor(hub_data$gene, levels = hub_data$gene[order(hub_data$degree)])

p1 <- ggplot(hub_data, aes(x = degree, y = gene, fill = type)) +
  geom_col(width = 0.6) +
  geom_text(aes(label = degree), hjust = -0.3, size = 3.5, fontface = "bold") +
  scale_fill_manual(values = c("Ferroptosis" = CORAL, "Apoptosis" = TEAL),
                    name = "Gene type") +
  xlim(0, 28) +
  labs(
    title    = "Hub gene interaction degrees in co-expressed ferroptosis–apoptosis network",
    subtitle = "CDKN1A (ferroptosis) has the highest degree with 23 interactions",
    x        = "Number of interactions (degree)",
    y        = NULL,
    caption  = source_note
  ) +
  theme_thesis

ggsave("charts/R_chart1_hub_degrees.png", p1, width = 9, height = 5, dpi = 150)
cat("Saved: R_chart1_hub_degrees.png\n")


# ── Chart R2: KEGG pathway enrichment ─────────────────────────────────────────

kegg_data <- data.frame(
  pathway = c("Pathways in cancer", "Colorectal cancer", "Small cell lung cancer",
              "HTLV-1 infection", "Renal cell carcinoma",
              "Platinum drug resistance", "p53 signalling pathway"),
  genes   = c(4, 3, 3, 3, 2, 2, 2),
  highlight = c(FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE)
)
kegg_data$pathway <- factor(kegg_data$pathway,
                             levels = kegg_data$pathway[order(kegg_data$genes)])

p2 <- ggplot(kegg_data, aes(x = genes, y = pathway, fill = highlight)) +
  geom_col(width = 0.55) +
  geom_text(aes(label = paste0(genes, " gene", ifelse(genes > 1, "s", ""))),
            hjust = -0.15, size = 3.5) +
  scale_fill_manual(values = c("FALSE" = PURPLE, "TRUE" = CORAL),
                    labels = c("Other cancer pathway", "Clinically significant to OC therapy"),
                    name = NULL) +
  xlim(0, 6.5) +
  labs(
    title    = "KEGG pathway enrichment of ferroptosis–apoptosis hub genes",
    subtitle = "Platinum drug resistance and p53 signalling are most relevant to ovarian cancer",
    x        = "Number of hub genes in pathway",
    y        = NULL,
    caption  = source_note
  ) +
  theme_thesis

ggsave("charts/R_chart2_kegg_pathways.png", p2, width = 10, height = 5, dpi = 150)
cat("Saved: R_chart2_kegg_pathways.png\n")


# ── Chart R3: DEG filtering funnel ────────────────────────────────────────────

funnel_data <- data.frame(
  stage = c("Total DEGs\n(with ref GTF)", "Significant\n(p < 0.05)",
            "Highly significant\n(p < 0.01)", "Ferroptosis +\nApoptosis genes"),
  count = c(7862, 8002, 6577, 289),
  fill  = c("start", "sig", "sig", "final")
)
funnel_data$stage <- factor(funnel_data$stage, levels = funnel_data$stage)

p3 <- ggplot(funnel_data, aes(x = stage, y = count, fill = fill)) +
  geom_col(width = 0.5) +
  geom_text(aes(label = format(count, big.mark = ",")),
            vjust = -0.5, fontface = "bold", size = 4) +
  scale_fill_manual(values = c("start" = "#D3D1C7", "sig" = TEAL, "final" = CORAL),
                    guide = "none") +
  scale_y_continuous(labels = scales::comma, expand = expansion(mult = c(0, 0.1))) +
  labs(
    title   = "Differential gene expression filtering funnel",
    subtitle = "From 7,862 total DEGs to 289 ferroptosis + apoptosis candidate genes",
    x       = NULL,
    y       = "Number of genes",
    caption = source_note
  ) +
  theme_thesis

ggsave("charts/R_chart3_deg_funnel.png", p3, width = 9, height = 5, dpi = 150)
cat("Saved: R_chart3_deg_funnel.png\n")


# ── Chart R4: Alignment scores ────────────────────────────────────────────────

align_data <- data.frame(
  sample  = c("SRR25637181", "SRR25637182", "SRR25637208*", "SRR25637216",
              "SRR25637217", "SRR25637220", "SRR25637224*",
              "SRR10313349", "SRR10313350", "SRR10313351",
              "SRR10313352", "SRR10313353", "SRR10313354"),
  score   = c(97.23, 97.56, 42.36, 96.88, 97.48, 97.86, 56.23,
              96.30, 96.29, 96.48, 96.26, 96.42, 96.54),
  group   = c(rep("Diseased", 7), rep("Control", 6)),
  passed  = c(TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, FALSE,
              TRUE, TRUE, TRUE, TRUE, TRUE, TRUE)
)
align_data$sample <- factor(align_data$sample, levels = align_data$sample)

p4 <- ggplot(align_data, aes(x = sample, y = score, fill = interaction(group, passed))) +
  geom_col(width = 0.65) +
  geom_hline(yintercept = 80, linetype = "dashed", color = "red", alpha = 0.7) +
  annotate("text", x = 1, y = 82, label = "80% threshold", color = "red",
           size = 3, hjust = 0) +
  scale_fill_manual(
    values = c("Diseased.TRUE" = CORAL, "Diseased.FALSE" = "#F09595",
               "Control.TRUE"  = TEAL,  "Control.FALSE"  = "#9FE1CB"),
    labels = c("Diseased (passed)", "Diseased (excluded)",
               "Control (passed)",  "Control (excluded)"),
    name = NULL
  ) +
  scale_y_continuous(labels = function(x) paste0(x, "%"), limits = c(0, 105)) +
  labs(
    title   = "HISAT2 alignment scores — diseased vs control samples",
    subtitle = "Samples marked * were excluded (score < 80%)",
    x       = NULL,
    y       = "Alignment score (%)",
    caption = source_note
  ) +
  theme_thesis +
  theme(axis.text.x = element_text(angle = 40, hjust = 1, size = 8))

ggsave("charts/R_chart4_alignment_scores.png", p4, width = 12, height = 5, dpi = 150)
cat("Saved: R_chart4_alignment_scores.png\n")

cat("\nAll R charts generated in charts/ folder.\n")
