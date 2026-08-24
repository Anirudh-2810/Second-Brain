# Second Brain — Knowledge Base Index

> Master catalog of the BTech Knowledge Base (K.J. Somaiya / KJSCE).
> Organized by **Semester** and **Course Code**. Append every change to [[log]].

## How to Use
- Each `## Semester N` section lists course pages under **Courses** (concept nodes + unit pages).
- **Labs** and **Assessments** are cataloged under their own subheadings per semester.
- Course pages live in `/wiki/courses/`, labs in `/wiki/labs/`, assessments in `/wiki/assessments/`.
- Add courses under the correct semester header when ingesting new source material.


## 🗂 Domain Map

| Ask about… | Scan folder | Hub |
|---|---|---|
| 💼 Business / career / trading | `wiki/business/` | [[business/INDEX]] |
| 💻 Coding / DSA / case studies | `wiki/programming/` | [[programming/INDEX]] |
| 🤖 AI / ML / data science | `wiki/ai-data/` | [[ai-data/INDEX]] |
| ⚙️ Engineering coursework | `wiki/engineering/` | [[engineering/INDEX]] |
| 🧠 Self-dev / habits | `wiki/self-dev/` | [[self-dev/INDEX]] |
| 🔨 My builds | `wiki/builds/` | [[builds/INDEX]] |
| 🗺 All roadmaps | — | [[roadmaps/INDEX]] |

Browser dashboard: `index.html` (regenerate: `python .scripts/generate-index.py`).

---

## Semester 1

### Courses
- _(none ingested yet)_

### Labs
- _(none yet)_

### Assessments
- _(none yet)_

## Semester 2

### Courses
- _(none ingested yet)_

### Labs
- _(none yet)_

### Assessments
- _(none yet)_

## Semester 3

### Courses
- _(none ingested yet)_

### Labs
- _(none yet)_

### Assessments
- _(none yet)_

## Semester 4

### Courses
- _(none ingested yet)_

### Labs
- _(none yet)_

### Assessments
- _(none yet)_

## Semester 5

### Courses
- _(none ingested yet)_

### Labs
- _(none yet)_

### Assessments
- _(none yet)_

## Semester 6

### Courses
- _(none ingested yet)_

### Labs
- _(none yet)_

### Assessments
- _(none yet)_

## Semester 7

### Courses
- _(none ingested yet)_

### Labs
- _(none yet)_

### Assessments
- _(none yet)_

## Semester 8

### Courses
- _(none ingested yet)_

### Labs
- _(none yet)_

### Assessments
- _(none yet)_

---

## Cross-Cutting Modules

> Skill/topic clusters that are not tied to a single semester or course code.

### Programming & Computer Science
> Source: [[raw-sources/youtube_transcript.txt]] + 5 timestamped transcripts + JSON in `/raw-sources/`. One-page digest: vault-root `NOTES.md`.
> Main catalog: `[[modules/index#programming--computer-science|Programming & CS in the modules catalog]]`.
- **[[programming/overview|Programming — Theme Overview & Synthesis]]** — the 5-video "PROGRAM" operating loop + concept map + reading order (start here).
- **[[programming/cs50/index|Harvard CS50x — Full Course Notes]]** — Scratch · C · Arrays · Algorithms · Memory · Data Structures · Python · SQL · HTML/CSS/JS · Flask · Cybersecurity + [[programming/cs50/problem-sets|PSet catalog]]. The practiced, 11-week embodiment of the fundamentals.
- **[[programming/programming-cs-fundamentals|CS Fundamentals (21-segment deep dive)]]** — syntax, variables, conditionals, arrays, loops, errors, debugging, functions, imports, recursion, searching, pseudocode, language choice.
- **[[programming/math-for-programming|Why Programming Needs Math]]** — the ASCII donut: rotation matrices, dot-product shading, the "1% math edge."
- **[[programming/mathematics-of-creativity|The Mathematics of Creativity]]** — Genius = attempts × combinations × time × (chaos−order).
- **[[programming/winning-in-tech-art-of-winning|The Art of Winning in Tech]]** — surfer vs spectator, build-first, visible work, short feedback loops.
- **[[programming/learn-python-fast-system|Learn Python FAST — 6-Step System]]** — one course, embrace discomfort, AI-as-tutor, Codewars/Python Tutor, 30 Days of Python, build a SaaS.
- **[[programming/programming-flowcharts|Programming — Master Flowcharts]]** — learning / debug / build loops (Mermaid + ASCII).
- **[[programming/SAAS_BUILD_NOTES|SaaS Build Notes — JS Mastery LMS Course]]** — architectural roadmap, error mitigation matrix, 7-day execution plan, 10 vertical micro-SaaS concepts from the 3:56h Next.js/Supabase/Clerk/Stripe/Vapi course (XUkNR-JfHwo).

