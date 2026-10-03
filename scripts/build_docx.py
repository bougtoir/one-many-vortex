#!/usr/bin/env python3
"""Build submission docx files for the One/Many vortex manuscript.

Outputs (build/):
  manuscript_inline.docx   figures + tables embedded at first-citation points
  manuscript_clean.docx    same document (no tracked changes present)
  cover_letter.docx
  title_page.docx
Formatting: Times New Roman 12pt body, 10pt captions, OMML equations via $...$ tokens.
"""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import docx_math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build")
os.makedirs(BUILD, exist_ok=True)

FIGS = {
    "FIG1": ("figures/fig1_architectures.png",
             "Figure 1. Three partitions of the same schematic semantic feature "
             "space across divine agents. Shaded cells mark a nonzero feature-agent "
             "association: (A) one bundled agent; (B) a hierarchical architecture; "
             "(C) multiple specialized agents."),
    "FIG2": ("figures/fig2_vortex.png",
             "Figure 2. The Vortex of One and Many. Recurrent movement through "
             "differentiation, aggregation, authoritative unity, internal "
             "differentiation, interpretive multiplication, and reintegration; "
             "the spiral indicates path dependence — later states are never "
             "identical to earlier ones — since each return deposits texts, "
             "precedents, and institutions."),
    "FIG3": ("figures/fig3_inversion.png",
             "Figure 3. Representational inversion and temporal authority "
             "extension. A norm first carried by a divine representation becomes "
             "grounded in divine will (inversion); novel problems then route "
             "interpretation through the same authority."),
    "FIG4": ("figures/fig4_paths.png",
             "Figure 4. Historical novelty as the engine of the vortex. Path A: "
             "authority-scope release through internalization and functional "
             "release; Path B: authority extension through authorized "
             "interpretation and interpretive multiplication."),
    "FIG5": ("figures/fig5_statespace.png",
             "Figure 5. Divine representation as a multidimensional state vector. "
             "Monotheism and polytheism are not positions on a single axis but "
             "different vectors over analytically separable dimensions. The "
             "profiles shown are schematic illustrations only; values are not "
             "empirical estimates."),
}

