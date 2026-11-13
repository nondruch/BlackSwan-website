"""Track record page (Divisions & Performance → Performance). Built to hold real results; shows a clean pre-launch state."""

DIVS = [("all", "All divisions"), ("bf", "Business & Finance"), ("ep", "Economics & Politics"),
        ("cd", "Cross-Domain"), ("ms", "Market Studies"), ("ad", "Algorithmic Development")]
DIVLINK = {"bf": "business-and-finance", "ep": "economics-and-politics", "cd": "cross-domain", "ms": "market-studies", "ad": "algorithmic-development"}

SCORE = [
  ("Net PnL", "Across all closed and open positions"),
  ("Return on capital", "Net PnL over capital deployed"),
  ("Hit rate", "Resolved calls that went our way"),
  ("Brier score", "Mean squared forecast error, lower is better"),
  ("Log loss", "Penalises confident misses more heavily"),
  ("Edge at entry", "Our probability minus the market price"),
  ("Sharpe ratio", "Risk-adjusted return, annualised"),
  ("Max drawdown", "Largest peak-to-trough decline"),
]

DEFS = [
  ("Net PnL", "Realised and unrealised profit or loss across all positions, marked to the last traded price and reported before costs."),
  ("Hit rate", "The share of resolved calls in which the outcome we assigned the higher probability to occurred."),
  ("Brier score", "The mean squared difference between our stated probability and the outcome (1 or 0). A perfect forecaster scores 0; always guessing 50% scores 0.25."),
  ("Log loss", "The average negative log-likelihood of our forecasts. It rewards calibrated confidence and penalises confident misses heavily."),
  ("Edge at entry", "Our probability minus the market-implied probability at the time a position is opened, in percentage points."),
  ("Sharpe ratio", "Average period return divided by its standard deviation, annualised. Reported once enough history exists to be meaningful."),
  ("Max drawdown", "The largest fall in cumulative PnL from a previous peak, in the reporting currency."),
]

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _cal_svg():
    S, P = 320, 36
    a = S - P - 14
    g = []
    for i in range(5):
        v = i * 25; x = P + i * a / 4; y = 14 + a - i * a / 4
        g.append(f'<line class="g" x1="{P}" x2="{P+a}" y1="{y:.1f}" y2="{y:.1f}"/><line class="g" x1="{x:.1f}" x2="{x:.1f}" y1="14" y2="{14+a}"/>')
        g.append(f'<text x="{P-8}" y="{y+4:.1f}" text-anchor="end">{v}</text><text x="{x:.1f}" y="{14+a+18}" text-anchor="middle">{v}</text>')
    g.append(f'<line class="diag" x1="{P}" y1="{14+a}" x2="{P+a}" y2="14"/>')
    return f'<svg class="tr-cal" viewBox="0 0 {S} {S+6}" aria-hidden="true">{"".join(g)}</svg>'


def _hist_svg():
    W, H = 520, 200
    bars = "".join(f'<rect x="{20+i*24}" y="{H-30-h}" width="18" height="{h}" rx="1"/>' for i, h in enumerate(
        [6, 10, 16, 24, 34, 46, 58, 66, 70, 66, 56, 44, 32, 22, 14, 9, 6, 4, 3, 2]))
    return (f'<svg class="tr-hist" viewBox="0 0 {W} {H}" preserveAspectRatio="none" aria-hidden="true"><g class="ghost">{bars}</g>'
            f'<line class="g" x1="0" x2="{W}" y1="{H-30}" y2="{H-30}"/><line class="z" x1="236" x2="236" y1="10" y2="{H-30}"/>'
            f'<text x="20" y="{H-10}">Loss</text><text x="236" y="{H-10}" text-anchor="middle">0</text><text x="{W-20}" y="{H-10}" text-anchor="end">Profit</text></svg>')


