"""Division pages. Built for Business & Finance first; the same template takes the other four."""
import base64, pathlib, sys
D = pathlib.Path(__file__).parent
sys.path.insert(0, str(D))
import team

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

HDR = "data:image/webp;base64," + base64.b64encode((D / "values-hero.webp").read_bytes()).decode()

DIVS = {
  "business-and-finance": dict(
    n=1, name="Business & Finance", group="Investment research",
    lead="The Business & Finance Division applies fundamental analysis and probabilistic modelling to prediction markets surrounding corporate performance and transactions. Our analysts examine the commercial, financial and strategic forces behind each event, translating company research into explicit forecasts. We seek to identify where market expectations diverge from the evidence, whether through an overlooked operating driver, an optimistic timetable or a misinterpretation of transaction terms.",
    tags=["Earnings", "Industry rankings", "M&A"],
    lead2="Our approach combines bottom-up research with disciplined scrutiny of market expectations. Drawing on financial statements, company disclosures, industry data and historical precedents, teams develop scenarios, assess their likelihood and test the assumptions that determine their conclusions. Each investment thesis must articulate a precise disagreement with the prevailing price, withstand a credible counterargument and identify the developments that would warrant revision.",
    reports=[("NVIDIA Price by Nov 30th", None), ("Anthropic Valuation by Dec 31", "Yes / No, based on the Nasdaq Private Company valuation"), ("Largest Company by December 2026: Apple or Nvidia", None), (None, None), (None, None)],
    heads=["niklas-ondruch", "loyd-hegarty"],
    prev=("algorithmic-development", "Algorithmic Development"), next=("economics-and-politics", "Economics & Politics"),
  ),
}

BLANK = [(None, None)] * 5

DIVS.update({
  "economics-and-politics": dict(
    n=2, name="Economics & Politics", group="Investment research",
    lead="The Economics & Politics Division applies macroeconomic analysis and probabilistic modelling to prediction markets surrounding monetary policy, economic data and political outcomes. Our analysts study central bank decisions, inflation and labour-market releases, elections, legislation, trade policy and geopolitical developments, translating that research into explicit forecasts. We seek to identify where market expectations diverge from the evidence, whether through a misread policy reaction function, an overreaction to a single poll or a misunderstanding of how a contract resolves.",
    tags=["Central banks", "Macro data", "Elections & policy"],
    lead2="Our approach combines top-down analysis with close attention to the data that drives each outcome. Drawing on official statistics, central bank communication, polling, historical precedents and institutional rules, teams build scenarios, weigh them against forecasts and survey data, and track how markets absorb new information. Each thesis must state a precise disagreement with the prevailing price, withstand a credible counterargument and identify the releases or events that would warrant revision.",
    reports=BLANK, heads=["carlo-giolla"],
    prev=("business-and-finance", "Business & Finance"), next=("cross-domain", "Cross-Domain"),
  ),
  "cross-domain": dict(
    n=3, name="Cross-Domain", group="Investment research",
    lead="The Cross-Domain Division covers prediction markets outside traditional finance, from cryptocurrency prices and weather outcomes to public appearances and mention markets. Our analysts bring quantitative methods and domain-specific research to questions where information is fragmented and participants rely on very different sources. We seek to identify where market expectations diverge from the evidence, whether through a poorly calibrated volatility assumption, an overlooked forecast model or a misreading of what counts towards resolution.",
    tags=["Crypto", "Weather", "Appearances & mentions"],
    lead2="Our approach adapts to the structure of each market. For price-based contracts, teams model the distribution of outcomes using volatility, historical behaviour and current market conditions; for weather and event markets, they compare forecasts and base rates across independent sources; for mention and appearance markets, they study schedules, precedents and the precise wording of the resolution criteria. Each thesis must state where and why our probability differs from the market, withstand a credible counterargument and identify what would change our view.",
    reports=BLANK, heads=["harry-downey"],
    prev=("economics-and-politics", "Economics & Politics"), next=("market-studies", "Market Studies"),
  ),
  "market-studies": dict(
    n=4, name="Market Studies", group="Markets & models",
    lead="The Market Studies Division examines prediction markets themselves: how prices form, how quickly they absorb new information and how accurate they prove once questions resolve. Rather than taking positions on individual events, our analysts study the behaviour of markets across many contracts, producing reports and statistical research on what closed markets reveal about calibration, liquidity and the drivers of price movements.",
    tags=["Closed markets", "Statistical analysis", "Price drivers"],
    lead2="Our approach is empirical. Teams assemble data on resolved markets, define testable hypotheses and apply statistical methods to measure accuracy, bias and reaction to news, with careful attention to sample selection, contract design and trading conditions. Findings are reviewed critically before publication, and the patterns they uncover inform the research of the other divisions and the models built by Algorithmic Development.",
    reports=BLANK, heads=["can-deniz", "hrishikesh-subhash"],
    prev=("cross-domain", "Cross-Domain"), next=("algorithmic-development", "Algorithmic Development"),
  ),
  "algorithmic-development": dict(
    n=5, name="Algorithmic Development", group="Markets & models",
    lead="The Algorithmic Development Division builds and evaluates statistical models and systematic strategies for prediction markets. Our analysts turn research ideas into testable rules, using quantitative methods to search for persistent sources of edge and to measure whether they survive realistic trading conditions.",
    tags=["Statistical models", "Backtesting", "Systematic trading"],
    lead2="Our approach follows a disciplined research process. Each strategy begins with a clear hypothesis, is developed on historical data and is tested out of sample, with explicit treatment of transaction costs, liquidity, position sizing and the risk of overfitting. Models are documented so that their assumptions can be scrutinised, and their live performance is compared against backtested expectations to decide whether they should be refined, scaled or retired.",
    reports=BLANK, heads=["thomas-tumini"],
    prev=("market-studies", "Market Studies"), next=("business-and-finance", "Business & Finance"),
  ),
})

