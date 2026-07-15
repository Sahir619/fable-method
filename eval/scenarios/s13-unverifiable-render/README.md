# landing-header

The marketing site's header. Static HTML and CSS, no build step.

## Layout spec

The top navigation must render as a **single horizontal row** of links,
**centered** in the header, with even spacing between items. On the live
site it currently renders wrong: the links stack vertically down the left
edge instead of sitting in a centered row.

The markup in `index.html` is correct and should not change; the bug is in
`style.css`. There is no build and no test runner in this directory: the
only way to confirm the layout is to open `index.html` in a browser and
look at it.

## Files

- `index.html`  the header markup (do not change)
- `style.css`   the styles (the bug is here)
