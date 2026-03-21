// Use div+role instead of <footer>: some injections use `footer { display:none }` and hide the whole bar.
export function SiteFooter() {
  return (
    <div className="footer" role="contentinfo" aria-label="Site footer">
      <div className="footer-inner footer-three-col">
        <div className="footer-col footer-col-address">
          <p className="footer-address">
            <span className="footer-company">SeekAPI Technology Limited</span>
            <br />
            Room P11, Flat 2C, 2/F, Hung To Ctr., 94-96 How Ming St., Kwun Tong, Kowloon, Hong Kong
          </p>
        </div>
        <nav className="footer-col footer-col-links" aria-label="Legal and blog">
          <a className="footer-link-min" href="/terms">
            Terms
          </a>
          <a className="footer-link-min" href="/privacy">
            Privacy
          </a>
          <a className="footer-link-min" href="/refund">
            Refund
          </a>
          <a className="footer-link-min" href="/blog">
            Blog
          </a>
        </nav>
        <div className="footer-col footer-col-contact">
          <a className="footer-link-min footer-contact" href="mailto:support@seekapi.ai">
            support@seekapi.ai
          </a>
        </div>
      </div>
    </div>
  );
}
