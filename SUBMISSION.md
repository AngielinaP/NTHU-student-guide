# NTHU Student Survival Guide

Submission title: NTHU 115065434 IMPISA Angelina Panyananda — NTHU Student Survival Guide
Replace the bracketed information with your own details.

## Project introduction
NTHU Fieldnotes is an unofficial English-language Student Survival Guide for National Tsing Hua University students. It helps new and continuing students find practical guidance on course selection, study spaces, campus transport, dorm life, daily budgeting, and international student support. It includes six guide pages, searchable category filters, a first-week checklist, and links to official university resources. Checklist progress is saved locally in the visitor's browser.

## GitHub repository
https://github.com/AngielinaP/NTHU-student-guide

## Public webpage
https://angielinap.github.io/NTHU-student-guide/

## AGENTS.md
The project root includes AGENTS.md. A public copy is also available through the website footer. It defines the project purpose, technology, file structure, visual style, content schema, verification requirements, accessibility, and rules for future changes.

## How the rules support future expansion
Guide content is stored in content/guides.json using a fixed schema. To add a guide, AI reads AGENTS.md, copies the guide template, writes the new content with official sources, and runs build.py. The script creates the guide page and updates the homepage automatically. The shared CSS and renderer keep every guide visually consistent; the existing search and filters automatically include the new guide. validate.py checks the required fields and generated internal links.

For example: “Follow AGENTS.md and add a guide about preparing for midterm exams under Academics. Verify university-specific information, rebuild, and validate the website.” This request can extend the project without redesigning it or repeating the original instructions.

## Relationship between rules and implementation
- Shared design rules → one stylesheet and one shared page renderer.
- Content formatting rules → a defined JSON schema and reusable template.
- Information accuracy rules → official source links and review dates on guide pages.
- Accessibility rules → labeled controls, visible focus, semantic headings, and responsive layouts.
- Development rules → repeatable build and validation commands.

## AI assistance
AI assisted with the initial implementation and writing. Review and personalize the guide before submitting and explain your own project choices honestly.