TABLES = {
"TABLE1": ("Table 1. Nearest prior concepts and the novelty boundary.",
[["Concept", "Nearest prior literature", "Novelty boundary"],
 ["Directional Symmetry Test", "Teleology critique: Tylor, Schmidt, Bellah, Evans-Pritchard, Masuzawa", "The reversal test itself, as an operational device"],
 ["Aggregation/Differentiation operators", "Bellah (unidirectional differentiation); Luhmannian differentiation", "Symmetric operator pair over a representational architecture"],
 ["Representational granularity", "Hornung; Versnel; Floridi (levels of abstraction)", "Deity number as partition resolution of a feature space (W)"],
 ["Vortex", "Religious-cycle models; Sorokin-style oscillation; Bellah stages", "Path-dependent recurrence driven by historical novelty; non-closed"],
 ["Representational inversion", "Feuerbach; Big Gods (Norenzayan); Durkheim", "Direction-of-warrant reversal, not an origin claim"],
 ["Temporal authority extension", "Newman; usul al-fiqh (Hallaq); magisterial instructions", "Named mechanism linking novelty to differentiation"],
 ["Interpretive distance / load", "Hard cases in law; responsa literatures", "Distance from stabilization environment, not age"],
 ["Interpretive accumulation", "Newman's development notes; legal accretion", "Dual effect: stabilization + plurality generation"],
 ["Authority-scope release", "deus otiosus; Casanova's differentiation sub-thesis", "Jurisdiction relinquished while sacred standing persists"],
 ["Divine retirement", "deus otiosus (Eliade)", "Metaphor only; the operator is authority-scope release"]]),

"TABLE2": ("Table 2. Definitions of central concepts.",
[["Term", "Definition"],
 ["Semantic feature space (F)", "The set of attributes, functions, domains, and values a tradition predicates of the divine"],
 ["Divine agents (G)", "The agents to which features are assigned in a tradition's texts, rituals, and institutions"],
 ["Feature–agent matrix (W)", "Assignment weights w_ij linking each feature to each agent; the representational architecture"],
 ["Aggregation (A)", "Operator bundling a family of agents into a compressed representation"],
 ["Differentiation (D)", "Operator re-distributing features across agents, aspects, or interpretive lineages"],
 ["Representational inversion", "Shift from a norm carried by a divine representation to a norm authorized by divine will"],
 ["Historical novelty", "A change in the context vector generating problems outside the repertoire's stabilization environment"],
 ["Normative carryover problem", "Application of a stabilized norm to a materially different problem environment with no determined mapping"],
 ["Interpretive distance", "Distance between a novel problem and the repertoire's stabilization environment (not chronological age)"],
 ["Interpretive load", "Total interpretive work required to sustain continuity across an environmental shift"],
 ["Authorized interpretation", "Institutionally sanctioned derivation of binding norms from non-self-applying sources"],
 ["Interpretive accumulation", "The growing deposit of precedents, distinctions, commentaries, and rulings (ΔI per period)"],
 ["Authority-scope release", "Relinquishment of regulatory jurisdiction by an authority that retains sacred standing"],
 ["Vortex", "Path-dependent recurrence of aggregation and differentiation in which successive states are non-identical"],
 ["Directional Symmetry Test", "Audit requiring that directional descriptions support developmental claims only via direction-independent criteria"]]),

"TABLE3": ("Table 3. Comparative cases mapped to vortex operators.",
[["Case", "Operators instantiated", "Analytical function", "Key documentation"],
 ["Ancient Egypt (Amun-Re; Amarna; restoration)", "Aggregation, imposed compression, re-differentiation under memory", "Illustration; boundary case of imposed aggregation", "Hornung 1996; Assmann 1996, 2008; Baines 2000"],
 ["Israel/Judah (convergence–differentiation of Yahweh)", "Aggregation, differentiation, representational inversion, jurisdiction boundary", "Historical sequence evidence for both directions", "Smith 2001, 2002; Assmann 1996"],
 ["Greco-Roman late antiquity (henotheism, theos hypsistos, Neoplatonism)", "Register coexistence of One and Many without synthesis", "Counterexample to runaway aggregation", "Versnel 1990, 2011; Athanassiadi & Frede 1999; Mitchell & Van Nuffelen 2010"],
 ["Hindu traditions (Brahman/devas; sectarian theisms)", "Ontological unity as interpretive resource; recurrent re-specification", "Plausibility demonstration of recurrent specification", "Klostermaier 2007"],
 ["Structural illustrations (Islamic names & ijtihad; Christian doctrinal development)", "Authorized interpretation under novelty; interpretive accumulation", "Illustration of the temporal mechanism", "Hallaq 2001; Newman 1845; Donum Vitae 1987; Dignitas Personae 2008"]]),

"TABLE4": ("Table 4. Hypotheses and falsification conditions.",
[["#", "Hypothesis", "Falsified if"],
 ["H1", "Greater distance between novel problems and a repertoire's stabilization environment increases interpretive load", "Interpretive load does not covary with problem-environment distance"],
 ["H2", "Broader novel-domain jurisdiction of one divine authority increases the institutional importance of authorized interpretation", "Jurisdiction scope unrelated to interpretive institutionalization"],
 ["H3", "Underdetermination of inherited authority produces interpretive multiplication under ontological unity", "Unity consistently predicts interpretive unity under novelty"],
 ["H4", "Multiplication elicits reintegration where exclusivity, centralization, and uniformity incentives are jointly high", "Reintegration occurs independently of those three conditions"],
 ["H5", "Authority-scope release permits normative adaptation without equivalent growth of authorized interpretation", "Release cannot be identified, or adaptation always requires interpretation growth"],
 ["H6", "Interpretive accumulation both stabilizes tradition and increases defensible interpretive pathways", "Accumulation reduces plurality or destabilizes in all observed cases"],
 ["H7", "Sequences show recurrent aggregation and differentiation with non-identical successive states", "Recurrence is absent, or successive states prove identical"]]),
}

BOLD_RE = re.compile(r'\*\*([^*]+)\*\*')

