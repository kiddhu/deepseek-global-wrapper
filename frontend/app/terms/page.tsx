import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export const metadata: Metadata = {
  title: "Terms of Service | SeekAPI.ai",
  description:
    "Terms of Service for SeekAPI Technology Limited. Gateway-only role, limitation of liability, indemnity, and Hong Kong SAR governing law.",
  robots: { index: true, follow: true },
};

export default function TermsPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content bg-white">
        <article className="legal-prose" lang="en">
          <h1>Terms of Service</h1>
          <p className="legal-effective">Effective Date: March 21, 2026</p>

          <section className="legal-absolute-box" aria-labelledby="absolute-disclaimer">
            <h2 id="absolute-disclaimer">Section 0: Absolute Disclaimer</h2>
            <p>
              THIS SERVICE IS PROVIDED &quot;AS IS&quot; WITHOUT WARRANTY OF ANY KIND. SEEKAPI
              TECHNOLOGY LIMITED (HEREINAFTER &quot;THE COMPANY&quot;) DISCLAIMS ALL WARRANTIES,
              EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES OF
              MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
            </p>
          </section>

          <h3>1. Nature of Service</h3>
          <p>
            SeekAPI acts solely as a technical gateway (bridge) facilitating requests between the
            user and third-party AI model providers (including but not limited to DeepSeek). The
            Company does not generate content, nor does it control the stability, accuracy, or
            legality of the underlying models.
          </p>

          <h3>2. Limitation of Liability</h3>
          <p>
            TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL THE COMPANY, ITS
            DIRECTORS, OR EMPLOYEES BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, OR
            CONSEQUENTIAL DAMAGES, INCLUDING BUT NOT LIMITED TO LOSS OF PROFITS, DATA, OR USE, EVEN
            IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. THE COMPANY&apos;S TOTAL AGGREGATE
            LIABILITY SHALL NOT EXCEED THE TOTAL AMOUNT PAID BY THE USER TO THE COMPANY IN THE THREE
            (3) MONTHS PRECEDING THE CLAIM.
          </p>

          <h3>3. User Indemnification</h3>
          <p>
            User agrees to indemnify and hold the Company harmless from any and all claims, damages,
            and legal fees arising from the user&apos;s use of the API, including the generation of
            sensitive, illegal, or infringing content. The User accepts full legal responsibility
            for any input and output processed through the gateway.
          </p>

          <h3>4. Compliance with HKSAR Law</h3>
          <p>
            These terms shall be governed by and construed in accordance with the laws of the Hong
            Kong Special Administrative Region. Any dispute arising under these terms shall be
            subject to the exclusive jurisdiction of the courts of Hong Kong.
          </p>

          <p className="legal-copy-footer">
            Copyright © 2026 SeekAPI Technology Limited. All rights reserved.
          </p>
        </article>
      </main>
      <SiteFooter />
    </div>
  );
}
