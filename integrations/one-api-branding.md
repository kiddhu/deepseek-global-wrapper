# One-API visual patch (SeekAPI / dash.seekapi.ai)

Operator: **SeekAPI Technology Limited**

Paste into your One-API admin **Custom CSS** and **Custom announcement / header HTML** (field names vary by version—use the closest “custom CSS” and “site notice” or “header HTML” settings).

---

## 1) Custom CSS (copy everything below)

```css
/* SeekAPI Console — One-API “visual facelift”
   Targets Ant Design + Semi Design + common layouts. Inspect and extend if your build differs. */

@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap");

:root {
  --seekapi-black: #000000;
  --seekapi-ink: #111827;
  --seekapi-muted: #6b7280;
  --seekapi-bg: #ffffff;
  --seekapi-border: #e5e7eb;
}

html,
body,
#root,
#app {
  font-family:
    Inter,
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif !important;
  background: var(--seekapi-bg) !important;
  color: var(--seekapi-ink) !important;
}

/* —— Force-hide top-left header logo <img> (multiple selectors for version drift) —— */
.ant-layout-header img,
.ant-pro-global-header img,
.ant-pro-layout-header img,
header[class*="header"] img,
.semi-layout-header img,
.semi-navigation-header img,
.semi-navigation img:first-of-type,
[class*="layout-header"] img {
  display: none !important;
  visibility: hidden !important;
  width: 0 !important;
  height: 0 !important;
  opacity: 0 !important;
  pointer-events: none !important;
  position: absolute !important;
  clip: rect(0, 0, 0, 0) !important;
}

/* Optional: text mark next to hidden logo */
.ant-layout-header .logo::after,
.ant-pro-global-header .logo::after,
header .logo::after {
  content: "SeekAPI";
  display: inline-block;
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: 0.02em;
  color: var(--seekapi-ink);
}

/* —— Primary tone: pure black —— */
.ant-btn-primary,
.semi-button-primary,
button[type="submit"].ant-btn-primary {
  background: var(--seekapi-black) !important;
  border-color: var(--seekapi-black) !important;
  color: #ffffff !important;
}

.ant-btn-primary:hover,
.semi-button-primary:hover {
  background: #1f2937 !important;
  border-color: #1f2937 !important;
  color: #ffffff !important;
}

/* Links & focus accents */
a.ant-btn-link,
.ant-menu-item-selected,
.ant-tabs-tab-active .ant-tabs-tab-btn {
  color: var(--seekapi-black) !important;
}

.ant-checkbox-checked .ant-checkbox-inner,
.ant-switch-checked,
.ant-radio-checked .ant-radio-inner {
  background-color: var(--seekapi-black) !important;
  border-color: var(--seekapi-black) !important;
}

/* —— Buttons: 8px radius —— */
.ant-btn,
.semi-button,
button {
  border-radius: 8px !important;
}

.ant-input,
.ant-input-affix-wrapper,
.ant-select-selector,
.ant-picker,
.semi-input,
.semi-select,
textarea {
  border-radius: 8px !important;
}

.ant-card,
.semi-card {
  border-radius: 8px !important;
  border-color: var(--seekapi-border) !important;
  box-shadow: none !important;
}

/* Header / shell: minimal white */
.ant-layout-header,
.ant-pro-global-header,
.semi-layout-header,
header[class*="header"] {
  background: var(--seekapi-bg) !important;
  border-bottom: 1px solid var(--seekapi-border) !important;
  box-shadow: none !important;
}

.ant-layout-sider,
.semi-layout-sider {
  background: #fafafa !important;
  border-right: 1px solid var(--seekapi-border) !important;
}

.ant-layout,
.semi-layout {
  background: var(--seekapi-bg) !important;
}

/* —— Hide One-API open-source / branding in footer (links + common containers) —— */
.ant-layout-footer a[href*="songquanpeng"],
.ant-layout-footer a[href*="one-api"],
.ant-layout-footer a[href*="One-API"],
.ant-pro-global-footer a[href*="github.com"],
footer a[href*="songquanpeng"],
footer a[href*="one-api"],
footer a[href*="One-API"],
.semi-layout-footer a[href*="github"],
.semi-layout-footer a[href*="one-api"],
.semi-layout-footer a[href*="One-API"] {
  display: none !important;
}

/* Pro layout global footer strip */
.ant-pro-global-footer {
  display: none !important;
}

/* If your build prints plain “One API” text in footer, hide the whole footer bar (use custom HTML notice instead). Uncomment if needed:
.ant-layout-footer { display: none !important; }
*/
```

---

## 2) Home / announcement HTML (copy everything below)

Use as **system announcement**, **login page notice**, or **custom HTML block** (per your One-API version).

```html
<div
  style="
    margin: 0 0 16px 0;
    padding: 20px 22px;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    font-family: Inter, system-ui, -apple-system, sans-serif;
    color: #111827;
    box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
  "
>
  <div
    style="font-size: 11px; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase; color: #6b7280; margin-bottom: 8px;"
  >
    SeekAPI
  </div>
  <h1
    style="margin: 0 0 8px 0; font-size: 22px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.2;"
  >
    SeekAPI Console
  </h1>
  <p style="margin: 0; font-size: 15px; line-height: 1.55; color: #4b5563;">
    Secure gateway to world-class reasoning models.
  </p>
</div>
```

---

## Notes

- If **Inter** is blocked by CSP, remove the `@import` line; the stack falls back to system UI.
- After pasting CSS, **hard refresh** (Ctrl+Shift+R) and re-check; some builds cache admin assets.
- **SeekAPI Technology Limited** is the legal entity for customer-facing copy on seekapi.ai; this patch is for the dashboard skin only.
