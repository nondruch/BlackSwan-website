"""Our Team page + one profile page per board member."""
import base64, pathlib
D = pathlib.Path(__file__).parent

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# (slug, name, role, group, linkedin, division-focus or None)
PEOPLE = [
  ("marco-similea", "Marco Similea", "President", "Leadership", "https://www.linkedin.com/in/marco-similea-b7a9b6287", None),
  ("leo-scully", "Leo Scully", "Vice President", "Leadership", "https://www.linkedin.com/in/leoscully", None),
  ("horia-timofti", "Horia Timofti", "Senior Advisor", "Leadership", "https://www.linkedin.com/in/horia-timofti", None),
  ("mohammed-el-zein", "Mohammed El-Zein", "Senior Advisor", "Leadership", "https://www.linkedin.com/in/mohammed-el-zein-43b1a818a", None),
  ("carlo-giolla", "Carlo Giolla", "Head of Economics & Politics", "Divisions", "https://www.linkedin.com/in/carlogiolla", "Economics & Politics"),
  ("niklas-ondruch", "Niklas Ondruch", "Co-Head of Business & Finance", "Divisions", "https://www.linkedin.com/in/niklas-ondruch", "Business & Finance"),
  ("loyd-hegarty", "Loyd Hegarty", "Co-Head of Business & Finance", "Divisions", "https://www.linkedin.com/in/loyd-hegarty", "Business & Finance"),
  ("harry-downey", "Harry Downey", "Head of Cross-Domain", "Divisions", "https://www.linkedin.com/in/harry-downey", "Cross-Domain"),
  ("can-deniz", "Can Deniz", "Co-Head of Market Studies", "Divisions", "https://www.linkedin.com/in/can-deniz-t-kahraman", "Market Studies"),
  ("hrishikesh-subhash", "Hrishikesh Subhash", "Co-Head of Market Studies", "Divisions", "https://www.linkedin.com/in/hrishipillai", "Market Studies"),
  ("thomas-tumini", "Thomas Tumini", "Head of Algorithmic Development", "Divisions", "https://www.linkedin.com/in/thomastumini", "Algorithmic Development"),
  ("maria-mateescu", "Maria Mateescu", "Co-Head of Media & News", "Media, Operations & Recruitment", "https://www.linkedin.com/in/maria-mateescu-48b3833aa", None),
  ("sofia-damean", "Sofia Damean", "Co-Head of Media & News", "Media, Operations & Recruitment", None, None),
  ("matteo-mascaretti", "Matteo Mascaretti", "Head of Operations & Outreach", "Media, Operations & Recruitment", "https://www.linkedin.com/in/matteo-mascaretti-a272b43a2", None),
  ("james-moser", "James Moser", "Head of Software Development", "Media, Operations & Recruitment", "https://www.linkedin.com/in/jamesnmoser", None),
  ("adrian-tsonev", "Adrian Tsonev", "Head of Recruitment", "Media, Operations & Recruitment", "https://www.linkedin.com/in/adrian-tsonev-9b3221276", None),
]

GROUP_INTRO = {
  "Leadership": "Sets the society's direction and holds every division to the same standard.",
  "Divisions": "Each division head runs the research agenda and the calls in their own domain.",
  "Media, Operations & Recruitment": "Keeps the society running, visible and growing.",
}

DIV_LINE = {
  "Economics & Politics": "markets tied to central bank decisions, macro data, elections and policy",
  "Business & Finance": "corporate and financial events, from earnings and industry rankings to M&A",
  "Cross-Domain": "markets outside traditional finance: crypto, weather, appearances and mentions",
  "Market Studies": "statistical research on what prediction markets reveal once they have closed",
  "Algorithmic Development": "statistical models, backtesting and systematic trading strategies",
}