def add_rich(p, text, font_size=None, base_bold=False):
    last = 0
    for m in BOLD_RE.finditer(text):
        if m.start() > last:
            docx_math.add_text_to_para(p, text[last:m.start()], bold=base_bold,
                                       font_size=font_size)
        r = p.add_run(m.group(1)); r.bold = True
        if font_size: r.font.size = Pt(font_size)
        last = m.end()
    if last < len(text):
        docx_math.add_text_to_para(p, text[last:], bold=base_bold,
                                   font_size=font_size)

def style_doc(doc):
    st = doc.styles['Normal']
    st.font.name = 'Times New Roman'
    st.font.size = Pt(12)
    st.paragraph_format.line_spacing = 2.0
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for s in doc.sections:
        s.left_margin = s.right_margin = Inches(1)
        s.top_margin = s.bottom_margin = Inches(1)

def caption(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text); r.font.size = Pt(10)
    return p

def add_table(doc, rows, cap):
    caption(doc, cap)
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = 'Table Grid'
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            c = t.cell(i, j)
            c.text = ''
            r = c.paragraphs[0].add_run(cell)
            r.font.size = Pt(10)
            if i == 0: r.bold = True
    doc.add_paragraph()

def add_fig(doc, key):
    path, cap = FIGS[key]
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(os.path.join(ROOT, path), width=Inches(5.6))
    caption(doc, cap)

def build_manuscript(out_name):
    doc = Document(); style_doc(doc)
    md = open(os.path.join(ROOT, "manuscript/manuscript.md")).read()
    refs = [l[2:].strip() for l in
            open(os.path.join(ROOT, "refs/references.md")).read().splitlines()
            if l.startswith("- ")]
    for block in md.split("\n\n"):
        block = block.strip()
        if not block: continue
        if block.startswith("<<") and block.endswith(">>"):
            key = block[2:-2]
            if key in FIGS: add_fig(doc, key)
            elif key in TABLES: cap, rows = TABLES[key]; add_table(doc, rows, cap)
            continue
        if block.startswith("# "):
            p = doc.add_paragraph()
            r = p.add_run(block[2:]); r.font.size = Pt(12)
        elif block.startswith("## References"):
            p = doc.add_paragraph(); r = p.add_run("References")
            for ref in refs:
                rp = doc.add_paragraph()
                rp.paragraph_format.left_indent = Inches(0.4)
                rp.paragraph_format.first_line_indent = Inches(-0.4)
                docx_math.add_text_to_para(rp, ref, font_size=12)
        elif block.startswith("## "):
            p = doc.add_paragraph()
            r = p.add_run(block[3:]); r.font.size = Pt(12)
        elif block.startswith("(assembled"):
            continue
        else:
            p = doc.add_paragraph()
            add_rich(p, " ".join(block.split()))
    doc.save(os.path.join(BUILD, out_name))
    print("wrote", out_name)

def build_cover_letter():
    doc = Document(); style_doc(doc)
    md = open(os.path.join(ROOT, "manuscript/cover_letter.md")).read()
    for block in md.split("\n\n"):
        block = block.strip()
        if not block: continue
        p = doc.add_paragraph()
        docx_math.add_text_to_para(p, " ".join(block.split()), font_size=12)
    doc.save(os.path.join(BUILD, "cover_letter_FINAL.docx"))
    print("wrote cover_letter_FINAL.docx")

def build_title_page():
    doc = Document(); style_doc(doc)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("The Reincarnation of the Divine: The Vortex of One and Many "
                  "in Ever-Changing Worlds"); r.bold = True; r.font.size = Pt(16)
    for line in ["", "[Author name]", "[Affiliation]", "[ORCID]",
                 "[Corresponding author: name, address, email]",
                 "Word count (main text): approximately 7,100",
                 "Target journal: Method & Theory in the Study of Religion",
                 "", "Declarations",
                 "Funding: [to be completed by author]",
                 "Conflicts of interest: none declared [confirm]",
                 "Acknowledgments: [optional — to be completed by author]",
                 ""]:
        q = doc.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
        q.add_run(line)
    doc.save(os.path.join(BUILD, "title_page_FINAL.docx"))
    print("wrote title_page_FINAL.docx")

if __name__ == "__main__":
    build_manuscript("manuscript_inline_FINAL.docx")
    build_manuscript("manuscript_clean_FINAL.docx")
    build_cover_letter()
    build_title_page()
