import base64, html, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import hero4 as hero
import footer as pfoot
import perf
import team
import introp
import divpage
import trk
import apply as applyp
import events as evp
import pubs
import philo
import values
D = pathlib.Path(__file__).parent
LOGO = "data:image/png;base64," + base64.b64encode((D / "logo.png").read_bytes()).decode()
esc = html.escape
LOGIN = "https://www.blackswanstudents.com/login"
CUR = ' aria-current="page"'
ICON = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><circle cx="8" cy="5.5" r="2.75"/><path d="M2.75 14c.6-2.7 2.7-4.25 5.25-4.25S12.65 11.3 13.25 14" stroke-linecap="round"/></svg>'

# ---------- Content (edit names / descriptions here) ----------
# Standard dropdowns: (key, label, intro, [(slug, title, description)])
STD = [
  ("who", "Who we are", None, [
    ("introduction", "Introduction", "What Black Swan is, why prediction markets, and how the society started at Bocconi."),
    ("our-team", "Our team", "The board and the people who lead each of our five divisions."),
    ("philosophy-and-process", "Philosophy and process", "How we think in probabilities, and how a research idea becomes a priced view."),
    ("our-values", "Our values", "The principles behind how we research, trade and work together."),
  ]),
  ("publications", "Publications", "Research and commentary written by our members.", [
    ("investment-research", "Investment Research", "Investment pitches and the mispricings our research divisions find, with the case behind each trade."),
    ("market-perspectives", "Market Perspectives", "Articles on prediction markets, from how they work to what closed markets tell us once the result is in."),
  ]),
  ("opportunities", "Student opportunities", "Ways to get involved with Black Swan at Bocconi.", [
    ("events", "Events", "Talks, workshops and socials with people who trade, research and build for a living."),
    ("how-to-apply", "Apply", "How to join, what we look for, and when the next round opens."),
  ]),
]

# Divisions & Performance (special panel). Copy taken from the homepage.
DIV_LABEL = "Divisions & Performance"
DIVISIONS = [
  dict(slug="business-and-finance", group="research", title="Business & Finance", short="Earnings · M&A",
       desc="Corporate and financial events, from company earnings and industry rankings to the course of an acquisition and whether the deal closes at all.",
       tags="Earnings · Industry rankings · M&A",
       questions=[("Will the announced deal close by year end?", "Yes / No"), ("How far will earnings beat consensus?", "Range")]),
  dict(slug="economics-and-politics", group="research", title="Economics & Politics", short="Central banks · Elections",
       desc="Markets tied to macroeconomic and political outcomes: central bank decisions, inflation data, elections, trade policy and geopolitics.",
       tags="Central banks · Macro data · Elections & policy",
       questions=[("Will the ECB cut rates at its next meeting?", "Yes / No"), ("Which party wins the most seats?", "Multi-outcome")]),
  dict(slug="cross-domain", group="research", title="Cross-Domain", short="Crypto · Weather · Mentions",
       desc="Work outside traditional finance, on crypto, weather, public appearances and mention markets, comparing probabilities across sources.",
       tags="Crypto · Weather · Appearances & mentions",
       questions=[("Where will Bitcoin close the month?", "Range"), ("Will a given word be said in tonight's speech?", "Yes / No")]),
  dict(slug="market-studies", group="markets", title="Market Studies", short="Closed markets",
       desc="Market reports and statistical research on what prediction markets reveal once they have closed.",
       tags="Closed markets · Statistical analysis · Price drivers", questions=None),
  dict(slug="algorithmic-development", group="markets", title="Algorithmic Development", short="Models · Backtesting",
       desc="Looking for alpha through statistical models and systematic trading, turning research ideas into testable strategies.",
       tags="Statistical models · Backtesting · Systematic trading", questions=None),
]
PERF = ("performance", "Performance", "How our calls have scored across every division: hit rates, calibration and Brier scores.")
GROUPS = [("research", "Investment research", "3 divisions"), ("markets", "Markets & models", "2 divisions")]
ASOF = "Polymarket · 11 Nov, 18:00"

