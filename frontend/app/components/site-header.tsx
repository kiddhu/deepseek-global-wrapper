const NAV_ITEMS = [
  { href: "/", label: "Home" },
  { href: "/pricing", label: "Pricing" },
  { href: "/compare", label: "Compare" },
  { href: "/docs", label: "Docs" },
  { href: "/blog", label: "Blog" },
  { href: "/status", label: "Status" },
  { href: "/terms", label: "Terms" },
  { href: "/refund", label: "Refund" },
  { href: "/privacy", label: "Privacy" },
];

export function SiteHeader() {
  return (
    <header className="site-header">
      <div className="site-header-inner">
        <a href="/" className="site-brand" aria-label="SeekAPI Home">
          <img
            src="https://github.com/kiddhu/seekapi-assets/blob/main/logo5.png?raw=true"
            alt="SeekAPI"
            className="site-logo"
          />
        </a>
        <nav className="site-nav" aria-label="Primary">
          {NAV_ITEMS.map((item) => (
            <a key={item.href} href={item.href} className="site-nav-link">
              {item.label}
            </a>
          ))}
        </nav>
      </div>
    </header>
  );
}
