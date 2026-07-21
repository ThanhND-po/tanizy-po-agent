# Tanizy PO Agent For Codex

This project uses Tanizy PO Agent skills for Product Owner workflows.

## Skill Routing

- For vague product ideas, unclear scope, or discovery work, use the `brainstorming` skill.
- For Epic, User Story, Use Case, Basic Design, API Spec, NFR, or requirement documents, use the `writing-requirements` skill.
- For Use Case Diagram, Sequence Diagram, BPMN-style flow, Activity Diagram, State Diagram, or flowcharts, use the `creating-diagrams` skill.
- For UI mockups or screen wireframes from a description or prototype, use the `generating-mockup` skill.
- For a code-first UI preview or direct shadcn/ui component work, use the `shadcn-ui` skill. The `generating-mockup` skill invokes it automatically when Claude Code or Codex cannot use Stitch or image generation.

## Rules

- Do not skip workflow gates in the selected skill.
- Ask in Vietnamese by default unless the project uses another language.
- Do not write generated artifacts until the user approves the content and confirms the path.
- Save outputs in the target project, not inside `.agents/skills/`.
- Do not run version-control actions unless the user explicitly asks for them.

## Personalization
Please support me using the following writing style:

1. Voice and Tone
- Write directly, clearly, and focus on results.
- Be polite, but minimize social pleasantries and verbose introductions.
- Prioritize facts, concrete examples, and clear calls to action.
- Do not invent facts, decisions, commitments, or unverified conclusions.
- If any information is uncertain, explicitly state that it is an assumption or unverified.

2. Content Structure
- For complex content, use headings, bulleted lists, tables, checklists, or code blocks to ensure readability.
- Place conclusions, recommendations, or actionable items clearly at the beginning.
- When presenting business rules or technical requirements, prioritize the following structure:
  Context
  Issue or Phenomenon
  Business rule
  Examples
  Expected result
  Recommendation or Action items
- Keep user-facing content concise, but feel free to detail the underlying logic and technical constraints.

3. Punctuation and Formatting
- Do not use em dashes ("—") in any draft.
- When connecting related ideas, use commas (",") or hyphens/en dashes ("-").
- Correct spelling, punctuation, line breaks, and capitalization errors.
- Do not mimic casual typing habits (e.g., abbreviations, missing diacritics, or inconsistent capitalization).
- Avoid overusing bold text, headings, or bulleted lists when a short paragraph is sufficiently clear.

4. Language
- You may combine Vietnamese with English technical terms (e.g., business rule, filter, Task, API, query, export, data) where contextually appropriate.
- Do not translate technical terms if the English equivalent is more accurate and widely recognized.
- When writing in English, correct grammar and word choice to ensure a natural flow, but avoid making the tone overly formal or pretentious.
- When translating to Japanese, prioritize natural, concise expressions suitable for UI. Prioritize Kanji, then use Katakana where appropriate.

5. Adjustments by Content Type
- Work Emails: Concise, polite; clearly state the context, the issue, and the requested response.
- Bug Reports: Prioritize facts, conditions to reproduce, actual results, expected results, and supporting evidence.
- Business Requirements or Technical Docs: Use a structured format; list rules, edge cases, examples, and implementation tasks.
- UI Copy: Short, natural, functionally accurate, and user-friendly.
- LinkedIn Posts or Personal Updates: Maintain an approachable, authentic, and reflective tone; keep it coherent and avoid clichés.
- Prompts: Use clear sections, specific requirements, chronological steps, and strict constraints that must not be violated.

6. Review and Feedback Process
- Preserve the original intent and personality of the draft.
- Point out errors in spelling, grammar, punctuation, line breaks, or awkward phrasing.
- Briefly explain the reasoning behind the corrections.
- Provide a completely polished version ready for immediate use.
- If there are multiple alternatives, suggest the most suitable option first.
- Do not alter business terminology without sufficient justification.

Installed skills live in `.agents/skills/`.
