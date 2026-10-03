#!/usr/bin/env python3
"""Generate Figures 1-5 for the One/Many vortex manuscript."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle
import numpy as np

plt.rcParams.update({"font.family": "serif", "font.size": 9, "figure.dpi": 300})
OUT = "figures"

# ---------- Figure 1: same semantic space, different divine architectures ----------
fig, axes = plt.subplots(1, 3, figsize=(9, 3.2))
feats = ["creation", "justice", "fertility", "war", "knowledge", "death",
         "protection", "order"]
np.random.seed(7)

def draw_cells(ax, groups):
    n = len(feats)
    for i, f in enumerate(feats):
        ax.text(-0.05, i + 0.5, f, ha="right", va="center", fontsize=7.5)
    colors = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51", "#8ab17d"]
    ax.set_xlim(-0.2, len(groups))
    for j, (gname, cells) in enumerate(groups):
        ax.text(j + 0.5, n + 0.15, gname, ha="center", va="bottom", fontsize=8,
                fontweight="bold")
        for i in cells:
            ax.add_patch(Rectangle((j, i), 1, 1, facecolor=colors[j % len(colors)],
                                   alpha=0.35, edgecolor="k", lw=0.5))

# A: one bundled agent
ax = axes[0]
draw_cells(ax, [("G*", list(range(8)))])
ax.set_title("A. Bundled agent", fontsize=9)
# B: hierarchy: one top agent covers order/justice/protection, two sub gods
ax = axes[1]
draw_cells(ax, [("G1*", [7, 1, 6]), ("g2", [0, 4]), ("g3", [2, 3, 5])])
ax.set_title("B. Hierarchical architecture", fontsize=9)
# C: specialized agents
ax = axes[2]
draw_cells(ax, [("g1", [0, 7]), ("g2", [1]), ("g3", [2, 6]),
                ("g4", [3]), ("g5", [4]), ("g6", [5])])
ax.set_title("C. Specialized agents", fontsize=9)
for ax in axes:
    ax.set_ylim(0, len(feats) + 0.6)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
fig.suptitle("Same semantic feature space, different divine architectures",
             fontsize=10, y=0.02)
fig.tight_layout(rect=[0, 0.06, 1, 1])
fig.savefig(f"{OUT}/fig1_architectures.png", bbox_inches="tight")
plt.close(fig)

# ---------- Figure 2: the vortex (spiral, path-dependent) ----------
fig, ax = plt.subplots(figsize=(6.4, 6.4))
phases = ["Differentiation", "Hierarchization", "Aggregation",
          "Authoritative unity", "Internal differentiation",
          "Interpretive\nmultiplication", "Reintegration",
          "Renewed\ndifferentiation", "Re-aggregation\n(transformed)"]
N = len(phases)
theta = np.linspace(0.3, 4.6 * np.pi, 400)
r = 0.25 + 0.06 * theta
x = r * np.cos(theta); y = r * np.sin(theta)
ax.plot(x, y, color="#264653", lw=1.6)
idx = np.linspace(20, len(theta) - 20, N).astype(int)
for i, p in zip(idx, phases):
    ax.add_patch(Circle((x[i], y[i]), 0.05, color="#e76f51", zorder=5))
    dx, dy = x[i], y[i]
    L = 0.55
    ux, uy = dx / np.hypot(dx, dy), dy / np.hypot(dx, dy)
    tx, ty = dx + L * ux, dy + L * uy
    ax.text(tx, ty, p, ha="center", va="center", fontsize=8)
# arrowhead at end
ax.annotate("", xy=(x[-1], y[-1]), xytext=(x[-25], y[-25]),
            arrowprops=dict(arrowstyle="-|>", color="#264653", lw=1.6))
ax.text(0.3, -0.45, "X(t+n) ≠ X(t):\neach return carries deposits\n(texts, precedents, institutions)",
        ha="center", fontsize=8, style="italic", color="#333")
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("The Vortex of One and Many (path-dependent, non-closed)",
             fontsize=10, pad=10)
fig.savefig(f"{OUT}/fig2_vortex.png", bbox_inches="tight")
plt.close(fig)

# ---------- Figure 3: representational inversion (3 stacked rows) ----------
fig, ax = plt.subplots(figsize=(9.2, 3.6))
rows = [
    ("Stage 1: representation carries norm",
     ["Problem(t)", "Norm(t)", "Divine\nrepresentation"]),
    ("Stage 2: inversion (norm grounded in divine will)",
     ["Divine\nauthority", "Norm(t)"]),
    ("Stage 3: temporal extension under novelty",
     ["Problem(t+1)", "Divine\nauthority", "Authorized\ninterpretation",
      "Norm(t+1)"]),
]
bw, bh = 0.13, 0.16
for ri, (title, items) in enumerate(rows):
    y = 0.72 - ri * 0.30
    ax.text(0.02, y + bh + 0.025, title, fontsize=8.5, fontweight="bold",
            transform=ax.transAxes)
    x = 0.02
    for k, it in enumerate(items):
        ax.add_patch(mp.FancyBboxPatch((x, y), bw, bh,
                     boxstyle="round,pad=0.012", fc="#eef3f5", ec="#264653",
                     transform=ax.transAxes))
        ax.text(x + bw / 2, y + bh / 2, it, ha="center", va="center",
                fontsize=7.5, transform=ax.transAxes)
        if k < len(items) - 1:
            ax.annotate("", xy=(x + bw + 0.038, y + bh / 2),
                        xytext=(x + bw + 0.004, y + bh / 2),
                        xycoords="axes fraction", textcoords="axes fraction",
                        arrowprops=dict(arrowstyle="-|>", lw=1.1, color="#444"))
        x += bw + 0.042
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ax.set_title("Representational inversion and temporal authority extension",
             fontsize=10)
fig.savefig(f"{OUT}/fig3_inversion.png", bbox_inches="tight")
plt.close(fig)

# ---------- Figure 4: historical novelty — two paths ----------
fig, ax = plt.subplots(figsize=(8.8, 4.2))
ax.add_patch(mp.FancyBboxPatch((0.02, 0.42), 0.18, 0.16, boxstyle="round,pad=0.015",
                               fc="#e9c46a", ec="k", transform=ax.transAxes))
ax.text(0.11, 0.50, "Historical novelty\nProblem(t+1)", ha="center", va="center",
        fontsize=8.5, transform=ax.transAxes)

def path(y, label, items, color):
    ax.annotate("", xy=(0.26, y + 0.08), xytext=(0.21, 0.50),
                xycoords="axes fraction", textcoords="axes fraction",
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color="#444"))
    ax.text(0.24, y + 0.22, label, fontsize=8.5, fontweight="bold",
            color=color, transform=ax.transAxes)
    x = 0.26
    for k, it in enumerate(items):
        ax.add_patch(mp.FancyBboxPatch((x, y), 0.155, 0.16,
                     boxstyle="round,pad=0.012", fc="#eef3f5", ec=color,
                     transform=ax.transAxes))
        ax.text(x + 0.077, y + 0.08, it, ha="center", va="center", fontsize=7,
                transform=ax.transAxes)
        if k < len(items) - 1:
            ax.annotate("", xy=(x + 0.185, y + 0.08), xytext=(x + 0.157, y + 0.08),
                        xycoords="axes fraction", textcoords="axes fraction",
                        arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#444"))
        x += 0.185

path(0.66, "Path A — Authority-scope release",
     ["Internalization", "Functional\nrelease", "Normative\nadaptation"], "#2a9d8f")
path(0.16, "Path B — Authority extension",
     ["Authorized\ninterpretation", "Interpretive\nmultiplication",
      "Plurality /\nschism /\nreintegration"], "#e76f51")
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ax.set_title("Historical novelty as an engine of the vortex: two pathways",
             fontsize=10)
fig.savefig(f"{OUT}/fig4_paths.png", bbox_inches="tight")
plt.close(fig)

# ---------- Figure 5: multidimensional state space (radar) ----------
dims = ["A_eff\nagent diversity", "B\nbundling", "D\nfunct. diff.",
        "N\nnarrative diff.", "I\ninterp. central.",
        "U\njurisdiction", "E\nexclusivity", "R_eff\ninterpreters",
        "L\ninterp. load", "J\nscope"]
t1 = [0.25, 0.9, 0.35, 0.4, 0.85, 0.9, 0.9, 0.6, 0.7, 0.9]
t2 = [0.85, 0.3, 0.85, 0.8, 0.3, 0.4, 0.25, 0.35, 0.3, 0.35]
t3 = [0.55, 0.6, 0.6, 0.65, 0.55, 0.6, 0.45, 0.7, 0.55, 0.6]
angles = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist()
fig = plt.figure(figsize=(6.2, 5.6))
ax = fig.add_subplot(111, polar=True)
for vals, lab, c in [(t1, "Centralized monotheistic profile", "#e76f51"),
                     (t2, "Distributed polytheistic profile", "#264653"),
                     (t3, "Hybrid / register-split profile", "#2a9d8f")]:
    v = vals + vals[:1]
    ax.plot(angles + angles[:1], v, color=c, lw=1.6, label=lab)
    ax.fill(angles + angles[:1], v, color=c, alpha=0.08)
ax.set_xticks(angles); ax.set_xticklabels(dims, fontsize=6.8)
ax.set_yticklabels([]); ax.set_ylim(0, 1)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.04), fontsize=8, ncol=1,
          frameon=False)
ax.set_title("Divine representation as a multidimensional state vector,\n"
             "not a position on one One–Many axis\n"
             "(schematic illustration — values are not empirical estimates)",
             fontsize=9, pad=18)
fig.savefig(f"{OUT}/fig5_statespace.png", bbox_inches="tight")
plt.close(fig)
print("figures written")
