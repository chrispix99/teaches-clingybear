#!/usr/bin/env python3
"""Build the teaches.clingybear.com static site: 15 pages with full SEO."""
import json, os, html

BASE = "https://teaches.clingybear.com"
SITE = os.path.dirname(os.path.abspath(__file__))
GA4 = "G-S5WCYTCSVP"
BIO = "Learn to get the most out of your AI assistant \U0001F428 Real workflows. Zero fluff. Lessons dropping soon."
YT = "https://www.youtube.com/@ClingyBearTeaches"
IG = "https://www.instagram.com/clingybearteaches/"
TH = "https://www.threads.com/@clingybearteaches"
TT = "https://www.tiktok.com/@clingybearteaches"
KOALA_ABS = BASE + "/assets/koala.png"

HEAD = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Clingy Bear Teaches">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{koala}">
<meta property="og:image:alt" content="Clingy Bear, the pink koala mascot of Clingy Bear Teaches">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="{koala}">
<link rel="icon" type="image/png" href="/assets/koala.png">
<link rel="apple-touch-icon" href="/assets/koala.png">
<link rel="stylesheet" href="/assets/site.css">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={ga}"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{ga}');
</script>
{jsonld}"""

NAV = """<nav class="topnav" aria-label="Primary">
<a class="brand" href="/"><img src="/assets/koala.png" alt="Clingy Bear logo" width="36" height="36"><span>Clingy Bear Teaches</span></a>
<div class="links">
<a href="/">Home</a>
<a href="/brave/">BRAVE</a>
<a href="/season-1/">Season 1</a>
<a class="yt" href="{yt}">▶ YouTube</a>
</div>
</nav>"""

FOOTER = """<footer>
<nav class="socials" aria-label="Social links">
<a href="{yt}">📺 YouTube</a>
<a href="{ig}">📸 Instagram</a>
<a href="{th}">🧵 Threads</a>
<a href="{tt}">🎵 TikTok</a>
</nav>
<p>Clingy Bear Teaches · <a href="{yt}">youtube.com/@ClingyBearTeaches</a></p>
<p>A Clingy Bear Production</p>
</footer>""".format(yt=YT, ig=IG, th=TH, tt=TT)

def crumbs(*items):
    """items: list of (label, url_or_None)."""
    lis = []
    for label, url in items:
        if url:
            lis.append(f'<li><a href="{url}">{label}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{label}</li>')
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(lis) + "</ol></nav>"

def page(filename, *, title, desc, keywords, canonical, og_title, og_desc,
         body_html, jsonld):
    head = HEAD.format(title=html.escape(title), desc=html.escape(desc),
                       keywords=html.escape(keywords), canonical=canonical,
                       og_title=html.escape(og_title), og_desc=html.escape(og_desc),
                       koala=KOALA_ABS, ga=GA4, jsonld=jsonld)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head}
</head>
<body>
{NAV.format(yt=YT)}
<main class="wrap">
{body_html}
</main>
{FOOTER}
</body>
</html>
"""
    path = os.path.join(SITE, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", filename, f"{len(doc)//1024}KB")

ORG = {"@type": "Organization", "name": "Clingy Bear Teaches",
       "url": BASE + "/", "logo": KOALA_ABS,
       "sameAs": [YT, IG, TH, TT]}

# ---------------------------------------------------------------- episodes
EPISODES = [
 (1, "stop-chatting-start-collaborating", "Stop Chatting. Start Collaborating.",
  "The BRAVE method through seven real projects.",
  "The channel's promise in one lesson. Software engineer Chris Pick introduces the BRAVE method through seven real projects — mining-claim research, text-message patterns, airline points, vineyard media production, music albums, shipped apps, and business operations — and shows how a vague request becomes a brief an agent can actually run with. It ends with the two questions to always answer: what does done look like, and what evidence would make you trust it?",
  ["Seven real project families: mining claims, text analysis, travel hacking, vineyard media, music albums, shipped apps, and business ops",
   '"Tell me about abandoned mines" vs. a BRAVE brief that ranks Washington land by distance from Spokane and separates patented claims from public-land records',
   '"Make me an app" becomes a product brief: audience, workflow, data, constraints, deployment target, analytics, and definition of done',
   "What an agent can do (research, build files, take approved actions) — and where explicit authorization is required",
   "The two questions to always answer: what does done look like, and what evidence would make you trust it?"]),
 (2, "give-your-ai-the-map", "Give Your AI the Map",
  "Context and continuity through the mining-claim story.",
  "Context is decision-changing information, not an autobiography. This lesson builds a one-page project map — objective, known facts, vocabulary, source hierarchy, constraints, completed work, unresolved questions, and next action — and follows the mining-claim story across sessions, showing why precise terms and durable facts matter.",
  ["Build a one-page project map: objective, facts, vocabulary, sources, constraints, completed work, open questions, next action",
   "Precise terms matter: patented claim, unpatented claim, fee land, placer claim, hard-rock mine, parcel, and BLM record are not interchangeable",
   "Continuity: research the record, later amend criteria, then plan a prospecting trip without re-teaching the whole project",
   "Correct a durable fact once — and make the correction explicit",
   "Memory vs. proof: remembered context accelerates work, but legal, travel, price, and availability facts still need fresh verification"]),
 (3, "receipts-or-it-didnt-happen", "Receipts or It Didn't Happen",
  "Evidence-first BLM, land, and genealogy research.",
  "Evidence-first research, applied to BLM land records and genealogy. Learn the source ladder — primary record, authoritative database, reputable secondary source, community lead, unsourced claim — and the discipline of asking the assistant to quote the line, keep the source link, and explain any contradiction.",
  ["The source ladder: primary record, authoritative database, reputable secondary source, community lead, unsourced claim",
   "Turn a broad land hunt into a research table: candidate, location, distance, ownership type, mine evidence, source, uncertainty, next verification",
   "Genealogy: a proven marriage certificate is not an inferred family-tree link",
   "Negative-claim discipline: 'I did not find it in the sources checked' is different from 'it does not exist'",
   "Keep a correction log — when new evidence reverses a conclusion, update the record and say what changed"]),
 (4, "what-the-texts-actually-say", "What the Texts Actually Say",
  "Privacy-safe SMS sentiment analysis over time.",
  "A privacy-first way to analyze your own message history. Consent and scope come first: analyze messages you lawfully control, redact names, phone numbers, intimate content, and third-party details before teaching anything on screen. Then build the schema, clean the archive, and measure only what is observable.",
  ["Establish consent and scope; redact names, phone numbers, intimate content, and third-party details before teaching on screen",
   "Define the schema: timestamp, contact, direction, text, medium, thread — direction is a hard data field, not a guess",
   "Clean the archive: normalize dates, keep empty media messages as events, remove duplicates carefully, never alter original text",
   "Measure the observable: reply latency, initiation balance, question rate, future-planning language, warmth and conflict markers, gaps",
   "Separate measurement from interpretation — 'response time increased' is an observation, 'they no longer care' is an unsupported inference",
   "Ask for counterexamples and uncertainty; close with human judgment — the analysis reveals patterns, it cannot diagnose a person"]),
 (5, "make-the-miles-work-harder", "Make the Miles Work Harder",
  "Travel constraints, points, routes, and verification.",
  "Points and miles are an optimization problem — and the assistant can't solve it without your real constraints. Build the travel brief, define the objective function (cheapest cash, fewest points, best cents per point, best elite-qualifying return, and lowest disruption risk are different winners), and verify at decision time.",
  ["Build the travel brief: traveler, dates, origin and destination, time windows, bags, status, points balances, flexibility, deal-breakers",
   "Define the objective function — different winners for cheapest cash, fewest points, cents per point, elite-qualifying return, disruption risk",
   "Cash-versus-points math without worshiping a single valuation: cash saved, taxes, cancellation terms, opportunity cost",
   "Separate planning from live booking: strategy can be explored broadly, but fares and award inventory must be checked at decision time",
   "Account for the whole trip: positioning flights, hotel, ground transport, lounges, baggage, missed-connection risk",
   "Run a final verification checklist before purchasing"]),
 (6, "turn-a-footage-pile-into-a-production-system", "Turn a Footage Pile into a Production System",
  "The AI Vineyard media workflow.",
  "How a pile of raw camera files becomes a production system, using the AI Vineyard footage workflow. Start with the media inventory — not the timeline — then turn raw footage into searchable story beats, build an edit brief, run real editorial correction cycles, and reconcile the catalog after production.",
  ["Start with the media inventory: file identity, date, camera, metadata, transcript, description, tags, proxy, master location, status",
   "Why filenames and pairing rules matter — one 360-degree clip can have multiple master files",
   "Turn raw footage into searchable story beats: planting, irrigation, equipment, mistakes, wildlife, progress, payoff",
   "Build an edit brief: audience promise, narrative spine, target duration, must-use moments, 'never do this' rules",
   "Editorial correction cycles: trim clapboards, remove dead air, cover narration with B-roll, fix jump cuts, orient graphics",
   "Render a short preview before committing to an expensive full-resolution master; repurpose deliberately"]),
 (7, "from-song-idea-to-six-album-slate", "From Song Idea to Six-Album Slate",
  "Creative direction, generation, selection, and release.",
  "From one song idea to a multi-album slate. Define the creative system before generating anything — album concept, subject map, constraints, voice, release structure — then write tight track briefs, batch with discipline, and let human taste choose the canonical versions.",
  ["Define the creative system before generating: album concept, track count, subject map, musical constraints, voice, tone shifts, release structure",
   "Write track briefs that are specific without scripting the music to death: subject, emotional arc, lyrical anchors, prohibited clichés, energy target",
   "Batch carefully: generate enough variation to choose from, but respect plan credits, time, and the human review bottleneck",
   "Preserve taste as a human decision — Chris's hearts, not an AI score, choose the canonical versions",
   "Track variants, durations, lyrics, credits, cover assets, and publication state in one catalog",
   "Correction loop: fix a factual lyric, regenerate only what changed, and don't disturb approved tracks",
   "Publish album by album, verify playback and metadata, update the public catalog"]),
 (8, "build-the-tool-you-wish-existed", "Build the Tool You Wish Existed",
  "Ground School Trainer and NeuroSpicy.",
  "Turn an itch into a shipped app, through two real builds: the Ground School Trainer and NeuroSpicy. Start with the user and the moment of use — not the tech stack — define the smallest complete loop, write testable acceptance criteria, and keep every stage observable.",
  ["Start with the user and the moment of use, not the tech stack",
   "Define the smallest complete loop — Ground School: sign in, practice, feedback, progress. NeuroSpicy: answer, understand, reflect, revisit",
   "Write acceptance criteria that can be tested: progress belongs to the right user, a question scores correctly, a result reads well on mobile",
   "Decide what data is sensitive and what should never become public analytics",
   "Scaffold, implement, test, deploy, verify — make each stage observable",
   "Keep a correction loop: reproduce the issue, change the smallest surface, rerun tests, verify the live page",
   "What 'shipped' means: public URL, correct auth, real data behavior, mobile check, analytics, and a rollback path"]),
 (9, "ship-a-real-data-product", "Ship a Real Data Product",
  "VMenu's research, imports, audits, and deployment.",
  "The unglamorous engine behind real data products, through VMenu. Define the data contract before collecting anything, separate collection from normalization from deduplication from import from audit, and verify everything from the user's side.",
  ["Define the data contract before collecting data: identity, address, sections, items, prices, sources, update status, timestamps",
   "Separate collection, normalization, deduplication, import, and audit into distinct stages",
   "Idempotency: rerunning the same batch should reconcile, not duplicate or erase fields",
   "Why partial updates are dangerous when an endpoint replaces a full record",
   "Build quality reports: missing data, suspiciously thin records, duplicates, closed businesses",
   "Treat timeouts as unknown outcomes — reconcile counts before retrying",
   "Deploy with correct authorship, environment variables, and production checks",
   "Verify from the user's side: search, inspect, test mobile, confirm analytics"]),
 (10, "give-the-business-its-own-brain", "Give the Business Its Own Brain",
  "24 Legs, maximusPoints, and operations.",
  "Give a small business an operating memory, through 24 Legs and maximusPoints. Build an operating map — products, owners, customers, revenue model, systems, decisions, commitments, risks — separate draft operations from financial authority, and track every 'waiting for' so nothing disappears between bursts of attention.",
  ["Create an operating map: products, owners, customers, revenue model, systems, current decisions, commitments, risks",
   "24 Legs product ops: inventory, revision status, print requirements, play-test feedback, launch gates",
   "maximusPoints consumer-data product: benefits catalog, account connection boundaries, recurring refresh, trust",
   "Separate draft operations from financial authority — preparing an invoice is not sending one",
   "Build a weekly review that surfaces only decisions, blockers, deadlines, and anomalies",
   "Track 'waiting for' items; close resolved commitments and record the result, not just the plan"]),
 (11, "run-several-projects-without-losing-the-plot", "Run Several Projects Without Losing the Plot",
  "Delegation, durable memory, and background work.",
  "How to run several projects at once without losing the plot. Classify work — immediate conversation, delegated research, build task, monitored event, scheduled recurrence — give every track a concrete deliverable with a return condition, parallelize what's independent, and keep project records so every run resumes where it left off.",
  ["Classify work: immediate conversation, delegated research, build task, monitored event, scheduled recurrence",
   "Give every track a concrete deliverable, boundary, evidence requirement, and return condition",
   "Parallelize independent work; sequence tasks that share data, credentials, or judgment gates",
   "Use one successful pilot before launching a large batch",
   "Preserve state in a project record: last completed step, artifact location, unresolved issue, next action",
   "Distinguish 'started' from 'finished' — queued, running, and deployed are not the same as verified",
   "Surface failures immediately with the consequence and the safest next move",
   "Avoid notification sludge: notify on completions, blockers, genuine risk, or decisions — not every heartbeat"]),
 (12, "trust-but-verify-and-ship", "Trust, but Verify — and Ship",
  "Permissions, privacy, failure recovery, and the capstone.",
  "The capstone. Review the trust stack — scope, source, permission, preview, approval, verification, rollback — learn the 'show me' habit for everything the assistant claims, build a preflight for private data and a protocol for failure, and finish with a human approval gate and a visible verification pass.",
  ["The trust stack: scope, source, permission, preview, approval, verification, rollback",
   "Reversible vs. consequential: researching and drafting are not sending, publishing, purchasing, or deleting",
   "The 'show me' habit: source excerpt, data count, diff, test result, rendered page, or live URL",
   "Preflight for private data: minimize, redact, anonymize — never use another person's information in public demos",
   "Failure protocol: stop, state what failed, preserve completed work, explain the consequence, do not invent success",
   "A cross-project bug reel: direction mixups, terminology slips, stale travel data, broken renders, lost records",
   "Capstone: ship with a human approval gate and a visible verification pass"]),
]

EP_KW = "Clingy Bear Teaches, AI assistant course, BRAVE method, AI workflows, Chris Pick"

# ---------------------------------------------------------------- home
home_jsonld = json.dumps({
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "WebSite", "name": "Clingy Bear Teaches", "url": BASE + "/",
     "description": BIO,
     "publisher": ORG},
    ORG
  ]}, indent=2)
