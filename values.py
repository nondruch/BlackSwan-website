"""Our Values page (Who we are → Our values)."""

ICONS = {
  "Initiative": '<path d="M7 17 17 7M9 7h8v8"/>',
  "Community": '<circle cx="9" cy="10" r="4"/><circle cx="15" cy="10" r="4"/><circle cx="12" cy="15" r="4"/>',
  "Integrity": '<path d="M12 4v16M6 8h12M6 8l-3 6a3 3 0 0 0 6 0L6 8Zm12 0-3 6a3 3 0 0 0 6 0l-3-6ZM9 20h6"/>',
  "Growth and Development": '<path d="M4 18 9.5 12.5l3.5 3.5L20 9M15 9h5v5"/>',
}

VALUES = [
  ("Initiative", "Build what isn’t here yet.",
   "We value initiative because Black Swan is new. Founded in 2026, the society has no long-established playbook to follow: its research agenda, events and traditions are being created by the members who step forward and take ownership.",
   "We give members room to pitch projects, propose events and lead new initiatives, and we back good ideas with the time and support needed to make them happen."),
  ("Community", "Better judgments are made together.",
   "We value community because good forecasting is rarely a solo effort. Our best work comes from people who trust each other enough to share unfinished ideas, question each other’s reasoning and change their minds in the open.",
   "We bring members together through joint projects, peer mentorship, professional events and informal gatherings, so that everyone knows the people they work alongside."),
  ("Integrity", "Say what you think, and show how you got there.",
   "We value integrity because a forecast is only useful if it is honest. Overstating confidence, hiding assumptions or explaining away a poor call undermines both the research and the trust placed in it.",
   "We separate evidence from assumption, credit the work of others and review our calls openly, including the ones that went against us."),
  ("Growth and Development", "Leave sharper than you arrived.",
   "We have a strong commitment to growth and development because a student society should leave its members more capable than it found them. Prediction markets provide constant, honest feedback, which makes them an exceptional place to learn.",
   "Experienced members mentor newer ones, feedback is specific and constructive, and members publish research under their own names, building a body of work that shows their progress."),
]

DIVERSITY = [
    "Black Swan believes diversity of thought is essential to sound research and well-functioning prediction markets. The wisdom of a crowd depends on the independence of its judgments: when participants rely on the same sources, assumptions and methods, their agreement can reinforce a shared bias rather than reflect stronger evidence.",
    "We therefore seek students who approach questions differently, bring unfamiliar perspectives and are willing to challenge the prevailing view—including our own. Across Bocconi’s undergraduate and graduate community, we welcome members of all backgrounds and levels of experience.",
    "Through collaborative research, peer mentorship and open debate, we aim to give every member the confidence and opportunity to contribute an independent voice.",
]


import pathlib as _pl
COMPASS = (_pl.Path(__file__).parent / "compass.svg").read_text()


def page():
    cards = "".join(
        f'<article class="vl-card"><span class="vl-wm" aria-hidden="true">{k+1:02d}</span>'
        f'<div class="vl-head"><span class="vl-ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">{ICONS[t]}</svg></span>'
        f'<div><h3 class="vl-t">{t}</h3><p class="vl-s">{m}</p></div></div>'
        f'<div class="vl-parts"><div><p class="vl-p">{why} {com}</p></div></div></article>'
        for k, (t, m, why, com) in enumerate(VALUES))
    import base64, pathlib
    order = ["marco-similea","leo-scully","horia-timofti","mohammed-el-zein","carlo-giolla","niklas-ondruch","loyd-hegarty","harry-downey",
             "can-deniz","hrishikesh-subhash","maria-mateescu","sofia-damean","matteo-mascaretti","james-moser","adrian-tsonev"]
    tiles = "".join(f'<span class="vl-mt ph-{n}"></span>' for n in order)
    photo = (f'<figure class="vl-photo" aria-label="Members of the Black Swan board"><div class="vl-mosaic" aria-hidden="true">{tiles}</div>'
             f'<figcaption class="vl-cap"><span class="vl-cap-k">The board</span><span class="vl-cap-t">The people who hold us to these values every day.</span>'
             f'<a class="vl-cap-a" href="#our-team">Meet the team <span aria-hidden="true">→</span></a></figcaption></figure>')
    chips = "".join(f'<li>{t}</li>' for t, *_ in VALUES)
    div = "".join(f'<p class="{"vl-dlead" if i == 0 else "vl-dp"}">{t}</p>' for i, t in enumerate(DIVERSITY))
    return f'''<main class="flex-1 ip vl" data-view="our-values" hidden tabindex="-1">
<header class="vl-hero vl-hero-gl"><div class="vl-gl-bg" aria-hidden="true"></div><p class="ph-credit">Photo: Darryl Low / Unsplash</p><div class="tm-wrap mx-auto w-full px-gutter vl-gl-in">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><span>Who we are</span><span aria-hidden="true">/</span><span aria-current="page">Our values</span></nav>
<div class="vl-gl-c">
<p class="vl-eyebrow">Who we are</p>
<h1 class="vl-h1">Our values</h1>
<p class="vl-intro">The principles behind how we research, debate and build the society together.</p>
<p class="vl-list"><b>Initiative</b><span aria-hidden="true">|</span><b>Community</b><span aria-hidden="true">|</span><b>Integrity</b><span aria-hidden="true">|</span><b>Growth and Development</b></p>
</div>
</div></header>

<div class="tm-wrap mx-auto w-full px-gutter vl-body">
<section aria-label="Our values"><div class="vl-grid">{cards}</div></section>

</div>
<section class="vl-dband" aria-labelledby="vl-div-h"><div class="tm-wrap mx-auto w-full px-gutter">
<div class="vl-dmark" aria-hidden="true"><span></span><em>Diversity</em><span></span></div>
<div class="vl-div">
<div class="vl-div-l"><p class="vl-k">Diversity</p><h2 class="vl-dh" id="vl-div-h">Independent views make better forecasts.</h2></div>
<div class="vl-div-r">{div}</div>
</div>
</div></section>
</main>'''
