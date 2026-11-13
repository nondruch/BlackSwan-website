def hero_html(logo_hero, esc):
    return '''<section id="top" class="hero band-dark" aria-label="Introduction">
<div class="hero-media" aria-hidden="true">
<canvas id="hero-film"></canvas>
<div class="hero-shade"></div>
<div class="hero-grain"></div>
</div>
<div class="hero-body mx-auto w-full px-gutter">
<div class="hero-copy">
<h1 class="hero-h"><span>Black Swan</span> <span>Student Society</span></h1>
<p class="hero-p">Combining rigorous research, probabilistic thinking, and diverse perspectives to uncover insights and identify opportunities in prediction markets.</p>
<a class="hero-cta" href="#how-to-apply">Apply Now</a>
</div>
</div>
</section>'''

HERO_JS = r'''<script>
(() => {
const bootFilm = () => {
  /* "Footage": a slow, shallow-focus camera move across a live prediction-market terminal. */
  const cv = document.getElementById('hero-film'); if (!cv) return;
  if (!cv.isConnected) return;
  const ctx = cv.getContext('2d');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const TW = 2400, TH = 1350;
  const tex = document.createElement('canvas'); tex.width = TW; tex.height = TH; const tx = tex.getContext('2d');
  const soft = document.createElement('canvas'); soft.width = TW / 4; soft.height = TH / 4; const sx = soft.getContext('2d');
  const work = document.createElement('canvas'); const wx = work.getContext('2d');
  let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const MONO = '"IBM Plex Mono", ui-monospace, monospace', SANS = '"Instrument Sans", system-ui, sans-serif';

  // live state
  let chart = []; { let x = 0.4; for (let i = 0; i < 220; i++) { x += (rnd() - 0.47) * 0.12; chart.push(1 / (1 + Math.exp(-x))); } }
  const book = Array.from({ length: 14 }, (_, i) => ({ p: 0, s: 400 + rnd() * 9000 }));
  const rows = [
    ['Fed decision in December?', 'Economics & Politics', .86], ['ECB rate cut at next meeting?', 'Economics & Politics', .41],
    ['Bitcoin above $100k on 31 Dec?', 'Cross-Domain', .37], ['Deal closes by year end?', 'Business & Finance', .64],
    ['Q4 earnings beat consensus?', 'Business & Finance', .58], ['Milan above 15°C tomorrow?', 'Cross-Domain', .22],
    ['Coalition holds to March?', 'Economics & Politics', .71]
  ].map(r => ({ q: r[0], d: r[1], p: r[2], c: 0, v: 20 + rnd() * 900 }));

  function tick() {
    let last = chart[chart.length - 1], x = Math.log(last / (1 - last)) + (rnd() - 0.48) * 0.09;
    chart.push(1 / (1 + Math.exp(-x))); if (chart.length > 220) chart.shift();
    rows.forEach(r => { const d = (rnd() - 0.5) * 0.02; r.p = Math.min(.98, Math.max(.02, r.p + d)); r.c = d; r.v += rnd() * 3; });
    book.forEach(b => { b.s = Math.max(100, b.s + (rnd() - 0.5) * 900); });
  }

  function panel(x, y, w, h, title) {
    tx.fillStyle = '#111d2c'; tx.fillRect(x, y, w, h);
    tx.strokeStyle = '#243549'; tx.lineWidth = 2; tx.strokeRect(x, y, w, h);
    tx.fillStyle = '#7f93ad'; tx.font = `600 22px ${SANS}`; tx.textBaseline = 'top'; tx.fillText(title, x + 28, y + 24);
  }
  function paint() {
    tx.fillStyle = '#0a111b'; tx.fillRect(0, 0, TW, TH);
    // header strip
    tx.fillStyle = '#0c131d'; tx.fillRect(0, 0, TW, 70);
    tx.font = `600 24px ${SANS}`; tx.fillStyle = '#c9d4e3'; tx.textBaseline = 'middle'; tx.fillText('BLACK SWAN  ·  MARKETS', 40, 36);
    tx.font = `22px ${MONO}`; tx.fillStyle = '#6f84a0';
    ['ECON & POL', 'BUS & FIN', 'CROSS-DOMAIN', 'STUDIES', 'ALGO'].forEach((t, i) => tx.fillText(t, 520 + i * 230, 36));
    // chart panel
    const cx = 40, cy = 100, cw = 1440, ch = 700; panel(cx, cy, cw, ch, 'Fed decision in December?  ·  25 bps increase');
    const px = cx + 90, py = cy + 90, pw = cw - 140, ph = ch - 150;
    tx.font = `20px ${MONO}`; tx.textBaseline = 'middle';
    for (let g = 0; g <= 4; g++) {
      const yy = py + ph - g * ph / 4; tx.strokeStyle = '#18233180'; tx.strokeStyle = '#162130'; tx.lineWidth = 2;
      tx.beginPath(); tx.moveTo(px, yy); tx.lineTo(px + pw, yy); tx.stroke(); tx.fillStyle = '#566a84'; tx.fillText(g * 25 + '%', cx + 26, yy);
    }
    const X = i => px + i / (chart.length - 1) * pw, Y = v => py + ph - v * ph;
    const grad = tx.createLinearGradient(0, py, 0, py + ph); grad.addColorStop(0, 'rgba(96,150,214,.35)'); grad.addColorStop(1, 'rgba(96,150,214,0)');
    tx.beginPath(); chart.forEach((v, i) => i ? tx.lineTo(X(i), Y(v)) : tx.moveTo(X(i), Y(v))); tx.lineTo(X(chart.length - 1), py + ph); tx.lineTo(px, py + ph); tx.closePath(); tx.fillStyle = grad; tx.fill();
    tx.beginPath(); chart.forEach((v, i) => i ? tx.lineTo(X(i), Y(v)) : tx.moveTo(X(i), Y(v))); tx.strokeStyle = '#8fb6e8'; tx.lineWidth = 4; tx.stroke();
    const lv = chart[chart.length - 1];
    tx.fillStyle = '#ffffff'; tx.beginPath(); tx.arc(X(chart.length - 1), Y(lv), 8, 0, 7); tx.fill();
    tx.font = `600 64px ${MONO}`; tx.fillStyle = '#e8eef7'; tx.textBaseline = 'top'; tx.fillText(Math.round(lv * 100) + '%', cx + cw - 230, cy + 20);
    // order book
    const bx = 1520, by = 100, bw = 840, bh = 700; panel(bx, by, bw, bh, 'Order book  ·  YES');
    tx.font = `24px ${MONO}`; tx.textBaseline = 'middle';
    const mid = Math.round(lv * 100);
    book.forEach((b, i) => {
      const ask = i < 7, price = ask ? mid + (7 - i) : mid - (i - 6), yy = by + 100 + i * 42;
      const w = Math.min(1, b.s / 10000) * (bw - 80);
      tx.fillStyle = ask ? 'rgba(214,110,110,.16)' : 'rgba(110,190,150,.16)'; tx.fillRect(bx + bw - 40 - w, yy - 17, w, 34);
      tx.fillStyle = ask ? '#d98c8c' : '#8fcfaa'; tx.fillText(price + '¢', bx + 40, yy);
      tx.fillStyle = '#9fb0c6'; tx.textAlign = 'right'; tx.fillText(Math.round(b.s).toLocaleString('en-US'), bx + bw - 50, yy); tx.textAlign = 'left';
    });
    // market table
    const mx = 40, my = 840, mw = 2320, mh = 480; panel(mx, my, mw, mh, 'Most active');
    tx.textBaseline = 'middle';
    rows.forEach((r, i) => {
      const yy = my + 100 + i * 52;
      tx.fillStyle = i % 2 ? '#111d2c' : '#142236'; tx.fillRect(mx + 2, yy - 26, mw - 4, 52);
      tx.font = `26px ${SANS}`; tx.fillStyle = '#d5deea'; tx.fillText(r.q, mx + 30, yy);
      tx.font = `22px ${SANS}`; tx.fillStyle = '#6f84a0'; tx.fillText(r.d, mx + 900, yy);
      tx.font = `26px ${MONO}`; tx.fillStyle = '#e8eef7'; tx.fillText(Math.round(r.p * 100) + '%', mx + 1400, yy);
      tx.fillStyle = r.c >= 0 ? '#8fcfaa' : '#d98c8c'; tx.fillText((r.c >= 0 ? '▲ ' : '▼ ') + Math.abs(r.c * 100).toFixed(1), mx + 1560, yy);
      tx.fillStyle = '#7f93ad'; tx.fillText('$' + Math.round(r.v) + 'k', mx + 1820, yy);
    });
    sx.filter = 'blur(3.5px)'; sx.clearRect(0, 0, soft.width, soft.height); sx.drawImage(tex, 0, 0, soft.width, soft.height); sx.filter = 'none';
  }

  let W = 0, H = 0, dpr = 1;
  function size() {
    const r = cv.getBoundingClientRect(); dpr = 0.5;   // render below screen resolution: the footage is soft by design, and this keeps it smooth
    W = r.width; H = r.height; cv.width = work.width = Math.round(W * dpr); cv.height = work.height = Math.round(H * dpr);
  }
  const ease = t => t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
  // Plays for everyone (gently slower if the viewer prefers reduced motion); starts mid-move so motion is visible at once.
  const speed = reduce ? 0.5 : 1;
  let t0 = performance.now() - 7000 / speed, paused = false, pausedAt = 0, offset = 0;
  function frame(now) {
    if (!cv.width || !cv.height) return;
    const t = ((paused ? pausedAt : now) - t0 - offset) / 1000 * speed;
    const k = ease((Math.sin(t / 30 * Math.PI * 2 - Math.PI / 2) + 1) / 2);   // 30 s ping-pong
    const scale = Math.max(W / TW, H / TH) * (1.18 + 0.08 * k);
    const camX = TW * (0.40 + 0.2 * k), camY = TH * (0.5 + 0.05 * Math.sin(t / 17));
    const setCam = c => { c.setTransform(1, 0, 0, 1, 0, 0); c.translate(cv.width * 0.62, cv.height * 0.5); c.rotate(-0.07); c.transform(1, 0.04, -0.12, 1, 0, 0); c.scale(scale * dpr, scale * dpr); c.translate(-camX, -camY); };
    // out-of-focus layer
    setCam(ctx); ctx.imageSmoothingQuality = 'high'; ctx.drawImage(soft, 0, 0, TW, TH);
    // in-focus band, feathered
    wx.setTransform(1, 0, 0, 1, 0, 0); wx.clearRect(0, 0, work.width, work.height);
    setCam(wx); wx.drawImage(tex, 0, 0);
    wx.setTransform(1, 0, 0, 1, 0, 0); wx.globalCompositeOperation = 'destination-in';
    const fx = work.width * (0.66 + 0.06 * Math.sin(t / 11)), fy = work.height * 0.5;
    const g = wx.createRadialGradient(fx, fy, 0, fx, fy, work.width * 0.42);
    g.addColorStop(0, 'rgba(0,0,0,1)'); g.addColorStop(0.45, 'rgba(0,0,0,.85)'); g.addColorStop(1, 'rgba(0,0,0,0)');
    wx.fillStyle = g; wx.fillRect(0, 0, work.width, work.height); wx.globalCompositeOperation = 'source-over';
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.drawImage(work, 0, 0);
    // monitor glow / bokeh
    ctx.globalCompositeOperation = 'screen';
    for (let i = 0; i < 3; i++) {
      const bx = cv.width * ((0.2 + i * 0.21 + t * 0.004 * (i % 2 ? 1 : -1)) % 1.1), by = cv.height * (0.15 + ((i * 37) % 70) / 100), br = cv.width * (0.05 + (i % 3) * 0.025);
      const bg = ctx.createRadialGradient(bx, by, 0, bx, by, br); bg.addColorStop(0, 'rgba(120,160,220,.14)'); bg.addColorStop(1, 'rgba(120,160,220,0)');
      ctx.fillStyle = bg; ctx.beginPath(); ctx.arc(bx, by, br, 0, 7); ctx.fill();
    }
    ctx.globalCompositeOperation = 'source-over';
  }
  let last = 0, visible = true;
  function loop(now) {
    if (!visible || document.hidden) { looping = false; return; }
    if (now - last < 50 || now - lastScroll < 180) { requestAnimationFrame(loop); return; }   // ~24 fps, and hold still while the page is scrolling
    last = now; frame(now); requestAnimationFrame(loop);
  }
  let looping = false, lastScroll = 0;
  addEventListener('scroll', () => { lastScroll = performance.now(); }, { passive: true });
  const kick = () => { if (!looping && visible && !document.hidden) { looping = true; requestAnimationFrame(loop); } };
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; kick(); }).observe(cv);
  document.addEventListener('visibilitychange', kick);
  function start() { size(); paint(); frame(performance.now()); kick(); }
  start();
  if (document.fonts) document.fonts.ready.then(paint);
  new ResizeObserver(() => { size(); frame(performance.now()); }).observe(cv);
  setInterval(() => { if (!paused && visible && !document.hidden) { tick(); paint(); } }, 3000);

};
/* Start now, and again whenever the viewer swaps in a new version of the page without a full reload. */
const run = () => { const cv = document.getElementById('hero-film'); if (cv && !cv.dataset.booted) { cv.dataset.booted = '1'; bootFilm(); } };
if (window.claude && window.claude.hot && window.claude.hot.ready) window.claude.hot.ready(run); else run();
document.addEventListener('DOMContentLoaded', run); addEventListener('load', run);

})();
</script>'''


