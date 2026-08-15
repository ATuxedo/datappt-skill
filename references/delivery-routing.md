# Delivery Routing

Choose one route before PPT authoring. Record the choice in `PROJECT_HANDOFF.md`.

## Decision Table

| User need | Route | Production capability | Final editability |
| --- | --- | --- | --- |
| framework, diagnosis, or outline only | D | DataPPT analysis | no PPTX |
| editable deck from scratch | A | `Presentations` + `@oai/artifact-tool` | native objects |
| edit an existing editable deck/template | A | `Presentations` template-following | native inherited objects |
| maximum visual unity, editability not needed | B | `codex-ppt` | full-slide images |
| explicit `codex-ppt` plus editable output | C | `codex-ppt` then `image-to-editable-ppt` / `editppt` | reconstructed objects |
| image/PDF/scanned deck already exists and must become editable | C | `image-to-editable-ppt` / `editppt` | reconstructed objects |

## Route A: Native Editable

Use the installed `Presentations` skill as the authoring authority. Read its required style, routing, template, and artifact-tool documentation before authoring.

Prefer this route when:

- the user repeatedly changes text, numbers, or charts;
- a source PPTX already contains a strong editable master/layout system;
- data accuracy and future replacement matter more than pixel-perfect image styling;
- a deadline makes page-by-page reconstruction inefficient.

Use native PowerPoint text, shapes, tables, and charts. Keep photographs and illustrations as image assets. Report `object-level editable`.

## Route B: codex-ppt Image Deck

Read `codex-ppt/SKILL.md` and every phase-specific reference it requires. Its approval gates and image-backend constraints remain mandatory.

Use this route when:

- the user values a unified high-fashion/editorial visual system;
- the deck is primarily for review or presenting;
- object-level editing is not required.

Report `image-based`; do not call it editable merely because the `.pptx` opens in PowerPoint.

## Route C: Image to Editable

Use `image-to-editable-ppt` when the source is already visual: codex-ppt output, screenshots, PDF pages, scanned slides, or an image-based PPTX.

The workflow is a reconstruction, not a file-format conversion:

1. render the visual source;
2. derive text hints/OCR;
3. separate or regenerate foreground assets;
4. rebuild text, shapes, charts, images, and backgrounds as positioned objects;
5. validate every page manifest;
6. assemble the recorded pages.

Report `reconstructed editable`. Warn that tiny typographic differences, complex charts, and generated imagery may remain raster assets even when the surrounding page is editable.

## Route Integrity

- Do not enter the `codex-ppt` workflow and silently replace its final slide-image backend with programmatic drawing.
- Do not use a full-slide screenshot with editable text overlaid and call it reconstructed editable.
- Do not use Route C when Route A can directly preserve a strong editable source deck with less fidelity loss.
- If the user says only “生成PPT” without editability requirements, select based on visual need and state the route before production.
