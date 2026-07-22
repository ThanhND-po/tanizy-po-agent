---
name: generating-mockup
description: Use when a Product Owner needs UI mockups, screen wireframes, a standalone interactive HTML prototype, or a client-facing screen preview generated from a requirement document, prototype, user story, or description. Supports local HTML prototypes, Stitch MCP, code-first shadcn/ui prototypes with browser screenshots, agent-native image generation, and Google Image generation.
---

# Generating Mockup

Generate a UI mockup that a Product Owner can attach to a Basic Design or present to a customer. Use standalone interactive HTML when the artifact must be broadly shareable without a project runtime or external generation service.

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
| 2 | Standalone interactive HTML + local browser preview | The user needs a self-contained shareable prototype, clickable state transitions, or exact UI text, and does not need the target application's runtime or backend |
| 3 | Code-first shadcn/ui + browser screenshot | The project has usable UI context, the user needs production-like component composition, or the preview is likely to become implementation source |
| 4 | Agent-native image generation | The current agent exposes an image generation tool and the user wants a visual concept rather than executable UI source |
| 5 | Google Image generation | Available and explicitly selected by the user or required by the current environment |

Figma is a reference source, not a default generation fallback. When the user provides a Figma file or link and the Figma integration is available, read its design context, variables, screenshot, and assets before selecting a generation mode.

If no browser or screenshot capability is available for a HTML or code-first path, provide the runnable preview source and clearly state that an image screenshot could not be captured. Do not claim that an image was generated.

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
- Required output, image only, standalone interactive HTML prototype, runnable code preview, or both

Ask one question at a time when information is missing. Stop until the user confirms the completed brief. Do not check Stitch, Figma, browser, or image tools before this confirmation.

### 2. Audit the layout and component plan

After the brief is confirmed:

1. Load `web-design-guidelines/SKILL.md` and apply its accessibility, hierarchy, form, focus, content, image, and responsive rules.
2. For the standalone HTML path, read `../creating-diagrams/references/interactive-html.md` and apply its self-contained artifact, accessibility, interaction, and local-validation rules.
3. For the code-first path, load `shadcn-ui/SKILL.md` and map the screen to existing shadcn/ui components before proposing custom markup.
4. Correct issues before generation. Examples include missing form labels, unclear primary action, missing empty or error states, unsupported contrast, incorrect overlay structure, or a component that should use a standard shadcn pattern.
5. Present the audited brief and wait for confirmation before proceeding.

Use the installed skill path for the current tool. It may be `.agents/skills/`, `.claude/skills/`, or `skills/`, depending on the adapter.

### 3. Select the generation mode

Use this decision order after the audited brief is confirmed:

- Use Stitch when it is connected and the user needs a generated screen image.
- Use standalone interactive HTML when the user needs a browser-openable single file, UI behavior that can be reviewed without a backend, or a prototype that must not call external generation services.
- Use code-first shadcn/ui when the target project's components and design tokens must be represented faithfully, or when the prototype is likely to become implementation source.
- Use the current agent's native image tool when it is available and appropriate for a visual concept.
- Use Google Image only when it is available and selected or required by the environment.

For Claude Code and Codex, do not ask the BA/PO to configure Stitch or Google Image. Prefer standalone interactive HTML for a self-contained shareable prototype. Prefer the code-first shadcn/ui path when project component fidelity or reusable implementation source matters. Explain the selected mode and ask only for confirmation of the audited brief.

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

For standalone HTML, use this implementation brief:

```text
Build a self-contained interactive HTML preview for [SCREEN_NAME] at [DIMENSIONS].
Preserve the approved component hierarchy, exact text, tokens, viewport, and relevant states.
Use semantic HTML, inline CSS, and small inline JavaScript only for approved review interactions.
Do not use a CDN, remote font, image, icon, tracker, iframe, API call, fetch, browser storage, or backend simulation.
The primary flow must be understandable without clicking. Controls must work with keyboard and have visible focus.
Render locally and capture a screenshot.
```

Do not invent text, colors, component states, or dimensions. If the approved brief does not define them, ask before generating.

### 5. Run the pre-flight checklist

Before generating or rendering, confirm:

- [ ] The complete component hierarchy is present.
- [ ] The brief includes the primary user, purpose, and screen entry point.
- [ ] Loading, empty, error, disabled, and permission states are covered when relevant.
- [ ] The layout has been audited with `web-design-guidelines`.
- [ ] The standalone HTML path has been audited with `interactive-html.md`, including no external runtime assets or calls.
- [ ] The code-first path has been audited with `shadcn-ui`.
- [ ] The primary action color and background use exact values or approved semantic tokens.
- [ ] Exact UI text is preserved.
- [ ] Platform and dimensions are explicit.
- [ ] `deviceType` is set for Stitch: `MOBILE`, `TABLET`, or `DESKTOP`.
- [ ] The selected tool is available and matches the user's environment.

If any item fails, stop and resolve it before generating.

### 6. Generate or render

- Stitch: call `generate_screen_from_text` with the complete prompt and correct `deviceType`. Generate high-accuracy screens individually.
- Standalone HTML: create the preview in a temporary workspace outside the target project. Keep CSS, JavaScript, icons, and images inline. Render it locally at the approved viewport and capture a screenshot. Do not start a public server or use a public renderer.
- Code-first: use `shadcn-ui`. If the target project has no `components.json`, create the preview in a temporary workspace instead of initializing or changing the target project. Run the local app and capture the requested viewport with the available browser or screenshot tool.
- Agent-native image generation: use the complete image prompt without compression.
- Google Image: prefix the prompt with `UI mockup screenshot of...`, preserve the complete prompt, and specify the platform ratio.

### 7. Verify similarity and usability

Compare the result against the approved brief:

- Check text, layout, hierarchy, color, spacing, viewport, component states, and branding.
- Check accessibility and interaction affordances against `web-design-guidelines`.
- For standalone HTML, inspect the source for remote assets or network calls, test each approved interaction with keyboard, verify the no-JavaScript baseline where applicable, and check desktop plus narrow viewport rendering.
- For code-first output, inspect the rendered screenshot and source for incorrect imports, missing components, invalid composition, and responsive issues.
- If the result is not usable, describe the gap and propose a targeted correction.

For refinements:

- Stitch: use `edit_screens` with only the approved delta.
- Standalone HTML: update the temporary source, re-render locally, and capture again.
- Code-first: update the preview source, re-render, and capture again.
- Image generation: regenerate with the corrected complete prompt.

### 8. Request approval and save

Ask:

> Does this mockup match the approved brief? If not, tell me what needs to change.

After approval, ask where to save the final artifact. Suggested locations are `docs/mockups/` for images and `docs/design/` for approved source or preview files. Use the screen name as the filename, such as `leave-request-list.png` or `leave-request-list.html`.

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

## Standalone Interactive HTML Rules

- Read `../creating-diagrams/references/interactive-html.md` before generating this mode.
- Deliver one self-contained `.html` file that opens in a modern browser without installing dependencies.
- Use interaction only for approved UI behavior or review aids. Do not imply that a backend workflow is implemented.
- Do not use external resources or automatic network requests. Include SVG icons or illustrations inline, or omit them.
- Do not save the approved source into the target project until the user approves the local preview and destination.
