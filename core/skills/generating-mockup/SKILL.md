---
name: generating-mockup
description: Use when a Product Owner needs UI mockups, screen wireframes, or a client-facing screen preview generated from a requirement document, prototype, user story, or description. Supports Stitch MCP, code-first shadcn/ui prototypes with browser screenshots, agent-native image generation, and Google Image generation.
---

# Generating Mockup

Generate a UI mockup that a Product Owner can attach to a Basic Design or present to a customer. Use the code-first path when the current agent cannot access Stitch or an image generation tool.

## Hard Gates

- Do not call any generation tool or check tool availability until the screen description, visual style, and target platform are fully clarified and confirmed by the user.
- Do not abbreviate, paraphrase, or summarise the final prompt before sending it to an image generation tool. Send the complete prompt.
- Do not save final image or source files into the target project until the user approves the generated image or browser preview and confirms the destination path.
- Temporary files used only to render a preview may be created outside the target project when the environment supports them. Do not leave unapproved preview artifacts in the target project.
- Do not run version-control actions.

## Tool Priority

Choose the first available mode that can satisfy the requested output. Tell the user which mode is selected before generating. Do not switch modes mid-session without explaining why and getting confirmation.

| Priority | Mode | Use when |
|---|---|---|
| 1 | Stitch MCP | Connected and the user needs an image or generated screen with high visual fidelity |
| 2 | Code-first shadcn/ui + browser screenshot | The user uses Claude Code, Codex, or another coding agent without Stitch or image generation; also preferred when exact UI text matters |
| 3 | Agent-native image generation | The current agent exposes an image generation tool and the user wants a visual concept rather than executable UI source |
| 4 | Google Image generation | Available and explicitly selected by the user or required by the current environment |

Figma is a reference source, not a default generation fallback. When the user provides a Figma file or link and the Figma integration is available, read its design context, variables, screenshot, and assets before selecting a generation mode.

If no browser or screenshot capability is available for the code-first path, provide the runnable preview source and clearly state that an image screenshot could not be captured. Do not claim that an image was generated.

## Workflow

### 1. Gather and confirm the screen brief

Read the relevant Basic Design, user story, prototype file, or feature specification. Identify:

- Screen name and business purpose
- User role and entry point
- Complete component list
- Main flow, alternative flow, loading, empty, error, disabled, and permission states
- Exact UI text, including non-Latin text
- Visual style, colors, typography, spacing, radius, shadows, and brand rules
- Target platform and viewport, such as iOS 390x844, Android 360x800, tablet, or desktop 1440px
- Required output, image only, runnable code preview, or both

Ask one question at a time when information is missing. Stop until the user confirms the completed brief. Do not check Stitch, Figma, browser, or image tools before this confirmation.

### 2. Audit the layout and component plan

After the brief is confirmed:

1. Load `web-design-guidelines/SKILL.md` and apply its accessibility, hierarchy, form, focus, content, image, and responsive rules.
2. For the code-first path, load `shadcn-ui/SKILL.md` and map the screen to existing shadcn/ui components before proposing custom markup.
3. Correct issues before generation. Examples include missing form labels, unclear primary action, missing empty or error states, unsupported contrast, incorrect overlay structure, or a component that should use a standard shadcn pattern.
4. Present the audited brief and wait for confirmation before proceeding.

Use the installed skill path for the current tool. It may be `.agents/skills/`, `.claude/skills/`, or `skills/`, depending on the adapter.

### 3. Select the generation mode

Use this decision order after the audited brief is confirmed:

- Use Stitch when it is connected and the user needs a generated screen image.
- Use code-first shadcn/ui when working in Claude Code or Codex without Stitch or image generation, or when exact text and interaction states matter more than decorative imagery.
- Use the current agent's native image tool when it is available and appropriate for a visual concept.
- Use Google Image only when it is available and selected or required by the environment.

For Claude Code and Codex, do not ask the BA/PO to configure Stitch or Google Image. Default to the code-first shadcn/ui path, explain that the preview will be rendered in a browser, and ask only for confirmation of the audited brief.

### 4. Build the complete generation brief

For image generation, send a complete prompt with this structure:

