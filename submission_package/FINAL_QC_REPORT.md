# FINAL_QC_REPORT.md — Fixed QC gate, Paper 3/3 (MTSR)

Manuscript: "The Reincarnation of the Divine: The Vortex of One and Many in Ever-Changing Worlds"
Baseline: `submission_package/` rebuilt from `manuscript/manuscript.md`, `refs/references.md`,
`figures/make_figures.py`, `scripts/build_docx.py` on branch `devin/1791016708-one-many-vortex` (bougtoir/wip).
Audit date: 2026-10-28. Target journal: *Method & Theory in the Study of Religion* (Brill, author–date style).

## Summary table

| QC item | Status | Evidence | Fix |
|---|---|---|---|
| Hostile review (Part 1, A–J) | PASS AFTER FIX | FINAL_HOSTILE_REVIEW.md; all 10 attack fronts answered from text or fixed | Citation completions only; no conceptual change |
| Hardcode audit (Part 6) | PASS (empirical: N/A) | FINAL_HARDCODE_AUDIT.md; full numeric inventory | w_ij subscript; word-count claim corrected |
| Public-code reproduction (Part 7) | PASS (scientific results: N/A) | Scripts exist at `one_many_vortex/{figures,scripts}` in bougtoir/wip @ this commit; `make_figures.py` regenerated 5/5 PNGs byte-identical to packaged copies; `build_docx.py` regenerated all 4 DOCX | none needed after verification |
| Reference existence (Part 4) | PASS AFTER FIX | 14/14 DOIs checked against Crossref; 4 DOIs were wrong and corrected; non-DOI items covered by `reports/reference_validation.md` (catalog/publisher verification) | Assmann→10.2307/2928707; Bellah→10.2307/2091480; Ginges→10.1073/pnas.0701768104; Turchin→10.21237/C7clio6127917 |
| Bibliography→text (Part 3A) | PASS AFTER FIX | 52 entries; 2 orphans found (J. Z. Smith 1982, Lang 1898) | both now cited in §1 |
| Text→bibliography (Part 3B) | PASS | Every author–year pair in text resolves to an entry (verified by script) | — |
| Retraction audit (Part 5) | PASS | Whitehouse et al. 2019 *Nature* 568 is RETRACTED (Crossref flags "RETRACTED ARTICLE"); cited only as the retracted precursor of Whitehouse et al. 2023 "Retake" + Beheim 2021 critique; labeled in text and bibliography | — |
| Figure citation (Part 8) | PASS | Figures 1–5 each cited in text | — |
| Table citation (Part 8) | PASS | Tables 1–4 each cited in text | — |
| Figure order (Part 9) | PASS | First citations: Fig1 §2 → Fig2 §4 → Fig3 §5 → Fig4 §7 → Fig5 §11 | — |
| Table order (Part 9) | PASS | First citations: T1 §1 → T2 §2 → T3 §10 → T4 §11 | — |
| Text/figure/table numeric consistency (Part 10) | PASS | 7 hypotheses in text = 7 rows in Table 4; 9 falsification conditions counted; 10-component state vector = 10 axes in Fig 5; 4 cases | — |
| OMML (Part 11) | PASS | 47 `<m:oMath>` equations in each manuscript DOCX; 0 residual `$`, `\mathrm`, ASCII pseudo-math in prose (w_ij in Table 2 now a real subscript run) | w_ij fix |
| Asterisk / Markdown residue (Part 12) | PASS | 0 `**`, 0 backticks, 0 heading markers in rendered DOCX text/XML | — |
| Manual line breaks / char-count wrapping (Part 13) | PASS | 0 `<w:br>` elements in all 4 DOCX; paragraphs rely on Word layout | — |
| Full visual page review (Part 14) | PASS | 35-page PDF render, all pages inspected; no clipped text/equations, no off-page objects, no blank pages, no orphan headings; tables legible; figs embedded at first-citation points | — |
| Journal reference style (Part 15) | PASS AFTER FIX | MTSR uses author–date alphabetical references (Chicago-like, Brill); list is alphabetical; Klostermaier/Lang order repaired | order fix applied |
| Placeholders (Part 18) | AUTHOR ACTION | Title page: [Author name], [Affiliation], [ORCID], [Corresponding author…], funding/acknowledgment fields; cover letter signature block | author must fill |
| Cover letter (Part 17) | PASS AFTER FIX | Single-author "I" throughout; exact title & journal names; calibrated claims; no tracked changes/comments; word count corrected to ~5,700 | word-count fix |
| Title page | PASS (with AUTHOR ACTION placeholders) | Title, journal, word count correct; author metadata intentionally blank | — |

