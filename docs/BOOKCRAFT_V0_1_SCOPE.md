# BOOKCRAFT_AI_V0_1

## Mission

Build a reusable AI-assisted book production pipeline for Chinese long-form manuscripts.

This is not a general writing assistant and not a report generator. The v0.1 target is book production from an existing manuscript with strict source fidelity.

## Primary document classes

- memoir / autobiography
- oral history
- biography
- family history
- commemorative book
- image-rich long-form nonfiction

## Source-of-truth rule

For memoir/oral-history projects, source wording is frozen by default.

Allowed transformations without author approval:

- typography and layout
- heading hierarchy normalization
- paragraph/style normalization
- image placement and caption styling
- TOC generation
- page-number generation
- obvious whitespace cleanup

Require explicit review:

- wording changes
- sentence rewrites
- factual additions
- name/date normalization when source is ambiguous
- inferred historical claims
- deletion of substantive content

## v0.1 pipeline

```text
DOCX / structured manuscript
        |
        v
INGEST
  paragraphs / headings / tables / images / notes
        |
        v
BOOK MODEL
  front matter / chapters / sections / figures / appendices
        |
        v
NORMALIZE
  styles / captions / anchors / metadata
        |
        v
LAYOUT
  trim size / mirrored margins / chapter openers / running heads
        |
        v
RENDER
  HTML/CSS -> print PDF
        |
        v
QA
  TOC / page breaks / orphans / image-caption splits / overflow
        |
        v
DELIVER
  print PDF + editable source package
```

## v0.1 acceptance gates

1. `CONTENT_FIDELITY_PASS`
   - manuscript text is preserved byte-for-byte after normalization where no approved edit exists.

2. `STRUCTURE_PASS`
   - front matter, chapters, appendices, figures and captions are represented explicitly.

3. `BOOK_LAYOUT_PASS`
   - mirrored margins, recto/verso pages, running heads, page numbering and chapter starts are stable.

4. `TOC_PASS`
   - generated TOC page numbers match final rendered locations.

5. `FIGURE_PASS`
   - figures never silently detach from captions; oversized images are handled deterministically.

6. `PRINT_QA_PASS`
   - no obvious overflow, clipped text, blank-content accidents or broken page anchors.

## Non-goals for v0.1

- generative rewriting of memoir content
- automatic historical fact invention
- full InDesign replacement
- automated commercial printing/vendor ordering
- OCR-heavy recovery of damaged scans
- collaborative web editor

## First real validation case

A 100+ page Chinese family memoir / oral-history manuscript containing:

- front matter
- chapter structure
- photographs
- captions
- footnotes / explanatory notes
- appendices
- family-person tables
- dialect glossary

Private customer material must remain outside the public repository.