# Order of the top bar
ORDER = ["who", "divisions", "publications", "opportunities"]
LABELS = {k: l for k, l, *_ in STD} | {"divisions": DIV_LABEL}

# ---------- Header ----------
def trigger(key):
    return f'<li><button type="button" class="nav-link nav-trigger" aria-expanded="false" aria-controls="panel-{key}" data-menu="{key}">{esc(LABELS[key])}<span class="plus" aria-hidden="true"></span></button></li>'

def std_panel(key, label, intro, items):
    cells = "".join(
        f'<li><a class="mega-item" href="#{s}"><span class="mega-title">{esc(t)}<span class="arrow" aria-hidden="true">→</span></span><span class="mega-desc">{esc(d)}</span></a></li>'
        for s, t, d in items)
    return (f'<div class="mega" id="panel-{key}" data-panel="{key}" data-open="false"><div class="mx-auto w-full max-w-shell px-gutter mega-inner">' +
            (f'<div class="std"><div class="std-intro"><h2>{esc(label)}</h2><p class="intro-p">{esc(intro)}</p><p class="eyebrow">Explore <span aria-hidden="true">→</span></p></div>' if intro else '<div class="std no-intro">') +
            f'<ul class="std-items" style="--cols:{len(items)}" aria-label="{esc(label)}">{cells}</ul></div></div></div>')

def dv_panel():
    groups = []
    for g, name, count in GROUPS:
        rows = "".join(
            f'<li><a class="dv-row" href="#{d["slug"]}" data-div="{d["slug"]}"><span class="n">{esc(d["title"])}</span><span class="t">{esc(d["short"])}</span><span class="arrow" aria-hidden="true">→</span></a></li>'
            for d in DIVISIONS if d["group"] == g)
        groups.append(f'<div class="dv-group"><h3>{esc(name)}<small>{count}</small></h3><ul class="dv-list">{rows}</ul></div>')
    s, t, d = PERF
    groups.append(f'<div class="dv-group"><h3>{t}<small>All divisions</small></h3><ul class="dv-list"><li><a class="dv-row" href="#{s}" data-div="overview"><span class="n">Track record</span><span class="t">Hit rate · Calibration</span><span class="arrow" aria-hidden="true">→</span></a></li></ul></div>')
    return (f'<div class="mega" id="panel-divisions" data-panel="divisions" data-open="false"><div class="mx-auto w-full max-w-shell px-gutter mega-inner">'
            f'<div class="dv"><div class="dv-card" aria-live="polite"><div class="dv-view" id="dv-view"></div></div>'
            f'<nav class="dv-board" aria-label="{esc(DIV_LABEL)}">{"".join(groups)}</nav></div></div></div>')

panels, mobile = [], []
for key in ORDER:
    if key == "divisions":
        panels.append(dv_panel())
        items = [(d["slug"], d["title"], d["tags"]) for d in DIVISIONS] + [PERF]
    else:
        k, label, intro, items = next(x for x in STD if x[0] == key)
        panels.append(std_panel(k, label, intro, items))
    mitems = "".join(f'<a class="m-item" href="#{s}"><b>{esc(t)}</b><span>{esc(d)}</span></a>' for s, t, d in items)
    mobile.append(f'<div class="m-group"><button type="button" class="m-trigger" aria-expanded="false" aria-controls="m-{key}">{esc(LABELS[key])}<span class="plus" aria-hidden="true"></span></button><div class="m-list" id="m-{key}" hidden>{mitems}</div></div>')

header = f'''<a href="#main" class="skip-link band-dark">Skip to content</a>
<header id="site-header" data-scrolled="false" data-open="false" class="band-nav nav-bar">
<nav aria-label="Primary" class="mx-auto w-full max-w-shell px-gutter"><div class="nav-row">
<a class="brand" href="#top" aria-label="Black Swan Student Society, home"><img alt="" src="{LOGO}" width="140" height="194"><span class="brand-rule" aria-hidden="true"></span><span class="brand-text"><span class="brand-name">Black Swan</span><span class="brand-sub">Student Society</span></span></a>
<ul class="primary">{"".join(trigger(k) for k in ORDER)}</ul>
<div class="nav-end"><a class="login nav-login" href="{LOGIN}" target="_blank" rel="noopener" aria-label="Members login">{ICON}Login</a>
<button type="button" class="nav-link menu-toggle" aria-expanded="false" aria-controls="mobile-menu">Menu<span class="plus" aria-hidden="true"></span></button></div>
</div></nav>
{"".join(panels)}
<div class="mobile" id="mobile-menu" hidden><div class="mx-auto w-full max-w-shell px-gutter mobile-inner">{"".join(mobile)}<a class="login" href="{LOGIN}" target="_blank" rel="noopener" aria-label="Members login">{ICON}Login</a></div></div>
</header>'''