```text
[SCREEN_NAME] screen for [APP_OR_PROJECT]

Purpose and user:
[Business purpose and primary user]

Components:
[Complete component list and hierarchy, copied verbatim from the approved brief when a source document exists]

States and interactions:
[Loading, empty, error, disabled, permission, validation, and key interaction states]

Visual Style:
- Primary color or gradient with exact hex values
- Background color with exact hex value
- Typography, font family, sizes, and weights
- Spacing scale, corner radius, border, and shadow treatment
- Brand assets and language-specific text copied exactly

Platform:
[Device or browser and exact dimensions]

Output:
[UI mockup screenshot, no invented text, no unrelated decorative elements]
```

For the code-first path, use the equivalent implementation brief:

```text
Build a [PLATFORM] UI preview for [SCREEN_NAME] using the project's shadcn/ui components.
Preserve the approved component hierarchy, exact text, design tokens, viewport, and all states.
Read components.json and project context before choosing APIs, aliases, base primitives, Tailwind version, and icon library.
Use semantic tokens and built-in component variants. Render the preview at [DIMENSIONS] and capture a screenshot.
```

Do not invent text, colors, component states, or dimensions. If the approved brief does not define them, ask before generating.

### 5. Run the pre-flight checklist

Before generating or rendering, confirm:

- [ ] The complete component hierarchy is present.
- [ ] The brief includes the primary user, purpose, and screen entry point.
- [ ] Loading, empty, error, disabled, and permission states are covered when relevant.
- [ ] The layout has been audited with `web-design-guidelines`.
- [ ] The code-first path has been audited with `shadcn-ui`.
- [ ] The primary action color and background use exact values or approved semantic tokens.
- [ ] Exact UI text is preserved.
- [ ] Platform and dimensions are explicit.
- [ ] `deviceType` is set for Stitch: `MOBILE`, `TABLET`, or `DESKTOP`.
- [ ] The selected tool is available and matches the user's environment.

If any item fails, stop and resolve it before generating.

### 6. Generate or render

- Stitch: call `generate_screen_from_text` with the complete prompt and correct `deviceType`. Generate high-accuracy screens individually.
- Code-first: use `shadcn-ui`. If the target project has no `components.json`, create the preview in a temporary workspace instead of initializing or changing the target project. Run the local app and capture the requested viewport with the available browser or screenshot tool.
- Agent-native image generation: use the complete image prompt without compression.
- Google Image: prefix the prompt with `UI mockup screenshot of...`, preserve the complete prompt, and specify the platform ratio.

### 7. Verify similarity and usability

Compare the result against the approved brief:

- Check text, layout, hierarchy, color, spacing, viewport, component states, and branding.
- Check accessibility and interaction affordances against `web-design-guidelines`.
- For code-first output, inspect the rendered screenshot and source for incorrect imports, missing components, invalid composition, and responsive issues.
- If the result is not usable, describe the gap and propose a targeted correction.

For refinements:

- Stitch: use `edit_screens` with only the approved delta.
- Code-first: update the preview source, re-render, and capture again.
- Image generation: regenerate with the corrected complete prompt.

### 8. Request approval and save

Ask:

> Does this mockup match the approved brief? If not, tell me what needs to change.

After approval, ask where to save the final artifact. Suggested locations are `docs/mockups/` for images and `docs/design/` for approved source or preview files. Use the screen name as the filename, such as `leave-request-list.png`.

### 9. Continue the workflow

Ask whether the user wants to generate another screen, attach the mockup to the Basic Design, create a diagram, or stop.

## Stitch Rules

- Always include the full component list, exact text, visual tokens, platform, and dimensions.
- Always append the full Visual Style and Platform sections.
- Always set `deviceType` explicitly.
- Generate each high-accuracy screen separately.
- Preserve all specified color, typography, spacing, dimension, and text values.

## Code-First shadcn/ui Rules

- Use existing components and documented composition before custom markup.
- Use semantic tokens such as `bg-background`, `bg-primary`, and `text-muted-foreground`.
- Use `gap-*` instead of `space-x-*` or `space-y-*`, `size-*` for equal dimensions, and `cn()` for conditional classes.
- Do not assume `lucide-react`; use the icon library from project context.
- Give Dialog, Sheet, and Drawer an accessible title, and keep items inside their required groups.
- Use `Field` patterns for forms, `Empty` for empty states, `Skeleton` for loading, `Alert` for callouts, and `Badge` for status.
- Do not initialize, overwrite, or modify the target project before approval.
