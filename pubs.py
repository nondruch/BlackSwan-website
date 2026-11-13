"""Publications pages: Investment Research and Market Perspectives."""
import html
IG = "https://www.instagram.com/blackswanstudentsociety/"
IR_DESC = "Investment pitches and the mispricings our research divisions find, with the case behind each trade."
MP_DESC = "Articles on prediction markets, from how they work to what closed markets tell us once the result is in."

DIVS = [("business-and-finance", "Business & Finance"), ("economics-and-politics", "Economics & Politics"), ("cross-domain", "Cross-Domain")]

# (division slug, title, note)
REPORTS = [
  ("business-and-finance", "NVIDIA Price by Nov 30th", None),
  ("business-and-finance", "Anthropic Valuation by Dec 31", "Yes / No, based on the Nasdaq Private Company valuation"),
  ("business-and-finance", "Largest Company by December 2026: Apple or Nvidia", None),
]

e = html.escape


def _head(slug, title, desc):
    tabs = "".join(f'<a class="pb-tab" href="#{s}"{" aria-current=\"page\"" if s == slug else ""}>{t}</a>' for s, t in [("investment-research", "Investment Research"), ("market-perspectives", "Market Perspectives")])
    return f'''<header class="ap-hero pb-hero"><div class="tm-wrap mx-auto w-full px-gutter">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><span>Publications</span><span aria-hidden="true">/</span><span aria-current="page">{title}</span></nav>
<h1 class="ap-h1">{title}</h1>
<p class="ap-lead">{desc}</p>
<nav class="pb-tabs" aria-label="Publications">{tabs}</nav>
</div></header>'''


def _cover():
    return '<div class="pb-cv" aria-hidden="true"><span class="pb-cv-top"><i>Black Swan</i></span><span class="pb-cv-l w80"></span><span class="pb-cv-l w60"></span><span class="pb-cv-ch"></span><span class="pb-cv-l w70"></span></div>'


def page_ir():
    names = dict(DIVS)
    rows = "".join(
        f'<li class="pb-row" data-div="{d}">{_cover()}<div class="pb-main"><p class="pb-div">{e(names[d])}</p><h3>{e(t)}</h3>'
        + (f'<p class="pb-note">{e(n)}</p>' if n else '') +
        f'</div><div class="pb-side"><span class="pb-type">Investment pitch</span><span class="pb-stat">Forthcoming</span></div></li>'
        for d, t, n in REPORTS)
    chips = '<button type="button" class="pb-chip" aria-pressed="true" data-f="all">All divisions</button>' + "".join(
        f'<button type="button" class="pb-chip" aria-pressed="false" data-f="{s}">{e(n)}</button>' for s, n in DIVS)
    return f'''<main class="flex-1 ap pb" data-view="investment-research" hidden tabindex="-1">
{_head("investment-research", "Investment Research", IR_DESC)}
<div class="tm-wrap mx-auto w-full px-gutter pb-body">
<div class="pb-bar"><h2 class="pb-h2">Reports</h2></div>
<div class="pb-empty"><p><b>Our first reports are in preparation.</b> They will be published here and announced on our Instagram.</p><a class="ap-link" href="{IG}" target="_blank" rel="noopener">Follow for updates →</a></div>
<p class="pb-foot">Research produced by Black Swan is for educational purposes only and does not constitute investment advice.</p>
</div>
</main>'''


def page_mp():
    return f'''<main class="flex-1 ap pb" data-view="market-perspectives" hidden tabindex="-1">
{_head("market-perspectives", "Market Perspectives", MP_DESC)}
<div class="tm-wrap mx-auto w-full px-gutter pb-body">
<div class="pb-bar"><h2 class="pb-h2">Articles</h2></div>
<div class="pb-empty"><p><b>The first articles are in preparation.</b> They will be published here and announced on our Instagram.</p><a class="ap-link" href="{IG}" target="_blank" rel="noopener">Follow for updates →</a></div>
<p class="pb-foot">Looking for our research? <a class="ap-link" href="#investment-research">Browse Investment Research →</a></p>
</div>
</main>'''
