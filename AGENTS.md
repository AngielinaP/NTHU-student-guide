# AGENTS.md — NTHU Student Survival Guide

## 1. Mission and audience
Build an independent, English-language student guide for National Tsing Hua University (NTHU), Hsinchu, Taiwan. Help new and continuing students, including international students, find practical next steps and authoritative university resources. Do not confuse NTHU with NTU. This project is not an official university website.

## 2. Technology and commands
Use static HTML, CSS, and vanilla JavaScript. Python 3's standard library generates the HTML. No package installation, framework, database, or API key is required.
- Build: `python build.py`
- Validate: `python validate.py` and `node --check assets/app.js`
- Preview: `python -m http.server 8000 --directory dist` and open http://localhost:8000
- Hosting: publish `dist/`. Relative links must work under a GitHub Pages repository subpath.

## 3. Files and ownership
- `content/guides.json`: source of truth for all guide content.
- `templates/guide-template.json`: copyable example of the required content schema.
- `build.py`: shared HTML layout, homepage, and guide renderer.
- `assets/style.css`: shared design system and responsive styles.
- `assets/app.js`: search, category filtering, and local checklist behavior.
- `dist/index.html`: generated homepage.
- `dist/guides/<slug>.html`: generated guide pages.
- `dist/assets/`: generated copies of shared assets.
- `dist/AGENTS.md`: generated public copy of these instructions.
- `validate.py`: validates content and generated internal links.
- `README.md`: local development and GitHub Pages setup.
- `SUBMISSION.md`: assignment description and reusable-workflow explanation.
- `.github/workflows/pages.yml`: builds and deploys GitHub Pages.
- `.openai/hosting.json`: hosting identity for the separate Sites deployment; preserve its project ID.
Never hand-edit generated files in `dist/`; edit sources and rebuild.

## 4. Visual design
Use the existing warm paper background, dark green text, sage panels, thin borders, and restrained orange accents. CSS custom properties in `:root` define the colors. Use Manrope for headings, DM Sans for body text, and Georgia for italic accents; retain local fallback fonts. Use generous whitespace, rounded guide cards, and clear numbered steps. Keep the illustrated campus decorative: it is not an accurate map. Do not add an official NTHU seal or imply university endorsement.
Use one shared header/footer and consistent guide layout. Use a three-column desktop guide grid, two columns at tablet widths, and one on small phones. Preserve mobile navigation and prevent horizontal overflow at 375px.

## 5. Required content schema
Every object in `content/guides.json` must have these fields:
- `slug`: unique lowercase ASCII words separated by hyphens; use for filenames and stable URLs.
- `short`: concise card and page-navigation title.
- `title`: helpful human-readable page heading.
- `category`: exactly `Academics`, `Campus life`, or `Daily essentials`.
- `icon`: a unique two-digit guide number, such as `07`.
- `summary`: one short sentence explaining what the reader can do with this guide.
- `intro`: audience, scope, and relevant qualification of changing details.
- `steps`: 3–6 arrays, each containing a step heading and explanatory paragraph.
- `tips`: 2–4 concrete suggestions; label them as advice, not policy.
- `checklist`: 3–6 short, actionable items.
- `sources`: at least one `[label, https_url]` pair for relevant official resources.
- `updated`: the actual content-review date in YYYY-MM-DD format.
Write plain English, with Traditional Chinese terms only when useful. Explain unfamiliar abbreviations. No invented experiences, testimonials, contacts, requirements, or prices.

## 6. Information accuracy
Verify factual NTHU claims against official university pages before publishing. Include the source link in the guide. Prefer the responsible office over unofficial reposts. For registration deadlines, shuttle schedules, office hours, fees, and eligibility, link to current notices rather than copying volatile values. If exact values are necessary, include their applicable period and verify them at edit time. Distinguish student suggestions from university policy. Do not infer immigration, employment, insurance, or medical eligibility; direct students to the responsible official resource. If a claim cannot be verified, omit it or clearly state what the reader needs to confirm. Update the review date only after reviewing content and sources.

## 7. Procedure for adding a guide
1. Read this file and two existing guide objects.
2. Copy `templates/guide-template.json`, fill every field, and append it to `content/guides.json`.
3. Pick a unique slug and guide number; use an existing category.
4. Verify relevant university sources and add the actual review date.
5. Run `python build.py`. The homepage card, category filtering, searchable text, guide page, and checklist are generated automatically.
6. Run the validators and inspect the new page on desktop and mobile.
7. Check its source links and test homepage search, filters, and back navigation.
8. Summarize the content added, sources checked, and validation performed.
Do not create a separate layout, stylesheet, or navigation menu for each guide.

## 8. Rules for modifications
Keep stable guide slugs. Do not delete unrelated content or rewrite the entire site for a small edit. Fix the shared renderer for changes that affect all pages. Preserve source attribution and the unofficial-site notice. Never insert user account details, student IDs, private documents, credentials, or personal contact information. No analytics or tracking by default.
The checklist uses browser localStorage with the prefix `nthu-fieldnotes-v1:` and `<slug>-<index>` keys. If reordering existing checklist items, migrate keys or explicitly clear the affected guide's old keys so stored checks do not attach to different tasks. Do not clear other browser storage. The homepage reset affects only first-week checklist entries.

## 9. Accessibility and interactions
Use semantic HTML, a single h1 per page, ordered heading levels, descriptive links, a skip link, visible keyboard focus, and label-associated inputs. Category buttons must expose `aria-pressed`; search results must announce their count. Supply a useful empty state. Respect reduced motion. External links opened in a new tab must include `rel="noopener noreferrer"`. Checklists must remain usable if storage is blocked. Core guide text and links must remain available without JavaScript.

## 10. Definition of done
- All content fields pass validation; all generated local links resolve.
- Every page uses the shared design and contains official-source links and a review date.
- Search works with a query, a category, both together, and zero matches.
- Checklist count updates, survives reload when storage is available, and resets correctly.
- No horizontal overflow on mobile; keyboard navigation and focus are usable.
- Build and JavaScript syntax checks pass; record any verification limits honestly.
- Deployment contains the exact generated output; never claim GitHub or publication success without a returned link or verified result.

## Example future request
“Follow AGENTS.md. Add a guide about preparing for midterm exams in the Academics category. Use official NTHU resources where relevant, label study strategies as suggestions, rebuild the website, and validate all links and interactions.”
