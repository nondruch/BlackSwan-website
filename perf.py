"""Performance tracker v2: one PnL chart switchable by division; metrics follow the selection.

Real results go in REAL below (JS). While a division has no data it shows a faint,
clearly-labelled illustrative curve and dashes for every metric.
"""
import json

DIVS = [("all", "All divisions"), ("bf", "Business & Finance"), ("ep", "Economics & Politics"),
        ("cd", "Cross-Domain"), ("ms", "Market Studies"), ("ad", "Algorithmic Development")]

TILES = [
    ("pnl", "Net PnL", "Closed and open positions"),
    ("hit", "Hit rate", "Resolved calls that went our way"),
    ("brier", "Brier score", "Forecast accuracy, lower is better"),
    ("edge", "Edge at entry", "Our probability vs. market price"),
    ("sharpe", "Sharpe ratio", "Risk-adjusted return, annualised"),
    ("dd", "Max drawdown", "Largest peak-to-trough decline"),
]


def html():
    chips = "".join(
        f'<button type="button" class="pt-chip" data-d="{k}" aria-pressed="{"true" if k == "all" else "false"}">{n.replace("&", "&amp;")}</button>'
        for k, n in DIVS)
    tabs = "".join(
        f'<button type="button" role="tab" class="pt-tab" data-p="{k}" aria-selected="{"true" if k == "3m" else "false"}">{lab}</button>'
        for k, lab in [("1m", "1M"), ("3m", "3M"), ("6m", "6M"), ("1y", "1Y"), ("all", "All")])
    tiles = "".join(
        f'<div class="pt-tile" data-m="{k}"><span class="pt-k">{n}</span><span class="pt-v">—</span><span class="pt-d">{d}</span></div>'
        for k, n, d in TILES)
    return f'''<section id="track-record" class="pt" aria-labelledby="pt-h">
<div class="pt-inner mx-auto w-full px-gutter">
<div class="pt-head">
<div><p class="pt-eyebrow">Performance</p><h2 class="pt-h" id="pt-h">Track record</h2></div>
<div class="pt-status"><span class="pt-dot" aria-hidden="true"></span><span><b>Pre-launch.</b> Tracking begins with our first published research call.</span></div>
</div>

<div class="pt-panel">
<div class="pt-toolbar">
<div class="pt-chips" role="group" aria-label="Division">{chips}</div>
<div class="pt-tabs" role="tablist" aria-label="Period">{tabs}</div>
</div>

<div class="pt-main">
<div class="pt-summary">
<p class="pt-sel" id="pt-sel">All divisions</p>
<p class="pt-big"><span id="pt-big">No PnL yet</span></p>
<p class="pt-range" id="pt-range"></p>
<ul class="pt-counts"><li><b id="pt-open">0</b> open positions</li><li><b id="pt-res">0</b> resolved</li><li><b id="pt-mkts">0</b> markets covered</li></ul>
</div>
<figure class="pt-chartbox" aria-label="Cumulative PnL chart">
<div class="pt-ylab" aria-hidden="true"><span>Profit</span><span>0</span><span>Loss</span></div>
<div class="pt-plot">
<svg class="pt-svg" id="pt-svg" viewBox="0 0 1000 300" preserveAspectRatio="none" aria-hidden="true">
<defs><linearGradient id="pt-fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f6aa8" stop-opacity=".16"/><stop offset="1" stop-color="#2f6aa8" stop-opacity="0"/></linearGradient></defs>
<g class="pt-grid-l"><line x1="0" x2="1000" y1="30" y2="30"/><line x1="0" x2="1000" y1="90" y2="90"/><line x1="0" x2="1000" y1="210" y2="210"/><line x1="0" x2="1000" y1="270" y2="270"/></g>
<line class="pt-zero" x1="0" x2="1000" y1="150" y2="150"/>
<path class="pt-area" id="pt-area" d=""/>
<path class="pt-line" id="pt-line" d=""/>
</svg>
<span class="pt-tag">Illustrative only · not actual results</span>
</div>
<div class="pt-xlab" id="pt-xlab" aria-hidden="true"></div>
</figure>
</div>

<div class="pt-tiles" id="pt-tiles">{tiles}</div>
</div>

<p class="pt-note">Every call will be logged with its entry price, size and our probability at the time, then tracked until the question resolves. Figures will be updated monthly, with the full methodology published alongside the first results. The curve shown is a placeholder to illustrate the format.</p>
</div>
</section>'''


