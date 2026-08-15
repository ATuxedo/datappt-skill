# Data and Slide Contract

Use this reference when building the data pack, defining analytical pages, or accepting specialist module outputs.

## Evidence Grades

| Grade | Meaning | Slide treatment |
| --- | --- | --- |
| A | User-provided, platform/backend, or directly verified source | cite source, period, scope, and metric definition |
| B | Credible public or third-party evidence | cite publisher, date, scope, and access path |
| C | Strategy assumption or synthetic placeholder | label `策略假设/待平台回填`; include replacement field |

Never fabricate an A/B source. Do not combine different periods or denominators without a visible normalization note.

## Data Map Fields

Maintain one row per claim or chart series:

- `data_id`
- `metric_or_claim`
- `value`
- `unit`
- `time_window`
- `population_or_scope`
- `source_path_or_url`
- `evidence_grade`
- `calculation`
- `used_on_slides`
- `replacement_status`
- `replacement_owner`
- `notes`

## Framework Module Contract

Each module must define:

1. `Business question`
2. `Data needed`
3. `Conclusion to prove or test`
4. `Demo/reference expression`
5. `Expected slide range`
6. `Dependencies on other modules`

This is the preferred way to turn a user's descriptive framework into a buildable deck.

## Slide Contract

For every analytical slide, write:

```text
Page question:
Answer-title:
Takeaway:
Evidence objects:
Derivation:
Dominant visual:
Storyline role:
Source / period / evidence grade:
Replacement field:
```

The title must remain defensible if the body is hidden. Use one dominant chart, matrix, heatmap, funnel, timeline, benchmark, or data table. Supporting objects must explain the dominant visual, not compete with it.

## Data Density Rules

- Use enough observations to establish a pattern, not a single decorative number.
- Prefer exact months when the business decision is monthly; do not collapse into broad ranges without reason.
- Put annotations on or beside the chart where the pattern occurs.
- Use a small source footer; do not repeat a separate conclusion bar when the title already states the answer.
- Use tables for exact lookup, charts for patterns, matrices for choices, timelines for sequencing, and funnels for conversion.
- Replace visual cards with a flat evidence canvas when cards do not add grouping meaning.

## Module Return Contract

Accept a specialist module only when it returns:

```text
Cleaned artifact path:
Sources and periods:
Metric definitions/calculations:
Key findings (3–5):
Slide-ready objects:
Proposed conclusion titles:
Open risks:
Replacement fields:
QA performed:
```

If an output cannot meet this contract, keep it as research material rather than presenting it as slide-ready evidence.
