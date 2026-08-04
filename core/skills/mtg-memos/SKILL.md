---
name: mtg-memos
description: Read Japanese, Vietnamese, English, or multilingual meeting memo and transcript files, clarify uncertain context without guessing, and produce a concise channel-ready meeting summary with the MTG name, Meeting Overview, highlighted Key Concepts, and priority-ordered Action Items with PIC when stated. Use when the user provides a meeting memo file or folder and asks to understand, translate, summarize, recap, or prepare the discussion for sharing.
---

# MTG Memos

Turn meeting memos and transcripts into accurate, concise summaries suitable for posting to a team channel.

## Hard Gates

- Read the user-provided memo files before summarizing.
- Do not infer missing context, decisions, commitments, PICs, deadlines, or priorities without sufficient evidence.
- Ask one focused question at a time when an uncertainty could change the Meeting purpose, Key topics, Key concepts, decisions, or Action Items.
- Do not produce the final summary until all material uncertainties are resolved.
- Do not write or modify files unless the user explicitly asks to save the approved summary and confirms the target path.
- Do not run version-control actions.

## Workflow

### 1. Resolve the input scope

- Accept a meeting memo file or folder path from the user.
- If the input is a folder, inspect its files and determine whether they belong to one MTG or multiple MTGs.
- If the folder contains multiple MTGs or unrelated files, ask which MTG or files are in scope before reading further.
- If one MTG is split across multiple files, read all relevant parts in chronological order when that order can be established from file metadata or content.
- Report inaccessible, unsupported, empty, or apparently incomplete files. Do not silently omit them.

### 2. Understand the discussion

- Identify the explicit MTG name, participants when relevant, purpose, Key topics, Key concepts, decisions, concerns, dependencies, and agreed follow-up work.
- Treat the memo as potentially machine-generated. Check for mistranscribed names, inconsistent terminology, broken sentences, duplicated passages, and contradictions.
- Distinguish statements discussed as possibilities from decisions or commitments. Do not convert a suggestion into an Action Item.
- Preserve Product names, Feature names, proper nouns, and established business or technical terminology.
- When a Japanese memo appears to represent a Vietnamese or multilingual discussion, derive meaning only from the available text. Do not reconstruct missing original speech.

### 3. Run the Context Gate

Before drafting, confirm internally that the available evidence establishes:

- the MTG name;
- the Meeting purpose;
- the Key topics and their relationship;
- the Key concepts that require emphasis or explanation;
- each agreed Action Item;
- the PIC for an Action Item when explicitly assigned;
- the relative priority of each Action Item.

If any material item is unclear, ask the user one focused question and wait for the answer. Use the transcript evidence in the question so the user can resolve the ambiguity quickly. Do not present a speculative interpretation as a choice unless the transcript actually supports that interpretation.

For priority, use `High`, `Medium`, or `Low`. Base the ranking on explicit urgency, deadlines, blocking dependencies, or ordering agreed in the MTG. If the transcript does not provide enough evidence to rank an Action Item, ask the user to confirm its priority.

### 4. Run the Meeting Overview Value Gate

Write `Meeting Overview` only from information that helps the reader understand the Meeting purpose, business or Product scope, important decisions, implementation direction, outcomes, or dependencies.

Reject and rewrite the overview if it contains any of the following:

- notes about how the summary was produced;
- generic transcript-quality disclaimers;
- observations about automatic transcription, mixed languages, recognition errors, or source formatting;
- generic statements such as `The meeting discussed...` that do not explain the actual purpose, direction, or outcome;
- caveats that do not change the interpretation of the MTG;
- content that belongs in an internal evidence assessment rather than the channel-ready summary.

Use transcript quality only as an internal confidence constraint. If a source issue creates a material ambiguity, stop and ask the user to clarify it under the Context Gate. Do not replace clarification with a disclaimer in `Meeting Overview`.

Before proceeding, confirm that every sentence in `Meeting Overview` contributes at least one of these values:

- explains why the MTG was held;
- identifies the Product or implementation scope;
- records an agreed direction or decision;
- explains an important relationship, sequence, or dependency;
- communicates an outcome needed by the target audience.

### 5. Draft the summary

- Write the summary in Vietnamese by default unless the user requests another output language.
- Keep the result concise and ready to paste into a team channel.
- Correct obvious transcription noise only when the intended meaning is unambiguous.
- Order Action Items from `High` to `Low`.
- Use `Not specified` for a PIC only when the Action Item is explicit but no PIC was assigned.
- Omit sections or facts that are outside the required format instead of adding unsupported detail.

Use this exact structure:

```markdown
# <MTG Name>

## Meeting Overview

<Tóm tắt ngắn gọn Meeting purpose và Key topics.>

### Key Concepts

- **<English term>**: <Giải thích ngắn gọn bằng ngôn ngữ output.>

## Action Items

| Priority | Action Item | PIC |
|---|---|---|
| High | <Agreed action> | <Explicit PIC or Not specified> |
```

If the MTG has no agreed Action Items, state `No Action Items were agreed in the MTG.` Do not invent follow-up work.

## Terminology Rules

- Write every business, Product, process, role, Feature, system, data, and technical term in English.
- Use the output language only to explain a term or connect the factual summary.
- Prefer the established English term over a Vietnamese or Japanese translation when the meaning is known.
- Keep the original term and ask the user when converting it to English could change its business meaning.
- Highlight each Key Concept with bold formatting, followed by a plain-language explanation.
- Keep abbreviations such as `MTG`, `PIC`, `API`, and `UI` unchanged when appropriate.

Example:

```markdown
### Key Concepts

- **Deep-sealing (learning) process**: Quy trình phân rã một skill cấp cao thành các thành phần có thể học và thực hành.
- **Micro-skills**: Các skill nhỏ có thể được dạy, luyện tập và đánh giá độc lập.
- **Knowledge base / database**: Kinh nghiệm và skill được tổ chức thành data có cấu trúc gồm các bước cơ bản.
```

## Save Gate

- Present the summary in chat first.
- If the user asks to save it, recommend Markdown.
- Prefer an existing meeting-notes folder in the target project.
- If none exists, propose creating a `meeting-notes/` folder in that project.
- Follow the existing project filename convention. If no convention exists, propose a descriptive English lowercase kebab-case filename.
- Wait for the user to approve the exact file path before writing.
- After writing, run the project's Markdown validator when one exists.