# ---------- Placeholder sub-pages ----------
SECTIONS = [(LABELS[k], items) for k, _, _, items in STD]
SECTIONS.insert(1, (DIV_LABEL, [(d["slug"], d["title"], d["desc"]) for d in DIVISIONS] + [PERF]))
pages = []
for label, items in SECTIONS:
    for slug, t, d in items:
        sibs = "".join(
            f'<a class="sib" href="#{s}"{CUR if s == slug else ""}><span class="font-display text-d4 text-heading">{esc(st)}</span><span class="mt-3 text-sm text-muted" style="display:block">{esc(sd)}</span></a>'
            for s, st, sd in items)
        pages.append(f'''<main class="flex-1" data-view="{slug}" hidden tabindex="-1">
<section class="band-dark grain relative bg-bg text-copy"><div class="relative z-[2]"><div class="mx-auto w-full max-w-shell px-gutter pt-24 pb-20">
<div class="flex items-baseline justify-between gap-4 border-t border-rule-strong pt-4"><nav class="crumbs text-xs" aria-label="Breadcrumb"><a href="#top">Home</a><span class="text-muted">/</span><span class="text-muted">{esc(label)}</span></nav><span class="soon">Content coming soon</span></div>
<h1 class="mt-16 font-display text-d2 text-heading">{esc(t)}</h1>
<p class="mt-8 max-w-measure text-lead text-copy">{esc(d)}</p>
</div></div></section>
<section class="band-paper grain relative bg-bg text-copy py-section"><div class="relative z-[2]"><div class="mx-auto w-full max-w-shell px-gutter">
<div class="flex items-baseline justify-between gap-4 border-t border-rule-strong pt-4"><span class="text-xs text-muted">In {esc(label)}</span></div>
<div class="mt-14 sib-grid">{sibs}</div>
</div></div></section>
</main>''')
ROUTES = [s for _, items in SECTIONS for s, _, _ in items]
ROUTES += team.ROUTES
pages = [pg for pg in pages if 'data-view="our-team"' not in pg and 'data-view="introduction"' not in pg and not any(f'data-view="{k}"' in pg for k in divpage.DIVS) and 'data-view="philosophy-and-process"' not in pg and 'data-view="our-values"' not in pg and 'data-view="performance"' not in pg and 'data-view="how-to-apply"' not in pg and 'data-view="events"' not in pg and 'data-view="investment-research"' not in pg and 'data-view="market-perspectives"' not in pg] + [trk.page(), applyp.page(), evp.page(), pubs.page_ir(), pubs.page_mp(), *(divpage.page(k) for k in divpage.DIVS), introp.page(), philo.page(), values.page(), team.team_page(), team.profile_pages()]