INTRO = '''<section id="origin" class="intro" aria-labelledby="intro-eyebrow">
<div class="intro-panel">
<div class="intro-row mx-auto w-full px-gutter">
<p class="intro-eyebrow" id="intro-eyebrow">Who we are</p>
<div class="intro-text">
<p>Founded in 2026, Black Swan is Bocconi University’s first student society dedicated to prediction markets. We bring together independent thinkers to challenge consensus, assess probabilities and identify market inefficiencies through rigorous research and disciplined analysis.</p>
<div class="intro-cta"><a class="block-btn" href="#introduction"><span class="label">Explore Who We Are</span></a></div>
</div>
</div>
</div>
</section>'''

CARDS_DATA = [
  ("Development", "Invested in Your Growth",
   "Build your analytical skills through practical research, with experienced students offering guidance on CVs, internships and recruitment. Publish under your own name and build a body of work that demonstrates your capabilities."),
  ("Community", "Diverse Perspectives. Shared Ambition.",
   "Join 60+ members across five specialised divisions, brought together by intellectual curiosity. Exchange ideas with traders, researchers and industry professionals, and build lasting relationships through regular society events and informal gatherings."),
  ("Ownership", "Help Shape What Comes Next",
   "Founded in 2026, Black Swan is still taking shape. Members have the opportunity to lead new initiatives, influence our research agenda and help define the future of Bocconi’s first prediction market society."),
]
CARDS = '<section id="why-join" class="why" aria-label="Why join Black Swan"><div class="why-inner mx-auto w-full px-gutter"><div class="why-grid">' + "".join(
    f'<article class="why-card"><span class="why-eyebrow">{e}</span><h3 class="why-h">{h}</h3><p class="why-p">{p}</p></article>' for e, h, p in CARDS_DATA
) + '</div></div></section>'

