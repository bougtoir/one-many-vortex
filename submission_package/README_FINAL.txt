# The Reincarnation of the Divine: The Vortex of One and Many in Ever-Changing Worlds

Paper 3 of 3 — a theory-of-religion manuscript targeting *Method & Theory in the Study of Religion* (Brill/NAASR).

## Submission package (`submission_package/`)

| File | Contents |
|---|---|
| `manuscript_inline.docx` | Main manuscript, TNR 12pt, inline figures + tables, OMML equations, author–date references |
| `manuscript_clean.docx` | Same text without embedded objects (for reviewers who want text-only) |
| `title_page.docx` | Title, author/affiliation placeholders, abstract, keywords, word count |
| `cover_letter.docx` | Cover letter to the MTSR editors |
| `figures/fig1–fig5.png` | Standalone 300-dpi figures |
| `figures.pptx` | Editable-caption figure deck |
| `reports/` | GO report, journal-selection report, reference-validation report, reviewer critique, final QC report |

## Working files

- `manuscript/manuscript.md`, `manuscript/cover_letter.md` — sources
- `refs/references.md` — verified author–date reference list
- `figures/make_figures.py` — regenerates all figures
- `scripts/build_docx.py` + `scripts/docx_math.py` — regenerates all DOCX (OMML via latex2mathml → mathml_to_omml)
- `docs/` — process documents: `prior_art.md`, `go_modify_nogo.md`, `journal_selection.md`, `cases_and_model.md`, `prompt.txt`

## Rebuild

```
python3 figures/make_figures.py
python3 scripts/build_docx.py   # requires python-docx, latex2mathml, docx-equation, matplotlib
```

Theory paper: no empirical dataset is shipped; the W-matrix is a conceptual instrument (see `docs/cases_and_model.md`, Phase 5).