TILES = [("pnl", "Net PnL", "Closed and open positions"), ("hit", "Hit rate", "Resolved calls that went our way"),
         ("brier", "Brier score", "Forecast accuracy, lower is better"), ("edge", "Edge at entry", "Our probability vs. market price"),
         ("sharpe", "Sharpe ratio", "Risk-adjusted return, annualised"), ("dd", "Max drawdown", "Largest peak-to-trough decline")]

SECTIONS = [("dv-overview", "Overview"), ("dv-performance", "Performance"), ("dv-research", "Research")]


def page(slug):
    d = DIVS[slug]
    people = {p[0]: p for p in team.PEOPLE}
    analysts = next(a[3] for a in team.ANALYSTS if a[1] == slug)
    analysts = sorted(analysts, key=lambda n: n.lower())
    toc = "".join(f'<li><button type="button" class="ip-toc-b" data-t="{i}">{t}</button></li>' for i, t in SECTIONS)
    tags = '<span aria-hidden="true">|</span>'.join(f"<b>{esc(t)}</b>" for t in d["tags"])
    tabs = "".join(f'<button type="button" role="tab" class="pt-tab" data-p="{k}" aria-selected="{"true" if k == "3m" else "false"}">{l}</button>'
                   for k, l in [("1m", "1M"), ("3m", "3M"), ("6m", "6M"), ("1y", "1Y"), ("all", "All")])
    tiles = "".join(f'<div class="pt-tile"><span class="pt-k">{n}</span><span class="pt-v">—</span><span class="pt-d">{t}</span></div>' for _, n, t in TILES)
    def rep(i, t, note):
        no = f"Report {i+1:02d}"
        body = (f'<p class="rp-title">{esc(t)}</p>' + (f'<p class="rp-note">{esc(note)}</p>' if note else '') if t else '')
        lab = esc(t) if t else "Coming soon"
        return (f'<li class="rp{" rp-blank" if not t else ""}"><a class="rp-a" href="#investment-research" aria-label="{lab}, coming soon">'
                f'<div class="rp-page"><div class="rp-top"><span class="rp-mark">Black Swan</span><span class="rp-no">{no}</span></div>'
                f'<p class="rp-cat">{esc(d["name"])}</p>{body}'
                f'<span class="rp-l w90"></span><span class="rp-l w75"></span><span class="rp-chart"></span><span class="rp-l w60"></span>'
                f'<span class="rp-badge">Coming soon</span></div>'
                f'<p class="rp-cap"><b>{lab}</b></p></a></li>')
    reps = "".join(rep(i, t, n) for i, (t, n) in enumerate(d["reports"]))
    pv, nx = d["prev"], d["next"]
    return f'''<main class="flex-1 ip dvp" data-view="{slug}" hidden tabindex="-1">
<header class="ip-hero ip-hero-ph dvp-hero"><div class="ip-hbg" aria-hidden="true" style="background-image:url({HDR})"></div><div class="tm-wrap mx-auto w-full px-gutter ip-hin">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><a href="#divisions">Divisions &amp; Performance</a><span aria-hidden="true">/</span><span aria-current="page">{esc(d["name"])}</span></nav>
<div class="dvp-hc">
<p class="dvp-k">Division {d["n"]:02d} · {esc(d["group"])}</p>
<h1 class="dvp-h1">{esc(d["name"])}</h1>
<p class="dvp-tags">{tags}</p>
<p class="dvp-fig"><span><b>{len(d["heads"])}</b> division head{"s" if len(d["heads"])!=1 else ""}</span><span class="tm-sep" aria-hidden="true">|</span><span><b>{len(analysts)}</b> analysts</span><span class="tm-sep" aria-hidden="true">|</span><span><b>0</b> published reports</span></p>
</div>
</div></header>

<div class="tm-wrap mx-auto w-full px-gutter ip-body">
<aside class="ip-toc" aria-label="On this page"><p class="ip-toc-h">On this page</p><ol>{toc}</ol></aside>
<div class="ip-content dvp-content">

<section class="ip-sec" id="dv-overview" aria-labelledby="dv-overview-h">
<h2 class="ip-h2" id="dv-overview-h">Overview</h2>
<p class="ip-lead">{esc(d["lead"])}</p>
<p class="ip-p">{esc(d["lead2"])}</p>
</section>

<section class="ip-sec pt dvp-perf" id="dv-performance" aria-labelledby="dv-performance-h">
<div class="dvp-ph"><h2 class="ip-h2" id="dv-performance-h">Performance</h2><div class="pt-status"><span class="pt-dot" aria-hidden="true"></span><span><b>Pre-launch.</b> Tracking begins with the division’s first published call.</span></div></div>
<div class="pt-panel">
<div class="pt-toolbar"><p class="pt-sel">{esc(d["name"])}</p><div class="pt-tabs" role="tablist" aria-label="Period">{tabs}</div></div>
<div class="pt-main">
<div class="pt-summary">
<p class="pt-big">No PnL yet</p>
<p class="pt-range dv-range"></p>
<ul class="pt-counts"><li><b>0</b> open positions</li><li><b>0</b> resolved</li><li><b>0</b> markets covered</li></ul>
</div>
<figure class="pt-chartbox" aria-label="Cumulative PnL chart">
<div class="pt-ylab" aria-hidden="true"><span>Profit</span><span>0</span><span>Loss</span></div>
<div class="pt-plot">
<svg class="pt-svg" viewBox="0 0 1000 300" preserveAspectRatio="none" aria-hidden="true">
<defs><linearGradient id="dv-fill-{slug}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f6aa8" stop-opacity=".16"/><stop offset="1" stop-color="#2f6aa8" stop-opacity="0"/></linearGradient></defs>
<g class="pt-grid-l"><line x1="0" x2="1000" y1="30" y2="30"/><line x1="0" x2="1000" y1="90" y2="90"/><line x1="0" x2="1000" y1="210" y2="210"/><line x1="0" x2="1000" y1="270" y2="270"/></g>
<line class="pt-zero" x1="0" x2="1000" y1="150" y2="150"/>
<path class="pt-area dv-area" d="" style="fill:url(#dv-fill-{slug})"/><path class="pt-line dv-line" d=""/>
</svg>
<span class="pt-tag">Illustrative only · not actual results</span>
</div>
<div class="pt-xlab dv-xlab" aria-hidden="true"></div>
</figure>
</div>
<div class="pt-tiles">{tiles}</div>
</div>
<p class="pt-note">Every call will be logged with its entry price, size and our probability at the time, then tracked until the question resolves. The curve shown is a placeholder to illustrate the format.</p>
</section>

<section class="ip-sec" id="dv-research" aria-labelledby="dv-research-h">
<div class="dvp-ph"><h2 class="ip-h2" id="dv-research-h">Research</h2><div class="gl-ctrl"><button type="button" class="gl-btn rp-prev" aria-label="Previous report"><span aria-hidden="true">←</span></button><button type="button" class="gl-btn rp-next" aria-label="Next report"><span aria-hidden="true">→</span></button></div></div>
<p class="dvp-rnote">The division’s first reports are in preparation. Each will open from here once published.</p>
<ul class="rp-track">{reps}</ul>
</section>

<nav class="pp-nav dvp-nav" aria-label="Other divisions">
<a href="#{pv[0]}" class="pp-nav-a"><span class="pp-nav-k">← Previous division</span><span class="pp-nav-n">{esc(pv[1])}</span></a>
<a href="#divisions" class="pp-nav-all">All divisions</a>
<a href="#{nx[0]}" class="pp-nav-a pp-nav-r"><span class="pp-nav-k">Next division →</span><span class="pp-nav-n">{esc(nx[1])}</span></a>
</nav>

</div>
</div>
''' + SCRIPT.replace("__SLUG__", slug) + "</main>"