### Artificial Intelligence & Machine Learning
- Source: **5 Minutes Engineering — "Complete AI Artificial Intelligence in One Shot"** (Shridhar Mankar) — 9-hour YouTube course; video + playlist + video→module mapping in the hub.
- Main catalog: `[[modules/index#ai--ml-cross-cutting|AI / ML in the modules catalog]]`.
- **[[ai-data/ai/index|AI — Module Hub]]** — complete study library: syllabus map, reading order, video→module mapping (start here).
- **[[ai-data/ai/AI_MASTER_NOTES|AI Master Notes]]** — one-file master notes across all 6 modules (tables, diagrams, quick-revision summary).
- **[[ai-data/ai/sub-notes/MODULE_1_AI_FOUNDATIONS_AGENTS|Module 1 — AI Foundations & Agents]]** — AI vs human intelligence, AI⊇ML⊇DL⊇NLP, PEAS, agent architecture, 5 agent types.
- **[[ai-data/ai/sub-notes/MODULE_2_PROBLEM_SOLVING_SEARCH|Module 2 — Problem Solving & Search]]** — BFS/DFS/UCS/IDDFS, A* & AO*, minimax & alpha-beta, CSP backtracking & AC-3.
- **[[ai-data/ai/sub-notes/MODULE_3_KNOWLEDGE_REPRESENTATION_LOGIC|Module 3 — Knowledge Representation & Logic]]** — propositional & FOL, resolution & CNF, unification, chaining, semantic networks.
- **[[ai-data/ai/sub-notes/MODULE_4_FUZZY_LOGIC|Module 4 — Fuzzy Logic]]** — fuzzy sets, membership functions, FIS, Mamdani vs Sugeno, defuzzification, worked examples.
- **[[ai-data/ai/sub-notes/MODULE_5_PLANNING_NEURAL_NETWORKS|Module 5 — Planning & Neural Networks]]** — STRIPS & partial-order planning; perceptrons, MLP, backprop derivation.
- **[[ai-data/ai/sub-notes/MODULE_6_GENETIC_ALGORITHMS|Module 6 — Genetic Algorithms]]** — GA lifecycle, selection/crossover/mutation, schema theory, worked examples.

### Robotics & ROS2
> Source: docs.ros.org + design.ros2.org + docs.nav2.org (deep web research, 2026-08-17): distro cadence (Jazzy/Lyrical LTS), ROS2 architecture (nodes/topics/services/actions), DDS/QoS/discovery, tf2 + Nav2.
> Main catalog: `[[modules/index#robotics--ros2-cross-cutting|Robotics & ROS2 in the modules catalog]]`.
- **[[engineering/robotics/index|Robotics & ROS2 — Module Hub]]** — reading order, module map, autonomy-stack diagram (start here).
- **[[engineering/robotics/overview|Robotics — Overview & Mental Model]]** — the sense–plan–act loop, robot anatomy, software stack, vault connections.
- **[[engineering/robotics/robotics-fundamentals|Robotics Fundamentals]]** — sensors, actuators, kinematics, PID/MPC, Kalman/AMCL, SLAM, motion planning, perception.
- **[[engineering/robotics/ros2-architecture|ROS2 Architecture]]** — nodes · topics · services · actions · parameters · executors; ROS1 vs ROS2.
- **[[engineering/robotics/ros2-communication|ROS2 Communication]]** — DDS, QoS policies & profiles, discovery, domain ID, middleware vendors.
- **[[engineering/robotics/ros2-installation-setup|Installation & Setup]]** — distro pick (Jazzy), install, colcon workspace, first package.
- **[[engineering/robotics/ros2-beginner-guide|Beginner Guide]]** — turtlesim → publisher/subscriber → services/actions → tf2 → rviz2 → Gazebo → Nav2, with commands.
- **[[engineering/robotics/worked-example-odom-ekf|Worked Example — Odometry + EKF]]** — differential-drive odometry + 2D EKF fully implemented in rclpy, with a fake-robot simulator and verification.
- **[[engineering/robotics/ros2-tools-debugging|Tools & Debugging]]** — `ros2` CLI introspection, rqt/rviz2, rosbag, tf2 tools, Nav2 debug pipeline.
- **[[engineering/robotics/ros2-cheatsheet|ROS2 Cheat Sheet]]** — every command on one page.

