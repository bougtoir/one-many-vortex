# The Reincarnation of the Divine: The Vortex of One and Many in Ever-Changing Worlds

Paper 3 of 3 — a theory-of-religion manuscript targeting *Method & Theory in the
Study of Religion* (Brill, author–date references). LOCKED submission package
(final fixed-QC gate, 2026-10-28).

## Submission package

| File | Contents |
|---|---|
| `manuscript_inline_FINAL.docx` | Main manuscript, TNR 12pt, inline figures + tables at first-citation points, 47 OMML equations |
| `manuscript_clean_FINAL.docx` | Same text without embedded figure images (tables kept as text) |
| `title_page_FINAL.docx` | Title, author/affiliation/ORCID placeholders (AUTHOR ACTION), abstract keywords, word count |
| `cover_letter_FINAL.docx` | Cover letter to the MTSR editors |
| `figures/fig1–fig5.png` | Standalone 300-dpi figures |
| `figures_FINAL.pptx` | Editable-caption figure deck (5 slides) |
| `tables/tables_FINAL.docx` + `table1–4_FINAL.csv` | Standalone tables |
| `reports/` | GO/journal-fit/citation-ecology/reference-validation/QC reports |
| `FINAL_HOSTILE_REVIEW.md`, `FINAL_HARDCODE_AUDIT.md`, `FINAL_QC_REPORT.md`, `FINAL_HANDOFF.txt` | Final fixed-QC gate outputs (also under `reports/`) |

## Final QC gate (this package)

Four audit documents at package root record the fixed-gate results:
hostile review (PASS AFTER FIX), hardcode audit (no empirical results; Figure 5
schematic), reference audit (14/14 DOIs Crossref-verified, 4 metadata corrections
applied; Whitehouse 2019 retracted + labeled), full correspondence/order/OMML/
residue/visual checks. Fixes applied: Lang 1898 + J. Z. Smith 1982 citations,
alphabetical order, 4 DOI corrections, word-count correction (~5,700), clean-DOCX
embedded-object removal, w_ij subscript.

## Working files (in repo `one_many_vortex/`, bougtoir/wip)

- `manuscript/manuscript.md`, `manuscript/cover_letter.md` — sources
- `refs/references.md` — verified author–date reference list (works cited only)
- `figures/make_figures.py` — regenerates all figures (verified byte-identical)
- `scripts/build_docx.py` + `scripts/docx_math.py` — regenerates all DOCX
  (OMML via latex2mathml → mathml_to_omml)
- `docs/` — process documents: `prior_art.md`, `go_modify_nogo.md`,
  `journal_selection.md`, `cases_and_model.md`, `prompt.txt`

## Rebuild

```
python3 figures/make_figures.py
python3 scripts/build_docx.py   # requires python-docx, latex2mathml, docx-equation, matplotlib
```

Theory paper: no empirical dataset is shipped; the W-matrix is a conceptual
instrument (see `docs/cases_and_model.md`). Public-code scientific reproduction:
N/A; figure/document regeneration verified — see FINAL_QC_REPORT.md Part 7.
