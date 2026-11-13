"""Events page (Student opportunities → Events)."""
IG = "https://www.instagram.com/blackswanstudentsociety/"

INTRO = [
  "Black Swan’s events bring members together to exchange ideas, develop practical skills and explore how research informs decisions beyond the classroom. Through conversations with industry professionals, practical workshops and research presentations, we connect our interests in prediction markets, finance, economics and technology with the experience of people working in these fields.",
  "Alongside professional development, our events create space for members to get to know one another. Informal discussions, recruiting sessions and social gatherings help students share advice, build friendships and find collaborators across divisions.",
]

# (date line, type, title, description, location, has_photo_placeholder)
PAST = [
  ("Autumn 2026", "Social", "Joining Aperitivo", "An aperitivo welcoming new members to Black Swan, bringing together the board and analysts from all five divisions.", "Milan", True),
  ("Autumn 2026", "Recruiting", "Associations on Display", "Black Swan’s stand at Bocconi’s Associations on Display, where students met members of the board and learned about the society and its divisions.", "Bocconi University", True),
]

PH_ICON = '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1.5"/><circle cx="9" cy="10" r="1.6"/><path d="M21 16l-5.5-5.5L6 19"/></svg>'


def page():
    intro = "".join(f"<p>{p}</p>" for p in INTRO)
    past = ""
    for d, t, title, desc, loc, ph in PAST:
        fig = f'<figure class="ev-ph" aria-label="Photo placeholder">{PH_ICON}<figcaption>Photo</figcaption></figure>' if ph else ""
        past += f'''<article class="ev-item">{fig}<div class="ev-txt"><p class="ev-meta"><span>{d}</span><span class="ev-dot" aria-hidden="true"></span><span>{t}</span></p><h3>{title}</h3><p class="ev-desc">{desc}</p><p class="ev-loc">{loc}</p></div></article>'''
    return f'''<main class="flex-1 ap ev" data-view="events" hidden tabindex="-1">
<header class="ap-hero"><div class="tm-wrap mx-auto w-full px-gutter">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><span>Student opportunities</span><span aria-hidden="true">/</span><span aria-current="page">Events</span></nav>
<h1 class="ap-h1">Events</h1>
<p class="ap-lead">Talks, workshops, and gatherings for members of Black Swan.</p>
</div></header>

<div class="tm-wrap mx-auto w-full px-gutter ev-body">
<section class="ev-intro" aria-labelledby="ev-intro-h">
<h2 id="ev-intro-h">Black Swan Events</h2>
<div class="ev-intro-p">{intro}</div>
</section>

<section class="ev-sec" aria-labelledby="ev-up-h">
<h2 class="ap-rule" id="ev-up-h">Upcoming events</h2>
<div class="ev-empty"><p><b>No upcoming events are scheduled at the moment.</b> New events are announced here and on our Instagram.</p><a class="ap-link" href="{IG}" target="_blank" rel="noopener">Follow for updates →</a></div>
</section>

<section class="ev-sec" aria-labelledby="ev-past-h">
<h2 class="ap-rule" id="ev-past-h">Past events</h2>
<div class="ev-list">{past}</div>
</section>
</div>
</main>'''