home_jsonld = f'<script type="application/ld+json">\n{home_jsonld}\n</script>'

ep_cards = "\n".join(
  f'<article class="card"><div class="n">EPISODE {n}</div><h3><a href="/season-1/ep-{n}-{slug}/">{html.escape(title)}</a></h3><p>{html.escape(tag)}</p></article>'
  for n, slug, title, tag, _, _ in EPISODES)

home_body = f"""
<header class="hero">
<img class="koala" src="/assets/koala.png" alt="Clingy Bear, the pink koala mascot of Clingy Bear Teaches" width="360" height="360">
<p class="kicker">A YouTube class by Chris Pick</p>
<h1>Clingy Bear Teaches</h1>
<p class="tagline">Real projects. Better AI. No prompt theater.</p>
<p class="bio">{html.escape(BIO)}</p>
<a class="cta" href="{YT}">▶ Watch on YouTube</a>
</header>

<section>
<h2>What is BRAVE?</h2>
<p class="sub">BRAVE is the signature method behind every lesson — five habits that turn an AI assistant from a chat window into a capable collaborator. <a href="/brave/">Read the full breakdown →</a></p>
<div class="grid brave">
<div class="card"><span class="letter" aria-hidden="true">B</span><h3>Brief the outcome</h3><p>Say what finished looks like, who it is for, and the format you need.</p></div>
<div class="card"><span class="letter" aria-hidden="true">R</span><h3>Reveal relevant context</h3><p>Supply the facts, constraints, prior decisions, examples, and source material that change the answer.</p></div>
<div class="card"><span class="letter" aria-hidden="true">A</span><h3>Authorize the next action</h3><p>Distinguish research from sending, drafting from publishing, and reversible work from consequential work.</p></div>
<div class="card"><span class="letter" aria-hidden="true">V</span><h3>Verify the evidence</h3><p>Ask for source links, read primary records, inspect rendered files, test deployments, and reconcile counts.</p></div>
<div class="card"><span class="letter" aria-hidden="true">E</span><h3>Evolve the system</h3><p>Preserve useful decisions, templates, and lessons so the next run starts smarter.</p></div>
</div>
</section>

<section>
<div class="spotlight">
<div class="ep">Episode 1</div>
<h3>Stop Chatting. Start Collaborating.</h3>
<p>The channel's promise in one lesson: the BRAVE method shown through seven real projects — mining-claim research, text-message patterns, airline points, vineyard media production, music albums, shipped apps, and business operations. Software engineer Chris Pick shows how a vague request becomes a brief, how an agent researches and builds, and the two questions to always answer: <em>what does done look like, and what evidence would make you trust it?</em></p>
<p><a class="cta" href="/season-1/ep-1-stop-chatting-start-collaborating/">Episode 1 guide →</a></p>
</div>
</section>

<section>
<h2>Season 1 — 12 lessons</h2>
<p class="sub">Every episode is anchored in work Chris has actually done with Clingy Bear — a practical capability ladder from first brief to capstone ship. <a href="/season-1/">Browse all episodes →</a></p>
<div class="grid eps">
{ep_cards}
</div>
</section>

<section>
<h2>Follow along</h2>
<p class="sub">Lessons land on YouTube first, with clips and updates across the other channels.</p>
</section>"""