ROLE_LINE = {
  "President": "leads Black Swan, setting its direction and representing the society within Bocconi and beyond",
  "Vice President": "works alongside the President on the society's direction and oversees the day-to-day running of the divisions",
  "Senior Advisor": "advises the board on strategy and research standards, drawing on experience across the society",
  "Co-Head of Media & News": "runs the society's media and news output, from announcements to coverage of our research",
  "Head of Operations & Outreach": "runs the society's operations and builds relationships with partners, speakers and other societies",
  "Head of Software Development": "builds and maintains the society's software, from this website to the tools behind our research",
  "Head of Recruitment": "leads recruitment, from application rounds to bringing new members into the divisions",
}

CUSTOM_BIO = {
  "loyd-hegarty": 'Loyd co-leads Black Swan’s Business and Finance Division and is a second-year International Economics and Finance student at Bocconi. With a French-British background and an education in Romania, he developed an interest in financial markets that led him to internships in Global Markets at Société Générale in Paris. He has also explored company valuation through equity research at Minerva Investment Management Society and merger analysis at Bocconi’s Distressed Investing and Restructuring Club. At Black Swan, he aims to bring these perspectives together, helping analysts connect financial research with market expectations to develop informed views on prediction markets. Outside university, he enjoys football and going to the gym.',
  "adrian-tsonev": 'Adrian (Adi) Tsonev leads Black Swan’s Market Updates and Career Guidance sector and is a second-year International Economics and Finance student at Bocconi. Raised in London by Bulgarian parents, he first gained an interest in finance when he pursued an internship at Ares Management during high school. Since then, he has gained experience in high-yield credit trading during the Barings Spring Week, Sales and Trading during the Goldman Sachs Insight Program, and long/short credit trading at hedge fund Sternlight Capital Partners. His strong interest in financial markets and finding investment opportunities within them inspired him to help establish Black Swan. Outside university, he enjoys playing rugby, football, tennis and piano.',
  "horia-timofti": 'Horia serves as Senior Advisor to Black Swan’s leadership, supporting the President and division heads on strategic and operational matters. He is a third year International Economics and Finance student at Bocconi.',
  "mohammed-el-zein": 'Mohammed (Moe) serves as Senior Advisor to Black Swan’s leadership, supporting the President and division heads on strategic and operational matters. He is a second-year MSc student in Accounting & Financial Management at Bocconi, where he is completing a Double Degree with Grenoble Ecole de Management. He previously studied Quantitative Economics at the University of Konstanz, where he served as a Research Assistant at the Chair of Applied Microeconomics. Having grown up between Germany and Lebanon and studied in France and Italy, he has learned to feel at home wherever the conversation is most interesting. He has gained experience through internships in investment banking at UniCredit in Corporate Structured & Acquisition Finance, in M&A advisory for German Mittelstand companies at Menold Bezler, in the Corporate Bank at Commerzbank, and in the Financial Services Industry practice at Deloitte. At Grenoble, he serves as Programme Representative for all MSc Finance programmes. His interest in how global events move markets, and in how people from different backgrounds reach better decisions together, drew him to Black Swan. Outside university, he enjoys exploring new coffee shops and restaurants, playing padel, and spending time with friends and family.',
  "niklas-ondruch": "Niklas (Niki) co-leads Black Swan’s Business and Finance Division and is a second-year International Economics and Finance student at Bocconi. Raised in London by French and German parents, he first explored investing at 14 through a virtual trading portfolio. He has since gained experience through internships in credit investing at hedge fund Sternlight Capital Partners, equity research at Astellon Capital Partners – a former hedge fund turned family office – and Sales and Trading at Marex Group. His interest in behavioural economics and how markets bring together different perspectives inspired him to help establish Black Swan. Outside university, he enjoys football, basketball, chess and training for Ironman triathlons.",
}

LI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28ZM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13ZM7.12 20.45H3.56V9h3.56v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0Z"/></svg>'


def photo(slug):
    f = D / "team" / f"{slug}.webp"
    return "data:image/webp;base64," + base64.b64encode(f.read_bytes()).decode() if f.exists() else None

PHOTOS = {p[0]: photo(p[0]) for p in PEOPLE}
CSS_PHOTOS = "".join(f'.ph-{s}{{background-image:url({u})}}' for s, u in PHOTOS.items() if u)


def first(name):
    return name.split()[0]


