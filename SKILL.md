---
name: datappt-skill
description: Orchestrate and produce data-backed strategy presentations from rough notes, MD/PDF frameworks, research, spreadsheets, screenshots, existing decks, and multi-thread project artifacts. Use for Chinese marketing pitches, brand strategy, campaign planning, annual/H2/monthly plans, competitor and audience analysis, data-heavy consulting decks, cross-conversation PPT projects, editable PowerPoint delivery, codex-ppt image decks, image-to-editable reconstruction, or final-deck integration and repair.
---

# DataPPT Skill

## Mission

Turn a complex presentation project into a controlled chain:

`source authority -> business question -> data evidence -> conclusion -> slide contract -> visual route -> validated deliverable -> resumable handoff`

Own the project from intake through final integration. Use other presentation skills as production engines; do not duplicate or weaken their hard requirements.

## Non-Negotiable Rules

1. Start from the business decision, not decoration.
2. Make every analytical slide answer one question and contain at least one meaningful data object.
3. Use the user's latest approved framework as the storyline authority. Treat old decks and handoffs as history unless explicitly promoted.
4. Separate verified facts, third-party evidence, and strategy assumptions. Never present assumptions as observed facts.
5. Show the derivation chain: `data -> pattern -> insight -> implication -> action`.
6. Put the answer in the title or the sentence directly below it. Avoid detached bottom conclusion bars unless requested.
7. Preserve approved visual samples, brand rules, page-level decisions, and later-plan direction across revisions.
8. State whether the final deck is `image-based`, `object-level editable`, or `hybrid/reconstructed editable`.
9. Keep intermediates under `work/` and final user-facing PPTX files under `outputs/`.

## Phase 1: Establish Project Truth

Inspect all supplied notes, frameworks, PDFs, spreadsheets, screenshots, decks, brand assets, previous task outputs, and later execution plans.

Resolve conflicts in this order:

1. Latest explicit user instruction and latest approved framework.
2. Current raw/source data.
3. Latest approved visual sample, brand guide, or editable template.
4. Current approved strategy decisions and later-plan direction.
5. Previous decks, chat summaries, and handoff documents.

Record meaningful conflicts and decisions. Do not let an old handoff silently override a newer framework.

For multi-stage, multi-thread, or revision-heavy work, initialize project state with `scripts/init_datappt_project.py` and maintain the four files copied from `assets/project-starter/`.

Read `references/project-orchestration.md` before splitting modules, merging task outputs, resuming a project, or preparing a handoff.

## Phase 2: Build the Strategy and Evidence System

Use a conclusion-first pyramid. For each framework module, define:

- `Business question`: the decision this module supports.
- `Data needed`: the minimum evidence required.
- `Conclusion`: the judgment the evidence should prove or test.
- `Demo`: a representative chart, table, or layout reference.

For each slide, define:

- `Page question`
- `Answer-title`
- `Takeaway`
- `Evidence objects`
- `Derivation`
- `Dominant visual`
- `Storyline role`
- `Source / time window / evidence grade`
- `Replacement field` for temporary data

Use evidence grades:

- `A`: user-provided or platform/backend source, directly verified.
- `B`: credible public or third-party source, cited with date and scope.
- `C`: strategy assumption or synthetic placeholder, visibly marked for replacement.

If the user allows provisional data, create internally coherent C-grade data and a replacement map. Never invent sources. Read `references/data-and-slide-contract.md` for the detailed data pack and module-return contract.

Read `references/deck-framework.md` when building a marketing, brand, campaign, annual, H2, or front-strategy storyline.

## Phase 3: Control Specialist Work and Revisions

Split independent research or data modules only when boundaries are clear. Each module must return:

1. cleaned data or calculation file;
2. source and time-window notes;
3. three to five decision-relevant findings;
4. slide-ready data objects or one to two page proposals;
5. unresolved questions and replacement fields.

The parent project owns storyline integration, terminology, evidence grading, style consistency, and the final deck. Update the decision log after page-level feedback so rejected patterns do not return.

## Phase 4: Select Exactly One Delivery Route

Read `references/delivery-routing.md` before authoring a PPTX.

### Route A — Native editable PPT

Choose when the user asks for editable slides, an editable template exists, or charts/text must be revised frequently.

- Use the installed `Presentations` skill and its required `@oai/artifact-tool` workflow for new or edited local PPTX files.
- If a user-provided editable PPTX supplies the visual system, inherit its master/layout/slide structure instead of flattening it.
- Use native text, shapes, tables, and charts; use image generation only for photographic or illustrative assets.
- This is the default route for editable-from-scratch data decks.

### Route B — codex-ppt image deck

Choose when visual unity and presentation polish matter more than object-level editability.

- Read the installed `codex-ppt/SKILL.md` in full and follow its outline, style, backend, one-sample approval, slide-job, subagent, QA, notes, and assembly gates.
- Treat every page as a generated 16:9 image.
- Do not claim that the resulting text, charts, or shapes are editable.

### Route C — codex-ppt to editable reconstruction

Choose when the user explicitly wants both codex-ppt visual fidelity and editable PowerPoint objects.

1. Complete Route B and approve the image deck.
2. Read and run the installed `image-to-editable-ppt` skill.
3. Rebuild each page into native objects with `editppt`; do not use a full-slide screenshot plus editable text overlay.
4. Finalize only after every page is recorded and validation passes.

This route is slower and can introduce reconstruction variance. State that tradeoff before production.

### Route D — Framework or analysis only

Choose when the user requests only a storyline, data plan, diagnosis, or slide outline. Do not manufacture a PPTX.

If the request names `codex-ppt` and also requires editability, default to Route C. If it only says “可编辑PPT”, default to Route A.

## Phase 5: Visual Direction

Treat visual style separately from strategy content.

- If the user names a `codex-ppt` style reference, load and apply it only within Route B or Route C.
- If the user provides an editable reference deck, prefer Route A and inherit the deck's real layouts.
- Preserve one palette, typography system, chart language, image treatment, and source-footer convention.
- Prefer one dominant composition over repeated UI-card grids.
- For Chinese Office delivery, prefer `Microsoft YaHei` or another Office-safe CJK font.

## Phase 6: QA, Integration, and Handoff

Read `references/production-checklist.md` before finalization.

Verify:

- storyline continuity and page order;
- every claim's evidence grade, source, period, and replacement status;
- chart/data consistency;
- approved feedback and rejected-pattern compliance;
- slide count, aspect ratio, notes, fonts, overflow, overlap, media, and openability;
- final output type: image-based, native editable, or reconstructed editable;
- all final files are under `outputs/` and temporary files remain under `work/`.

Update `PROJECT_HANDOFF.md` with the current authority set, final outputs, unfinished replacements, and the exact next action. Report the final path and validation result plainly.

## Resources

- `references/project-orchestration.md`: source hierarchy, project files, module work, revisions, integration, and handoff.
- `references/data-and-slide-contract.md`: evidence grades, data map, slide contract, and module return schema.
- `references/deck-framework.md`: reusable strategy storyline patterns.
- `references/delivery-routing.md`: native editable, codex-ppt image, and reconstructed editable routes.
- `references/production-checklist.md`: production, conversion, repair, validation, and delivery checks.
- `assets/project-starter/`: reusable project-control templates.
- `scripts/init_datappt_project.py`: initialize resumable project state under `work/datappt/`.
- `scripts/fix_ppt_font_normalize.py`: normalize fragile CJK font declarations in existing PPTX packages.