page("index.html",
     title="Clingy Bear Teaches — Real projects. Better AI. No prompt theater.",
     desc="Learn to get the most out of your AI assistant. Real workflows. Zero fluff. Clingy Bear Teaches is software engineer Chris Pick's practical class in turning an AI assistant into a capable collaborator.",
     keywords="Clingy Bear Teaches, AI assistant course, learn AI, BRAVE method, AI workflows, Chris Pick",
     canonical=BASE + "/",
     og_title="Clingy Bear Teaches — Real projects. Better AI. No prompt theater.",
     og_desc=BIO,
     body_html=home_body, jsonld=home_jsonld)

# ---------------------------------------------------------------- brave
brave_jsonld = json.dumps({
  "@context": "https://schema.org", "@type": "Article",
  "headline": "The BRAVE Method — Clingy Bear Teaches",
  "description": "BRAVE is the signature method behind Clingy Bear Teaches: five habits that turn an AI assistant from a chat window into a capable collaborator.",
  "author": {"@type": "Person", "name": "Chris Pick"},
  "publisher": ORG, "mainEntityOfPage": BASE + "/brave/"}, indent=2)
brave_jsonld = f'<script type="application/ld+json">\n{brave_jsonld}\n</script>'

pillars = [
 ("B", "Brief the outcome", "Say what finished looks like, who it is for, and the format you need.",
  "Most bad AI output starts with a bad ask. A brief names the finish line: the audience, the shape of the result, and the format it must arrive in. Compare “tell me about abandoned mines” with “find Washington land containing abandoned hard-rock workings, rank candidates by distance from Spokane, and separate patented claims from public-land records.” The second one is workable; the first one is a slot machine.",
  "Why it prevents failure: vague prompts get vague answers. A brief turns guessing into execution."),
 ("R", "Reveal relevant context", "Supply the facts, constraints, prior decisions, examples, and source material that change the answer.",
  "Context is decision-changing information, not an autobiography. Give the assistant the facts, constraints, vocabulary, and source hierarchy that alter the result — and keep it durable: one correction, stored once, made explicit, so you never re-teach the whole project. Precise terms matter: a patented claim, an unpatented claim, and fee land are not interchangeable.",
  "Why it prevents failure: the assistant can't know what you never said. Missing context becomes confident invention."),
 ("A", "Authorize the next action", "Distinguish research from sending, drafting from publishing, and reversible work from consequential work.",
  "An agent can research, build files, and sometimes take approved actions — but access varies, and consequential steps need explicit authorization. Research is not sending. A draft is not published. A local build is not a deployment. BRAVE keeps the boundary sharp: say which actions are approved before anything irreversible happens.",
  "Why it prevents failure: the worst AI mistakes are actions nobody authorized. Permission is a workflow step, not an afterthought."),
 ("V", "Verify the evidence", "Ask for source links, read primary records, inspect rendered files, test deployments, and reconcile counts.",
  "Receipts or it didn't happen. Ask for the source link and read it. Quote the relevant line. Check the primary record, inspect the rendered file, test the deployment, reconcile the counts. Remembered facts accelerate work, but legal, travel, price, and availability facts must be checked fresh — and negative claims get discipline: “I didn't find it in the sources checked” is different from “it doesn't exist.”",
  "Why it prevents failure: unverified output is a draft wearing a suit. Evidence is what makes it trustworthy."),
 ("E", "Evolve the system", "Preserve useful decisions, templates, and lessons so the next run starts smarter.",
  "Every run should make the next run cheaper. Keep the decisions, templates, checklists, and corrections that proved useful — a project record with the last completed step, artifact locations, open issues, and the next action. When new evidence reverses a conclusion, update the record and say what changed. A correction log is how a one-off win becomes a system.",
  "Why it prevents failure: without memory, every session is day one. Evolve once, benefit forever."),
]

