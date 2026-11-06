# one-many-vortex

Figure-generation code for a theoretical study of how divine unity and plurality are aggregated, differentiated, and reorganized across historical time.

The study is conceptual: it ships no empirical dataset, and the figures are schematic diagrams. This repository contains only the code needed to regenerate them.

## Contents

- `figures/make_figures.py` — generates Figures 1–5.

## Requirements

Python 3 with `matplotlib` and `numpy` (tested with matplotlib 3.10 and numpy 2.2).

## Usage

```
python3 figures/make_figures.py
```

Output is written to `figures/` as PNG at 300 dpi by default. Optional environment variables:

| Variable | Default | Effect |
|---|---|---|
| `FIG_DPI` | `300` | Output resolution |
| `FIG_OUT` | `figures` | Output directory |
| `FIG_FONT` | (matplotlib serif) | Comma-separated serif font list; also switches mathtext to STIX |
| `FIG2_CENTER` | `X_(t+n) != X_t` | Center label of Figure 2 (matplotlib mathtext allowed) |

Example (high-resolution TIFF-ready rendering):

```
FIG_DPI=1200 FIG_FONT="Times New Roman, Liberation Serif" FIG2_CENTER='$X(t+n) \neq X(t)$' python3 figures/make_figures.py
```
