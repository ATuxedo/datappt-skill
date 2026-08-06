# Production Checklist

Use this reference when the user asks for actual PPT/PPTX files, editable conversion, or repair.

## Outline To Image-Based PPT

1. Confirm slide count, cover/no-cover, and fixed outline constraints.
2. Build an MD outline with one section per slide. Each slide section should include:
   - title
   - key takeaway
   - data
   - chart recommendation
   - role in the storyline
3. If using `codex-ppt`, read that skill before execution and follow its sample/QA workflow.
4. Generate one approved sample slide before full production when the user asks for a specific style.
5. Use the user's background image if supplied. Do not substitute a decorative background without permission.
6. Produce speaker notes (`speech.md`) when the deck is for pitching or presenting.
7. Validate final PPTX page count, notes count, and image/media count.

## Image-Based PPT To Editable PPT

1. Use `image-to-editable-ppt` when the user wants editable slides from images, scans, PDFs, or image-based PPTX.
2. Run `editppt doctor` and ensure:
   - image backend is ready
   - text hints use PaddleOCR if a valid token is available
   - network/full-access is available if image asset separation is required
3. For multi-page runs, dispatch page workers as the skill requires. Record only pages with top-level `validation.json.passed: true`.
4. Do not finalize until every page is recorded.
5. Run `editppt run finalize <run>` and check the final validation JSON.

## PowerPoint Repair / Garbled Text

Symptoms:

- PowerPoint says it found unreadable content and offers to repair.
- After repair, Chinese text becomes symbols, apple glyphs, or unreadable characters.
- Validation says the PPTX structure passed, but PowerPoint rendering is wrong.

Likely cause:

- The PPTX XML contains correct text, but Office maps CJK text to a fragile or unavailable font.
- In this workflow, `PingFang SC` may open poorly after PowerPoint repairs the file.

Repair path:

```bash
python scripts/fix_ppt_font_normalize.py input.pptx --out output_fixed.pptx --font "Microsoft YaHei"
```

Then verify:

```bash
editppt validate or validate_pptx.py, when available
soffice --headless --convert-to pdf output_fixed.pptx
pdftoppm -png -f 1 -singlefile output_fixed.pdf page1
```

If the rendered first page is readable and structural validation passes, deliver the `_fixed.pptx` and tell the user to avoid opening the unrepaired file.

## Final Response

Report:

- final PPTX path
- whether it is image-based or object-level editable
- slide count and notes count
- validation result
- any warnings or known limitations
