const NAV_ITEMS = [
  { href: "/", label: "Home" },
  { href: "/about", label: "About" },
  { href: "/pricing", label: "Pricing" },
  { href: "/compare", label: "Compare" },
  { href: "/docs", label: "Docs" },
  { href: "/status", label: "Status" },
];

export function SiteHeader() {
  return (
    <header className="site-header">
      <div className="site-header-inner">
        <a href="/" className="site-title" aria-label="SeekAPI Home">
          SeekAPI
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