def page():
    chips = "".join(f'<button type="button" class="pt-chip" data-d="{k}" aria-pressed="{"true" if k == "all" else "false"}">{n.replace("&", "&amp;")}</button>' for k, n in DIVS)
    tabs = "".join(f'<button type="button" role="tab" class="pt-tab" data-p="{k}" aria-selected="{"true" if k == "3m" else "false"}">{l}</button>'
                   for k, l in [("1m", "1M"), ("3m", "3M"), ("6m", "6M"), ("1y", "1Y"), ("all", "All")])
    score = "".join(f'<div class="tr-sc"><span class="tr-sk">{k}</span><span class="tr-sv">—</span><span class="tr-sd">{d}</span></div>' for k, d in SCORE)
    rows = "".join(
        f'<tr><th scope="row"><a href="#{DIVLINK[k]}">{n.replace("&", "&amp;")}</a></th><td>0</td><td>0</td><td>—</td><td>—</td><td>—</td><td>—</td>'
        f'<td><span class="tr-spark" aria-hidden="true"></span></td></tr>' for k, n in DIVS[1:])
    heat_rows = "".join(
        f'<tr><th scope="row">{y}</th>' + "".join('<td><span>—</span></td>' for _ in MONTHS) + '<td class="tr-ytd"><span>—</span></td></tr>' for y in (2026, 2027))
    heat_head = "".join(f'<th scope="col">{m}</th>' for m in MONTHS)
    ghost = "".join(
        f'<tr class="tr-ghost" aria-hidden="true"><td><i style="width:{a}%"></i></td><td><i style="width:{b}%"></i></td><td><i style="width:{c}%"></i></td>'
        f'<td><i style="width:60%"></i></td><td><i style="width:50%"></i></td><td><i style="width:50%"></i></td><td><i style="width:55%"></i></td><td><i style="width:45%"></i></td></tr>'
        for a, b, c in [(70, 90, 60), (65, 75, 70), (72, 85, 55), (68, 80, 65)])
    defs = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in DEFS)
    return f'''<main class="flex-1 tr" data-view="performance" hidden tabindex="-1">
<header class="tr-hero"><div class="tr-grid-bg" aria-hidden="true"></div><div class="tm-wrap mx-auto w-full px-gutter tr-hin">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><a href="#divisions">Divisions &amp; Performance</a><span aria-hidden="true">/</span><span aria-current="page">Track record</span></nav>
<div class="tr-hc">
<div>
<p class="tr-k">Performance</p>
<h1 class="tr-h1">Track record</h1>
<p class="tr-lead">Every call we publish is logged with its entry price, size and our probability at the time, then tracked until the question resolves. This page reports the results in full, including the calls that went against us.</p>
</div>
<div class="tr-status"><span class="pt-dot" aria-hidden="true"></span><div><b>Pre-launch</b><span>Tracking begins with our first published call.</span></div></div>
</div>
<dl class="tr-kpis">
<div><dt>Calls logged</dt><dd>0</dd></div>
<div><dt>Resolved</dt><dd>0</dd></div>
<div><dt>Markets covered</dt><dd>0</dd></div>
<div><dt>Divisions reporting</dt><dd>0 <small>/ 5</small></dd></div>
<div><dt>Tracking since</dt><dd class="tr-dim">First call</dd></div>
</dl>
</div></header>

<div class="tr-subnav"><div class="tm-wrap mx-auto w-full px-gutter"><nav aria-label="On this page">
<a href="#tr-pnl" data-t="tr-pnl">PnL</a><a href="#tr-score" data-t="tr-score">Scorecard</a><a href="#tr-div" data-t="tr-div">By division</a><a href="#tr-method" data-t="tr-method">Methodology</a>
</nav></div></div>

<div class="tm-wrap mx-auto w-full px-gutter tr-body pt">

<section class="tr-sec" id="tr-pnl" aria-labelledby="tr-pnl-h">
<div class="tr-sh"><h2 id="tr-pnl-h">Cumulative PnL</h2><p>Society-wide and by division, over any period.</p></div>
<div class="pt-panel">
<div class="pt-toolbar"><div class="pt-chips" role="group" aria-label="Division">{chips}</div><div class="pt-tabs" role="tablist" aria-label="Period">{tabs}</div></div>
<div class="pt-main">
<div class="pt-summary"><p class="pt-sel tr-sel">All divisions</p><p class="pt-big">No PnL yet</p><p class="pt-range tr-range"></p>
<ul class="pt-counts"><li><b>0</b> open positions</li><li><b>0</b> resolved</li><li><b>0</b> markets covered</li></ul></div>
<figure class="pt-chartbox" aria-label="Cumulative PnL chart">
<div class="pt-ylab" aria-hidden="true"><span>Profit</span><span>0</span><span>Loss</span></div>
<div class="pt-plot">
<svg class="pt-svg" viewBox="0 0 1000 300" preserveAspectRatio="none" aria-hidden="true">
<defs><linearGradient id="tr-fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f6aa8" stop-opacity=".16"/><stop offset="1" stop-color="#2f6aa8" stop-opacity="0"/></linearGradient></defs>
<g class="pt-grid-l"><line x1="0" x2="1000" y1="30" y2="30"/><line x1="0" x2="1000" y1="90" y2="90"/><line x1="0" x2="1000" y1="210" y2="210"/><line x1="0" x2="1000" y1="270" y2="270"/></g>
<line class="pt-zero" x1="0" x2="1000" y1="150" y2="150"/>
<path class="pt-area tr-area" d="" style="fill:url(#tr-fill)"/><path class="pt-line tr-line" d=""/>
</svg>
<span class="pt-tag">Illustrative only · not actual results</span>
</div>
<div class="pt-xlab tr-xlab" aria-hidden="true"></div>
</figure>
</div>
</div>
</section>

<section class="tr-sec" id="tr-score" aria-labelledby="tr-score-h">
<div class="tr-sh"><h2 id="tr-score-h">Scorecard</h2><p>Profitability and forecast quality, measured separately.</p></div>
<div class="tr-scores">{score}</div>
</section>

<section class="tr-sec" id="tr-div" aria-labelledby="tr-div-h">
<div class="tr-sh"><h2 id="tr-div-h">By division</h2><p>How each division contributes to the whole.</p></div>
<div class="tr-card tr-tablewrap"><table class="tr-table">
<thead><tr><th scope="col">Division</th><th scope="col">Calls</th><th scope="col">Resolved</th><th scope="col">Hit rate</th><th scope="col">Brier</th><th scope="col">Edge</th><th scope="col">Net PnL</th><th scope="col">Trend</th></tr></thead>
<tbody>{rows}</tbody></table></div>
</section>

<section class="tr-sec" id="tr-method" aria-labelledby="tr-method-h">
<div class="tr-sh"><h2 id="tr-method-h">Methodology</h2><p>How the numbers on this page are calculated.</p></div>
<dl class="tr-defs">{defs}</dl>
<p class="tr-fine">Figures will be updated monthly and reported before costs. Positions are sized according to the society’s internal guidelines. Past performance, once reported, is no guarantee of future results; nothing on this page is investment advice.</p>
</section>

</div>
''' + SCRIPT + "</main>"


