#!/usr/bin/env python3
"""Generate Figures 1-5 for the One/Many vortex manuscript."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle
import numpy as np

import os
DPI = int(os.environ.get("FIG_DPI", "300"))
FONT = os.environ.get("FIG_FONT")
plt.rcParams.update({"font.family": "serif", "font.size": 9, "figure.dpi": DPI})
if FONT:
    plt.rcParams["font.serif"] = [f.strip() for f in FONT.split(",")]
    plt.rcParams["mathtext.fontset"] = "stix"
OUT = os.environ.get("FIG_OUT", "figures")

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
fig.tight_layout()
fig.savefig(f"{OUT}/fig1_architectures.png", bbox_inches="tight")
plt.close(fig)

# ---------- Figure 2: the vortex (open spiral, path-dependent) ----------
# Ordered nodes on an outward Archimedean spiral; an arrowhead on every
# segment makes the traversal direction unambiguous. The spiral is open:
# the terminal state does not coincide with the initial state.
fig, ax = plt.subplots(figsize=(6.8, 6.8))
phases = ["Differentiation", "Hierarchization", "Aggregation",
          "Authoritative\nunity", "Internal\ndifferentiation",
          "Interpretive\nmultiplication", "Reintegration",
          "Renewed\ndifferentiation", "Re-aggregation\n(transformed)"]
N = len(phases)
B = 0.075  # radial growth per radian: inter-arm gap = 2*pi*B ~ 0.47
theta = np.linspace(0.2 * np.pi, 4.2 * np.pi, 2000)
r = 0.12 + B * theta
x = r * np.cos(theta); y = r * np.sin(theta)
ax.plot(x, y, color="#264653", lw=1.4, zorder=1)

def pt(th):
    rr = 0.12 + B * th
    return rr * np.cos(th), rr * np.sin(th)

node_theta = np.linspace(1.35, 12.7, N)
# arrowheads at the midpoint of every inter-node segment, all pointing
# in the direction of travel (outward, counter-clockwise)
for i in range(1, N):
    tm = 0.5 * (node_theta[i - 1] + node_theta[i])
    x1, y1 = pt(tm - 0.055); x2, y2 = pt(tm + 0.055)
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), zorder=3,
                arrowprops=dict(arrowstyle="-|>", color="#264653",
                                lw=1.6, mutation_scale=15))
# arrowhead entering the terminal node
ax.annotate("", xy=pt(node_theta[-1] - 0.015),
            xytext=pt(node_theta[-1] - 0.12),
            arrowprops=dict(arrowstyle="-|>", color="#264653",
                            lw=1.6, mutation_scale=15), zorder=3)
for i, (th, label) in enumerate(zip(node_theta, phases), start=1):
    nx, ny = pt(th)
    ax.add_patch(Circle((nx, ny), 0.065, color="#e76f51", zorder=5))
    ax.text(nx, ny, str(i), ha="center", va="center", fontsize=8,
            fontweight="bold", color="white", zorder=7)
    ux, uy = nx / np.hypot(nx, ny), ny / np.hypot(nx, ny)
    lx, ly = nx + 0.30 * ux, ny + 0.30 * uy
    ax.plot([nx + 0.07 * ux, lx - 0.05 * ux],
            [ny + 0.07 * uy, ly - 0.05 * uy],
            color="#999", lw=0.7, zorder=4)
    ax.text(lx, ly, label,
            ha="center", va="center", fontsize=8, zorder=6,
            bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.15))
ax.text(0, 0, os.environ.get("FIG2_CENTER", "X_(t+n) != X_t"), ha="center", va="center",
        fontsize=9.5, style="italic", color="#333")
ax.set_aspect("equal"); ax.axis("off")
fig.savefig(f"{OUT}/fig2_vortex.png", bbox_inches="tight")
plt.close(fig)

# ---------- Figure 3: representational inversion (3 stacked rows) ----------
fig, ax = plt.subplots(figsize=(9.2, 3.6))
rows = [
    ("1 Representation",
     ["Problem(t)", "Norm(t)", "Divine\nrepresentation"]),
    ("2 Inversion",
     ["Divine\nauthority", "Norm(t)"]),
    ("3 Temporal extension",
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
fig.savefig(f"{OUT}/fig5_statespace.png", bbox_inches="tight")
plt.close(fig)
print("figures written")
