# Production Checklist

Use this reference for actual PPTX production, editable reconstruction, final integration, repair, and delivery.

## Before Authoring

- Confirm goal, audience, page count, cover/no-cover, required sections, exclusions, and delivery type.
- Confirm the authority set and latest approved framework.
- Complete the module and slide contracts.
- Confirm data periods, metric definitions, evidence grades, and replacement fields.
- Choose exactly one route from `delivery-routing.md`.
- Confirm the approved visual reference, template, or named style.

## Route A: Native Editable

- Read the installed `Presentations` skill and all route-required references.
- Load the bundled workspace dependencies before authoring.
- Use `@oai/artifact-tool`; do not use `python-pptx` for net-new authoring.
- If a source PPTX defines the style, inherit its masters/layouts and edit existing objects where practical.
- Keep charts, tables, text, and diagrams as native objects.
- Render every slide, inspect at full size, and fix overlap, clipping, wrapping, and chart/data mismatches.

## Route B: codex-ppt Image Deck

- Read `codex-ppt/SKILL.md` and its phase-specific references.
- Approve the outline, visual direction, image backend, and exactly one representative sample before full production.
- Keep the approved backend and sample generation method fixed.
- Generate and record every page image through the codex-ppt workflow.
- Assemble only after all page states are accepted/recorded.
- Report that the deck is image-based.

## Route C: Reconstructed Editable

- Complete the approved visual source first.
- Read `image-to-editable-ppt/SKILL.md` and required references.
- Run `editppt prepare`; use OCR/text hints as configured.
- Dispatch or locally reconstruct pages exactly as the skill requires.
- Record only pages whose top-level validation passes.
- Finalize only when every page is recorded.
- Verify no slide uses an invalid full-page source screenshot plus editable text overlay.
- Report that the deck is reconstructed editable and identify any raster-only foreground assets.

## Integration QA

Verify:

- slide count, aspect ratio, page order, and section transitions;
- title-level storyline continuity;
- source, period, scope, and evidence grade for every non-trivial claim;
- C-grade assumptions are labeled and appear in the replacement map;
- data labels match the actual chart/table values;
- user-approved decisions are preserved and rejected patterns are absent;
- fonts are Office-safe and Chinese text is readable;
- no text overflow, unintended overlap, broken connectors, missing images, or unresolved placeholders;
- speaker notes and source blocks exist when required;
- the PPTX opens and passes the route-specific validator.

## CJK Font Repair

If PowerPoint reports unreadable content or repaired Chinese text becomes symbols, normalize the existing PPTX package:

```bash
python scripts/fix_ppt_font_normalize.py input.pptx --out output_fixed.pptx --font "Microsoft YaHei"
```

Render and inspect the repaired deck before delivery. Do not deliver the unrepaired file as the preferred output.

## File Management

- Put scripts, generated assets, previews, renders, QA files, logs, caches, and intermediate deck versions under `work/`.
- Put only final user-facing PPTX files under `outputs/`.
- Preserve user-provided and pre-existing files.
- After validation, remove only regenerable temporary files created by the current task.

## Final Report

Report:

- final PPTX path;
- slide count and notes count when applicable;
- delivery route and editability type;
- validation result;
- remaining replacement items or known limitations.