pillar_html = "\n".join(
 f"""<article class="pillar" id="{letter.lower()}">
<div class="phead"><span class="letter" aria-hidden="true">{letter}</span><h3>{html.escape(name)}</h3></div>
<p class="plede">{html.escape(lede)}</p>
<p>{html.escape(body)}</p>
<p class="pwhy"><strong>{html.escape(why)}</strong></p>
</article>""" for letter, name, lede, body, why in pillars)

brave_body = f"""
{crumbs(("Home", "/"), ("BRAVE", None))}
<h1>The BRAVE Method</h1>
<p class="lede">BRAVE is the signature method behind every Clingy Bear Teaches lesson — five habits that turn an AI assistant from a chat window into a capable collaborator. Software engineer Chris Pick built it from real projects: mining-claim research, text-message analysis, travel hacking, vineyard media production, music albums, shipped apps, and business operations. On-screen shorthand: <strong>Brief → Context → Action → Verify → Remember.</strong></p>
<div class="pillars">
{pillar_html}
</div>
<section class="cta-box">
<h2>See BRAVE in action</h2>
<p>Episode 1 runs the full method through seven real projects — and shows how a vague request becomes a brief.</p>
<p><a class="cta" href="/season-1/ep-1-stop-chatting-start-collaborating/">Watch the Episode 1 guide →</a></p>
</section>"""

