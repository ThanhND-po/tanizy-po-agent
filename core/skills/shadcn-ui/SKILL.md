---
name: shadcn-ui
description: Project-aware shadcn/ui workflow for building code-first UI mockups, composing accessible components, and reviewing component usage. Use when creating a UI mockup with HTML/CSS/React, when the project has components.json, or when the user asks to use shadcn/ui, shadcn components, registries, or presets.
---

# shadcn/ui

Use shadcn/ui as a source-code component system for realistic, reviewable UI mockups. Prefer existing components, project tokens, and documented composition patterns over custom markup.

## Workflow

1. Inspect the project before writing code.

   - Read `components.json` when present.
   - Run `shadcn@latest info --json` only when `components.json` exists and the project's package runner is available.
   - Read the project context fields when available: `framework`, `packageManager`, `base`, `style`, `iconLibrary`, `aliases`, `resolvedPaths`, `tailwindVersion`, and `tailwindCssFile`.
   - Use the project's package runner for every CLI command: `npx shadcn@latest`, `pnpm dlx shadcn@latest`, or `bunx --bun shadcn@latest`.

   If `components.json` is missing, follow [Missing `components.json`](#missing-componentsjson) before running any shadcn command.

2. Map the screen to components before implementing it.

   - Check installed components first.
   - Search configured registries before writing a custom component.
   - Fetch component docs and examples before using unfamiliar components.
   - Do not guess a third-party registry. Ask for the registry when the request does not identify one.

3. Compose the mockup with the project's actual component API.

   - Use built-in variants and sizes before custom styles.
   - Use semantic tokens such as `bg-background`, `bg-primary`, and `text-muted-foreground`.
   - Preserve the project's aliases, base library, icon library, Tailwind version, and CSS token file.
   - If the project is not a shadcn project, use a temporary preview workspace when available. Do not initialize or alter the target project without approval.

4. Review the result.

   - Read every added or changed UI file.
   - Check component composition, imports, loading states, empty states, error states, responsive behavior, keyboard access, and visible focus.
   - Render the screen at the requested viewport and capture a browser screenshot when the environment supports it.
   - Fix issues before presenting the mockup for approval.

5. Update existing components cautiously.

   - Preview changes with `add --dry-run` and inspect diffs with `add --diff`.
   - Preserve local changes unless the user explicitly approves overwriting them.
   - Never use `--overwrite` without explicit approval.

## Missing `components.json`

Treat the absence of `components.json` as an unknown project state, not as proof that shadcn/ui is installed or unavailable.

1. Inspect the project without changing it.

   - Read `package.json` and the lockfile to identify the framework and package manager.
   - Look for `src/components`, `components/ui`, `app`, `pages`, Tailwind configuration, global CSS, and existing design tokens.
   - Check whether the project already contains shadcn-style components or another component system.

2. Choose the correct mode.

   - **Mockup-only request:** create a temporary preview workspace outside the target project. Initialize shadcn there only if the framework and package manager are clear, then render the mockup and capture the screenshot. Do not create `components.json` in the target project.
   - **Implementation request:** explain that the project is not yet configured as a shadcn project. Ask for approval before running `shadcn init` or creating `components.json` in the target project.
   - **Existing component system:** use that system unless the user explicitly asks to migrate to shadcn/ui. Do not mix APIs and do not claim that existing components are shadcn components.
   - **No compatible framework or CLI access:** create a semantic HTML/CSS preview that follows the shadcn composition and accessibility rules, and state that it is shadcn-inspired markup rather than installed shadcn/ui source.

3. After initializing a temporary or approved project, read the generated `components.json`, run `shadcn@latest info --json`, and continue with the normal workflow.

Never run `shadcn add`, `shadcn apply`, or `shadcn init` against a target project with missing `components.json` without explicit approval.

## Composition Rules

- Use `Button` for actions and its built-in `variant` and `size` values.
- Use `CardHeader`, `CardTitle`, `CardDescription`, `CardContent`, and `CardFooter` when composing a card.
- Use `FieldGroup` and `Field` for forms. Use `FieldSet` and `FieldLegend` for related checkbox or radio groups.
- Use `ToggleGroup` for a small set of mutually exclusive options instead of manually managing active buttons.
- Keep `SelectItem` inside `SelectGroup`, `DropdownMenuItem` inside `DropdownMenuGroup`, and `CommandItem` inside `CommandGroup`.
- Give `Dialog`, `Sheet`, and `Drawer` an accessible title, using a visually hidden title when appropriate.
- Place `TabsTrigger` inside `TabsList`.
- Give `Avatar` an `AvatarFallback`.
- Use `Alert`, `Empty`, `Separator`, `Skeleton`, `Badge`, and `sonner` for their corresponding patterns instead of custom styled markup.
- Use the project's icon library. Do not assume `lucide-react`.

## Styling Rules

- Use semantic design tokens and component variants, not raw Tailwind colors or one-off typography overrides.
- Use `flex` or `grid` with `gap-*`, not `space-x-*` or `space-y-*`.
- Use `size-*` when width and height are equal.
- Use `truncate` or `line-clamp-*` for long content and `min-w-0` on flex children that contain text.
- Use `cn()` for conditional classes.
- Do not add manual `z-index` to Dialog, Sheet, Popover, or Drawer overlays.
- Use `data-icon` for icons inside buttons and do not add manual icon sizing inside components.

## Mockup Component Map

| UI need | Preferred components |
|---|---|
| Primary action | `Button` |
| Form input | `Field`, `Input`, `Textarea`, `Select`, `Combobox`, `Checkbox`, `RadioGroup`, `Switch` |
| Navigation | `Sidebar`, `NavigationMenu`, `Breadcrumb`, `Tabs`, `Pagination` |
| Data display | `Table`, `Card`, `Badge`, `Avatar` |
| Overlay | `Dialog`, `Sheet`, `Drawer`, `AlertDialog` |
| Feedback | `Alert`, `sonner`, `Progress`, `Skeleton`, `Spinner` |
| Empty state | `Empty` |
| Menus and commands | `DropdownMenu`, `ContextMenu`, `Menubar`, `Command` inside `Dialog` |
| Layout | `Separator`, `Resizable`, `ScrollArea`, `Accordion`, `Collapsible` |

## Commands

Use the project package runner instead of assuming npm:

```bash
npx shadcn@latest info --json
npx shadcn@latest search
npx shadcn@latest docs button card dialog
npx shadcn@latest view @shadcn/button
npx shadcn@latest add button card --dry-run
npx shadcn@latest add button card
```

Replace `npx` with `pnpm dlx` or `bunx --bun` when required by the project.

## Source

Adapted for the Tanizy PO Agent from the [shadcn/ui skill](https://github.com/shadcn-ui/ui/blob/main/skills/shadcn/SKILL.md) and the [UI Skills shadcn reference](https://www.ui-skills.com/skills/shadcn-ui/shadcn). Keep this skill concise and load the upstream component docs only when a specific component is needed.
