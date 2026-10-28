# FINAL_HARDCODE_AUDIT.md

Manuscript: "The Reincarnation of the Divine" — conceptual theory paper.
Audit date: 2026-10-28. Baseline: FINAL build in `submission_package/` and `build/`.

## A. Empirical-result hardcoding

**No empirical results are reported; empirical-result hardcoding is not applicable.**

The manuscript contains no dataset, no estimation, and no claimed measurements. Every formal quantity (W, A_eff, B, D, L, J, X_t, d, ΔI) is introduced as a conceptual instrument; §11 states "None of these arms is performed here."

## B. Schematic / illustrative value audit

Every number in the manuscript, tables, captions, figures, and equations was inventoried and classified:

| Value / location | Class | Status |
|---|---|---|
| Publication years in citations & bibliography (e.g. Tylor 1871, Lang 1898, Schmidt 1931) | bibliographic/historical | OK — Crossref/catalog-verified (see FINAL_QC_REPORT Part 4) |
| Donum Vitae 1987, Dignitas Personae 2008 | bibliographic/historical | OK |
| "1841/1989", "1922/1978" dual-dating (Feuerbach, Weber, Newman 1845/1989) | bibliographic convention | OK |
| Equation symbols & indices (w_ij, A_eff, B, D, N, I, U, E, R_eff, L, J; X_t, C_t, P_{t+1}, q_g, exp/ln/sum forms) | formula parameters / definitional | OK — 47 OMML equations, all definitional; no numeric RHS asserted |
| Figure 5 radar-chart profiles (three polygons over 10 axes) | schematic/illustrative | OK — title states "(schematic illustration — values are not empirical estimates)"; caption repeats it; §11 text says "purely illustratively" |
| Figure 1 cell shading (nonzero feature–agent associations) | schematic/illustrative | OK — binary presence/absence, caption says "schematic semantic feature space" |
| "four comparative cases", "H1–H7" (7 hypotheses), "nine falsification conditions", 10-component state vector | text-internal counts | OK — verified: 7 hypothesis rows in Table 4; 9 weakening conditions counted in §11 prose; state vector lists exactly 10 components matching Figure 5's 10 axes |
| "approximately 5,700 words" (title page, cover letter) | journal formatting | FIXED — was incorrectly "7,100"; actual main-text count ≈5,686 |
| Section numbers (§1–§11) | journal formatting | OK |
| Page geometry (TNR 12pt, 1-inch margins) | journal formatting | OK |

## Unsupported empirical-looking hardcoded values

**0 found.**

- No percentage, effect size, p-value, count of sources, or measurement appears anywhere in the manuscript, tables, or captions.
- All "data-like" visuals (Figures 1, 5) are explicitly labeled schematic.
- Table 1–4 contain only textual/conceptual content; the only digits are the H-numbers and years cited above.

## Notes

- `build/table2_FINAL.csv` previously wrote the feature–agent weight as ASCII `w_ij`; the DOCX build now renders it as italic w with a true subscript run (font-based, not Unicode). CSV text file keeps the ASCII spelling `w(i,j)` — a data-file convention, not typeset math.