page("brave/index.html",
     title="The BRAVE Method — 5 Habits for Working with AI | Clingy Bear Teaches",
     desc="BRAVE is the signature method behind Clingy Bear Teaches: Brief the outcome, Reveal context, Authorize action, Verify evidence, Evolve the system. Five habits for turning an AI assistant into a collaborator.",
     keywords="BRAVE method, AI collaboration method, prompt framework, AI assistant workflow, Clingy Bear Teaches",
     canonical=BASE + "/brave/",
     og_title="The BRAVE Method — 5 Habits for Working with AI",
     og_desc="Brief the outcome. Reveal relevant context. Authorize the next action. Verify the evidence. Evolve the system. The signature method behind Clingy Bear Teaches.",
     body_html=brave_body, jsonld=brave_jsonld)

# ---------------------------------------------------------------- season-1 index
items = [{
  "@type": "ListItem", "position": n,
  "item": {"@type": "Episode", "name": title, "episodeNumber": n,
            "url": f"{BASE}/season-1/ep-{n}-{slug}/", "description": tag}
} for n, slug, title, tag, _, _ in EPISODES]

s1_jsonld = json.dumps({
 "@context": "https://schema.org",
 "@graph": [
  {"@type": "VideoSeries", "name": "Clingy Bear Teaches — Season 1",
   "url": BASE + "/season-1/",
   "description": "Twelve lessons from software engineer Chris Pick on turning an AI assistant into a capable collaborator, anchored in real projects.",
   "publisher": ORG, "numberOfEpisodes": 12},
  {"@type": "ItemList", "name": "Season 1 episodes", "itemListElement": items}
 ]}, indent=2)