### Object-Oriented Programming (Python)
> Source: Python official docs (Tutorial §9 Classes, Data Model, PEP 557/dataclasses), Real Python (OOP, Classes, Inheritance & Composition, SOLID, Magic Methods, Descriptors, Metaclasses, Data Classes), Refactoring Guru (design patterns in Python), *Fluent Python* (Ramalho).
> Main catalog: `[[modules/index#object-oriented-programming-in-python-cross-cutting|OOP in the modules catalog]]`.
- **[[programming/object-oriented-programming/overview|OOP in Python — Theme Overview & Synthesis]]** — the 4-pillar system, concept map, source registry, reading order, golden rules (start here).
- **[[programming/object-oriented-programming/oop-foundations|OOP Foundations]]** — classes/objects/`self`/`__init__`, class vs instance attributes, 3 method kinds, `__dict__`, diagrams.
- **[[programming/object-oriented-programming/the-four-pillars|The Four Pillars]]** — encapsulation · abstraction · inheritance · polymorphism as one system with a working mini-design.
- **[[programming/object-oriented-programming/inheritance|Inheritance Deep Dive]]** — MRO, cooperative `super()`, diamond problem, mixins, ABCs, is-a vs has-a.
- **[[programming/object-oriented-programming/polymorphism|Polymorphism Deep Dive]]** — duck typing, overriding, operator overloading, `Protocol`, `singledispatch`.
- **[[programming/object-oriented-programming/magic-methods-dunder|Dunder Methods — Complete Reference]]** — every special method by category + protocols + idioms.
- **[[programming/object-oriented-programming/properties-and-descriptors|Properties & Descriptors]]** — `@property`, descriptor protocol, attribute lookup chain, `__slots__`.
- **[[programming/object-oriented-programming/design-principles-solid|SOLID Design Principles]]** — SRP/OCP/LSP/ISP/DIP with before/after Python + decision flowchart.
- **[[programming/object-oriented-programming/design-patterns|Design Patterns (Pythonic GoF)]]** — Singleton/Factory/Strategy/Observer/Template-Method/State/Adapter/Decorator + language-feature shortcuts.
- **[[programming/object-oriented-programming/modern-oop-dataclasses-typing|Modern OOP — Dataclasses & Typing]]** — `@dataclass` flags, `field()`, `__post_init__`, NamedTuple, Protocols, generics, pattern matching.
- **[[programming/object-oriented-programming/advanced-metaprogramming|Advanced OOP & Metaprogramming]]** — `__new__`, metaclasses, lookup chain, introspection.
- **[[programming/object-oriented-programming/cheatsheet|OOP Master Cheat Sheet]]** · **[[programming/object-oriented-programming/flowcharts|OOP Master Flowcharts]]** · **[[programming/object-oriented-programming/interview-questions|OOP Interview Q&A (34)]]** — reference + decision diagrams + interview bank.

### Quant Finance
- **Course**: _none assigned (self-study)_. Textbook: John C. Hull, *Options, Futures, and Other Derivatives*.
- Source: [[raw-sources/quant-finance-basics]] + primary PDFs (GGR pairs, Faber TAA, Jegadeesh-Titman momentum, Asness-Moskowitz-Pedersen V+M).
- Main catalog: `[[modules/index#quant-finance|Quant Finance in the modules catalog]]`.
- **[[quantitative-finance-foundations]]** — Module overview & core areas.
- **[[derivatives-options-futures]]** — Options, futures & other derivatives (Hull).
- **[[stochastic-calculus-black-scholes]]** — Ito's Lemma, GBM, Black-Scholes PDE.
- **[[market-microstructure]]** — Order books, liquidity, market makers, execution algos.
- **[[quant-toolkit-and-skills]]** — Linear algebra, probability, NumPy/pandas, C++.

