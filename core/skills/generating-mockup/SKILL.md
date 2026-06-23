---
name: generating-mockup
description: Use when a Product Owner needs UI mockups or screen wireframes generated from a description, prototype document, or user story. Generates images using Stitch MCP (preferred) or Google Image generation (fallback).
---

# Generating Mockup

Generate UI mockup images from descriptions, prototype files, or user stories.

## Hard Gates

- Do not generate a mockup until the screen description, visual style, and target platform are clear.
- Do not abbreviate, paraphrase, or summarise the prompt before sending it to any image generation tool. Always send the full, detailed prompt.
- Do not write or save a file until the user approves the generated image.
- Do not run version-control actions.

## Tool Priority

```
1st choice: Stitch MCP  →  generate_screen_from_text / edit_screens
2nd choice: Google Image generation (built-in)
```

Never switch tools mid-session without telling the user.

## Workflow

1. **Gather context**
   - Read the prototype file, user story, or feature spec relevant to the screen.
   - Identify: screen name, component list, visual style (colors, typography, spacing), and target platform.
   - If any of these are missing, ask one question at a time before proceeding.

2. **Check Stitch MCP availability**
   - Attempt to call a lightweight Stitch MCP tool (e.g. list available screens or a minimal test call).
   - If the call succeeds → Stitch is available, continue with Stitch workflow (Step 3).
   - If the call fails or the tool is not connected → inform the user:

     > "Stitch MCP is not currently connected. Would you like me to use Google Image generation instead, or would you prefer to set up Stitch first?"

   - Wait for user response before proceeding.

3. **Build the full prompt — NEVER abbreviate**
   - Compose a prompt that contains ALL of the following. If any item is missing, ask the user before generating.

   **Required prompt sections:**

   ```
   [SCREEN_NAME] screen — [App / Project name]

   Components:
   [Full component list from prototype or user description — copy verbatim if a prototype doc exists]

   Visual Style:
   - [Color palette with exact hex codes, e.g. primary gradient #6C63FF → #4A90D9]
   - [Background: light/dark and color value]
   - [Typography: font family and weight]
   - [Corner radius, spacing, shadow style]
   - [Any branding or language-specific text — copy exactly as specified]

   Platform: [e.g. iOS mobile (390x844, iPhone 15 Pro) | Android (360x800) | Web Desktop (1440px)]
   ```

   - If a prototype document is referenced, copy the component list **verbatim** — do not summarise.
   - Preserve all hex color codes, exact text strings (including non-Latin characters), and dimension values.

4. **Pre-flight checklist before generating**

   Run this checklist silently. If any item fails, fix it before sending the prompt.

   - [ ] Prompt contains the full component list (not summarised)?
   - [ ] Prompt contains at least one hex color code for the primary action color?
   - [ ] Prompt specifies the platform and screen dimensions?
   - [ ] All exact text strings (button labels, headings) are preserved?
   - [ ] `deviceType` is set correctly if using Stitch (MOBILE / DESKTOP / TABLET)?

   If any item is unchecked → stop, gather the missing information, then rerun the checklist.

5. **Generate**
   - **Stitch path**: call `generate_screen_from_text` with the full prompt and correct `deviceType`. For each screen that requires high accuracy, generate separately rather than in batch.
   - **Google Image path**: call the image generation tool with the full prompt. Do not compress or simplify it.

6. **Verify similarity**
   - After generation, describe what was produced to the user.
   - Ask: "Does this match your prototype? If not, please point out what needs to change."
   - If refinements are needed:
     - **Stitch**: use `edit_screens` with a targeted instruction (do not re-describe everything, only the delta).
     - **Google Image**: regenerate with the corrected prompt.

7. **Approval and save**
   - After approval, ask where to save the image file.
   - Suggested folder: `docs/mockups/` or `docs/design/`.
   - Save using the screen name as the filename, e.g. `welcome_screen.png`.

8. **Next step**
   - Ask whether the user wants to generate another screen, create a diagram, or stop.

## Stitch-Specific Rules

### Rule 1: No prompt abbreviation

```
❌ FORBIDDEN: "Japanese fintech welcome screen"
✅ REQUIRED:  "Welcome screen with dark navy gradient (#1A1B2E → #2D3561), shield+key icon,
               [App name] branding in large bold text, primary CTA button [label text],
               secondary link [label text]. iOS mobile (390x844, iPhone 15 Pro)."
```

### Rule 2: Always append Visual Style and Platform

Every single-screen prompt must end with:
```
Visual Style:
- [Full style description with hex codes]

Platform: [device + dimensions]
```

### Rule 3: deviceType must be explicit

| Target | deviceType value |
|---|---|
| Mobile (iOS / Android) | `MOBILE` |
| Tablet | `TABLET` |
| Web / Desktop | `DESKTOP` |

Never omit `deviceType` or let it default.

### Rule 4: Generate screens individually for high accuracy

When a prototype has multiple screens, generate each one separately rather than in one batch call. This maximises similarity to the prototype.

### Rule 5: Preserve design tokens exactly

Do not omit or approximate these values when they are specified:

| Token type | Examples | Required in prompt? |
|---|---|---|
| Primary color / gradient | `#6C63FF → #4A90D9` | ✅ Always |
| Background color | `#1A1B2E`, `#FFFFFF` | ✅ Always |
| Success / error colors | `#34C759`, `#FF6B6B` | ✅ When state is shown |
| Platform / dimensions | `390x844, iPhone 15 Pro` | ✅ Always |
| Exact UI text | Button labels, headings | ✅ Always |

## Google Image Fallback Rules

When using Google Image generation as fallback:

- Apply the same full prompt structure as Stitch (no abbreviation).
- Be explicit about UI mockup intent: prefix with `"UI mockup screenshot of..."` to steer toward interface rendering.
- Specify the platform and approximate screen ratio.
- If the result lacks fidelity, inform the user and recommend connecting Stitch MCP for higher quality.
