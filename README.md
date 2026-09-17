# BookCraft AI

AI-assisted book typesetting and publishing workflow for Chinese long-form books, memoirs, oral histories, biographies, family books, and image-rich manuscripts.

BookCraft AI is a second-generation adaptation inspired by [`alchaincyf/huashu-report`](https://github.com/alchaincyf/huashu-report). The upstream project provides a strong report rendering and QA pipeline; this repository reorients that foundation toward book production: content fidelity, chapters, mirrored margins, front matter, images and captions, footnotes, table of contents, print PDF, and editable deliverables.

## v0.1 goal

Turn a structured long-form manuscript into a professionally typeset book while preserving the author's voice and content boundaries.

The first real validation target is a 100+ page Chinese family memoir/oral-history manuscript. Customer source files and private content are **not** committed to this public repository.

## Principles

- Preserve source wording by default; typesetting is not rewriting.
- Separate content normalization from page design and rendering.
- Treat images, captions, notes, appendices, and TOC as first-class book elements.
- Produce print-ready PDF and maintain an editable source path.
- Run mechanical QA after rendering; do not trust layout by inspection alone.
- Keep customer manuscripts and personal data out of the repository.

## Status

`BOOKCRAFT_AI_V0_1` — implementation starting.
