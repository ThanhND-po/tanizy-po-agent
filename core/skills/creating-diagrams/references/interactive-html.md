# Standalone Interactive HTML Diagrams

Read this reference before generating an interactive HTML diagram or mockup.

## Artifact contract

- Deliver one standalone `.html` file that opens directly in a modern browser.
- Embed CSS, JavaScript, SVG icons, and illustrations inline. Do not use CDNs, remote fonts, external images, analytics, trackers, iframes, API calls, `fetch`, or browser storage.
- Use only information approved in the fact list or screen brief. Do not invent actors, system behavior, metrics, or UI text.
- Treat interaction as a review aid. It may reveal approved detail, filter an already-visible view, collapse a section, or move focus. It must not simulate an unimplemented backend.

## Document structure

- Use semantic landmarks: `header`, `main`, `section`, `nav`, and `footer` where relevant.
- Put the title, purpose, version or source context, legend, and reading instruction before the visual.
- For a Swimlane, use one labelled `section` per lane. Use CSS Grid for the lane layout and inline SVG with arrow markers for cross-lane connectors.
- Keep the happy path readable without any click. Put alternate, error, or detailed rationale in native `details` / `summary`, a labelled dialog, or a clearly named button with an adjacent panel.
- Give every control a semantic element, accessible name, visible keyboard focus, and a no-JavaScript baseline. Do not use a clickable `div`.

## Layout and interaction

- Use a readable desktop canvas and a responsive narrow layout. At small widths, retain lane names and flow order, with horizontal overflow only when it preserves a complex cross-lane flow better than reordering it.
- Use color only as a secondary cue. Include text labels and a legend for success, warning, error, manual action, and system action where applicable.
- Keep connectors behind cards, give arrow labels a solid background, and avoid crossed lines. Split the diagram when crossings cannot be resolved.
- Prefer `details` for optional step detail. If a modal, tab, or filter is necessary, implement Escape, focus management, and an obvious return path.
- Keep all JavaScript inline, small, and deterministic. It must not send or persist user data.

## Local validation

1. Open the temporary file locally and capture a desktop preview.
2. Test at a narrow mobile width and confirm no text, lane heading, connector label, or primary action is clipped.
3. Use keyboard only to reach and operate every interactive control. Confirm focus is visible and return focus after closing a modal or panel.
4. Inspect source for `http://`, `https://`, `fetch`, `XMLHttpRequest`, external `src` or `href` assets, and tracking code. External links explicitly approved for documentation are allowed only when they do not load automatically.
5. Compare visible paths with the fact list. Check every owner, handoff, decision outcome, alternate path, error path, and terminal state.

Report any check that could not be performed. Do not save the final HTML in the target project until the user approves the preview and destination.