js = r'''<script>
(() => {
  const header = document.getElementById('site-header');
  const triggers = [...header.querySelectorAll('.nav-trigger')];
  const panels = [...header.querySelectorAll('.mega')];
  const toggle = header.querySelector('.menu-toggle');
  const mobile = document.getElementById('mobile-menu');
  const ROUTES = __ROUTES__, DIVS = __DIVS__, PERF = __PERF__, ASOF = __ASOF__;
  let open = null;
  const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

  /* Brand lockup: track "Student Society" out to the exact width of "Black Swan". */
  function fitLockup() {
    const name = header.querySelector('.brand-name'), sub = header.querySelector('.brand-sub');
    sub.style.letterSpacing = '0px'; sub.style.marginRight = '0px';
    const gap = name.getBoundingClientRect().width - sub.getBoundingClientRect().width;
    const n = sub.textContent.length;
    const ls = Math.max(0, gap / (n - 1));
    sub.style.letterSpacing = ls + 'px'; sub.style.marginRight = -ls + 'px';
  }
  fitLockup(); document.fonts && document.fonts.ready.then(fitLockup); addEventListener('resize', fitLockup);

  /* Divisions & Performance preview card */
  const view = document.getElementById('dv-view');
  const rows = [...header.querySelectorAll('.dv-row')];
  function overviewHTML() {
    return `<div class="dv-top"><span class="dv-eyebrow">Overview</span><span class="dv-src">5 divisions</span></div>
      <p class="dv-title">Research measured against the market</p>
      <p class="dv-desc">Our five divisions span corporate events, macroeconomics and politics, alternative markets, market behaviour and quantitative strategy. Every forecast is stated as an explicit probability, set against the prevailing price and evaluated on its outcome.</p>
      <div class="dv-foot"><div class="dv-stats"><div><b>5</b><span>Divisions</span></div><div><b>60+</b><span>Members</span></div><div><b>3</b><span>Markets tracked today</span></div></div>
      <a class="dv-cta" href="#${PERF[0]}">View performance <span aria-hidden="true">→</span></a></div>`;
  }
  function divHTML(d, i) {
    const q = d.questions;
    const foot = q
      ? `<div class="dv-market"><p class="lbl">Questions we price</p><ul class="dv-qs">${q.map(x => `<li><span>${esc(x[0])}</span><em>${esc(x[1])}</em></li>`).join('')}</ul></div>`
      : `<div class="dv-market"><p class="lbl">Focus</p><p class="dv-q" style="margin-top:.35rem">${esc(d.tags)}</p></div>`;
    return `<div class="dv-top"><span class="dv-eyebrow">${d.group === 'research' ? 'Investment research' : 'Markets & models'}</span><span class="dv-src">Division ${String(i + 1).padStart(2, '0')}</span></div>
      <p class="dv-title">${esc(d.title)}</p><p class="dv-desc">${esc(d.desc)}</p>${q ? `<p class="dv-tags">${esc(d.tags)}</p>` : ''}
      <div class="dv-foot">${foot}</div>`;
  }
  let shown = null, swapT;
  function show(key, instant) {
    if (key === shown) return; shown = key;
    rows.forEach(r => r.classList.toggle('is-active', r.dataset.div === key && key !== 'overview'));
    const i = DIVS.findIndex(d => d.slug === key);
    const html = i < 0 ? overviewHTML() : divHTML(DIVS[i], i);
    clearTimeout(swapT);
    if (instant) { view.innerHTML = html; view.classList.remove('swap'); return; }
    view.classList.add('swap');
    swapT = setTimeout(() => { view.innerHTML = html; view.classList.remove('swap'); }, 140);
  }
  rows.forEach(r => { r.addEventListener('mouseenter', () => show(r.dataset.div)); r.addEventListener('focus', () => show(r.dataset.div)); });
  show('overview', true);

  const sync = () => header.dataset.open = (open || !mobile.hidden) ? 'true' : 'false';
  function setMenu(key) {
    if (key === 'divisions' && open !== 'divisions') show('overview', true);
    open = key;
    triggers.forEach(t => t.setAttribute('aria-expanded', String(t.dataset.menu === key)));
    panels.forEach(p => p.dataset.open = String(p.dataset.panel === key));
    sync();
  }
  triggers.forEach(t => t.addEventListener('click', e => { e.stopPropagation(); setMenu(open === t.dataset.menu ? null : t.dataset.menu); }));
  document.addEventListener('click', e => { if (open && !e.target.closest('.mega')) setMenu(null); });
  document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    if (open) { const t = triggers.find(t => t.dataset.menu === open); setMenu(null); t && t.focus(); }
    if (!mobile.hidden) closeMobile(true);
  });

  function closeMobile(focus) { mobile.hidden = true; toggle.setAttribute('aria-expanded', 'false'); toggle.firstChild.textContent = 'Menu'; sync(); if (focus) toggle.focus(); }
  toggle.addEventListener('click', () => {
    if (!mobile.hidden) return closeMobile();
    mobile.hidden = false; toggle.setAttribute('aria-expanded', 'true'); toggle.firstChild.textContent = 'Close'; sync();
  });
  mobile.querySelectorAll('.m-trigger').forEach(b => b.addEventListener('click', () => {
    const list = document.getElementById(b.getAttribute('aria-controls'));
    const reveal = list.hidden; list.hidden = !reveal; b.setAttribute('aria-expanded', String(reveal));
  }));
  header.addEventListener('click', e => { if (e.target.closest('a[href^="#"]')) { setMenu(null); if (!mobile.hidden) closeMobile(); } });
  matchMedia('(min-width: 64rem)').addEventListener('change', e => { if (e.matches) closeMobile(); else setMenu(null); });

  let scr = null; const onScroll = () => { const s = scrollY > 8; if (s !== scr) { scr = s; header.dataset.scrolled = String(s); } };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* Routing: #<page> shows a sub-page; anything else shows the homepage (and scrolls to that anchor). */
  const views = [...document.querySelectorAll('main[data-view]')];
  function route() {
    const h = decodeURIComponent(location.hash.slice(1));
    const page = ROUTES.includes(h) ? h : 'home';
    const cur = views.find(v => !v.hidden);
    views.forEach(v => v.hidden = v.dataset.view !== page);
    setMenu(null); closeMobile();
    if (page !== 'home') scrollTo({ top: 0, behavior: 'instant' });
    else if (cur && cur.dataset.view !== 'home') {
      const el = h && document.getElementById(h);
      el ? el.scrollIntoView({ behavior: 'instant' }) : scrollTo({ top: 0, behavior: 'instant' });
    }
  }
  addEventListener('hashchange', route); route();
})();
</script>'''
for k, v in {"__ROUTES__": ROUTES, "__DIVS__": DIVISIONS, "__PERF__": list(PERF), "__ASOF__": ASOF}.items():
    js = js.replace(k, json.dumps(v, ensure_ascii=False))