s1_jsonld = f'<script type="application/ld+json">\n{s1_jsonld}\n</script>'

s1_cards = "\n".join(
 f"""<article class="card ep-row">
<div class="n">EPISODE {n}</div>
<div><h3><a href="/season-1/ep-{n}-{slug}/">{html.escape(title)}</a></h3><p>{html.escape(tag)}</p></div>
</article>""" for n, slug, title, tag, _, _ in EPISODES)

s1_body = f"""
{crumbs(("Home", "/"), ("Season 1", None))}
<h1>Season 1 — 12 Lessons</h1>
<p class="lede">Season 1 is a practical capability ladder. Episodes 1–3 establish the working method; 4–7 apply it to personal data, travel, media, and music; 8–10 turn it into shipped products and business operations; 11–12 teach orchestration, trust, and a capstone. Every episode is anchored in work Chris has actually done with Clingy Bear.</p>
<div class="grid eps">
{s1_cards}
</div>"""

page("season-1/index.html",
     title="Season 1 — All 12 Episodes | Clingy Bear Teaches",
     desc="All 12 Season 1 lessons of Clingy Bear Teaches: from the BRAVE method through research, travel, media, music, shipped apps, business ops, orchestration, and the capstone. Lessons dropping soon.",
     keywords="Clingy Bear Teaches season 1, AI course episodes, BRAVE method lessons, learn AI workflows",
     canonical=BASE + "/season-1/",
     og_title="Season 1 — All 12 Episodes | Clingy Bear Teaches",
     og_desc="Twelve lessons from first brief to capstone ship: BRAVE method, evidence-first research, travel hacking, media production, music, shipped apps, and more.",
     body_html=s1_body, jsonld=s1_jsonld)