def bio(p):
    slug, name, role, group, li, div = p
    f = first(name)
    if div:
        lead = "leads" if role.startswith("Head") else "co-leads"
        return (f"{f} {lead} the {div} division, which covers {DIV_LINE[div]}. "
                f"The division sets its own research agenda, prices the questions in its domain and presents what it finds to the rest of the society.")
    return f"{f} {ROLE_LINE[role]}."


def portrait(p, cls):
    slug, name = p[0], p[1]
    if PHOTOS.get(slug):
        return f'<span class="{cls} ph ph-{slug}" role="img" aria-label="{esc(name)}"></span>'
    ini = "".join(w[0] for w in name.split()[:2])
    return f'<span class="{cls} ph ph-none" role="img" aria-label="{esc(name)}"><span class="ph-ini">{ini}</span></span>'


def card(p):
    slug, name, role, group, li, div = p
    lk = (f'<a class="tm-li" href="{li}" target="_blank" rel="noopener" aria-label="{esc(name)} on LinkedIn">{LI}</a>' if li else "")
    return (f'<li class="tm-card"><a class="tm-link" href="#team-{slug}" aria-label="{esc(name)}, {esc(role)}: view profile">'
            f'{portrait(p, "tm-ph")}<span class="tm-view">View profile <span aria-hidden="true">→</span></span></a>'
            f'<div class="tm-meta"><div><p class="tm-name">{esc(name)}</p><p class="tm-role">{esc(role)}</p></div>{lk}</div></li>')


def marquee():
    ppl = [p for p in PEOPLE if PHOTOS.get(p[0])]
    tiles = "".join(f'<span class="tq-t ph ph-{p[0]}"></span>' for p in ppl)
    return f'<div class="tq" aria-hidden="true" style="--n:{len(ppl)}"><div class="tq-track">{tiles}{tiles}</div></div><script>(()=>{{const t=document.currentScript.previousElementSibling.querySelector(".tq-track");if("IntersectionObserver" in window)new IntersectionObserver(([e])=>t.classList.toggle("is-off",!e.isIntersecting)).observe(t.parentElement)}})();</script>'


def team_page():
    groups = []
    for g in GROUP_INTRO:
        ppl = [p for p in PEOPLE if p[3] == g]
        groups.append(f'<section class="tm-group" aria-labelledby="tg-{len(groups)}"><div class="tm-ghead"><h2 class="tm-gh" id="tg-{len(groups)}">{esc(g)}</h2>'
                      f'<p class="tm-gp">{esc(GROUP_INTRO[g])}</p><span class="tm-gc">{len(ppl):02d}</span></div>'
                      f'<ul class="tm-grid">{"".join(card(p) for p in ppl)}</ul></section>')
    return f'''<main class="flex-1 tm" data-view="our-team" hidden tabindex="-1">
<section class="tm-hero tm-hero-ph">{marquee()}<div class="tm-wrap mx-auto w-full px-gutter tm-hin">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><span>Who we are</span><span aria-hidden="true">/</span><span aria-current="page">Our team</span></nav>
<div class="tm-hc">
<p class="tm-hc-k">Who we are</p>
<h1 class="tm-hc-h">The people behind Black Swan</h1>
<p class="tm-hc-p">The board leads Black Swan’s five research divisions, runs the society day to day and sets the standard for every call we publish. Select anyone to read more about them.</p>
<p class="tm-hc-f"><span><b>{len(PEOPLE)}</b> board members</span><span class="tm-sep" aria-hidden="true">|</span><span><b>{sum(len(a[3]) for a in ANALYSTS)}</b> analysts</span><span class="tm-sep" aria-hidden="true">|</span><span><b>5</b> divisions</span></p>
</div>
</div></section>
<div class="tm-wrap mx-auto w-full px-gutter tm-body">{"".join(groups)}{analysts_section()}</div>
</main>'''