home = (D / "home.html").read_text().replace("{{LOGO}}", LOGO).replace("<!--PAGES-->", "\n".join(pages))
LOGO_HERO = "data:image/webp;base64," + base64.b64encode((D / "logo-hero.webp").read_bytes()).decode()
_a = home.index('<section id="top"'); _b = home.index('<section id="origin"')
home = home[:_a] + hero.hero_html(LOGO_HERO, esc) + home[_b:]
_a = home.index('<section id="origin"'); _b = home.index('<section id="divisions"')
home = home[:_a] + hero.INTRO + home[_b:]
_a = home.index('<section id="divisions"'); _b = home.index('<section id="membership"')
home = home[:_a] + hero.CARDS + home[_b:]
_a = home.index('<section id="membership"'); _b = home.index('</main>', _a)
home = home[:_a] + hero.DIVX + perf.html() + home[_b:]
_a = home.index('<footer id="contact"'); _b = home.index('</footer>', _a) + len('</footer>')
home = home[:_a] + pfoot.footer_html(LOGO) + home[_b:]
out = f'''<title>Black Swan Student Society</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500&family=IBM+Plex+Mono:wght@400&family=Instrument+Sans:wght@400..700&display=swap">
<style>
{(D / "base.css").read_text()}
{(D / "header2.css").read_text()}
{(D / "hero4.css").read_text()}
{(D / "intro.css").read_text()}
{(D / "cards.css").read_text()}
{(D / "divx.css").read_text()}
{(D / "footer.css").read_text()}
{(D / "perf.css").read_text()}
{(D / "team.css").read_text()}
{(D / "introp.css").read_text()}
{(D / "divpage.css").read_text()}
{(D / "trk.css").read_text()}
{(D / "apply.css").read_text()}
{(D / "events.css").read_text()}
{(D / "pubs.css").read_text()}
{team.CSS_PHOTOS}
</style>
{header}
{home}
{js}
{hero.HERO_JS}
{hero.DIVX_JS}
{perf.JS}
'''
(D / "black-swan-site.html").write_text(out)
(D / "preview-local.html").write_text('<!doctype html><html lang="en" class="antialiased"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">' + out + '</html>')
print(len(out))
