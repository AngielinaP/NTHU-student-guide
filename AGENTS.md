# AGENTS.md — NTHU Student Survival Guide

These instructions apply to the entire project. Read this file before changing code or content. Extend the existing website using its shared content format and design rather than creating an unrelated page.

## 1. Project purpose

**Project name:** NTHU Fieldnotes — Student Survival Guide  
**University:** National Tsing Hua University (NTHU), Hsinchu, Taiwan  
**Repository:** https://github.com/AngielinaP/NTHU-student-guide  
**Website:** https://angielinap.github.io/NTHU-student-guide/

Help new and continuing NTHU students, especially international students, navigate everyday university life. Turn common questions into clear explanations, practical steps, and links to responsible university offices.

The initial guides cover course selection, libraries and study spaces, campus transportation, dorm life, daily budgeting, and international student support. Future guides should serve the same audience and use the same structure.

This is an independent student project, not an official university website. Keep this distinction visible. Do not confuse NTHU with National Taiwan University (NTU).

## 2. Overall webpage style

Create a calm, welcoming, readable website. Use simple English and a friendly, practical tone. Explain unfamiliar abbreviations; add Traditional Chinese names only when they help students identify a place or service.

Reuse the design tokens in `assets/style.css`:

| Element | Rule |
| --- | --- |
| Page background | Warm paper: `#f8f7f2` |
| Main text | Dark green: `#233d32` |
| Buttons and primary accents | Green: `#355c43` |
| Supporting text | Muted gray-green: `#687068` |
| Checklist panels | Pale sage: `#eaf0e3` |
| Borders | Light gray-green: `#dedfd4` |
| Headings | Manrope, with a sans-serif fallback |
| Body text | DM Sans, with a sans-serif fallback |
| Selected italic accents | Georgia, with a serif fallback |

Use generous spacing, subtle borders, rounded cards, and restrained decorative accents. Reuse shared styles instead of adding a new visual theme for each topic. Keep text readable if external fonts fail to load.

Use three guide-card columns on desktop, two at tablet widths, and one on small phones. Preserve readable navigation and prevent horizontal overflow at 375px. Keep the campus illustration labeled as decorative, not an accurate campus map. Do not imply endorsement by using an official seal.

## 3. Page structure

### Homepage

Keep these sections in order:

1. **Header:** project identity and links to guides, the first-week checklist, and official resources.
2. **Introduction:** explain whom the website helps and provide a clear link to the guides.
3. **Guide directory:** cards with category labels, search, category filters, and an empty-results message.
4. **First-week checklist:** actionable tasks, progress count, and a reset control.
5. **Official resources:** links to relevant university offices.
6. **Footer:** unofficial-project notice and a link to `AGENTS.md`.

### Individual guide

Every guide must use the shared renderer and include:

1. A link back to the guide directory.
2. Category, guide number, and one main heading.
3. A short introduction explaining the guide's scope.
4. The content-review date.
5. Three to six numbered action steps.
6. Two to four practical tips, clearly presented as suggestions.
7. A checklist of three to six next steps.
8. At least one relevant official-source link.
9. The shared navigation and footer.

Do not hand-code a separate layout or stylesheet for each guide.

## 4. File naming and placement

| Path | Purpose and editing rule |
| --- | --- |
| `AGENTS.md` | Project-wide instructions; keep consistent with the implementation. |
| `content/guides.json` | Source of truth for guide text and metadata. Add new guide objects here. |
| `templates/guide-template.json` | Copyable starting structure; replace inherited example content before use. |
| `build.py` | Generates the homepage and guide pages using shared layouts. |
| `assets/style.css` | Shared colors, typography, layout, and responsive rules. |
| `assets/app.js` | Search, category filtering, and local checklist behavior. |
| `dist/index.html` | Generated homepage. |
| `dist/guides/<slug>.html` | Generated individual guide pages. |
| `dist/assets/` | Generated copies of shared assets. |
| `dist/AGENTS.md` | Generated public copy of these instructions. |
| `validate.py` | Checks guide data and generated internal links. |
| `.github/workflows/pages.yml` | Builds, validates, and deploys `dist/` to GitHub Pages. |
| `README.md` | Project overview and development instructions. |
| `SUBMISSION.md` | Assignment introduction, links, and explanation of reuse. |

Use lowercase, hyphen-separated guide slugs, such as `exam-preparation`. Keep existing slugs stable because they determine public URLs. Do not place new guide HTML files at the repository root.

**Edit source files, then rebuild. Never use edits to `dist/` as the only implementation of a change.** If an alternate hosting configuration exists locally, preserve its identity; it is not required for GitHub Pages.

## 5. Formatting rules for new content

Each object in `content/guides.json` must contain all of these fields:

| Field | Required format |
| --- | --- |
| `slug` | Unique lowercase words separated by hyphens; no spaces. |
| `short` | Concise title for the homepage card. |
| `title` | Descriptive page heading that communicates the reader's goal. |
| `category` | Exactly `Academics`, `Campus life`, or `Daily essentials`. |
| `icon` | Unique two-digit guide number, such as `07`. |
| `summary` | One short sentence explaining the guide's benefit. |
| `intro` | Brief scope and context, including any details the reader must confirm. |
| `steps` | Three to six `[heading, paragraph]` pairs. |
| `tips` | Two to four short strings containing practical suggestions. |
| `checklist` | Three to six short, actionable strings. |
| `sources` | One or more `[descriptive_label, https_url]` pairs. |
| `updated` | Actual content-review date in `YYYY-MM-DD` format. |