#### Classic Strategy Deep Dives (primary-source analysis)
- **[[pairs-trading-gatev-goetzmann-rouwenhorst]]** — GGR (2006): SSD pair formation, z-score mean reversion, 11% ann. excess, bootstrap validation.
- **[[tactical-asset-allocation-faber]]** — Faber (2006/2013): 10-month SMA across 8–10 asset classes, equity-like returns / bond-like drawdowns.
- **[[momentum-jegadeesh-titman]]** — Jegadeesh & Titman (1993): J=12/K=1/skip-1 canonical momentum, 1.5%/mo, crashes & protection.
- **[[value-momentum-everywhere-asness-moskowitz-pedersen]]** — AMP (2013): 48 assets × 8 classes, global 3-factor model, value↔mom ρ=−0.6.
- **[[value-momentum-everywhere-deep-dive]]** — Extended AMP: full tables, alt bond value measures, liquidity risk, hedge fund pricing.
- **[[quant-finance-strategy-hub]]** — Integrated hub: master map, unified pipeline, correlation matrix, risk framework, parameter cheat sheet.

### Productivity & Systems
- Source: [[raw-sources/productivity-and-system]], `/raw-sources/_extracted/` (Focus · Little Book of Productivity · 101 Ways · APO Handbook · GTD full text).
- Main catalog: `[[modules/index#productivity--systems-cross-cutting|Productivity & Systems in the modules catalog]]`.
- **[[self-dev/productivity/overview|Productivity — Theme Overview & Synthesis]]** — the 8-pillar operating model + full source registry (start here).
- **[[self-dev/productivity/productive-flowchart|The Productive Loop — Flow Chart]]** — Mermaid + ASCII state machine for becoming productive.
- **[[deep-work-attention-economics]]** — Distraction-free concentration, attention residue, 4 execution disciplines.
- **[[pkm-code-framework]]** — CODE (Capture–Organize–Distill–Express) + PARA, Progressive Summarization.
- **[[atomic-habits-systems]]** — Identity-based habits & the Four Laws of Behavior Change.
- **[[gtd-task-management]]** — Capture–Clarify–Organize–Reflect–Engage; weekly review.
- **[[mental-models-for-execution]]** — Pareto, Eisenhower Matrix, Parkinson's Law, Inversion.
- **[[self-dev/productivity/focus-minimalism-babauta|Focus & Minimalism (Babauta)]]** · **[[self-dev/productivity/little-book-productivity-scott-young|Little Book (Scott Young)]]** · **[[self-dev/productivity/101-ways-workplace-productivity-fishel|101 Ways (Fishel)]]** · **[[self-dev/productivity/apo-handbook-productivity|APO Handbook]]** — research-source node pages.

### Self-Mastery
- Source: `/raw-sources/slice0*.txt.md` (7-slice normalized transcript of the *How To Level Up So Fast It Feels Like CHEATING* corpus). One-page digest: vault-root `NOTES.md`.
- Main catalog: `[[modules/index#self-mastery-cross-cutting|Self-Mastery in the modules catalog]]`.
- **[[self-dev/self-mastery/overview|Self-Mastery — Theme Overview & Synthesis]]** — the "LEVEL" operating loop + five cross-cutting laws + concept map + reading order (start here).
- **[[self-dev/self-mastery/belief-engineering|Belief Engineering]]** — placebo/nocebo science, belief audit, strategic delusion, superposition of self.
- **[[self-dev/self-mastery/manifestation-quadrant|The Manifestation Quadrant]]** — desire→belief→behavior→field, vacuum principle, effortless achievement, pain-as-fuel.
- **[[self-dev/self-mastery/subconscious-reprogramming|Subconscious Reprogramming]]** — hysteresis/compression, theta rehearsal, identity stack, borrowed vs true state, purpose antidote.
- **[[self-dev/self-mastery/psychological-execution|Psychological Execution]]** — overthinking, discipline design, dopamine protocol, boredom tolerance, god mode.
- **[[self-dev/self-mastery/life-systems-design|Life Systems Design]]** — thermostat & 1-week/12-month, learner's life, consistency, hyperfocus, subtraction, 24-hour empire.
- **[[self-dev/self-mastery/temptation-mastery|Temptation Mastery]]** - BHATT video distillation: 8-part arc, fortress model, refusal scripts + evidence-linked mechanisms. (2026-08-24)
- **[[self-dev/self-mastery/self-mastery-flowcharts|Self-Mastery — Master Flowcharts]]** — all runbooks as Mermaid + ASCII state machines.

