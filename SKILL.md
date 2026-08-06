---
name: dazhuang-ppt-skill
description: Create data-backed consulting-style strategy PPT workflows and decks, especially Chinese marketing pitch, brand strategy, campaign planning, H2/yearly planning, pre-strategy/front-planning, competitor analysis, and "make my PPT logic sharper" tasks. Use when the user asks to write a PPT, build a pitch deck framework, turn notes/MD/PDF into a slide outline or deck, make a McKinsey-style data-heavy presentation, match a front strategy to a later execution plan, generate a codex-ppt image deck, convert it to editable PPT, or repair PowerPoint font/garbled-text issues after conversion.
---

# Dazhuang PPT Skill

## Overview

Use this skill to turn rough business, marketing, or pitch material into an answer-first consulting deck: strategy logic first, per-slide data evidence second, slide production and validation last.

Prefer this skill for Chinese commercial decks where the user cares about "前策", "比稿", "洞察", "策略推导", "每页都有数据", "麦肯锡风", "无封面 10 页", "按月拆解", or "转成可编辑 PPT".

## Core Rules

1. Start from the business question, not from slide decoration.
2. Make every slide answer one question and carry at least one data object: number, index, matrix, heatmap, funnel, timeline, benchmark, or target.
3. When real data is missing and the user allows it, create "策略假设数据" and label it as replaceable by platform/backstage sources later.
4. Show the derivation chain: data input -> pattern/insight -> strategic implication -> event/content/action.
5. Put the key takeaway under the title, not in a bottom conclusion bar, unless the user explicitly wants a footer conclusion.
6. Avoid coarse ranges when the user asks for monthly strategy. Use `7月`, `8月`, `9月`, `10月`, `11月`, `12月` as separate labels instead of `7-8月` or `9-10月`.
7. Match later execution plans by leaning the front strategy toward the same direction, but do not copy later-plan content or data into the front-strategy section unless asked.
8. For Chinese editable PPT delivery, prefer `Microsoft YaHei` or another Office-safe CJK font over `PingFang SC`.

## Workflow

### 1. Intake

Inspect all supplied materials before building the framework: previous answers, MD outlines, PDFs, screenshots, existing PPTs, brand assets, and later execution plans. Extract immutable constraints such as page count, no-cover requirement, required visual style, user-supplied background image, and page-by-page feedback.

If the user asks only for the framework, deliver a structured outline. If the user asks to generate the PPT, proceed to production.

### 2. Strategy Storyline

Use a pyramid route:

`Benchmark / Market Context -> User Demand Shift -> Platform Behavior -> Content/Event Necessity -> Audience Conversion -> Strategic Model -> Execution Bridge`

For marketing-event decks, make the strategy end in a macro打法 rather than a single creative idea. Typical output directions:

- `IP体系化`: turn one-off events into a recognizable mother IP and monthly columns.
- `年轻新锐化`: make participation, language, creators, and emotional hooks younger.
- `套系生态化` / `价值套系化`: connect single-product attention to household scenarios, suites, services, and higher-value conversion.

Read `references/deck-framework.md` when building the slide storyline or a Gree/air-conditioner/H2-like deck.

### 3. Slide Contract

For every slide, define:

- `Page question`: what the slide proves.
- `Answer-title`: the title should contain the conclusion or sharp judgment.
- `Takeaway`: one sentence directly under the title.
- `Data`: concrete numbers, indexes, matrices, funnels, or targets.
- `Derivation`: how the data proves the takeaway.
- `Visual`: one dominant chart/table/matrix plus restrained supporting cards.
- `Role`: why this slide is needed before the next slide.

If a slide lacks data, add a reasonable strategy-assumption dataset or ask for the missing data only when guessing would create material risk.

### 4. Production

When making an actual deck:

1. Create or refine a clean MD outline first.
2. Use `codex-ppt` for a visually unified image-based PPT when the user asks for a polished deck.
3. Use `image-to-editable-ppt` when the user wants editable slides from screenshots/image-based decks.
4. Include speaker notes when the deck is meant for a pitch or review.
5. Read `references/production-checklist.md` before running production, editable conversion, or final QA.

### 5. QA

Before final delivery, verify:

- Slide count and no-cover/page-order constraints.
- Every slide has visible data and a clear title takeaway.
- No bottom conclusion bar when the user rejected that pattern.
- Monthly labels are split when requested.
- Text does not overflow or overlap.
- The PPTX opens or is at least structurally valid.
- If PowerPoint repairs the deck or text appears as symbols/garbage, run `scripts/fix_ppt_font_normalize.py` and deliver the repaired `_fixed.pptx`.

Report the final file path and validation result plainly.

## Resources

- `references/deck-framework.md`: reusable logic for strategy and marketing-event pitch decks, including the 10-page H2/Gree-style structure.
- `references/production-checklist.md`: deck generation, editable conversion, and repair checklist.
- `scripts/fix_ppt_font_normalize.py`: replace fragile CJK font declarations and normalize PPTX package structure.