## Part 4 — Reference existence detail

DOI-bearing entries verified programmatically against `api.crossref.org/works/<doi>`
(title, container, volume, issue, pages compared):

| Entry | DOI | Crossref result | Classification |
|---|---|---|---|
| Assmann 1996, *Representations* 56: 48–67 | 10.2307/2928707 (was 2928715 → pointed at a different article) | matches | VERIFIED WITH METADATA CORRECTION |
| Atran & Ginges 2012, *Science* 336(6083) | 10.1126/science.1216902 | matches | VERIFIED |
| Barrett & Keil 1996, *Cognitive Psychology* 31(3) | 10.1006/cogp.1996.0017 | matches | VERIFIED |
| Beheim et al. 2021, *Nature* 595 | 10.1038/s41586-021-03655-4 | matches | VERIFIED |
| Bellah 1964, *ASR* 29(3): 358–374 | 10.2307/2091480 (was 2091929 → wrong article) | matches | VERIFIED WITH METADATA CORRECTION |
| Floridi 2008, *Minds and Machines* 18 | 10.1007/s11023-008-9113-7 | matches | VERIFIED |
| Ginges et al. 2007, *PNAS* 104(18): 7357–7360 | 10.1073/pnas.0701768104 (was 0700591104 → wrong article) | matches | VERIFIED WITH METADATA CORRECTION |
| Hedges 2025, *JAAR* 92(2) | 10.1093/jaarel/lfae078 | matches | VERIFIED |
| Slingerland et al. 2024, *RBB* 14(2) | 10.1080/2153599X.2023.2200825 | matches | VERIFIED |
| Steinhart 2013, *Religious Studies* 49(3) | 10.1017/S0034412512000285 | matches | VERIFIED |
| Turchin et al. 2015, *Cliodynamics* 6(1) | 10.21237/C7clio6127917 (was …6127693 → 404) | matches | VERIFIED WITH METADATA CORRECTION |
| Watts et al. 2015, *Proc. R. Soc. B* 282 | 10.1098/rspb.2014.2556 | matches | VERIFIED |
| Whitehouse et al. 2019, *Nature* 568 | 10.1038/s41586-019-1043-4 | matches; Crossref title prefixed "RETRACTED ARTICLE" | VERIFIED — RETRACTED (labeled in ms & bib) |
| Whitehouse et al. 2023, *RBB* 13(2) | 10.1080/2153599X.2022.2074085 | matches | VERIFIED |

Non-DOI entries (books, Vatican instructions, 19th–20th c. works): covered by
`reports/reference_validation.md` (publisher/catalog verification, Phase 1) —
all VERIFIED; none unverifiable.

## Part 7 — Reproducibility decision

**Public-code scientific reproduction: N/A for scientific results** — the paper reports no
computational analysis or empirical results.

**Figure/document generation reproducibility: VERIFIED.**
Commands run on this branch:

```
python3 figures/make_figures.py   # → 5 PNGs, md5-identical to submission_package/figures/
python3 scripts/build_docx.py     # → manuscript_inline_FINAL.docx, manuscript_clean_FINAL.docx,
                                #    cover_letter_FINAL.docx, title_page_FINAL.docx
```

Dependencies installed: python-docx, latex2mathml, docx-equation, python-pptx, matplotlib.

## Part 14 — Visual page audit

35-page PDF (LibreOffice render of `manuscript_inline_FINAL.docx`), every page inspected:
no clipped text or equations; tables 1–4 render within margins; figures 1–5 embedded at their
first-citation points and legible at 300-dpi source; references hang correctly; consistent
TNR; no colored text; no broken references. One cosmetic note: a large table pushes a
fractional blank region onto the preceding page bottom (normal Word pagination, not a defect).

## Fixes applied in this gate (chronological)

1. §1: added `(Lang 1898)` after `Lang's "high gods"`.
2. §1: added `J. Z. Smith (1982)` to the manufactured-categories citation cluster.
3. `refs/references.md`: Klostermaier moved before Lang (alphabetical); 4 DOIs corrected.
4. `manuscript/cover_letter.md`, `scripts/build_docx.py`: word count 7,100 → ~5,700.
5. `scripts/build_docx.py`: `manuscript_clean_FINAL.docx` now omits embedded figure images
   (matches README "text without embedded objects"); Table 2 `w_ij` renders as italic w +
   subscript ij.
