"""Introduction page (Who we are → Introduction)."""
import base64, pathlib
D = pathlib.Path(__file__).parent
LOGO = "data:image/webp;base64," + base64.b64encode((D / "logo-hero.webp").read_bytes()).decode()

SECTIONS = [("ip-intro", "Introduction"), ("ip-mission", "Our Mission"), ("ip-story", "Our Story"), ("ip-growth", "Invested in Your Growth")]


def page():
    toc = "".join(f'<li><button type="button" class="ip-toc-b" data-t="{i}">{t}</button></li>'
                  for k, (i, t) in enumerate(SECTIONS))
    return f'''<main class="flex-1 ip" data-view="introduction" hidden tabindex="-1">
<header class="ip-hero ip-hero-ph ip-hero-intro"><div class="ip-hbg" aria-hidden="true"></div><p class="ph-credit">Bocconi University, Milan · Photo: Luca Musella / Unsplash</p><div class="tm-wrap mx-auto w-full px-gutter ip-hin">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><span>Who we are</span><span aria-hidden="true">/</span><span aria-current="page">Introduction</span></nav>
<div class="ip-hero-grid"><p class="tm-eyebrow">Who we are</p><h1 class="ip-h1">Bocconi’s first student society dedicated to prediction markets.</h1></div>
</div></header>

<div class="tm-wrap mx-auto w-full px-gutter ip-body">
<aside class="ip-toc ip-side" aria-label="On this page"><div class="ip-toc-in"><p class="ip-toc-h">On this page</p><ol>{toc}</ol></div><section class="ip-gal" aria-roledescription="carousel" aria-label="Photo gallery">
<div class="gl-head"><p class="gl-k">Gallery</p><div class="gl-ctrl"><span class="gl-count"><b class="gl-i">01</b> / 05</span><button type="button" class="gl-btn gl-prev" aria-label="Previous photo"><span aria-hidden="true">←</span></button><button type="button" class="gl-btn gl-next" aria-label="Next photo"><span aria-hidden="true">→</span></button></div></div>
<ul class="gl-track"><li class="gl-s" aria-roledescription="slide" aria-label="1 of 5"><div class="gl-ph"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"/><circle cx="12" cy="12.5" r="3.5"/><path d="M8.5 6l1.5-2h4l1.5 2"/></svg><span>Photo coming soon</span></div><p class="gl-cap"><b>Society launch</b><span>2026</span></p></li><li class="gl-s" aria-roledescription="slide" aria-label="2 of 5"><div class="gl-ph"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"/><circle cx="12" cy="12.5" r="3.5"/><path d="M8.5 6l1.5-2h4l1.5 2"/></svg><span>Photo coming soon</span></div><p class="gl-cap"><b>First general meeting</b><span>2026</span></p></li><li class="gl-s" aria-roledescription="slide" aria-label="3 of 5"><div class="gl-ph"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"/><circle cx="12" cy="12.5" r="3.5"/><path d="M8.5 6l1.5-2h4l1.5 2"/></svg><span>Photo coming soon</span></div><p class="gl-cap"><b>Division workshops</b><span>2026</span></p></li><li class="gl-s" aria-roledescription="slide" aria-label="4 of 5"><div class="gl-ph"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"/><circle cx="12" cy="12.5" r="3.5"/><path d="M8.5 6l1.5-2h4l1.5 2"/></svg><span>Photo coming soon</span></div><p class="gl-cap"><b>Speaker events</b><span>2026</span></p></li><li class="gl-s" aria-roledescription="slide" aria-label="5 of 5"><div class="gl-ph"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"/><circle cx="12" cy="12.5" r="3.5"/><path d="M8.5 6l1.5-2h4l1.5 2"/></svg><span>Photo coming soon</span></div><p class="gl-cap"><b>Socials</b><span>2026</span></p></li></ul>
<div class="gl-dots"><button type="button" class="gl-dot" aria-label="Go to photo 1" aria-current="true"></button><button type="button" class="gl-dot" aria-label="Go to photo 2"></button><button type="button" class="gl-dot" aria-label="Go to photo 3"></button><button type="button" class="gl-dot" aria-label="Go to photo 4"></button><button type="button" class="gl-dot" aria-label="Go to photo 5"></button></div>
</section></aside>
<div class="ip-content">

<section class="ip-sec" id="ip-intro" aria-labelledby="ip-intro-h">
<h2 class="ip-h2" id="ip-intro-h">Introduction</h2>
<p class="ip-lead">Black Swan is Bocconi’s first student society dedicated to prediction markets. With over 60 members across five divisions, we bring together undergraduate and graduate students interested in how markets form expectations—and where those expectations may be wrong.</p>
<p class="ip-p">Our work combines fundamental research, statistical analysis and debate. Members investigate real-world events, develop independent forecasts and compare their conclusions with market prices.</p>
</section>



<section class="ip-sec" id="ip-mission" aria-labelledby="ip-mission-h">
<h2 class="ip-h2" id="ip-mission-h">Our Mission</h2>
<p class="ip-lead">We aim to produce thoughtful, accessible research while helping members develop practical analytical skills and lasting relationships.</p>
<p class="ip-p">Prediction markets give our work a clear focus: what will happen, by when, and with what probability? Answering those questions requires members to weigh evidence, challenge assumptions and explain their reasoning. Reviewing the outcomes then gives them an opportunity to learn from both good judgments and mistakes.</p>
</section>

<section class="ip-sec" id="ip-story" aria-labelledby="ip-story-h">
<h2 class="ip-h2" id="ip-story-h">Our Story</h2>
<p class="ip-lead">Our name takes inspiration from Nassim Nicholas Taleb’s <cite>The Black Swan</cite>, which examines rare, consequential events that fall outside conventional expectations and often seem explainable only afterwards.</p>
<p class="ip-p">For us, the name is a reminder to question certainty, consider overlooked possibilities and recognise the limits of our knowledge. We do not claim that every surprise can be predicted. We believe that thinking carefully about uncertainty leads to better questions and better decisions.</p>
<p class="ip-p">Black Swan grew from a shared interest in exploring these ideas through prediction markets. After gathering student signatures and presenting the society to the university, we established a community where students could research, discuss and test their views together.</p>
</section>

<section class="ip-sec" id="ip-growth" aria-labelledby="ip-growth-h">
<h2 class="ip-h2" id="ip-growth-h">Invested in Your Growth</h2>
<p class="ip-lead">Black Swan gives members the opportunity to develop research they can put their names to and confidently discuss. Working alongside students with different experience and interests helps them strengthen their analysis, communicate clearly and learn from one another.</p>
<p class="ip-p">More experienced members also offer support with CVs, internships and recruiting. Alongside research, professional events and social activities help turn the society into a community.</p>
<p class="ip-p">We are still building Black Swan. Members have the opportunity to propose projects, develop new initiatives and shape what the society becomes.</p>
</section>

</div>
</div>
<script>(()=>{{const r=document.currentScript.closest('.ip');const bs=[...r.querySelectorAll('.ip-toc-b')];const secs=bs.map(b=>r.querySelector('#'+b.dataset.t));
bs.forEach((b,i)=>b.addEventListener('click',()=>{{const y=secs[i].getBoundingClientRect().top+scrollY-(document.getElementById('site-header').offsetHeight+24);scrollTo({{top:y,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'}})}}));
const set=i=>bs.forEach((b,k)=>b.classList.toggle('on',k===i));set(0);
const io=new IntersectionObserver(es=>{{es.forEach(e=>{{if(e.isIntersecting)set(secs.indexOf(e.target))}})}},{{rootMargin:'-35% 0px -55% 0px'}});secs.forEach(s=>io.observe(s));}})();</script>
<script>(()=>{{const g=document.currentScript.closest('.ip').querySelector('.ip-gal');if(!g)return;const t=g.querySelector('.gl-track'),sl=[...t.children],ds=[...g.querySelectorAll('.gl-dot')],ix=g.querySelector('.gl-i');let cur=0;
const go=i=>{{i=(i+sl.length)%sl.length;t.scrollTo({{left:sl[i].offsetLeft-t.offsetLeft,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'}})}};
const upd=()=>{{const x=t.scrollLeft;let b=0,d=1e9;sl.forEach((s,i)=>{{const dd=Math.abs(s.offsetLeft-t.offsetLeft-x);if(dd<d){{d=dd;b=i}}}});cur=b;ds.forEach((d,i)=>d.toggleAttribute('aria-current',i===b));ix.textContent=String(b+1).padStart(2,'0')}};
g.querySelector('.gl-prev').onclick=()=>go(cur-1);g.querySelector('.gl-next').onclick=()=>go(cur+1);ds.forEach((d,i)=>d.onclick=()=>go(i));
let tm;t.addEventListener('scroll',()=>{{clearTimeout(tm);tm=setTimeout(upd,60)}},{{passive:true}});
t.tabIndex=0;t.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'){{e.preventDefault();go(cur+1)}}if(e.key==='ArrowLeft'){{e.preventDefault();go(cur-1)}}}});}})();</script>
</main>'''