SCRIPT = r'''<script>(()=>{const r=document.currentScript.closest('.dvp');if(!r)return;
const bs=[...r.querySelectorAll('.ip-toc-b')],secs=bs.map(b=>r.querySelector('#'+b.dataset.t));
bs.forEach((b,i)=>b.addEventListener('click',()=>{const y=secs[i].getBoundingClientRect().top+scrollY-(document.getElementById('site-header').offsetHeight+24);scrollTo({top:y,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})}));
const set=i=>bs.forEach((b,k)=>b.classList.toggle('on',k===i));set(0);
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)set(secs.indexOf(e.target))}),{rootMargin:'-35% 0px -55% 0px'});secs.forEach(s=>io.observe(s));
const tabs=[...r.querySelectorAll('.pt-tab')],line=r.querySelector('.dv-line'),area=r.querySelector('.dv-area'),xl=r.querySelector('.dv-xlab'),rg=r.querySelector('.dv-range');
const M={'1m':1,'3m':3,'6m':6,'1y':12,'all':12},fmt=d=>d.toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'});
const seed=s=>[...s].reduce((a,c)=>(a*31+c.charCodeAt(0))>>>0,7)||1;
function curve(k,n){let s=seed(k);const R=()=>(s=(s*16807)%2147483647)/2147483647;const dr=.25+R()*.5,vol=.9+R()*.8;let v=0;const o=[0];for(let i=1;i<n;i++){v+=dr+(R()-.5)*2*vol;if(R()<.04)v-=3+R()*4;o.push(v)}return o}
function upd(p){tabs.forEach(t=>t.setAttribute('aria-selected',String(t.dataset.p===p)));
const n=p==='1m'?22:p==='3m'?64:p==='6m'?126:252,ys=curve('__SLUG__'+p,n),mx=Math.max(4,...ys.map(Math.abs))*1.15;
const d=ys.map((v,i)=>(i?'L':'M')+(i/(n-1)*1000).toFixed(1)+' '+(150-v/mx*120).toFixed(1)).join(' ');line.setAttribute('d',d);area.setAttribute('d',d+' L1000 150 L0 150 Z');
const L=line.getTotalLength?line.getTotalLength():0;if(L&&!matchMedia('(prefers-reduced-motion: reduce)').matches){line.style.transition='none';line.style.strokeDasharray=L;line.style.strokeDashoffset=L;line.getBoundingClientRect();line.style.transition='stroke-dashoffset 1.1s cubic-bezier(.2,.8,.2,1)';line.style.strokeDashoffset=0}
const e=new Date(),s=new Date(e);s.setMonth(s.getMonth()-M[p]);xl.innerHTML='';for(let i=0;i<5;i++){const dd=new Date(s.getTime()+(e-s)*i/4),sp=document.createElement('span');sp.textContent=(p==='1m'||p==='3m')?dd.getDate()+' '+dd.toLocaleDateString('en-GB',{month:'short'}):dd.toLocaleDateString('en-GB',{month:'short'})+' ’'+String(dd.getFullYear()).slice(2);xl.appendChild(sp)}
rg.textContent=p==='all'?'Since first position · not yet started':fmt(s)+' – '+fmt(e)}
tabs.forEach(t=>t.addEventListener('click',()=>upd(t.dataset.p)));upd('3m');const tr=r.querySelector('.rp-track');if(tr){const step=()=>{const c=tr.querySelector('.rp');return c?c.getBoundingClientRect().width+16:300};r.querySelector('.rp-prev').onclick=()=>tr.scrollBy({left:-step(),behavior:'smooth'});r.querySelector('.rp-next').onclick=()=>tr.scrollBy({left:step(),behavior:'smooth'});}})();</script>'''