Use plain text in content fields; the renderer escapes text for safe HTML display. Keep JSON valid: double-quoted strings, no comments, and no trailing commas. Do not invent a category without also updating the filters, validator, and documentation.

Search currently matches the card's `short`, `summary`, and `category` fields. Include useful topic words there; do not describe it as full-text search of the guide body.

## 6. Content accuracy and source rules

- Verify university-specific claims with the responsible official NTHU source before publishing them.
- Prefer links to current notices for registration dates, shuttle timetables, opening hours, fees, and requirements. If exact values are necessary, verify them and state their applicable period.
- Distinguish university policy from suggested student habits. A budgeting tip is not an official fee; a suggested checklist is not a university requirement.
- Give source links descriptive labels. Explain which resource the reader should use.
- Do not invent office contacts, eligibility rules, prices, personal experiences, or testimonials.
- If information cannot be verified, omit the claim or tell the reader what to confirm with the responsible office.
- Update `updated` only after reviewing the content and sources; a styling change alone does not justify a new review date.
- Keep private documents, student IDs, credentials, and personal contact details out of public guide pages.

## 7. Workflow for AI: adding a guide

1. Read this file, `build.py`, and two existing guide objects.
2. Check whether an existing guide already covers the requested topic.
3. Copy the structure from `templates/guide-template.json` and replace all example text with the new topic's content.
4. Choose an unused slug and guide number, and select an existing category.
5. Verify university-specific information, add relevant source links, and record the actual review date.
6. Append the completed object to `content/guides.json` without removing existing guides.
7. Run the build and validation commands below.
8. Inspect the new page, its card, navigation, filters, search, and checklist on desktop and mobile.
9. Summarize the changed files, sources checked, and checks performed. State any verification limits.

The build automatically creates the new guide page and homepage card. Search and filters use the generated cards, so a normal guide addition does not require manually editing homepage HTML.

## 8. Workflow for AI: modifying existing content

Make the smallest change that satisfies the request. Preserve unrelated content, working links, the shared design, and existing URLs. For a site-wide layout change, edit the shared renderer or stylesheet rather than individual generated pages.

Keep these behaviors intact:

- Category filters and search must work together and show a useful empty state.
- Checklist progress stays in the visitor's browser using `localStorage`; no account is needed.
- Storage keys use `nthu-fieldnotes-v1:` followed by a guide slug and item index. If reordering or removing existing checklist items, migrate or reset only the affected keys so stored checks do not attach to different tasks.
- The homepage reset changes only the first-week checklist. Never clear unrelated browser storage.
- Checklists remain usable during the current visit if storage is unavailable.

Do not add frameworks, databases, tracking, or login requirements for a normal content update. If a requested feature requires a larger architectural change, explain the reason before changing the project structure.

## 9. Development and GitHub Pages deployment

Use static HTML, CSS, vanilla JavaScript, and Python's standard library. No package installation or API key is required for the normal build.

Run from the repository root:

```bash
python build.py
python validate.py
node --check assets/app.js
```

For local preview:

```bash
python -m http.server 8000 --directory dist
```

Open `http://localhost:8000`. Node is required only for the JavaScript syntax check, not to serve the website.

GitHub Pages publishes the generated `dist/` directory through `.github/workflows/pages.yml`. Keep the repository's Pages source set to **GitHub Actions**. Pushes to `main` trigger the workflow; it can also be started manually.

Use relative internal URLs: `./assets/style.css` on the homepage and `../assets/style.css` on guide pages. Root-relative links such as `/assets/style.css` would omit the `/NTHU-student-guide/` repository path.

Check the workflow result and the published page before reporting a deployment as successful. A saved file or successful local build alone is not proof of publication.

## 10. Accessibility and completion checklist

Before finishing a change, verify the relevant items:

- [ ] Required fields, unique slugs, categories, and JSON syntax are correct.
- [ ] Build, content validation, internal-link checks, and JavaScript syntax checks pass.
- [ ] Every page has one `h1`, sensible heading order, semantic structure, and descriptive links.
- [ ] Inputs have labels; keyboard focus is visible; the skip link works.
- [ ] Filters expose `aria-pressed`, and search announces the result count.
- [ ] Search handles a query, a category, both together, and zero matches.
- [ ] Checklists update, persist after reload when storage is available, and reset correctly.
- [ ] Layout remains readable on desktop and a 375px-wide screen, with no horizontal overflow.
- [ ] Reduced-motion preferences are respected; core guide text and links work without JavaScript.
- [ ] External links opened in a new tab include `rel="noopener noreferrer"`.
- [ ] Official-source links, review dates, and the unofficial-project notice remain present.
- [ ] Any unperformed checks or remaining deployment issues are stated honestly.

## 11. Example extension request

> Follow AGENTS.md. Add a guide about preparing for midterm exams under Academics. Use the existing guide schema and shared layout. Clearly label study strategies as suggestions, verify any university-specific claims, add relevant official sources, rebuild the site, and validate the result.

Expected result: one new content object, one generated guide page, and an automatically generated homepage card that works with the existing search and filters. The new content should look and behave like the rest of the project without repeating the original design instructions.