# ---------------------------------------------------------------- episode pages
def episode_ld(n, slug, title, tag, longdesc):
    data = {
     "@context": "https://schema.org",
     "@graph": [
      {"@type": "Episode", "name": title, "episodeNumber": n,
       "description": longdesc[:280],
       "url": f"{BASE}/season-1/ep-{n}-{slug}/",
       "author": {"@type": "Person", "name": "Chris Pick"},
       "partOfSeries": {"@type": "VideoSeries", "name": "Clingy Bear Teaches — Season 1",
                        "url": BASE + "/season-1/"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Season 1", "item": BASE + "/season-1/"},
        {"@type": "ListItem", "position": 3, "name": title}]},
     ]}
    return '<script type="application/ld+json">\n' + json.dumps(data, indent=2) + "\n</script>"

def prevnext(n, slug):
    parts = []
    if n > 1:
        pn, pslug, ptitle, _, _, _ = EPISODES[n-2]
        parts.append(f'<a class="prev" href="/season-1/ep-{pn}-{pslug}/">← Episode {pn}: {html.escape(ptitle)}</a>')
    if n < 12:
        nn, nslug, ntitle, _, _, _ = EPISODES[n]
        parts.append(f'<a class="next" href="/season-1/ep-{nn}-{nslug}/">Episode {nn}: {html.escape(ntitle)} →</a>')
    return '<nav class="epnav" aria-label="Episode navigation">' + " ".join(parts) + "</nav>"