SCRIPT = r'''<script>(()=>{const r=document.currentScript.closest('.tr');if(!r)return;
const chips=[...r.querySelectorAll('.pt-chip')],tabs=[...r.querySelectorAll('.pt-tab')],line=r.querySelector('.tr-line'),area=r.querySelector('.tr-area'),xl=r.querySelector('.tr-xlab'),rg=r.querySelector('.tr-range'),sel=r.querySelector('.tr-sel');
let dv='all',per='3m';const M={'1m':1,'3m':3,'6m':6,'1y':12,'all':12},fmt=d=>d.toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'});
const seed=s=>[...s].reduce((a,c)=>(a*31+c.charCodeAt(0))>>>0,7)||1;
function curve(k,n){let s=seed(k);const R=()=>(s=(s*16807)%2147483647)/2147483647;const dr=.25+R()*.5,vol=.9+R()*.8;let v=0;const o=[0];for(let i=1;i<n;i++){v+=dr+(R()-.5)*2*vol;if(R()<.04)v-=3+R()*4;o.push(v)}return o}
function upd(){chips.forEach(c=>c.setAttribute('aria-pressed',String(c.dataset.d===dv)));tabs.forEach(t=>t.setAttribute('aria-selected',String(t.dataset.p===per)));
sel.textContent=chips.find(c=>c.dataset.d===dv).textContent;
const n=per==='1m'?22:per==='3m'?64:per==='6m'?126:252,ys=curve('trk'+dv+per,n),mx=Math.max(4,...ys.map(Math.abs))*1.15;
const d=ys.map((v,i)=>(i?'L':'M')+(i/(n-1)*1000).toFixed(1)+' '+(150-v/mx*120).toFixed(1)).join(' ');line.setAttribute('d',d);area.setAttribute('d',d+' L1000 150 L0 150 Z');
const L=line.getTotalLength?line.getTotalLength():0;if(L&&!matchMedia('(prefers-reduced-motion: reduce)').matches){line.style.transition='none';line.style.strokeDasharray=L;line.style.strokeDashoffset=L;line.getBoundingClientRect();line.style.transition='stroke-dashoffset 1.1s cubic-bezier(.2,.8,.2,1)';line.style.strokeDashoffset=0}
const e=new Date(),s=new Date(e);s.setMonth(s.getMonth()-M[per]);xl.innerHTML='';for(let i=0;i<5;i++){const dd=new Date(s.getTime()+(e-s)*i/4),sp=document.createElement('span');sp.textContent=(per==='1m'||per==='3m')?dd.getDate()+' '+dd.toLocaleDateString('en-GB',{month:'short'}):dd.toLocaleDateString('en-GB',{month:'short'})+' ’'+String(dd.getFullYear()).slice(2);xl.appendChild(sp)}
rg.textContent=per==='all'?'Since first position · not yet started':fmt(s)+' – '+fmt(e)}
chips.forEach(c=>c.addEventListener('click',()=>{dv=c.dataset.d;upd()}));tabs.forEach(t=>t.addEventListener('click',()=>{per=t.dataset.p;upd()}));upd();
const links=[...r.querySelectorAll('.tr-subnav a')],secs=links.map(a=>r.querySelector('#'+a.dataset.t));
links.forEach((a,i)=>a.addEventListener('click',e=>{e.preventDefault();const y=secs[i].getBoundingClientRect().top+scrollY-(document.getElementById('site-header').offsetHeight+r.querySelector('.tr-subnav').offsetHeight+16);scrollTo({top:y,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})}));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){const i=secs.indexOf(e.target);links.forEach((a,k)=>a.classList.toggle('on',k===i))}}),{rootMargin:'-30% 0px -60% 0px'});secs.forEach(s=>io.observe(s));
})();</script>'''