JS = r'''<script>
(() => {
  /* Real results go here once they exist, e.g.
     REAL.bf = { pnl: [[ "2027-01-15", 120 ], ...], metrics: { pnl: "+€1,240", hit: "62%", brier: "0.19", edge: "+6.1 pts", sharpe: "1.4", dd: "−€310" }, open: 3, resolved: 8, markets: 11 } */
  const REAL = {};
  const NAMES = __NAMES__;
  const boot = () => {
    const root = document.getElementById('track-record'); if (!root || root.dataset.booted) return; root.dataset.booted = '1';
    const $ = s => root.querySelector(s);
    const chips = [...root.querySelectorAll('.pt-chip')], tabs = [...root.querySelectorAll('.pt-tab')];
    let div = 'all', per = '3m';
    const months = { '1m': 1, '3m': 3, '6m': 6, '1y': 12, 'all': 12 };
    const fmt = d => d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });

    // deterministic illustrative path per division × period
    const seedOf = s => [...s].reduce((a, c) => (a * 31 + c.charCodeAt(0)) >>> 0, 7) || 1;
    function curve(key, n) {
      let s = seedOf(key); const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
      const drift = 0.25 + r() * 0.5, vol = 0.9 + r() * 0.8; let v = 0; const out = [0];
      for (let i = 1; i < n; i++) { v += drift + (r() - 0.5) * 2 * vol; if (r() < 0.04) v -= 3 + r() * 4; out.push(v); }
      return out;
    }
    function draw() {
      const n = per === '1m' ? 22 : per === '3m' ? 64 : per === '6m' ? 126 : 252;
      const ys = curve(div + per, n), max = Math.max(4, ...ys.map(Math.abs)) * 1.15;
      const X = i => (i / (n - 1)) * 1000, Y = v => 150 - (v / max) * 120;
      const d = ys.map((v, i) => (i ? 'L' : 'M') + X(i).toFixed(1) + ' ' + Y(v).toFixed(1)).join(' ');
      $('#pt-line').setAttribute('d', d);
      $('#pt-area').setAttribute('d', d + ' L1000 150 L0 150 Z');
      const line = $('#pt-line'), len = line.getTotalLength ? line.getTotalLength() : 0;
      if (len && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
        line.style.transition = 'none'; line.style.strokeDasharray = len; line.style.strokeDashoffset = len;
        line.getBoundingClientRect(); line.style.transition = 'stroke-dashoffset 1.1s cubic-bezier(.2,.8,.2,1)'; line.style.strokeDashoffset = 0;
      }
    }
    function labels() {
      const end = new Date(), start = new Date(end); start.setMonth(start.getMonth() - months[per]);
      const xl = $('#pt-xlab'); xl.innerHTML = '';
      for (let i = 0; i < 5; i++) {
        const d = new Date(start.getTime() + (end - start) * i / 4), s = document.createElement('span');
        s.textContent = per === '1m' || per === '3m' ? d.getDate() + ' ' + d.toLocaleDateString('en-GB', { month: 'short' }) : d.toLocaleDateString('en-GB', { month: 'short' }) + ' ’' + String(d.getFullYear()).slice(2);
        xl.appendChild(s);
      }
      $('#pt-range').textContent = per === 'all' ? 'Since first position · not yet started' : fmt(start) + ' – ' + fmt(end);
    }
    function metrics() {
      const r = REAL[div];
      $('#pt-sel').textContent = NAMES[div];
      $('#pt-big').textContent = r && r.metrics ? r.metrics.pnl : 'No PnL yet';
      $('#pt-open').textContent = r ? r.open : 0; $('#pt-res').textContent = r ? r.resolved : 0; $('#pt-mkts').textContent = r ? r.markets : 0;
      root.querySelectorAll('.pt-tile').forEach(t => {
        const v = t.querySelector('.pt-v'), nv = r && r.metrics ? r.metrics[t.dataset.m] : '—';
        if (v.textContent !== nv) { v.textContent = nv; }
        t.classList.remove('flash'); void t.offsetWidth; t.classList.add('flash');
      });
      root.classList.toggle('is-live', !!(r && r.metrics));
    }
    function update() { chips.forEach(c => c.setAttribute('aria-pressed', String(c.dataset.d === div))); tabs.forEach(t => t.setAttribute('aria-selected', String(t.dataset.p === per))); labels(); metrics(); draw(); }
    chips.forEach(c => c.addEventListener('click', () => { div = c.dataset.d; update(); }));
    tabs.forEach(t => t.addEventListener('click', () => { per = t.dataset.p; update(); }));
    update();
  };
  if (window.claude && window.claude.hot && window.claude.hot.ready) window.claude.hot.ready(boot); else boot();
  addEventListener('load', boot);
})();
</script>'''.replace("__NAMES__", json.dumps(dict(DIVS)))