DIVX_DATA = [
  ("business-and-finance", "Business & Finance", "Investment research",
   "We apply prediction markets to corporate and financial events, from company earnings and industry rankings to the course of an acquisition: what the buyer pays, how the tender offer and the negotiations go, and whether the deal closes at all.",
   ["Earnings", "Industry rankings", "M&A"]),
  ("economics-and-politics", "Economics & Politics", "Investment research",
   "We cover the markets tied to macroeconomic and political outcomes, from central bank decisions and inflation data to elections, trade policy and geopolitics. We watch how they take in new information, and measure their probabilities against the polls, forecasts and data.",
   ["Central banks", "Macro data", "Elections & policy"]),
  ("cross-domain", "Cross-Domain", "Investment research",
   "We work outside traditional finance, on crypto, weather, public appearances and mention markets. We watch how these markets respond to real-world information, and compare the probabilities across sources to see how expectations form and where they disagree.",
   ["Crypto", "Weather", "Appearances & mentions"]),
  ("market-studies", "Market Studies", "Markets & models",
   "We study the markets themselves, publishing market reports and statistical research on what prediction markets reveal once they have closed.",
   ["Closed markets", "Statistical analysis", "Price drivers"]),
  ("algorithmic-development", "Algorithmic Development", "Markets & models",
   "We look for alpha in prediction markets through statistical models and systematic trading, turning research ideas into testable strategies through algorithm design and backtesting.",
   ["Statistical models", "Backtesting", "Systematic trading"]),
]

