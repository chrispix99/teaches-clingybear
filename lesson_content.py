"""Full written lesson content for Clingy Bear & Nugget Teach Muse Season 1 episode pages.

Everything here is distilled from the channel playbook
(~/workspace/your_files/clingy-bear-teaches-playbook/) — real lesson outlines,
real project examples, real templates. No placeholder prose.
Copy rule: Chris is a "software engineer", never "coder".
"""

LESSONS = {

"ep-1-stop-chatting-start-collaborating": {
"intro": (
    "Most people meet their AI assistant in a chat box, and most of them stay there: "
    "one question, one answer, start over tomorrow. Software engineer Chris Pick does not "
    "work that way. He uses Clingy Bear, an assistant inside Meta\u2019s Muse app, across "
    "seven real project families \u2014 mining-claim research, text-message patterns, airline "
    "points optimization, vineyard media production, music albums, shipped apps, and business "
    "operations \u2014 and the difference is not a magic prompt. It is a working method called "
    "BRAVE: Brief the outcome, Reveal relevant context, Authorize the next action, Verify the "
    "evidence, Evolve the system. This lesson is the channel\u2019s promise in one sitting."
),
"problem": (
    "A vague prompt is a slot machine. \u201cTell me about abandoned mines\u201d can return anything "
    "from folklore to geology, and none of it is shaped for what you actually need. The result "
    "can\u2019t be trusted, can\u2019t be checked, and can\u2019t be reused \u2014 so every session starts "
    "over at zero. The problem this lesson solves is turning the assistant from a clever chat "
    "window into a collaborator that can research, build, and carry a project forward with evidence "
    "you can inspect."
),
"steps": [
    ("Start from finished outcomes, not prompts",
     "The lesson opens on proof: a fast montage of the seven project families and their finished "
     "outputs \u2014 a ranked mine-land table, an anonymized message-trend chart, a flight comparison, "
     "a vineyard edit timeline, an album page, and two live apps. Proof first is the channel\u2019s format "
     "rule: open on the finished outcome or the mistake that nearly broke it. You are learning a system "
     "that has already shipped real work."),
    ("See the contrast that makes briefs matter",
     "\u201cTell me about abandoned mines\u201d versus \u201cFind Washington land containing abandoned "
     "hard-rock workings, rank candidates by distance from Spokane, and separate patented claims from "
     "public-land records.\u201d The second version names the finish line, the audience, the ranking rule, "
     "and the categories that matter. That is a brief \u2014 and a brief is executable where a prompt is "
     "a wish."),
    ("Learn BRAVE and what each stage prevents",
     "B \u2014 Brief the outcome. R \u2014 Reveal relevant context. A \u2014 Authorize the next action. "
     "V \u2014 Verify the evidence. E \u2014 Evolve the system. On screen it is shorthand: Brief \u2192 "
     "Context \u2192 Action \u2192 Verify \u2192 Remember. Each stage prevents a specific common failure: "
     "vague asks, missing context, unauthorized actions, unverified claims, and the amnesia of starting "
     "over every session."),
    ("Turn \u201cmake me an app\u201d into a product brief",
     "The lesson upgrades a throwaway request into a product brief on screen: audience, workflow, data, "
     "constraints, deployment target, analytics, and definition of done. The same move works for research: "
     "who needs it, what shape the answer takes, what counts as a source, and what \u201cdone\u201d means. "
     "The downloadable one-page BRAVE brief worksheet (Outcome, Audience, Context, Inputs, Constraints, "
     "Authority, Evidence, Definition of done) makes this repeatable."),
    ("Know what the agent can actually do \u2014 and where it needs permission",
     "An agent can research, build files, and sometimes take approved actions \u2014 but access varies by "
     "setup, and consequential steps need explicit authorization. The channel is honest about this: it says "
     "what was available in the demonstrated setup, shows approval moments, and explains the fallback when "
     "an integration is unavailable. Researching is not sending. Drafting is not publishing. A local build "
     "is not a deployment."),
    ("Answer the two questions, every time",
     "The lesson ends with the habit that replaces prompt tricks: before any serious task, answer \u201cWhat "
     "does done look like?\u201d and \u201cWhat evidence would make me trust it?\u201d If you can\u2019t answer "
     "both, you don\u2019t have a brief yet \u2014 you have a chat."),
],
"example": (
    "On screen: \u201cHelp with my vineyard videos\u201d becomes a BRAVE brief. Outcome: a 10\u201312 minute "
    "episode cut from the season\u2019s footage. Audience: the AI Vineyard audience watching on phones. "
    "Context: the footage inventory, the season narrative, the never-do rules. Authority: the assistant may "
    "build the edit plan and preview renders, but the full-resolution master waits for Chris\u2019s approval. "
    "Evidence: a rendered preview to watch before committing. Definition of done: a verified master uploaded "
    "and catalogued. The assistant then returns a structured plan with a verification step built in \u2014 "
    "not an answer, a project."
),
"takeaways": [
    "A brief beats a prompt: name the finish line, the audience, and the format.",
    "BRAVE is the loop \u2014 Brief, Context, Action, Verify, Remember \u2014 and each stage prevents a real failure.",
    "Say what the assistant may do and what needs your approval before anything irreversible.",
    "End every brief with the two questions: what does done look like, and what evidence would make you trust it?",
    "Keep the one-page BRAVE brief worksheet; you will use it in every lesson after this one.",
],
},

"ep-2-give-your-ai-the-map": {
"intro": (
    "The assistant can\u2019t know what you never said \u2014 and what it doesn\u2019t know, it will invent "
    "confidently. This lesson is about context as decision-changing information: not your autobiography, "
    "but the facts, vocabulary, constraints, and prior decisions that change the answer. The vehicle is a "
    "real story: Chris\u2019s mining-claim research, where precise terms and a durable project map turned "
    "months of scattered questions into one continuous project."
),
"problem": (
    "Without a map, every session is day one. You re-teach the project, re-explain the terms, and watch the "
    "assistant confidently mix up things you thought were settled \u2014 like treating a patented claim, an "
    "unpatented claim, and fee land as interchangeable when they are legally different things. Worse, "
    "remembered context gets mistaken for proof: the assistant \u201cremembers\u201d last month\u2019s price "
    "or rule and presents it as current fact. The problem this lesson solves is building context once, "
    "keeping it correct, and knowing where memory ends and verification begins."
),
"steps": [
    ("Define context as decision-changing information",
     "Context is not everything about you. It is the specific information that would change the answer: the "
     "objective, the known facts, the vocabulary, the source hierarchy, the constraints, what\u2019s already "
     "done, what\u2019s unresolved, and the next action. If a detail wouldn\u2019t change the output, it\u2019s "
     "noise \u2014 leave it out."),
    ("Build the one-page project map",
     "Write it down, once: objective, known facts, vocabulary, source hierarchy, constraints, completed work, "
     "unresolved questions, next action. One page, durable, updated when facts change. This is the document "
     "you hand the assistant at the start of a session instead of re-explaining everything out loud."),
    ("Use precise terms \u2014 they are not interchangeable",
     "In the mining-claim story: patented claim, unpatented claim, fee land, placer claim, hard-rock mine, "
     "parcel, and BLM record are different legal and practical things. Swapping them doesn\u2019t just sound "
     "wrong \u2014 it produces wrong candidates, wrong ownership conclusions, and wasted prospecting trips. "
     "Put the vocabulary in the map."),
    ("Demonstrate continuity across sessions",
     "Session one: research the BLM record. Session two, weeks later: amend the search criteria \u2014 the "
     "assistant applies the new criteria to the existing map without re-teaching. Session three: plan a "
     "prospecting or camping trip using the researched record. No session starts from zero because the map "
     "carries the project."),
    ("Correct a durable fact once \u2014 explicitly",
     "When a fact in the map turns out wrong, say so on the record: what the old understanding was, what the "
     "new evidence says, and what changed. One explicit correction beats ten quiet ones, because quiet "
     "corrections leave the old fact alive in half the project\u2019s memory."),
    ("Separate memory from proof",
     "Remembered context accelerates work, but current legal, travel, price, and availability facts still need "
     "fresh verification. Memory tells you where to look; it does not tell you what is true today. The "
     "lesson\u2019s rule: trust the map for how the project works, verify the world for what the world says now."),
],
"example": (
    "Three sessions, one project. First, Chris and Clingy Bear research BLM records and build the candidate "
    "table. Weeks later, Chris amends the criteria \u2014 closer to Spokane, patented claims preferred \u2014 "
    "and the assistant re-ranks the existing candidates instead of starting a new search. Later still, "
    "planning a prospecting trip: the assistant pulls the researched parcels, access constraints, and open "
    "questions straight from the map. The trip brief writes itself because the research was preserved, not "
    "re-performed."
),
"takeaways": [
    "Context is decision-changing information \u2014 facts, terms, constraints, prior decisions \u2014 not your life story.",
    "Build a one-page project map and update it when facts change.",
    "Precise vocabulary prevents confident wrong answers; put definitions in the map.",
    "Correct durable facts explicitly, once, on the record.",
    "Memory accelerates; verification proves. Fresh-check anything legal, financial, or time-sensitive.",
],
},

"ep-3-receipts-or-it-didnt-happen": {
"intro": (
    "This lesson is the channel\u2019s proof of rigor: evidence-first research, demonstrated on BLM land "
    "records and genealogy. The rule is the title \u2014 receipts or it didn\u2019t happen. You\u2019ll learn "
    "the source ladder, how to turn a broad hunt into a research table, how to handle negative claims "
    "honestly, and how to keep a correction log so new evidence improves the record instead of "
    "embarrassing it."
),
"problem": (
    "AI assistants are fluent, and fluency looks like authority. A confident paragraph about a land parcel "
    "or a family line can be a well-structured guess \u2014 a family-tree inference presented as a proven "
    "marriage, a \u201cit doesn\u2019t exist\u201d that really means \u201cI didn\u2019t find it.\u201d The problem "
    "this lesson solves is making research checkable: every claim traceable to a source, every gap labeled, "
    "every reversal recorded."
),
"steps": [
    ("Climb the source ladder",
     "Rank every source before you trust it: primary record at the top, then authoritative database, then "
     "reputable secondary source, then community lead, and unsourced claim at the bottom. A BLM record beats "
     "a forum post. A marriage certificate beats a family-tree hint. The ladder decides how much weight a "
     "claim carries."),
    ("Turn a broad hunt into a research table",
     "Vague hunting becomes a table with columns: candidate, location, distance, ownership type, mine "
     "evidence, source, uncertainty, next verification. Every row is a decision waiting for evidence, and the "
     "\u201cuncertainty\u201d column is mandatory \u2014 it is what keeps the table honest."),
    ("Apply the same pattern to genealogy",
     "A proven marriage certificate is not an inferred family-tree link. The lesson shows both side by "
     "side: one claim you can cite, one you can only suspect. Teaching viewers to feel the difference is "
     "the whole point \u2014 rigor is a sensation before it\u2019s a skill."),
    ("Practice negative-claim discipline",
     "\u201cI did not find it in the sources checked\u201d is different from \u201cit does not exist.\u201d "
     "The first is honest and useful; the second is a claim you can\u2019t support. Name the sources you "
     "checked and stop there."),
    ("Make the assistant show its work",
     "Ask it to quote the relevant line, preserve the source link, and explain any contradiction \u2014 in its "
     "own words, not yours. A summary without a quoted line is a rumor with good formatting."),
    ("Keep a correction log",
     "When new evidence reverses a conclusion, update the record and say what changed: old conclusion, new "
     "evidence, new conclusion. The log is what lets a research project survive being wrong, which every "
     "real project will be at least once."),
    ("Plan the physical follow-up \u2014 without assuming permission",
     "Research ends at the trailhead. The lesson plans a prospecting or camping visit \u2014 access, weather, "
     "route, equipment, land-status checks \u2014 and draws the hard line: a planning assumption is not "
     "permission to enter. Verify land status before boots hit ground."),
],
"example": (
    "A candidate parcel row in the research table: location and distance from Spokane, ownership type pulled "
    "from the BLM record (unpatented claim, not fee land), mine evidence from a historical database, source "
    "links preserved, uncertainty flagged (\u201caccess road status unverified\u201d), next verification "
    "named (\u201ccounty recorder + on-site check\u201d). One month later, new evidence shows the access "
    "assumption was wrong \u2014 the correction log records the reversal, and the trip plan changes before "
    "anyone drives out. That\u2019s the system working."
),
"takeaways": [
    "Rank sources on the ladder before trusting them: primary record first, unsourced claim last.",
    "Turn hunts into tables \u2014 candidate, evidence, source, uncertainty, next verification.",
    "\u201cNot found in the sources checked\u201d is honest; \u201cit doesn\u2019t exist\u201d is a claim.",
    "Make the assistant quote the line, keep the link, and explain contradictions.",
    "Log corrections explicitly; a planning assumption is never permission.",
],
},

"ep-4-what-the-texts-actually-say": {
"intro": (
    "Years of your own messages are a dataset about your relationships \u2014 and a minefield if you handle "
    "them carelessly. This lesson shows a privacy-first way to analyze message history: consent and scope "
    "first, a strict schema, a cleaned archive, and measurements of only what is observable. The analysis "
    "reveals patterns; it never diagnoses a person."
),
"problem": (
    "Two failure modes haunt personal-data projects. The first is privacy: real names, numbers, and intimate "
    "content flashed on screen for a tutorial. The second is overreach: an assistant that guesses message "
    "direction from wording, or reads \u201cresponse time increased\u201d as \u201cthey no longer care.\u201d "
    "The problem this lesson solves is doing the analysis rigorously without either sin \u2014 careful with "
    "people\u2019s data, humble about what the data can say."
),
"steps": [
    ("Establish consent and scope \u2014 then redact",
     "Analyze only messages you lawfully control. Before anything goes on screen: redact names, phone "
     "numbers, intimate content, and third-party details. The channel\u2019s privacy-safe demo recipe applies: "
     "copy only the fields needed to teach the method, replace identifiers, coarsen dates when exact timing "
     "isn\u2019t essential, preserve the structural issue being demonstrated, label the demo as recreated, "
     "and secure the working copy afterward."),
    ("Define the schema \u2014 direction is a hard field",
     "Timestamp, contact, direction, text, medium, thread. Direction \u2014 who sent what \u2014 is a hard data "
     "field from the message record, not a guess from wording. Getting this wrong flips the entire analysis, "
     "so it is validated, never inferred."),
    ("Clean the archive without corrupting it",
     "Normalize dates, preserve empty multimedia messages as events (a photo sent is still a message), remove "
     "duplicates carefully, and keep original text immutable. Cleaning makes the data analyzable; immutability "
     "keeps it honest."),
    ("Measure only the observable",
     "Reply latency, initiation balance, question rate, future-planning language, warmth markers, conflict "
     "markers, conversation gaps. These are counts and timings \u2014 things the archive actually contains. "
     "Segment by week or relationship phase, and inspect real examples behind every trend before believing it."),
    ("Separate measurement from interpretation",
     "\u201cResponse time increased\u201d is an observation. \u201cThey no longer care\u201d is an unsupported "
     "inference. The lesson draws this line in red: the assistant reports the measurement and stops. The "
     "meaning is a human question, not a model output."),
    ("Ask for counterexamples and uncertainty",
     "Sentiment classifiers miss sarcasm, inside jokes, neurodivergent tone, and everything outside the "
     "archive. Demand the counterexamples: the warm message during a \u201ccold\u201d week, the slow reply "
     "during travel. Uncertainty is part of the result, not a footnote."),
    ("Close with human judgment",
     "The analysis can reveal patterns; it cannot diagnose a person or replace a conversation. The lesson "
     "ends where it must: the data is a mirror with smudges, and the human decides what to do with the "
     "reflection."),
],
"example": (
    "The archive shows reply latency doubling across March. The observable trend is real \u2014 the chart "
    "doesn\u2019t lie. But the examples behind it tell the story: a work trip, a family emergency, a dead "
    "phone. Three different causes, one identical chart shape. The analysis surfaced the question; only the "
    "human with context outside the archive could answer it. That\u2019s the lesson\u2019s boundary, demonstrated."
),
"takeaways": [
    "Consent, scope, and redaction come before any analysis \u2014 and before anything goes on screen.",
    "Direction is a data field, never a guess; original text stays immutable.",
    "Measure the observable: latency, initiation, questions, planning language, gaps.",
    "An observation is not an interpretation \u2014 don\u2019t let the model cross that line.",
    "Patterns inform; only humans conclude. The analysis can\u2019t diagnose a person.",
],
},

"ep-5-make-the-miles-work-harder": {
"intro": (
    "Points and miles are an optimization problem \u2014 and your assistant can\u2019t solve it without your "
    "real constraints. This lesson builds the travel brief, defines the objective function, teaches honest "
    "cash-versus-points math, and separates strategy (which can be explored broadly) from booking (which must "
    "be verified live). The prize: trips that cost less in every currency that matters."
),
"problem": (
    "\u201cFind me a cheap flight\u201d ignores the things that actually decide a trip: your status, your "
    "bags, your time windows, positioning flights, cancellation terms, and whether award seats even exist "
    "right now. Worse, a single \u201cpoints are worth 1.5 cents\u201d valuation quietly picks winners that "
    "lose on every other axis. The problem this lesson solves is giving the assistant the full constraint "
    "set and the real objective \u2014 so its recommendation optimizes your trip, not a generic one."
),
"steps": [
    ("Build the travel brief",
     "Traveler, exact dates, origin and destination, time windows, bags, elite status, points balances, "
     "flexibility, and deal-breakers. Every field earns its place: bags change the fare math, status changes "
     "the upgrade math, deal-breakers (no red-eyes, no basic economy) prune the search before it starts."),
    ("Define the objective function \u2014 there isn\u2019t one winner",
     "Cheapest cash fare, fewest points, best cents per point, best elite-qualifying return, and lowest "
     "disruption risk are different winners. Say which game you\u2019re playing before comparing options, "
     "or you\u2019ll compare a sprinter to a marathoner."),
    ("Do cash-versus-points math without worshiping one valuation",
     "Compare cash saved, taxes and fees, cancellation terms, and opportunity cost \u2014 not a single "
     "cents-per-point number treated as scripture. A \u201cgreat redemption\u201d with brutal cancellation "
     "terms can be the worse deal."),
    ("Separate planning from live booking",
     "Routes and strategy can be explored broadly and slowly. Schedules, award inventory, and fares must be "
     "checked at decision time \u2014 they change, and yesterday\u2019s availability is a rumor. The lesson "
     "labels every number with its freshness."),
    ("Account for the whole trip",
     "Positioning flights, hotel, ground transport, lounge access, baggage, missed-connection risk. The "
     "\u201ccheap\u201d itinerary that strands you overnight in a connection city wasn\u2019t cheap."),
    ("Ask for a recommendation and the best alternative",
     "Demand both, with reasons tied to your stated priorities \u2014 not generic pros and cons. The "
     "alternative is what makes the recommendation trustworthy: it proves the comparison was real."),
    ("Run the final verification checklist before purchasing",
     "Re-check fare, inventory, dates, traveler details, baggage rules, and cancellation terms immediately "
     "before paying. The checklist is the last BRAVE verify stage, applied to money."),
],
"example": (
    "Two itineraries, same trip. Option A: fewest points, but a tight connection and no lounge on a six-hour "
    "layover. Option B: slightly more points, a sane connection, and it earns elite-qualifying credit toward "
    "status you\u2019re 2,000 miles short of. Under \u201ccheapest points\u201d A wins; under \u201clowest "
    "disruption + status progress\u201d B wins by a mile. The brief you wrote in step one decides \u2014 which "
    "is exactly why you write it before comparing anything."
),
"takeaways": [
    "Write the travel brief first: dates, constraints, status, balances, deal-breakers.",
    "Name your objective \u2014 cheapest cash, fewest points, status, or lowest risk are different games.",
    "Do full cash-vs-points math: taxes, cancellation, opportunity cost.",
    "Strategy can be old; fares and award inventory must be checked at decision time.",
    "Price the whole trip, then verify everything again before you pay.",
],
},

"ep-6-turn-a-footage-pile-into-a-production-system": {
"intro": (
    "A hard drive full of camera files is not a production \u2014 it\u2019s a pile. This lesson follows the AI "
    "Vineyard media workflow and shows how raw footage becomes a system: inventory first, searchable story "
    "beats second, an edit brief third, real correction cycles fourth, and a reconciled catalog at the end. "
    "The timeline is the last thing you open, not the first."
),
"problem": (
    "Most creators open the timeline first and drown: thousands of clips, cryptic filenames, no idea what\u2019s "
    "usable, and a full-resolution render that takes all night \u2014 of a cut nobody approved. The problem "
    "this lesson solves is turning footage into a searchable, correctable, shippable system where every "
    "decision is reviewable before it gets expensive."
),
"steps": [
    ("Start with the media inventory, not the timeline",
     "For every file: identity, date, camera, technical metadata, transcript, description, tags, proxy, master "
     "location, status. The inventory is the project\u2019s memory \u2014 it\u2019s what makes 10,000 clips "
     "answer questions instead of asking them."),
    ("Respect filenames and pairing rules",
     "One 360-degree clip can have multiple master files that must stay paired. Filenames are load-bearing: "
     "lose the pairing and you lose the shot. The lesson shows why naming conventions are a production "
     "decision, not housekeeping."),
    ("Turn raw footage into searchable story beats",
     "Tag for story, not just content: planting, irrigation, equipment, mistakes, wildlife, progress, payoff. "
     "When the edit needs \u201ca mistake that taught us something,\u201d you search \u2014 you don\u2019t rewatch "
     "forty hours."),
    ("Build an edit brief",
     "Audience promise, narrative spine, target duration, must-use moments, and \u201cnever do this\u201d rules. "
     "The brief is the episode\u2019s contract: it tells the editor \u2014 human or AI \u2014 what the cut is "
     "for before a single trim."),
    ("Run real editorial correction cycles",
     "The lesson shows an actual cycle: trim clapboards, remove dead air, cover narration with B-roll, fix "
     "jump cuts, orient graphics correctly. Corrections are narrated, not hidden \u2014 mistakes are teaching "
     "material, and the channel\u2019s recording rules say so explicitly."),
    ("Render a short preview before the expensive master",
     "Approve the story on a cheap preview render. Only then commit to the full-resolution master. This one "
     "habit saves more production time than any plugin."),
    ("Reconcile the catalog after production",
     "Mark what shipped, where the masters live, what got cut. The system remembers so the next episode "
     "starts from knowledge, not archaeology."),
    ("Repurpose deliberately",
     "One production, many outputs by design: long-form episode, teaser, vertical short, date-stamped "
     "milestone, social caption. Repurposing is planned at the brief stage, not scraped from leftovers."),
],
"example": (
    "A vineyard episode\u2019s preview cut goes out for review. Two notes come back: a valley segment stutters "
    "where a take was clipped short, and a passport segment has an orphaned fragment. The fix: swap in the "
    "continuous raw take for the valley shot, keep the full passport take and remove the fragment. The "
    "preview is re-rendered, approved \u2014 and only then does the full-resolution master get built. The "
    "catalog records exactly what changed and why, so the next episode\u2019s editor doesn\u2019t repeat the "
    "mistake."
),
"takeaways": [
    "Inventory before timeline: every file gets identity, metadata, tags, and status.",
    "Filenames and pairing rules are production decisions \u2014 protect them.",
    "Brief the edit (promise, spine, duration, must-uses, never-dos) before cutting.",
    "Correct in cheap preview cycles; render the expensive master once.",
    "Reconcile the catalog after shipping, and plan repurposing up front.",
],
},

"ep-7-from-song-idea-to-six-album-slate": {
"intro": (
    "One song idea is a spark; a six-album slate is a system. This lesson covers creative direction with AI "
    "music generation: defining the creative system before generating anything, writing tight track briefs, "
    "batching with discipline, letting human taste choose the canonical versions, and running a correction "
    "loop that fixes what\u2019s wrong without disturbing what\u2019s approved."
),
"problem": (
    "Generative tools make it easy to produce hundreds of tracks and hard to finish one album. Without a "
    "system you get credit burn, a review bottleneck, a catalog nobody can navigate, and the classic "
    "disaster: regenerating everything because one lyric has a wrong date. The problem this lesson solves "
    "is running creative generation like a production \u2014 directed, selective, and correctable."
),
"steps": [
    ("Define the creative system before generating",
     "Album concept, track count, subject map, musical constraints, voice, tone shifts, release structure. "
     "The system is decided up front so individual generations serve the slate instead of wandering off into "
     "six different sounds."),
    ("Write track briefs \u2014 specific, not scripted",
     "Subject, emotional arc, lyrical anchors, prohibited clich\u00e9s, energy target. The brief directs the "
     "music without scripting it to death \u2014 enough constraint to be coherent, enough room to be good."),
    ("Batch carefully",
     "Generate enough variation to have real choices, but respect plan credits, time, and the human review "
     "bottleneck. Ten strong candidates beat a hundred unlistened files."),
    ("Let human taste choose \u2014 not an AI score",
     "Chris\u2019s hearts, not a model\u2019s rating, choose the canonical versions. Taste is a human decision "
     "the system is built around, not a step to automate away."),
    ("Keep one catalog for everything",
     "Variants, durations, lyrics, credits, cover assets, publication state \u2014 one catalog, always current. "
     "The catalog is what makes a \u201cslate\u201d real instead of a folder of maybe-files."),
    ("Run the correction loop surgically",
     "A factual lyric is wrong? Fix the line, regenerate only what changed, and don\u2019t disturb approved "
     "tracks. The loop is: identify the defect, change the smallest surface, regenerate, re-verify."),
    ("Publish album by album \u2014 then verify",
     "Release one album, verify playback and metadata, update the public catalog. Then the next. Shipping in "
     "albums keeps quality controllable and the catalog truthful."),
    ("Reuse the system without flattening the sound",
     "A new concept gets the same machinery \u2014 system, briefs, batching, taste, catalog \u2014 with new "
     "constraints. The system is reusable; the sound stays distinct."),
],
"example": (
    "A track about a historic mission ships with one wrong lyric \u2014 a date that\u2019s off by a decade. "
    "The correction loop: fix the single line in the brief, regenerate that track only, verify the new lyric "
    "against the source, and leave the eleven approved tracks untouched. Total cost: one generation credit "
    "and ten minutes. The alternative \u2014 regenerating the album \u2014 would have risked eleven good "
    "tracks to fix one line."
),
"takeaways": [
    "System first: concept, subject map, constraints, and release structure before any generation.",
    "Briefs direct without scripting; batches stay small enough for human review.",
    "Human taste picks the canonical versions \u2014 always.",
    "One catalog tracks variants, lyrics, credits, assets, and publication state.",
    "Fix surgically: regenerate only what changed, verify, and protect approved work.",
],
},

"ep-8-build-the-tool-you-wish-existed": {
"intro": (
    "The most satisfying AI collaboration is the one that ships software. This lesson turns an itch into a "
    "deployed app through two real builds: the Ground School Trainer, a study tool with per-user progress, "
    "and NeuroSpicy, a self-reflection assessment. The method: start with the user and the moment of use, "
    "define the smallest complete loop, write testable acceptance criteria, and make every stage observable."
),
"problem": (
    "Side projects die two ways: they start with the tech stack instead of the user, or they \u201cwork on my "
    "machine\u201d and never become something another human can use. Add untested auth, mystery analytics, "
    "and deploys nobody verified, and you get demo-ware. The problem this lesson solves is a repeatable path "
    "from idea to a live URL you can hand someone \u2014 with proof it works."
),
"steps": [
    ("Start with the user and the moment of use",
     "Not the framework. Who opens this, in what moment, trying to do what? Ground School: a student "
     "practicing before a checkride. NeuroSpicy: someone answering questions to understand themselves. "
     "Everything downstream serves that moment."),
    ("Define the smallest complete loop",
     "Ground School: sign in, practice, feedback, progress. NeuroSpicy: answer, understand, reflect, revisit. "
     "If the loop isn\u2019t complete, it isn\u2019t shippable \u2014 it\u2019s a demo with a dead end."),
    ("Write acceptance criteria you can actually test",
     "\u201cSaved progress belongs to the right user. A question scores correctly. A result reads well on "
     "mobile.\u201d Each criterion is a test waiting to happen \u2014 and the lesson runs them."),
    ("Decide what\u2019s sensitive before you collect it",
     "Name what data is sensitive and what should never become public analytics. Privacy is a design input, "
     "not a post-launch apology."),
    ("Scaffold, implement, test, deploy, verify \u2014 observably",
     "Each stage produces something you can look at: the scaffold renders, the tests pass or fail visibly, "
     "the deploy lands at a URL you open yourself. Nothing advances on \u201ctrust me.\u201d"),
    ("Add analytics only after defining the behavior worth measuring",
     "Metrics follow the loop: what does a successful practice session look like? Instrument that \u2014 not "
     "a dashboard of vanity counts."),
    ("Keep a correction loop",
     "Reproduce the issue, change the smallest surface, rerun the tests, verify the live page. The same "
     "surgical discipline as the music lesson, applied to code."),
    ("Know what \u201cshipped\u201d means",
     "Public URL, correct auth, real data behavior, mobile check, analytics, and a rollback path. If any "
     "one is missing, it isn\u2019t shipped \u2014 it\u2019s staged."),
],
"example": (
    "Acceptance criterion: saved progress belongs to the right user. The test: sign in as User A, complete "
    "three practice sets, sign out, sign in as User B \u2014 B sees a clean slate, A\u2019s progress intact. "
    "Then the adversarial version: A\u2019s session token in B\u2019s browser must not leak A\u2019s data. "
    "It passes, on the live URL, on a phone. That\u2019s what \u201ccorrect auth\u201d means \u2014 not a "
    "checkbox, a demonstration."
),
"takeaways": [
    "Start from the user\u2019s moment of use, not the tech stack.",
    "Ship the smallest complete loop \u2014 every dead end is a broken promise.",
    "Write testable acceptance criteria and run them on the live URL.",
    "Decide data sensitivity up front; instrument only meaningful behavior.",
    "\u201cShipped\u201d = public URL + correct auth + real data + mobile check + analytics + rollback path.",
],
},

"ep-9-ship-a-real-data-product": {
"intro": (
    "Behind every \u201csimple\u201d data product is an unglamorous engine: collection, normalization, "
    "deduplication, import, audit. This lesson follows VMenu \u2014 a real restaurant data product \u2014 and "
    "teaches the discipline that keeps tens of thousands of records trustworthy: contracts before "
    "collection, idempotent imports, honest handling of timeouts, and verification from the user\u2019s side."
),
"problem": (
    "Data projects fail silently. A re-run duplicates half the catalog. A partial update wipes fields the "
    "endpoint replaces wholesale. A timeout gets retried blindly and imports the same batch twice. The "
    "dashboard looks fine; the data is rotting. The problem this lesson solves is building a pipeline where "
    "every stage is separate, every re-run is safe, and every count reconciles."
),
"steps": [
    ("Define the data contract before collecting anything",
     "Restaurant identity, address, menu section, item, price, source, update status, timestamps. The "
     "contract is agreed before the first scrape \u2014 it\u2019s what \u201ccorrect\u201d means for every "
     "record that follows."),
    ("Separate the stages",
     "Collection, normalization, deduplication, import, and audit are distinct stages with distinct jobs. "
     "When stages blur, bugs hide: a dedup problem looks like an import problem, and you fix the wrong one."),
    ("Make imports idempotent",
     "Rerunning the same batch must reconcile, not duplicate or erase fields. Idempotency is the difference "
     "between \u201csafe to retry\u201d and \u201cpray it worked the first time.\u201d"),
    ("Respect the danger of partial updates",
     "When an endpoint replaces a full record, a partial update isn\u2019t partial \u2014 it\u2019s a deletion "
     "of everything you didn\u2019t send. Always pass the full record through, or use an endpoint that "
     "doesn\u2019t replace."),
    ("Build quality reports",
     "Menu-less venues, suspiciously thin menus, missing dayparts, duplicate candidates, closed businesses. "
     "The reports are the product\u2019s immune system \u2014 they find the rot the pipeline can\u2019t feel."),
    ("Treat timeouts as unknown outcomes",
     "A timed-out request didn\u2019t necessarily fail; the server may have finished. Reconcile exact counts "
     "before retrying. \u201cIt timed out, run it again\u201d is how duplicates are born."),
    ("Deploy like it matters",
     "Correct authorship on commits, environment variables in place before the deploy that needs them, "
     "production checks after. The lesson\u2019s hard-won rule: env changes don\u2019t apply to already-built "
     "deployments."),
    ("Verify from the user\u2019s side",
     "Search a venue, inspect menu sections, test mobile behavior, confirm analytics. The pipeline\u2019s "
     "opinion of itself doesn\u2019t count \u2014 the user\u2019s experience does."),
],
"example": (
    "An import batch of several hundred venues times out halfway. The wrong move: re-run the batch. The "
    "lesson\u2019s move: query what actually landed, reconcile exact counts against the source, identify the "
    "missing slice, and import only that \u2014 idempotently, so even an overlap reconciles instead of "
    "duplicating. Final counts match the source to the record. That reconciliation is the whole lesson in "
    "one incident."
),
"takeaways": [
    "Contract first: define the record shape before collecting a single row.",
    "Separate stages; make re-runs idempotent; never trust a blind retry.",
    "Partial updates on replace-style endpoints are deletions in disguise.",
    "Quality reports and count reconciliation are non-negotiable.",
    "Verify from the user\u2019s side \u2014 search it, open it on mobile, check analytics.",
],
},

"ep-10-give-the-business-its-own-brain": {
"intro": (
    "A small business runs on its owner\u2019s working memory \u2014 and working memory drops things. This "
    "lesson gives the business its own brain: an operating map of products, owners, customers, revenue, "
    "systems, decisions, commitments, and risks, demonstrated through two real operations \u2014 24 Legs, a "
    "games business, and maximusPoints, a consumer-data product. The assistant becomes the business\u2019s "
    "memory; the owner keeps the authority."
),
"problem": (
    "Between bursts of attention, businesses leak: the waiting-for email nobody followed up, the launch gate "
    "nobody checked, the invoice the assistant was never authorized to send. Decisions live in chat history, "
    "commitments live in heads, and \u201cwe\u2019ll get to it\u201d means never. The problem this lesson "
    "solves is an operating system for the business that survives the owner\u2019s attention gaps."
),
"steps": [
    ("Create the operating map",
     "Products, owners, customers, revenue model, systems, current decisions, commitments, risks \u2014 one "
     "map, kept current. It\u2019s the business equivalent of the project map from Episode 2, and it serves "
     "the same purpose: no re-teaching, ever."),
    ("Run product ops on 24 Legs",
     "Card inventory, revision status, print requirements, play-test feedback, launch gates. Physical "
     "products have physical constraints \u2014 the map tracks what\u2019s printed, what\u2019s revised, "
     "what\u2019s blocking launch."),
    ("Run data-product ops on maximusPoints",
     "Benefits catalog, account-connection boundaries, recurring refresh, trust. A consumer-data product "
     "lives or dies on trust, so the map tracks exactly what data moves, how often, and where the "
     "boundaries are."),
    ("Separate draft operations from financial authority",
     "The assistant may prepare an invoice or reconcile information. Sending, charging, or changing an "
     "account is a distinct, explicitly approved action. This is Episode 1\u2019s authorization stage, applied "
     "to money."),
    ("Hold a weekly review that surfaces only what matters",
     "Decisions, blockers, deadlines, anomalies. Not a status dump \u2014 a decision surface. If it doesn\u2019t "
     "need a human judgment, it doesn\u2019t make the review."),
    ("Template the recurring, protect the sensitive",
     "Use templates for recurring work, but keep real customer and financial data access-controlled. "
     "Efficiency for the routine; gates for the consequential."),
    ("Track every \u201cwaiting for\u201d \u2014 and close the loop",
     "Nothing disappears between bursts of attention because every waiting-for has an owner and a next "
     "check. Resolved commitments get closed with the result recorded \u2014 not just the plan, the outcome."),
],
"example": (
    "Monday\u2019s weekly review for 24 Legs: three decisions (approve the revised card back? switch printers? "
    "set the launch date?), one blocker (play-test feedback not yet collected from two groups), two "
    "deadlines (print file due Friday), and four waiting-for items with owners and check-dates. Twenty "
    "minutes, and the business\u2019s entire state is visible. Without the map, that same review would have "
    "been an hour of \u201cwait, where are we on\u2026?\u201d"
),
"takeaways": [
    "Give the business an operating map: products, owners, customers, revenue, systems, decisions, commitments, risks.",
    "Track physical ops (inventory, revisions, launch gates) and data ops (boundaries, refresh, trust) the same way.",
    "Drafting is not authorizing \u2014 financial actions need explicit approval.",
    "Weekly reviews surface decisions, blockers, deadlines, anomalies \u2014 nothing else.",
    "Track every \u201cwaiting for\u201d; close commitments with results, not plans.",
],
},

"ep-11-run-several-projects-without-losing-the-plot": {
"intro": (
    "Chris runs mining research, a vineyard production, music slates, apps, and businesses \u2014 sometimes in "
    "the same week. This lesson is the orchestration layer: how to classify work, give every track a "
    "deliverable and a return condition, parallelize what\u2019s independent, preserve state in project "
    "records, and tell the difference between \u201cstarted\u201d and \u201cfinished.\u201d"
),
"problem": (
    "Multiple projects in one chat become one confused project. Delegated work vanishes into the void. A "
    "batch job \u201cran\u201d but nobody knows if it finished. Notifications pile up until the real blockers "
    "are invisible. The problem this lesson solves is running many tracks at once with the same rigor you\u2019d "
    "give one \u2014 every track observable, every outcome verified, every failure surfaced."
),
"steps": [
    ("Classify the work",
     "Immediate conversation, delegated research, build task, monitored event, scheduled recurrence. "
     "Different classes get different handling \u2014 you don\u2019t babysit a recurrence like a conversation, "
     "and you don\u2019t fire-and-forget a build task."),
    ("Give every track a contract",
     "Concrete deliverable, boundary, evidence requirement, return condition. \u201cResearch X\u201d is not a "
     "track; \u201cresearch X, deliver a ranked table with sources, return when the table reconciles\u201d is."),
    ("Parallelize the independent, sequence the shared",
     "Independent tracks run in parallel. Tracks that share data, credentials, or judgment gates run in "
     "sequence. Parallelism is a scheduling decision, not a hope."),
    ("Pilot before you batch",
     "One successful pilot before launching a large batch. The pilot proves the method on real data; the "
     "batch scales what the pilot proved."),
    ("Preserve state in a project record",
     "Last completed step, artifact location, unresolved issue, next action. Every run resumes where the "
     "last one stopped \u2014 this is Episode 2\u2019s project map, grown up into operations."),
    ("Distinguish \u201cstarted\u201d from \u201cfinished\u201d",
     "Queued, running, and deployed are not the same as verified. Work is done when the evidence says so \u2014 "
     "the completion report template (Completed, Evidence, Changed, Not completed, Decision needed, Next "
     "action) is the receipts for orchestration."),
    ("Surface failures immediately \u2014 with the consequence and the next move",
     "No silent failures, ever. What failed, what it affects, what completed work is preserved, and the "
     "safest next step. Bad news early is cheap; bad news late is expensive."),
    ("Kill notification sludge",
     "Notify on completions, blockers, genuine risk, or decisions \u2014 not every heartbeat. A notification "
     "system that cries wolf trains you to ignore the wolf."),
],
"example": (
    "A nine-city data rebuild. The pilot: one city, end to end \u2014 collection through audit \u2014 with "
    "counts reconciled against the source. It works. Then the batch: remaining cities run as parallel tracks, "
    "each with its own project record (last completed step, artifact location, open issues). One city\u2019s "
    "track fails on a timeout \u2014 the failure surfaces immediately with the consequence (\u201ccity 4 "
    "incomplete, others unaffected\u201d) and the next move (reconcile counts, resume that track only). "
    "No re-running the world."
),
"takeaways": [
    "Classify work, then handle each class appropriately \u2014 don\u2019t babysit recurrences or fire-and-forget builds.",
    "Every track gets a deliverable, a boundary, an evidence requirement, and a return condition.",
    "Pilot once, then batch; keep a project record so every run resumes cleanly.",
    "\u201cStarted\u201d is not \u201cfinished\u201d \u2014 queued, running, and deployed are not verified.",
    "Surface failures fast with consequence + next move; notify only on what needs a human.",
],
},

"ep-12-trust-but-verify-and-ship": {
"intro": (
    "The capstone. Everything in Season 1 converges here: the trust stack \u2014 scope, source, permission, "
    "preview, approval, verification, rollback \u2014 the \u201cshow me\u201d habit, a preflight for private "
    "data, a protocol for failure, and a cross-project bug reel of real mistakes. It ends with a shipped "
    "capstone behind a human approval gate and a visible verification pass. Trust the system; verify the "
    "output; ship the thing."
),
"problem": (
    "The better the assistant gets, the easier it is to stop checking \u2014 and that\u2019s when the "
    "expensive mistakes happen. An unverified claim ships to the public. A private-data demo leaks a real "
    "name. A failed step gets papered over with invented success. The problem this lesson solves is making "
    "trust structural: permissions, evidence, and approval gates built into the workflow so safety doesn\u2019t "
    "depend on vigilance."
),
"steps": [
    ("Review the trust stack",
     "Scope, source, permission, preview, approval, verification, rollback \u2014 seven layers, in order. "
     "Every consequential action passes through all of them. The stack is the season\u2019s thesis in one "
     "diagram: BRAVE was the method; this is the safety architecture underneath it."),
    ("Separate reversible from consequential",
     "Researching, drafting, and building locally are reversible. Sending, publishing, purchasing, and "
     "deleting are not. The line between them is where permission lives \u2014 and crossing it without "
     "approval is the one unforgivable failure mode."),
    ("Build the \u201cshow me\u201d habit",
     "For everything the assistant claims: show me the source excerpt, the data count, the diff, the test "
     "result, the rendered page, the live URL. The habit is cheap and it catches nearly everything."),
    ("Run a preflight for private data",
     "Minimize, redact, anonymize \u2014 and never use another person\u2019s information in public "
     "demonstrations. Episode 4\u2019s privacy recipe becomes a standing preflight: check before the work "
     "starts, not after it ships."),
    ("Follow the failure protocol",
     "Stop. State what failed. Preserve completed work. Explain the consequence. Do not invent success. "
     "The protocol turns failures into recoverable incidents instead of hidden rot \u2014 and it\u2019s what "
     "makes the next step trustworthy."),
    ("Study the bug reel",
     "Real mistakes from real projects: an SMS direction mixup that flipped a whole analysis, a BLM "
     "terminology slip, stale travel data presented as fresh, a broken render shipped unreviewed, records "
     "lost to a replace-style update, a deployment with the wrong protection settings. Each one maps to a "
     "stack layer that would have caught it."),
    ("Ship the capstone \u2014 behind a human gate",
     "The season ends with a real ship: a human approval gate, then a visible verification pass \u2014 the "
     "completion report on screen (Completed, Evidence, Changed, Not completed, Decision needed, Next "
     "action). The audience watches the whole trust stack fire in sequence, one last time."),
],
"example": (
    "The capstone ship, narrated live: the work is previewed (scope \u2713, source \u2713, permission \u2713, "
    "preview \u2713), Chris approves at the gate (approval \u2713), the verification pass runs on screen \u2014 "
    "source links opened, counts reconciled, the live URL loaded and clicked through (verification \u2713) \u2014 "
    "and the rollback path is stated before anyone celebrates (rollback \u2713). Seven layers, ten minutes, "
    "zero drama. That\u2019s what \u201cshipped\u201d looks like when trust is structural."
),
"takeaways": [
    "Run the trust stack on consequential work: scope, source, permission, preview, approval, verification, rollback.",
    "Reversible and consequential are different universes \u2014 permission lives on the border.",
    "\u201cShow me\u201d everything: excerpts, counts, diffs, tests, rendered pages, live URLs.",
    "Preflight private data every time; follow the failure protocol when things break.",
    "Ship behind a human approval gate, and make the verification pass visible.",
],
},

}