### Stock Agent
> Deep-analysis module for the **user-built algorithmic trading platform** at `C:\Users\Vijaykumar\stock-agent` (Alpaca paper trading + FastAPI + React + ML). Main catalog: `[[modules/index#stock-agent-cross-cutting|Stock Agent in the modules catalog]]`.
- **[[builds/stock-agent/overview|Stock Agent — Overview & System Map]]** — what it is, stack, data flow, status at a glance.
- **[[builds/stock-agent/deep-review-report|Full-Depth Review Report]]** — strengths, 18 verified bugs (file:line), and a 5-phase action plan.
- **[[builds/stock-agent/architecture|Architecture Deep Dive]]** — routers, core, execution guards, ingestion, ML, frontend, deployment.
- **[[builds/stock-agent/functions-and-features|Functions & Features Inventory]]** — everything the app does, with endpoints.
- **[[builds/stock-agent/what-works-and-fails|What Works & Where It Fails]]** — honest scorecard (live-data gap, scheduler off, ML gaps, security).
- **[[builds/stock-agent/value-and-standalone|Value, Standalone Position & Potential]]** — what it helps you do and its current potential.
- **[[builds/stock-agent/improvement-roadmap|Improvement Roadmap (P0–P3)]]** — prioritized fixes with files, order, and checklist.

### German A1
> Free self-study using DW *Nicos Weg* + Goethe-Institut exercises. Main catalog: `[[modules/index#german-a1-cross-cutting|German A1 in the modules catalog]]`.
- **[[self-dev/german/overview|German A1 — Overview & Roadmap]]** — what A1 covers, 8-week plan, Goethe exam format, sources.
- **[[self-dev/german/alphabet-and-pronunciation|Alphabet & Pronunciation]]** — sounds, umlauts, ß, stress, pronunciation traps.
- **[[self-dev/german/grammar-essentials|Grammar Essentials (quick)]]** — the fast track: articles, sein/haben, word order, negation.
- **[[self-dev/german/nouns-and-cases|Nouns & Cases]]** — full declension tables, gender rules, plurals, pronouns, contractions.
- **[[self-dev/german/verbs-conjugation|Verbs & Conjugation]]** — strong verbs, separable verbs, modals, Perfekt, reflexive, imperative.
- **[[self-dev/german/word-order-and-questions|Word Order & Questions]]** — sentence bracket, W-words, negation, denn/weil.
- **[[self-dev/german/prepositions|Prepositions]]** — dative/accusative families + the two-way Wo?/Wohin? rule.
- **[[self-dev/german/adjectives-and-possessives|Adjectives & Possessives]]** — endings, mein/dein, dieser, comparatives.
- **[[self-dev/german/vocabulary-and-phrases|Vocabulary & Phrases]]** — all A1 exam themes + top 25 verbs.
- **[[self-dev/german/phrasebook-cheatsheet|Phrasebook Cheat Sheet]]** — one-page survival phrases for every situation.
- **[[self-dev/german/practice-and-exercises|Practice & Exercises]]** — 98-point test with answer key and scoring guide.

