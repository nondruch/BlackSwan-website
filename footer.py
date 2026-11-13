def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

FOOT_COLS = [
  ("Who We Are", [("Introduction", "#introduction"), ("Our Team", "#our-team"), ("Philosophy and Process", "#philosophy-and-process"), ("Our Values", "#our-values")]),
  ("Divisions & Performance", [("Business & Finance", "#business-and-finance"), ("Economics & Politics", "#economics-and-politics"), ("Cross-Domain", "#cross-domain"), ("Market Studies", "#market-studies"), ("Algorithmic Development", "#algorithmic-development"), ("Performance", "#performance")]),
  ("Publications", [("Investment Research", "#investment-research"), ("Market Perspectives", "#market-perspectives")]),
  ("Student Opportunities", [("Events", "#events"), ("Apply", "#how-to-apply"), ("Members Login", "https://www.blackswanstudents.com/login")]),
]

IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2.2c3.2 0 3.6 0 4.8.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1.1.4 2.2.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1.1.4-2.2.4-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1.1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1.1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2Zm0 1.8c-3.1 0-3.5 0-4.7.1-1 .1-1.6.2-1.9.3-.5.2-.8.4-1.1.7-.3.3-.6.7-.7 1.1-.1.4-.3.9-.3 1.9-.1 1.2-.1 1.6-.1 4.7s0 3.5.1 4.7c.1 1 .2 1.6.3 1.9.2.5.4.8.7 1.1.3.3.7.6 1.1.7.4.1.9.3 1.9.3 1.2.1 1.6.1 4.7.1s3.5 0 4.7-.1c1-.1 1.6-.2 1.9-.3.5-.2.8-.4 1.1-.7.3-.3.6-.7.7-1.1.1-.4.3-.9.3-1.9.1-1.2.1-1.6.1-4.7s0-3.5-.1-4.7c-.1-1-.2-1.6-.3-1.9-.2-.5-.4-.8-.7-1.1-.3-.3-.7-.6-1.1-.7-.4-.1-.9-.3-1.9-.3-1.2-.1-1.6-.1-4.7-.1Zm0 3.1a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8Zm0 8a3.1 3.1 0 1 0 0-6.2 3.1 3.1 0 0 0 0 6.2Zm6.2-8.2a1.15 1.15 0 1 1-2.3 0 1.15 1.15 0 0 1 2.3 0Z"/></svg>'
LI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28ZM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13ZM7.12 20.45H3.56V9h3.56v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0Z"/></svg>'
EM = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M2 5.5A1.5 1.5 0 0 1 3.5 4h17A1.5 1.5 0 0 1 22 5.5v13a1.5 1.5 0 0 1-1.5 1.5h-17A1.5 1.5 0 0 1 2 18.5v-13Zm2.1.3 7.3 6.1c.35.3.85.3 1.2 0l7.3-6.1H4.1ZM20 7.6l-6.1 5.1a2.9 2.9 0 0 1-3.8 0L4 7.6V18h16V7.6Z"/></svg>'


def _link(name, href):
    ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
    return f'<li><a class="pf-link" href="{href}"{ext}>{_esc(name)}</a></li>'


import pathlib
GRAPHIC = (pathlib.Path(__file__).parent / 'footer-graphic.svg').read_text()


def footer_html(logo):
    cols = "".join(
        f'<li class="pf-col"><span class="pf-title">{_esc(t)}</span><ul class="pf-sub">' + "".join(_link(n, h) for n, h in links) + '</ul></li>'
        for t, links in FOOT_COLS)
    legal = ("<li>© 2026 Black Swan Student Society. All Rights Reserved</li>"
             '<li><a class="pf-ulink" href="https://www.blackswanstudents.com/privacy" target="_blank" rel="noopener">Privacy Notice</a></li>'
             '<li><a class="pf-ulink" href="mailto:as.blackswan@unibocconi.it">Contact Us</a></li>'
             '<li><a class="pf-ulink" href="#how-to-apply">Apply</a></li>'
             '<li>Bocconi University, Milan</li>')
    social = (f'<a href="https://www.instagram.com/blackswanstudentsociety/" target="_blank" rel="noopener" aria-label="Instagram">{IG}</a>'
              f'<a href="https://www.linkedin.com/company/black-swan-student-society/" target="_blank" rel="noopener" aria-label="LinkedIn">{LI}</a>'
              f'<a href="mailto:as.blackswan@unibocconi.it" aria-label="Email">{EM}</a>')
    return ('<footer id="contact" class="pf"><div class="pf-container"><div class="pf-upper">'
            f'<div class="pf-brand"><a class="pf-logo" href="#top" aria-label="Black Swan Student Society, home"><img src="{logo}" alt="" width="140" height="194">'
            '<span class="pf-rule" aria-hidden="true"></span><span class="pf-word"><span class="pf-name">Black Swan</span><span class="pf-tag">Student Society</span></span></a>' + GRAPHIC + '</div>'
            f'<nav class="pf-menu" aria-label="Footer"><ul class="pf-cols">{cols}</ul></nav></div>'
            f'<div class="pf-utility"><nav aria-label="Legal"><ul class="pf-legal">{legal}</ul></nav><div class="pf-social">{social}</div></div>'
            '</div></footer>')
