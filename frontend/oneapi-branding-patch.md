# One-API Branding Patch (SeekAPI Minimal White)

Use this in One-API Admin:

- Custom CSS: paste the CSS block below.
- Header HTML: paste the HTML block below.

## Custom CSS

```css
/* SeekAPI visual override for One-API */
:root {
  --seek-primary: #000000;
  --seek-ink: #1f2937;
  --seek-bg: #ffffff;
  --seek-border: #e5e7eb;
}

/* Global */
body,
.layout,
.container,
.ant-layout {
  background: var(--seek-bg) !important;
  color: var(--seek-ink) !important;
}

/* Top navigation */
.ant-layout-header,
.semi-navigation,
.semi-navigation-header,
header {
  background: #ffffff !important;
  border-bottom: 1px solid var(--seek-border) !important;
  box-shadow: none !important;
}

.ant-layout-header *,
.semi-navigation *,
header * {
  color: var(--seek-ink) !important;
}

/* Cards and panels */
.ant-card,
.semi-card,
.ant-table,
.semi-table,
.ant-modal-content,
.semi-modal-content {
  border-radius: 8px !important;
  border: 1px solid var(--seek-border) !important;
  box-shadow: none !important;
}

/* Buttons */
.ant-btn,
.semi-button,
button {
  border-radius: 8px !important;
}

.ant-btn-primary,
.semi-button-primary {
  background: var(--seek-primary) !important;
  border-color: var(--seek-primary) !important;
  color: #ffffff !important;
}

/* Inputs */
.ant-input,
.semi-input,
.ant-select-selector {
  border-radius: 8px !important;
  border-color: var(--seek-border) !important;
}

/* Hide One-API brand traces in footer/header text blocks */
footer *:where(:not(script)):not(style),
.footer *:where(:not(script)):not(style),
.ant-layout-footer *:where(:not(script)):not(style) {
  color: transparent !important;
  text-shadow: none !important;
}

/* Replace image logos with SeekAPI text mark where possible */
img[alt*="One-API" i],
img[src*="one-api" i],
.logo img {
  opacity: 0 !important;
}

.logo::after,
[class*="logo"]::after {
  content: "SeekAPI";
  color: #111827;
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.04em;
}
```

## Header HTML

```html
<div
  id="seekapi-brand-header"
  style="display:flex;align-items:center;justify-content:space-between;padding:10px 16px;border-bottom:1px solid #e5e7eb;background:#fff;"
>
  <div style="font-size:18px;font-weight:700;letter-spacing:.04em;color:#111827;">SeekAPI</div>
  <div style="font-size:12px;color:#6b7280;">Global DeepSeek Gateway</div>
</div>
```

## Notes

- If your One-API panel supports custom login logo URL, upload a SeekAPI wordmark and set it in panel settings.
- If CSS selectors vary by One-API version/theme, inspect and map equivalent classes (`.ant-*` or `.semi-*`).
