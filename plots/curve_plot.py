import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, average_precision_score, roc_curve, roc_auc_score

# ========= THEME =========
FIG_BG   = "#0b1020"   # dark figure background
AX_BG    = "#141e2f"   # slightly brighter subplot background
FG       = "#e6f7ff"   # bright foreground (text/ticks)
AXIS_CLR = "#8bd3ff"   # axis lines at 0
PALETTE  = ["#00e5ff", "#ff6ad5", "#ffd166"]  # bright line colors

LINE_KW  = dict(linewidth=3.0, solid_capstyle="round")

def minimal_axes(ax, title, xlabel, ylabel):
    ax.set_facecolor(AX_BG)
    for sp in ax.spines.values():
        sp.set_visible(False)
    # axes at 0 (x and y)
    ax.axhline(0, linewidth=1.2, color=AXIS_CLR, zorder=0)
    ax.axvline(0, linewidth=1.2, color=AXIS_CLR, zorder=0)
    # ticks only at 0 and 1; lock to [0,1]
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.tick_params(length=3, labelsize=10, colors=FG)
    ax.set_title(title, fontsize=12, pad=8, color=FG)
    ax.set_xlabel(xlabel, color=FG)
    ax.set_ylabel(ylabel, color=FG)

# ========= Synthetic scores for smooth curves =========
def simulate_scores(n=200_000, pos_rate=0.3, sep=1.5, seed=7):
    """
    Generate smooth PR/ROC curves by sampling scores from class-conditional Gaussians:
    negatives ~ N(-sep/2, 1), positives ~ N(+sep/2, 1).
    Larger 'sep' => easier classification (more 'ideal').
    """
    rng = np.random.default_rng(seed)
    n_pos = int(n * pos_rate)
    n_neg = n - n_pos
    pos = rng.normal(loc=+sep/2, scale=1.0, size=n_pos)
    neg = rng.normal(loc=-sep/2, scale=1.0, size=n_neg)
    y   = np.concatenate([np.ones(n_pos, dtype=int), np.zeros(n_neg, dtype=int)])
    s   = np.concatenate([pos, neg])
    return y, s

# Three “idealness” levels (increase sep for more ideal curves)
cases = [
    ("Fair (sep=0.7)", 0.7),
    ("Good (sep=1.5)", 1.5),
    ("Ideal (sep=3.0)", 3.0),
]

# ========= Compute curves =========
curves_pr  = []
curves_roc = []
for name, sep in cases:
    y, score = simulate_scores(n=300_000, pos_rate=0.2, sep=sep, seed=42+int(sep*10))
    # Precision–Recall
    prec, rec, _ = precision_recall_curve(y, score)       # sklearn PR curve
    ap = average_precision_score(y, score)                 # AP (area)
    curves_pr.append((name, rec, prec, ap))
    # ROC
    fpr, tpr, _ = roc_curve(y, score)                      # ROC curve
    auc = roc_auc_score(y, score)                          # AUC
    curves_roc.append((name, fpr, tpr, auc))

# ========= Plot (1×2) =========
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.patch.set_facecolor(FIG_BG)
plt.subplots_adjust(wspace=0.6)

# Left: Precision–Recall
for (name, rec, prec, ap), color in zip(curves_pr, PALETTE):
    axes[0].plot(rec, prec, color=color, label=f"{name} — AP {ap:.3f}", **LINE_KW)
# PR baseline = prevalence (optional, faint)
prevalence = 0.2
axes[0].plot([0, 1], [prevalence, prevalence], color=FG, alpha=0.25, linewidth=1.2)
minimal_axes(axes[0], "Precision–Recall", "Recall", "Precision")
axes[0].legend(facecolor=AX_BG, edgecolor="none", labelcolor=FG)

# Right: ROC
for (name, fpr, tpr, auc), color in zip(curves_roc, PALETTE):
    axes[1].plot(fpr, tpr, color=color, label=f"{name} — AUC {auc:.3f}", **LINE_KW)
# Chance diagonal (optional, faint)
axes[1].plot([0, 1], [0, 1], color=FG, alpha=0.25, linewidth=1.2)
minimal_axes(axes[1], "ROC", "FPR", "TPR")
axes[1].legend(facecolor=AX_BG, edgecolor="none", labelcolor=FG)

# Save with dark background preserved
plt.savefig("pr_roc_1x2_smooth_dark.png", dpi=600, facecolor=FIG_BG, edgecolor=FIG_BG, bbox_inches="tight")
plt.show()
print("Saved to pr_roc_1x2_smooth_dark.png")
