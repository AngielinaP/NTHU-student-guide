# NTHU Fieldnotes — Student Survival Guide
An unofficial English-language guide for National Tsing Hua University students in Hsinchu, Taiwan. Six guide pages cover course selection, study spaces, transport, dorm life, budgeting, and international student support.

Website: https://angielinap.github.io/NTHU-student-guide/


## Features
Search and category filters; accessible, responsive pages; a first-week checklist with progress; per-guide saved checklists; links to official university sources. No login or database. Checklist data stays in the current browser. External fonts are optional and have local fallbacks.

## Run locally
Requires Python 3. Node is only needed for the optional JavaScript syntax check.
```
python build.py
python validate.py
node --check assets/app.js
python -m http.server 8000 --directory dist
```
Open http://localhost:8000. To stop the server, press Ctrl+C.

## Add a guide
Read AGENTS.md. Copy the schema in templates/guide-template.json into content/guides.json and fill in verified content. Run the build and validator. The new guide is automatically added to the homepage, search, and category filters. No manual homepage card is necessary.

The workflow builds and validates `dist/` before deployment. All local URLs are relative, so a repository subpath works. The separate `.openai/hosting.json` configuration is only used by Sites; GitHub Pages ignores it.

## Content policy and attribution
This is an independent student project, not an official NTHU service. University requirements and schedules remain authoritative at the linked official sources. Planning suggestions are clearly distinguished from policies. The campus illustration is an original stylized SVG, not an accurate map or an official university asset. AI assisted with code and initial content; the student should review, personalize, and be prepared to explain the work before submission.
