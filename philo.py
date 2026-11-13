"""Philosophy and Process page (Who we are → Philosophy and process). Same template as the Introduction page."""
import pathlib, re
D = pathlib.Path(__file__).parent
_SCRIPT = re.search(r"<script>.*?</script>", (D / "introp.py").read_text(), re.S).group(0).replace("{{", "{").replace("}}", "}")

SECTIONS = [("ps-philosophy", "Philosophy"), ("ps-process", "Process"), ("ps-rnd", "Research and Development")]

PROCESS = [
    "Working with their division heads, members develop projects suited to their interests and expertise. Teams combine undergraduate and graduate students from different academic backgrounds, bringing together subject knowledge, analytical skills and varied perspectives.",
    "Each project begins with a precise research question and an appropriate analytical framework. For event research, this means defining the outcome, deadline and contractual resolution criteria. For market studies and algorithm development, it means establishing a testable hypothesis, identifying suitable data and specifying how results will be evaluated.",
    "Teams then investigate the drivers of the outcome or behaviour under study. Methods may include primary-source research, economic and financial modelling, historical comparisons, statistical inference and backtesting. The choice of method follows the question, with assumptions and limitations made explicit.",
    "Findings are subjected to scenario analysis, sensitivity testing and critical review. Members consider competing explanations, assess the reliability of their evidence and examine whether conclusions remain credible under alternative assumptions. Where research informs a trading strategy, the analysis also accounts for execution costs, liquidity and the risk of overfitting historical data.",
    "Projects culminate in reports, presentations or research tools that make the evidence, methodology and conclusions open to scrutiny. Teams monitor subsequent developments and revisit their findings to improve both their judgments and their methods.",
]


def page():
    toc = "".join(f'<li><button type="button" class="ip-toc-b" data-t="{i}">{t}</button></li>' for i, t in SECTIONS)
    steps = "".join(f'<li><span class="ps-n" aria-hidden="true">{k+1:02d}</span><p>{t}</p></li>' for k, t in enumerate(PROCESS))
    return f'''<main class="flex-1 ip" data-view="philosophy-and-process" hidden tabindex="-1">
<header class="ip-hero ip-hero-ph ip-hero-sp"><div class="ip-hbg" aria-hidden="true"></div><p class="ph-credit">Bocconi University, Milan · Photo: Mattia Spotti / Unsplash</p><div class="tm-wrap mx-auto w-full px-gutter ip-hin">
<nav class="tm-crumbs" aria-label="Breadcrumb"><a href="#top">Home</a><span aria-hidden="true">/</span><span>Who we are</span><span aria-hidden="true">/</span><span aria-current="page">Philosophy and process</span></nav>
<div class="ip-hero-grid"><p class="tm-eyebrow">Who we are</p><h1 class="ip-h1">Philosophy and process</h1></div>
</div></header>

<div class="tm-wrap mx-auto w-full px-gutter ip-body">
<aside class="ip-toc" aria-label="On this page"><p class="ip-toc-h">On this page</p><ol>{toc}</ol></aside>
<div class="ip-content">

<section class="ip-sec" id="ps-philosophy" aria-labelledby="ps-philosophy-h">
<h2 class="ip-h2" id="ps-philosophy-h">Philosophy</h2>
<p class="ip-lead">Black Swan combines fundamental research, quantitative analysis and independent judgment to explore prediction markets. Across our five divisions, we investigate real-world events, study how markets form expectations and develop methods for identifying where prices may be wrong.</p>
<p class="ip-p">Our approach rests on independent judgment and intellectual rigour. Before challenging a market price or proposing an explanation, members establish the strongest alternative interpretation. Conclusions must follow from evidence, with a clear distinction between observed facts, modelling assumptions and forecasts.</p>
<p class="ip-p">We recognise that uncertainty cannot be eliminated. Our objective is to assess it carefully, communicate it clearly and revise our conclusions when the evidence changes. We evaluate research through the quality and consistency of its reasoning, recognising that individual outcomes do not necessarily validate or invalidate the underlying approach.</p>
</section>

<section class="ip-sec" id="ps-process" aria-labelledby="ps-process-h">
<h2 class="ip-h2" id="ps-process-h">Process</h2>
<ol class="ps-steps">{steps}</ol>
</section>

<section class="ip-sec" id="ps-rnd" aria-labelledby="ps-rnd-h">
<h2 class="ip-h2" id="ps-rnd-h">Research and Development</h2>
<p class="ip-lead">Our five divisions provide complementary approaches to prediction markets. Economics &amp; Politics, Business &amp; Finance and Cross-Domain develop research on events within their respective fields. Market Studies examines price formation, information processing and market behaviour, while Algorithm Development builds and evaluates statistical models and systematic strategies.</p>
<p class="ip-p">Collaboration between divisions connects detailed subject knowledge with broader empirical analysis. Event research can generate hypotheses for testing across markets, while quantitative findings can reveal patterns that warrant deeper investigation.</p>
<p class="ip-p">Through collaborative projects, structured feedback and published research, members develop practical capabilities in analysis, modelling, programming and communication. We aim to produce work that contributes to a better understanding of prediction markets while giving members a rigorous foundation for further study and professional practice.</p>
</section>

</div>
</div>
{_SCRIPT}
</main>'''