for n, slug, title, tag, longdesc, beats in EPISODES:
    canon = f"{BASE}/season-1/ep-{n}-{slug}/"
    beats_html = "\n".join(f"<li>{html.escape(b)}</li>" for b in beats)
    body = f"""
{crumbs(("Home", "/"), ("Season 1", "/season-1/"), (f"Episode {n}", None))}
<p class="epkicker">Season 1 · Episode {n}</p>
<h1>{html.escape(title)}</h1>
<p class="lede">{html.escape(tag)}</p>
<p class="epstatus">This lesson drops soon — <a href="{YT}">subscribe on YouTube</a> so you don't miss it.</p>
<h2>In this lesson</h2>
<p>{html.escape(longdesc)}</p>
<h2>Key beats</h2>
<ul class="beats">
{beats_html}
</ul>
<h2>The BRAVE lens</h2>
<p>Every episode runs through the <a href="/brave/">BRAVE method</a>: brief the outcome, reveal relevant context, authorize the next action, verify the evidence, and evolve the system.</p>
<section class="cta-box">
<h2>Watch it first on YouTube</h2>
<p><a class="cta" href="{YT}">▶ Clingy Bear Teaches on YouTube</a></p>
</section>
{prevnext(n, slug)}"""
    meta_desc = (tag + " " + longdesc)[:155].rsplit(" ", 1)[0] + "…"
    page(f"season-1/ep-{n}-{slug}/index.html",
         title=f"Episode {n}: {title} | Clingy Bear Teaches",
         desc=meta_desc,
         keywords=EP_KW + f", episode {n}",
         canonical=canon,
         og_title=f"Episode {n}: {title} — Clingy Bear Teaches",
         og_desc=tag,
         body_html=body, jsonld=episode_ld(n, slug, title, tag, longdesc))

# ---------------------------------------------------------------- sitemap + robots
pages = [("/",), ("/brave/",), ("/season-1/",)] + [
    (f"/season-1/ep-{n}-{slug}/",) for n, slug, *_ in EPISODES]
urls = "\n".join(
 f'  <url><loc>{BASE}{p[0]}</loc><lastmod>2026-09-22</lastmod><changefreq>weekly</changefreq></url>'
 for p in pages)
with open(os.path.join(SITE, "sitemap.xml"), "w") as f:
    f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
print("wrote sitemap.xml (15 URLs)")
with open(os.path.join(SITE, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
print("wrote robots.txt")
