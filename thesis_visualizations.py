"""
Visualizations — Ferroptosis Hub Genes & Apoptosis in Ovarian Cancer
MSc Bioinformatics Dissertation, Pondicherry University (2024)
Author: Shruti Banerjee

Generates 5 charts from the thesis data using Python.
Run: python visualizations.py
Output: PNG files saved to charts/ folder.

Requirements: pip install matplotlib numpy pandas
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

os.makedirs("charts", exist_ok=True)

plt.rcParams.update({
    'font.family': 'sans-serif',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.25,
    'grid.linestyle': '--',
    'figure.dpi': 150
})

PURPLE = '#534AB7'
TEAL = '#1D9E75'
CORAL = '#D85A30'
AMBER = '#BA7517'
GRAY = '#888780'
LIGHT = '#D3D1C7'
SOURCE = 'Source: Banerjee S. (2024). MSc Dissertation, Pondicherry University.'


# ── Chart 1: QC Pipeline — sample count ───────────────────────────────────────

fig, ax = plt.subplots(figsize=(9, 5))

stages = ['Raw data\ncollected', 'After\nQC filter', 'After alignment\nscore filter']
diseased = [15, 7, 5]
control = [12, 6, 6]
x = np.arange(len(stages))
w = 0.35

b1 = ax.bar(x - w/2, diseased, w, label='Diseased samples', color=CORAL, zorder=3, borderradius=3)
b2 = ax.bar(x + w/2, control, w, label='Control samples', color=TEAL, zorder=3)

for bar in list(b1) + list(b2):
    ax.annotate(str(int(bar.get_height())),
                xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                xytext=(0, 5), textcoords='offset points',
                ha='center', fontsize=11, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(stages)
ax.set_ylabel('Number of samples')
ax.set_ylim(0, 20)
ax.set_title('Sample count through the RNA-Seq QC and alignment pipeline\n(Ovarian cancer vs healthy controls)', fontsize=12, pad=12)
ax.legend()
ax.text(0.99, 0.02, SOURCE, transform=ax.transAxes, fontsize=8, color='gray', ha='right')
plt.tight_layout()
plt.savefig('charts/chart1_qc_pipeline.png', bbox_inches='tight')
print("Saved: chart1_qc_pipeline.png")
plt.close()


# ── Chart 2: HISAT2 alignment scores ──────────────────────────────────────────

fig, ax = plt.subplots(figsize=(10, 5))

d_ids = ['SRR25637181', 'SRR25637182', 'SRR25637208*', 'SRR25637216', 'SRR25637217', 'SRR25637220', 'SRR25637224*']
d_scores = [97.23, 97.56, 42.36, 96.88, 97.48, 97.86, 56.23]
c_ids = ['SRR10313349', 'SRR10313350', 'SRR10313351', 'SRR10313352', 'SRR10313353', 'SRR10313354']
c_scores = [96.30, 96.29, 96.48, 96.26, 96.42, 96.54]

x_d = np.arange(len(d_ids))
x_c = np.arange(len(c_ids))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

colors_d = [CORAL if s > 80 else '#F09595' for s in d_scores]
axes[0].bar(x_d, d_scores, color=colors_d, zorder=3)
axes[0].axhline(y=80, color='red', linestyle='--', alpha=0.6, label='Threshold (80%)')
axes[0].set_xticks(x_d)
axes[0].set_xticklabels(d_ids, rotation=35, ha='right', fontsize=9)
axes[0].set_ylim(0, 105)
axes[0].set_ylabel('Alignment score (%)')
axes[0].set_title('Diseased samples\n(* = excluded)', fontsize=11)
axes[0].legend(fontsize=9)
axes[0].grid(alpha=0.25, linestyle='--')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
for i, v in enumerate(d_scores):
    axes[0].text(i, v + 1, f'{v}%', ha='center', fontsize=8)

axes[1].bar(x_c, c_scores, color=TEAL, zorder=3)
axes[1].axhline(y=80, color='red', linestyle='--', alpha=0.6, label='Threshold (80%)')
axes[1].set_xticks(x_c)
axes[1].set_xticklabels(c_ids, rotation=35, ha='right', fontsize=9)
axes[1].set_ylim(0, 105)
axes[1].set_ylabel('Alignment score (%)')
axes[1].set_title('Control samples\n(all passed QC)', fontsize=11)
axes[1].legend(fontsize=9)
axes[1].grid(alpha=0.25, linestyle='--')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
for i, v in enumerate(c_scores):
    axes[1].text(i, v + 1, f'{v}%', ha='center', fontsize=8)

fig.suptitle('HISAT2 alignment scores — diseased vs control samples\n(Reference genome: ENSEMBL GRCh38)', fontsize=12, y=1.02)
fig.text(0.99, -0.06, SOURCE, fontsize=8, color='gray', ha='right')
plt.tight_layout()
plt.savefig('charts/chart2_alignment_scores.png', bbox_inches='tight')
print("Saved: chart2_alignment_scores.png")
plt.close()


# ── Chart 3: Hub gene interaction degrees ─────────────────────────────────────

fig, ax = plt.subplots(figsize=(9, 5))

genes = ['CDKN1A\n(Ferroptosis)', 'JUN\n(Apoptosis)', 'CCL2\n(Apoptosis)',
         'GDF15\n(Ferroptosis)', 'BTG2\n(Apoptosis)', 'FOSL1\n(Apoptosis)',
         'IER3\n(Apoptosis)', 'CYCS\n(Apoptosis)', 'HSPA1B\n(Apoptosis)', 'S100A11\n(Apoptosis)']
degrees = [23, 18, 15, 10, 8, 8, 8, 8, 5, 4]
colors = [CORAL if 'Ferroptosis' in g else TEAL for g in genes]

bars = ax.barh(genes, degrees, color=colors, zorder=3, height=0.6)

for bar, val in zip(bars, degrees):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
            str(val), va='center', fontsize=10, fontweight='bold')

ax.set_xlabel('Number of interactions (degree)')
ax.set_title('Hub gene interaction degrees in co-expressed\nferroptosis–apoptosis network', fontsize=12, pad=12)
ax.set_xlim(0, 28)

legend_items = [
    mpatches.Patch(color=CORAL, label='Ferroptosis gene'),
    mpatches.Patch(color=TEAL, label='Apoptosis gene')
]
ax.legend(handles=legend_items, loc='lower right')
ax.text(0.99, 0.02, SOURCE, transform=ax.transAxes, fontsize=8, color='gray', ha='right')
plt.tight_layout()
plt.savefig('charts/chart3_hub_gene_degrees.png', bbox_inches='tight')
print("Saved: chart3_hub_gene_degrees.png")
plt.close()


# ── Chart 4: KEGG pathway gene involvement ────────────────────────────────────

fig, ax = plt.subplots(figsize=(10, 5))

pathways = [
    'Pathways in cancer',
    'Colorectal cancer',
    'Small cell lung cancer',
    'Human T-cell\nleukemia virus 1',
    'Renal cell carcinoma',
    'Platinum drug resistance',
    'p53 signalling pathway'
]
gene_counts = [4, 3, 3, 3, 2, 2, 2]
highlight = ['Platinum drug resistance', 'p53 signalling pathway']
colors_k = [CORAL if p.strip() in highlight else PURPLE for p in pathways]

bars = ax.barh(pathways, gene_counts, color=colors_k, zorder=3, height=0.55)

for bar, val in zip(bars, gene_counts):
    ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
            f'{val} gene{"s" if val > 1 else ""}', va='center', fontsize=10)

ax.set_xlabel('Number of hub genes in pathway')
ax.set_title('KEGG pathway enrichment of co-expressed ferroptosis–apoptosis hub genes\n(highlighted = clinically significant to ovarian cancer therapy)', fontsize=11, pad=12)
ax.set_xlim(0, 6)

legend_items = [
    mpatches.Patch(color=CORAL, label='Clinically significant pathway'),
    mpatches.Patch(color=PURPLE, label='Other cancer pathway')
]
ax.legend(handles=legend_items, loc='lower right')
ax.text(0.99, 0.02, SOURCE, transform=ax.transAxes, fontsize=8, color='gray', ha='right')
plt.tight_layout()
plt.savefig('charts/chart4_kegg_pathways.png', bbox_inches='tight')
print("Saved: chart4_kegg_pathways.png")
plt.close()


# ── Chart 5: DEG filtering funnel ─────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(8, 5))

stages_f = ['Total DEGs\n(with ref GTF)', 'Significant\n(p < 0.05)', 'Highly significant\n(p < 0.01)', 'Ferroptosis +\nApoptosis genes']
counts = [7862, 8002, 6577, 289]
colors_f = [LIGHT, TEAL, TEAL, CORAL]

bars = ax.bar(stages_f, counts, color=colors_f, zorder=3, width=0.5)

for bar, val in zip(bars, counts):
    ax.annotate(f'{val:,}',
                xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                xytext=(0, 6), textcoords='offset points',
                ha='center', fontsize=11, fontweight='bold')

ax.set_ylabel('Number of genes')
ax.set_title('Differential gene expression filtering funnel\n(from raw count to ferroptosis + apoptosis candidate genes)', fontsize=12, pad=12)
ax.text(0.99, 0.02, SOURCE, transform=ax.transAxes, fontsize=8, color='gray', ha='right')
plt.tight_layout()
plt.savefig('charts/chart5_deg_funnel.png', bbox_inches='tight')
print("Saved: chart5_deg_funnel.png")
plt.close()

print("\nAll 5 charts generated in charts/ folder.")