def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def _panel(i, d):
    slug, name, group, desc, tags = d
    n = f"{i+1:02d}"
    tg = "".join(f"<li>{_esc(t)}</li>" for t in tags)
    return (f'<article class="dp{" is-open" if i == 0 else ""}" data-i="{i}">'
            f'<button type="button" class="dp-tab" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="dp-body-{i}"><span class="dp-n">{n}</span><span class="dp-name">{_esc(name)}</span></button>'
            f'<div class="dp-body" id="dp-body-{i}"><span class="dp-big" aria-hidden="true">{n}</span>'
            f'<div class="dp-top"><span class="dp-group">{_esc(group)}</span><span class="dp-count">{n} / 05</span></div>'
            f'<div class="dp-main"><h3 class="dp-h">{_esc(name)}</h3><p class="dp-p">{_esc(desc)}</p><ul class="dp-tags">{tg}</ul>'
            f'<a class="dp-link" href="#{slug}">Explore the division <span aria-hidden="true">→</span></a></div></div></article>')

DIVX = ('<section id="divisions" class="divx" aria-labelledby="divx-h"><div class="divx-inner mx-auto w-full px-gutter">'
        '<div class="divx-head"><h2 class="divx-eyebrow" id="divx-h">Our divisions</h2></div>'
        '<div class="divx-rail" role="list">' + "".join(_panel(i, d) for i, d in enumerate(DIVX_DATA)) + '</div></div></section>')

DIVX_JS = r'''<script>
(() => {
  const boot = () => {
    const rail = document.querySelector('.divx-rail'); if (!rail || rail.dataset.booted) return; rail.dataset.booted = '1';
    const panels = [...rail.querySelectorAll('.dp')];
    const fit = () => { const gaps = 12 * (panels.length - 1); rail.style.setProperty('--open-w', Math.floor((rail.clientWidth - gaps) * 6.5 / (6.5 + panels.length - 1) - 2) + 'px'); };
    fit(); new ResizeObserver(fit).observe(rail);
    const desk = matchMedia('(min-width: 64rem)');
    const open = i => panels.forEach((p, k) => { const on = k === i; p.classList.toggle('is-open', on); p.querySelector('.dp-tab').setAttribute('aria-expanded', String(on)); });
    panels.forEach((p, i) => {
      p.addEventListener('mouseenter', () => { if (desk.matches) open(i); });
      p.querySelector('.dp-tab').addEventListener('click', () => open(i));
      p.addEventListener('focusin', () => open(i));
    });
  };
  if (window.claude && window.claude.hot && window.claude.hot.ready) window.claude.hot.ready(boot); else boot();
  addEventListener('load', boot);
})();
</script>'''