def profile_pages():
    out = []
    n = len(PEOPLE)
    for i, p in enumerate(PEOPLE):
        slug, name, role, group, li, div = p
        prev, nxt = PEOPLE[(i - 1) % n], PEOPLE[(i + 1) % n]
        lk = (f'<a class="pp-btn pp-btn-li" href="{li}" target="_blank" rel="noopener">{LI}<span>View on LinkedIn</span></a>' if li
              else '<span class="pp-btn pp-btn-off">LinkedIn coming soon</span>')
        facts = [("Role", role), ("Team", group)]
        if div:
            facts.append(("Division", div))
        facts_html = "".join(f'<div><dt>{k}</dt><dd>{esc(v)}</dd></div>' for k, v in facts)
        divlink = ""
        if div:
            ds = div.lower().replace(" & ", "-and-").replace(" ", "-")
            divlink = f'<a class="pp-btn" href="#{ds}">The {esc(div)} division <span aria-hidden="true">→</span></a>'
        same = [q for q in PEOPLE if q[3] == group and q[0] != slug][:3]
        same_html = "".join(
            f'<a class="pp-mini" href="#team-{q[0]}">{portrait(q, "pp-mini-ph")}<span><b>{esc(q[1])}</b><span>{esc(q[2])}</span></span></a>' for q in same)
        out.append(f'''<main class="flex-1 pp" data-view="team-{slug}" hidden tabindex="-1">
<div class="tm-wrap mx-auto w-full px-gutter">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><a href="#our-team">Our team</a><span aria-hidden="true">/</span><span aria-current="page">{esc(name)}</span></nav>
<article class="pp-grid">
<div class="pp-photo">{portrait(p, "pp-ph")}<span class="pp-idx">{i+1:02d} / {n:02d}</span></div>
<div class="pp-body">
<p class="tm-eyebrow">{esc(group)}</p>
<h1 class="pp-name">{esc(name)}</h1>
<p class="pp-role">{esc(role)}</p>
{(f'<p class="pp-bio pp-bio-long">{esc(CUSTOM_BIO[slug])}</p>' if slug in CUSTOM_BIO else f'<p class="pp-bio">{esc(bio(p))}</p><p class="pp-soon">A fuller profile, with {esc(first(name))}’s background and interests, is coming soon.</p>')}
<dl class="pp-facts">{facts_html}</dl>
<div class="pp-actions">{lk}{divlink}</div>
{f'<div class="pp-same"><p class="pp-same-h">Also in {esc(group)}</p><div class="pp-same-row">{same_html}</div></div>' if same else ''}
</div>
</article>
<nav class="pp-nav" aria-label="More profiles">
<a href="#team-{prev[0]}" class="pp-nav-a"><span class="pp-nav-k">← Previous</span><span class="pp-nav-n">{esc(prev[1])}</span></a>
<a href="#our-team" class="pp-nav-all">All team members</a>
<a href="#team-{nxt[0]}" class="pp-nav-a pp-nav-r"><span class="pp-nav-k">Next →</span><span class="pp-nav-n">{esc(nxt[1])}</span></a>
</nav>
</div>
</main>''')
    return "\n".join(out)


ANALYSTS = [
  ("Business & Finance", "business-and-finance", ["niklas-ondruch", "loyd-hegarty"], [
    "Pietro Carlucci", "Massimiliano Catallo-Bauman", "Oliver Di-Marcello", "Mario Garrido Ruiz", "Aarav Gupta", "Abay Kurmanov",
    "Giovanni Paganini", "Toma Perukov", "Riccardo Pietranera", "Ismail Boukhris", "Zanobi Räderer", "Krishna Kapil Rastogi", "Woo Yan Yan (Angeline)",
    "Mark Höving", "Ana Milosevic", "Ludovico De Carolis", "Otto Braun"]),
  ("Economics & Politics", "economics-and-politics", ["carlo-giolla"], [
    "Felipe Mazur de Freitas", "Thomas Portelli", "Andrea Annibali", "Mustafa Nabi Shah", "Pietro Ludwig Speidel Molajoni", "Nikita Larionov",
    "Robin Choudhury-Collins", "Paulina Rienau", "Quentin Royer", "Noga Lidovski", "Uma Nayyar", "Maxime Dufour", "Jade Henni",
    "Iason Tsolakis", "Leif Keller", "Zachary Boynton Fine"]),
  ("Cross-Domain", "cross-domain", ["harry-downey"], [
    "Leonard Stengel", "Tamás Megyeri", "Leonardo Emanuel Jurgen Krumnack", "Francesco Mangini", "Stefano Zilio", "Deniz Denisa Sengezener"]),
  ("Market Studies", "market-studies", ["can-deniz", "hrishikesh-subhash"], [
    "Filippo Antonio Cadorin", "Diego Caupers", "Jiana Shah", "Alexander Gargiulo"]),
  ("Algorithmic Development", "algorithmic-development", ["thomas-tumini"], [
    "Eren Ali Aksoy", "Stefan Eriksson", "Darius Farcas", "Filip Lukasiewicz", "Matias Riveros", "Atila Soleimanian"]),
]