### Engineering Drawing
> Source: **N.D. Bhatt** + **BIS SP 46:2003** (line types, lettering, dimensioning). Main catalog: `[[modules/index#engineering-drawing-cross-cutting|Engineering Drawing in the modules catalog]]`.
- **[[engineering/engineering-drawing/overview|Overview — Beginner's Guide]]** — the universal language of engineers: tools, line types, scales, lettering, dimensioning.
- **[[engineering/engineering-drawing/orthographic-projections|Orthographic Projections]]** — first/third angle, HP/VP, points → lines → planes → solids.
- **[[engineering/engineering-drawing/isometric-and-sections|Isometric & Sections]]** — 3D views + cut-open sectional views.

### Mathematics
- Source: `/raw-sources/math/` (Algebra, Calculus, Coordinate, Trigonometry, Vector 3D, Math IIT Kota notes, Formula sheets). One-page digest: vault-root `NOTES.md`.
- Main catalog: `[[modules/index#mathematics-cross-cutting|Mathematics in the modules catalog]]`.
- **[[engineering/mathematics/overview|Mathematics — Theme Overview & Synthesis]]** — complete topic map (Algebra, Calculus, Coordinate, Trigonometry, Vector 3D), source registry, study strategy, high-yield topics (start here).
- **[[engineering/mathematics/formula-sheet-master|Mathematics Formula Sheet — Master]]** — complete compendium: Algebra, Calculus, Coordinate, Trigonometry, Vector & 3D, DE.
- **[[engineering/mathematics/formula-sheet-trigonometry|Trigonometry Formula Sheet]]** — specialized compendium: compound angles, multiple angles, transformations, equations, inverse trig, triangle properties.
- **[[engineering/mathematics/quick-revision-cards|Quick Revision Cards]]** — 18 ultra-condensed cards for final 48 hours.

### Chemistry
- Source: `/raw-sources/Chem/` (Atomic Structure, Organic Chemistry Brahmastra, Chemistry IIT Kota notes: 30+ chapters). One-page digest: vault-root `NOTES.md`.
- Main catalog: `[[modules/index#chemistry-cross-cutting|Chemistry in the modules catalog]]`.
- **[[engineering/chemistry/overview|Chemistry — Theme Overview & Synthesis]]** — complete topic map (Physical, Organic, Inorganic), source registry, study strategy, high-yield topics (start here).
- **[[engineering/chemistry/formula-sheet-physical|Physical Chemistry Formula Sheet]]** — complete compendium: Thermodynamics, Equilibrium, Ionic Eq, Electrochemistry, Kinetics, States of Matter, Solid State, Solutions, Surface Chem, Atomic Structure, Bonding.
- **[[engineering/chemistry/formula-sheet-organic|Organic Chemistry Reaction Map]]** — complete reaction map: GOC effects, hydrocarbons, alkyl halides, alcohols/phenols/ethers, carbonyls, carboxylic acids/derivatives, amines, aromatics, biomolecules, polymers, named reactions (100+).
- **[[engineering/chemistry/formula-sheet-inorganic|Inorganic Trends & Exceptions]]** — trends & exceptions compendium: periodic trends, diagonal relationships, all group anomalies, d-block exceptions, f-block, coordination exceptions, qualitative analysis.

### Physics
- Source: `/raw-sources/Physics/` (Physics IIT Kota notes: 17 chapters, Practice questions). One-page digest: vault-root `NOTES.md`.
- Main catalog: `[[modules/index#physics-cross-cutting|Physics in the modules catalog]]`.
- **[[engineering/physics/overview|Physics — Theme Overview & Synthesis]]** — complete topic map (Mechanics, Electrodynamics, Optics, Modern, Thermal, Waves), source registry, study strategy, high-yield topics (start here).
- **[[engineering/physics/formula-sheet-mechanics|Mechanics Formula Sheet]]** — complete compendium: Kinematics, Laws of Motion, Work-Energy-Power, Rotational, Gravitation, Fluid Mechanics, Properties of Matter, COM & Collisions.
- **[[engineering/physics/formula-sheet-electrodynamics|Electrodynamics Formula Sheet]]** — complete compendium: Electrostatics, Capacitors, Current Electricity, Magnetic Effects, EMI, AC, EM Waves.
- **[[engineering/physics/formula-sheet-optics|Optics Formula Sheet]]** — complete compendium: Ray (mirrors, lenses, prisms), Wave (YDS, thin film, diffraction, polarization), Instruments.
- **[[engineering/physics/formula-sheet-modern|Modern Physics Formula Sheet]]** — complete compendium: Dual nature, Atomic (Bohr, spectra), Nuclear (radioactivity, fission/fusion), Semiconductors (diodes, transistors, logic), Communication.
- **[[engineering/physics/formula-sheet-thermal-waves|Thermal & Waves Formula Sheet]]** — complete compendium: Thermodynamics (laws, processes, Carnot, entropy), Kinetic Theory, Heat Transfer, Calorimetry, SHM, Waves, Sound, Doppler.

### Projects (owner's GitHub — [Anirudh-2810](https://github.com/Anirudh-2810))
> Portfolio repos distilled into wiki pages. Catalog: `[[builds/projects/index|Projects catalog]]`.
- **[[builds/projects/inventory-system|StockOffline (inventory-system)]]** — offline-first inventory manager: zero-dep GUI/CLI + secured multi-user web tier, packaged as Windows exe.
- **[[builds/projects/algorithm101-aura|AURA — Neural Trend Engine (Algorithm101)]]** — YouTube music-trend dashboard with velocity scoring & viral prediction; quant-DNA cross-links.
- **[[builds/projects/handsens101|handsens101]]** — MediaPipe hand-gesture mouse control; perception→action pipeline.

### Retrieval Agent (Business Brain)
> n8n + Supabase Edge Function grounded Q&A agent. Never answers from own knowledge — only from vector-searched brain. Catalog: `[[builds/retrieval-agent/overview|Retrieval Agent Overview]]`.
- **[[builds/retrieval-agent/overview|System Overview]]** — architecture, components, data model, system prompt rules
- **[[builds/retrieval-agent/n8n-setup|n8n Configuration]]** — Chat Trigger, AI Agent, HTTP Request tool, system prompt
- **[[builds/retrieval-agent/edge-function|Supabase Edge Function]]** — Deno/TypeScript vector search API (embed + search modes)
- **[[builds/retrieval-agent/retrieval-agent|Agent Behavior]]** — search-first, multi-search, refusal logic, confidence weighting
- **[[builds/retrieval-agent/database-schema|Database Schema]]** — brain_chunks table, IVFFLAT index, RPC, RLS, maintenance


### Data Science & Machine Learning (field module)
> Theory, frameworks, topics, roadmaps, interview prep + expanded learning-resource repos. Hub: `[[ai-data/data-science/index|Data Science Field Index]]`.
- **[[ai-data/data-science/ml-theory-and-moocs|ML Theory & MOOCs]]** · **[[ai-data/data-science/python-datascience-frameworks|DS Frameworks]]** · **[[ai-data/data-science/python-datascience-topics|DS Topics]]** · **[[ai-data/data-science/mlops-production-deployment|MLOps & Production]]** · **[[ai-data/data-science/curated-reading-list|Curated Reading List (~190 essays)]]**
- Roadmaps: **[[ai-data/data-science/roadmap-data-scientist|DS Roadmap]]** · **[[ai-data/data-science/roadmap-ml-engineer|MLE Roadmap (incl. GenAI branch)]]** — with exit tests & quit points
- Prep: **[[ai-data/data-science/ml-interview-playbook|ML Interview Playbook]]** · **[[ai-data/data-science/kaggle-and-practice-guide|Kaggle Guide]]** · **[[ai-data/data-science/math-for-ml-survival-guide|Math Survival Guide]]**
- Expanded repos: [[ai-data/data-science/repo-ossu-data-science|OSSU DS]] · [[ai-data/data-science/repo-ml-roadmaps-mindmaps|ML Roadmaps/Mindmaps]] · [[ai-data/data-science/repo-ds-interviews-grigorev|DS Interviews Bank]] · [[ai-data/data-science/repo-mlcourse-ai|mlcourse.ai]] · [[ai-data/data-science/repo-awesome-deep-learning-papers|DL Papers Canon]] · [[ai-data/data-science/repo-tf-pytorch-learning-stack|TF/PyTorch Stack]] · [[ai-data/data-science/repo-data-engineer-roadmap|Data Engineer Roadmap]]

### Systems Design & Distributed Systems (field module)
> Building blocks, interview method, canonical study repo, case-study catalogs. Hub: `[[programming/systems-design/index|Systems Design Index]]`.
- **[[programming/systems-design/systems-design-distributed|Systems Design Reference]]** · **[[programming/systems-design/system-design-interview|System Design Interview Playbook]]** · **[[programming/systems-design/repo-system-design-primer|System Design Primer Expanded]]** · **[[programming/systems-design/repo-scalability-catalogs|Scalability Case-Study Catalogs]]**

### Web Development (field module)
> Resources + frontend/fullstack learning paths. Hub: `[[programming/web-development/index|Web Dev Index]]`.
- **[[programming/web-development/web-development-resources|Web Dev Resources]]** · **[[programming/web-development/repo-frontend-learning-resources|Frontend Resources & Handbook]]** · **[[programming/web-development/repo-fullstack-web-developer-path|Fullstack Path (week-by-week)]]**

### Learning Resource Catalogs (field module)
> The mega-catalogs (awesome, freeCodeCamp, OSSU CS, build-your-own-x...) converted into systems with anti-hoarding protocols. Hub: `[[programming/learning-resources/index|Learning Resources Index]]`.
- **[[programming/learning-resources/lr-awesome-meta|Awesome Meta-Catalog]]** · **[[programming/learning-resources/lr-free-for-dev|Free-for-Dev Tiers]]** · **[[programming/learning-resources/lr-free-programming-books|Free Programming Books]]** · **[[programming/learning-resources/lr-freecodecamp|freeCodeCamp]]** · **[[programming/learning-resources/lr-30soc-pbl|30-Seconds-of-Code + Project-Based Learning]]** · **[[programming/learning-resources/lr-developer-roadmap|roadmap.sh Developer Roadmaps]]** · **[[programming/learning-resources/lr-ossu-computer-science|OSSU Computer Science]]** · **[[programming/learning-resources/lr-build-your-own-x|Build Your Own X]]**

### Open-Source Case Studies (field module)
> Real codebases analyzed: architecture, extraction lessons, failure modes. Hub: `[[programming/case-studies/index|Case Studies Index]]`.
- Production ML: **[[programming/case-studies/cs-twitter-algorithm|X/Twitter Recommendation Algorithm]]**
- Historic/foundational: **[[programming/case-studies/cs-apollo-11|Apollo-11 Guidance Computer]]** · **[[programming/case-studies/cs-openusd|OpenUSD]]**
- Applications & tools: **[[programming/case-studies/cs-zulip|Zulip]]** · **[[programming/case-studies/cs-hydra-launcher|Hydra Launcher]]** · **[[programming/case-studies/cs-systeminformer-spyplusplus|System Informer + Spy++]]** · **[[programming/case-studies/cs-jj-vcs|Jujutsu VCS]]** · **[[programming/case-studies/cs-dura-z-tinytools|Dura + z Tiny Tools]]** · **[[programming/case-studies/cs-snekbox|Snekbox Sandbox]]** · **[[programming/case-studies/cs-liveportrait|LivePortrait]]** · **[[programming/case-studies/cs-treemaker-malt|TreeMaker + Malt]]**
- Lifecycle/ethics studies: **[[programming/case-studies/cs-riot-actionscript|Riot.js + ActionScript4]]** · **[[programming/case-studies/cs-gpt4free|gpt4free ⚠️ ethics study]]**

### Careers, Market & Interview Prep (field module)
> 2026 market analysis, interview system, portfolio playbook. Hub: `[[business/careers/index|Careers Index]]`.
- **[[business/careers/market-analysis-tech-2026|Market Analysis 2026 (sourced)]]** · **[[business/careers/interview-counter-guide|Interview Counter-Guide]]** · **[[business/careers/build-project-playbook|Build-Project Playbook]]** · **[[business/careers/example-question-bank|Question Bank]]** · **[[business/careers/roadmaps-and-study-guides|Roadmap Catalog]]**
---

## Ingest Checklist (per course)
1. [ ] Concept pages created in `/wiki/courses/` with YAML frontmatter.
2. [ ] Cross-links added between related pages.
3. [ ] Course added to the correct semester above.
4. [ ] Entry appended to `/wiki/log.md`.