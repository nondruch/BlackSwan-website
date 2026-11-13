"""Apply page (Student opportunities → Apply)."""
import base64, pathlib
D = pathlib.Path(__file__).parent
LOGO = "data:image/webp;base64," + base64.b64encode((D / "logo-hero.webp").read_bytes()).decode()
EMAIL = "as.blackswan@unibocconi.it"
IG = "https://www.instagram.com/blackswanstudentsociety/"

LOOK = [
  ("Curiosity", "A genuine interest in markets, current events and how uncertain outcomes are priced. You follow a story beyond the headline and want to know why the market sees it the way it does."),
  ("Analytical rigour", "The ability to work carefully with evidence, whether through financial statements, data, models or close reading of policy and rules. Quantitative and qualitative approaches are equally valued."),
  ("Independent judgment", "The confidence to form your own view, express it as a probability and defend it, together with the openness to change your mind when the evidence does."),
  ("Initiative", "Black Swan is still being built. We look for people who will contribute ideas, take ownership of projects and help shape what the society becomes."),
]

DIVS = [
  ("business-and-finance", "Business & Finance", "Investment research", "Earnings, industry rankings and M&A."),
  ("economics-and-politics", "Economics & Politics", "Investment research", "Central banks, macro data, elections and policy."),
  ("cross-domain", "Cross-Domain", "Investment research", "Crypto, weather, appearances and mentions."),
  ("market-studies", "Market Studies", "Markets & models", "How prediction markets behave once they close."),
  ("algorithmic-development", "Algorithmic Development", "Markets & models", "Statistical models, backtesting and systematic strategies."),
]

STEPS = [
  ("Apply online", "Complete a short form with your CV and your first and second division preferences."),
  ("Interview", "Shortlisted candidates meet the heads of their preferred division to discuss their interests and how they approach a question."),
  ("Offer", "Successful candidates receive an offer and join their division at the start of the following term."),
]

OFFER = [
  ("Research under your name", "Develop and publish work you can put your name to and confidently discuss."),
  ("Career support", "Experienced members offer guidance on CVs, internships and recruiting."),
  ("A community", "Professional events, speakers and social activities alongside the research."),
]

FAQ = [
  ("Who can apply?", "Black Swan is open to undergraduate and graduate students at Bocconi University, from any degree programme and year of study."),
  ("Do I need experience with prediction markets?", "No. We value curiosity, rigour and independent thinking over prior experience. Members learn the mechanics of prediction markets through their division’s work."),
  ("Can I apply to more than one division?", "You indicate a first and second preference on the application form. Where possible, we place candidates in their first choice."),
  ("When does the next round open?", "The next application round opens in January. It will be announced on this page and on our Instagram."),
  ("Who can I contact with questions?", f"Write to us at {EMAIL} and a member of the board will get back to you."),
]


def page():
    faq = "".join(f'<details class="ap-q"><summary>{q}<span class="plus" aria-hidden="true"></span></summary><p>{a}</p></details>' for q, a in FAQ)
    divs = ", ".join(n for _, n, _, _ in DIVS[:-1]) + " and " + DIVS[-1][1]
    return f'''<main class="flex-1 ap" data-view="how-to-apply" hidden tabindex="-1">
<header class="ap-hero"><div class="tm-wrap mx-auto w-full px-gutter ap-hin">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><span>Student opportunities</span><span aria-hidden="true">/</span><span aria-current="page">Apply</span></nav>
<h1 class="ap-h1">Join Black Swan</h1>
<p class="ap-lead">Research real-world events, form independent views and test them against the market.</p>
</div></header>

<div class="tm-wrap mx-auto w-full px-gutter ap-body">
<div class="ap-closed" role="status"><div><h2>Applications closed</h2><p>The next round opens in January.</p></div><a class="ap-cbtn" href="{IG}" target="_blank" rel="noopener">Follow for updates</a></div>

<section class="ap-row" aria-labelledby="ap-about-h">
<div class="ap-rh"><h2 id="ap-about-h">Black Swan Student Society</h2></div>
<div class="ap-rb">
<p class="ap-intro">Black Swan is promoted and run by students of Bocconi University. Founded in 2026, it is Bocconi’s first student society dedicated to prediction markets.</p>
<div class="ap-nums">
<div class="ap-num"><span class="ap-big" aria-hidden="true">5</span><h3>Divisions</h3><p>{divs.replace("&", "&amp;").replace("Cross-Domain", "Cross&#8209;Domain")}, each producing research on a distinct set of markets.</p></div>
<div class="ap-num"><span class="ap-big" aria-hidden="true">60+</span><h3>Members</h3><p>A board of 16 and 49 analysts, drawn from undergraduate and graduate programmes across the university.</p></div>
</div>
</div>
</section>

<section class="ap-row" aria-labelledby="ap-faq-h">
<div class="ap-rh"><h2 id="ap-faq-h">Frequently asked questions</h2><p class="ap-contact">Other questions? Write to <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div class="ap-rb"><div class="ap-faq">{faq}</div></div>
</section>
</div>
</main>'''