def _surname(n):
    base = n.split(" (")[0].split()
    return (base[0] if n.startswith("Woo ") else base[-1]).lower()

def analysts_section():
    names = {p[0]: p[1] for p in PEOPLE}
    total = sum(len(x[3]) for x in ANALYSTS)
    tabs, panels = [], []
    for i, (div, ds, heads, ppl) in enumerate(ANALYSTS):
        ppl = sorted(ppl, key=lambda n: n.lower())
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button type="button" role="tab" class="an-tab" id="an-t{i}" aria-controls="an-p{i}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">'
                    f'<span class="an-ti">{i+1:02d}</span><span class="an-tn">{esc(div)}</span><span class="an-tc">{len(ppl)}</span></button>')
        led = " &amp; ".join(f'<a href="#team-{h}">{esc(names[h])}</a>' for h in heads)
        items = "".join(f'<li><span class="an-n">{k+1:02d}</span><span class="an-name">{esc(n)}</span></li>' for k, n in enumerate(ppl))
        panels.append(f'<div class="an-panel" role="tabpanel" id="an-p{i}" aria-labelledby="an-t{i}"{"" if i == 0 else " hidden"}>'
                      f'<div class="an-ph"><div><p class="an-pk">Division {i+1:02d} of 05</p><h3 class="an-pt">{esc(div)}</h3>'
                      f'<p class="an-led">Led by {led}</p></div><div class="an-stat"><b>{len(ppl)}</b><span>analysts</span></div></div>'
                      f'<ol class="an-names">{items}</ol>'
                      f'<a class="an-more" href="#{ds}">About the {esc(div)} division <span aria-hidden="true">→</span></a></div>')
    js = """<script>(()=>{const r=document.currentScript.closest('.an');if(!r)return;const t=[...r.querySelectorAll('.an-tab')],p=[...r.querySelectorAll('.an-panel')];
const sel=i=>{t.forEach((x,k)=>{x.setAttribute('aria-selected',String(k===i));x.tabIndex=k===i?0:-1});p.forEach((x,k)=>{x.hidden=k!==i;if(k===i){x.classList.remove('in');void x.offsetWidth;x.classList.add('in')}})};
t.forEach((x,i)=>{x.addEventListener('click',()=>sel(i));x.addEventListener('keydown',e=>{const d={ArrowDown:1,ArrowRight:1,ArrowUp:-1,ArrowLeft:-1}[e.key];if(d){e.preventDefault();const n=(i+d+t.length)%t.length;t[n].focus();sel(n)}})});})();</script>"""
    return (f'<section class="tm-group an" aria-labelledby="tg-an"><div class="tm-ghead"><h2 class="tm-gh" id="tg-an">Analysts</h2>'
            f'<p class="tm-gp">The members who research, price and pitch across our five divisions.</p><span class="tm-gc">{total:02d}</span></div>'
            f'<div class="an-box"><div class="an-tabs" role="tablist" aria-label="Division" aria-orientation="vertical">{"".join(tabs)}</div>'
            f'<div class="an-panels">{"".join(panels)}</div></div>{js}</section>')

ROUTES = ["team-" + p[0] for p in PEOPLE]
