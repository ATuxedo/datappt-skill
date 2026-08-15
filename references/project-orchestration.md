# Project Orchestration

Use this reference for complex, multi-stage, multi-thread, or revision-heavy presentation projects.

## Authority Set

At project start and after every major revision, list the active authorities:

| Authority | Required record |
| --- | --- |
| User instruction | date/time and concise decision |
| Approved framework | path/version and approval status |
| Raw data | path, period, scope, owner |
| Visual reference | sample slide, deck, style reference, or template |
| Historical deck | path/version, explicitly marked non-authoritative |

Use the latest specific instruction over older general guidance. When two current sources disagree, pause only if the choice materially changes the result; otherwise apply the hierarchy in `SKILL.md` and record the decision.

## Project State

Run `scripts/init_datappt_project.py <workspace-root>` for projects that cross tasks, contain several data modules, or require multiple rounds of review. It creates:

```text
work/datappt/
  state/
    PROJECT_HANDOFF.md
    STRATEGY_FRAMEWORK.md
    DECISION_LOG.md
    DATA_MAP.csv
  data/
  modules/
  qa/
  renders/
outputs/
```

Maintain the files as follows:

- `PROJECT_HANDOFF.md`: current state, active authorities, latest approved outputs, unfinished items, and exact next action.
- `STRATEGY_FRAMEWORK.md`: module-level business questions, data needs, intended conclusions, and page mapping.
- `DECISION_LOG.md`: user feedback, accepted/rejected visual patterns, content decisions, and affected slides.
- `DATA_MAP.csv`: claim-level data provenance, evidence grade, time window, use, and replacement status.

## Module Delegation

Split only independent scopes such as industry data, audience, creators, search, competitors, media, or sales. Give each scope:

- authoritative inputs and forbidden sources;
- metric definitions and time windows;
- expected cleaned artifact;
- expected findings and page outputs;
- evidence-grade and citation requirements;
- completion and QA criteria.

Require each module to return its output path, source list, calculation notes, three to five findings, slide-ready objects, unresolved risks, and replacement fields. Do not accept prose-only returns for a data module.

The parent project must reconcile duplicated metrics, inconsistent periods, naming differences, and conclusions before slide integration.

## Revision Control

Convert feedback into durable rules:

- `Accepted`: preserve in later versions.
- `Rejected`: do not reintroduce without explicit user reversal.
- `Pending`: unresolved, with owner and next check.
- `Superseded`: historical decision replaced by a newer one.

For every major deck revision, record:

1. source deck/version;
2. changed slides and reason;
3. changed data or assumptions;
4. visual decisions inherited;
5. final output path and QA state.

## Integration Gate

Before calling a deck final, verify:

- the framework and page order reflect the latest authority set;
- every specialist output has been integrated or explicitly excluded;
- terminology, periods, denominators, and evidence grades are consistent;
- slide titles form a coherent argument when read alone;
- all C-grade values have visible labels and replacement owners;
- the final PPT route and editability level are accurately reported.

## Handoff Contract

A new task must be able to resume from `PROJECT_HANDOFF.md` without reading the full chat history. The handoff must name:

- project goal, audience, and current deliverable;
- latest approved framework and visual reference;
- current source-of-truth data;
- final and working deck paths;
- completed, pending, and rejected work;
- known risks and replacement items;
- next action, including the exact file and slide range to open first.
