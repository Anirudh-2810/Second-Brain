---
tags: [wiki, modules, catalog]
last_updated: "2026-08-13"
---

# Modules Catalog

> Cross-disciplinary modules and skill areas that sit outside the per-semester course structure.
> Like courses, each module is a cluster of [[wiki]] node pages with YAML frontmatter.

## Quant Finance

- **[[quantitative-finance-foundations]]** — Overview: disciplines, core areas, and learning path.
- **[[stochastic-calculus-black-scholes]]** — Continuous-time finance, Itô's Lemma (full proof), the Black–Scholes PDE derivation, closed form, Greeks; Python + C++20 pricers.
- **[[derivatives-options-futures]]** — Forwards/futures/options mechanics, put–call parity, CRR binomial tree.
- **[[markowitz-portfolio-theory]]** — Mean-variance optimization, efficient frontier derivation (Lagrange), two-fund + tangency portfolio; Python/Eigen code.
- **[[general-equilibrium-and-capm]]** — CAPM/SML derivation, beta, systematic vs idiosyncratic risk, factor models.
- **[[portfolio-optimization-practice]]** — Shrinkage, factor/clustering covariance, robust optimization, practical constraints.
- **[[model-estimation]]** — OLS, MLE, GMM, Ledoit–Wolf shrinkage, PCA/SVD, Kalman filter.
- **[[predictive-return-models]]** — Predictive regressions, cointegration, pairs trading, VAR/VECM.
- **[[model-selection-and-model-risk]]** — Overfitting, data snooping, walk-forward discipline, regularization.
- **[[forecasting-and-market-efficiency]]** — EMH, martingale view, long-horizon predictability, statistical traps.
- **[[risk-management-value-at-risk]]** — VaR/CVaR, stress testing, Monte Carlo risk, credit & copulas.
- **[[applications-of-quantitative-finance]]** — ESG integration, rare-event limitations, applied scope.
- **[[market-microstructure]]** — Limit order books, liquidity, impact, optimal execution.
- **[[quant-toolkit-and-skills]]** — Python (NumPy/pandas) & C++20 stack, engineering rigor.
- **[[quant-careers-and-industry]]** — Roles, buy/sell-side, skills matrix, industry survey.
- **[[learning-roadmap-and-study-plan]]** — Orchestrated study path; maps BTech assignments to modules.

### Classic Strategy Deep Dives (from primary sources)

> Primary PDFs: [[raw-sources/pairs-trading-performance-of-a-relative-value-arbitrage-rule.pdf|GGR (2006)]] · [[raw-sources/a-quantitative-approach-to-tactical-asset-allocation.pdf|Faber (2006)]] · [[raw-sources/jegadeesh-titman93.pdf|Jegadeesh–Titman (1993)]] · [[raw-sources/lasse_heje_pedersen_value_and_momentum_postprint.pdf|AMP Value & Momentum (2013)]].

- **[[pairs-trading-gatev-goetzmann-rouwenhorst]]** — GGR (2006): SSD pair formation, z-score mean reversion, 11% ann. excess, bootstrap validation, sector breakdowns, transaction-cost analysis.
- **[[tactical-asset-allocation-faber]]** — Faber (2006/2013): 10-month SMA across 8–10 asset classes, equity-like returns with bond-like drawdowns, vol-targeting, leverage, whipsaw filters.
- **[[momentum-jegadeesh-titman]]** — Jegadeesh & Titman (1993): J=12/K=1/skip-1 canonical momentum factor, 1.5%/mo pre-cost, January effect, momentum crashes, residual & time-series variants.
- **[[value-momentum-everywhere-asness-moskowitz-pedersen]]** — Asness, Moskowitz & Pedersen (2013): 48 test assets across 8 asset classes, value↔value ρ≈0.68, mom↔mom ρ≈0.65, value↔mom ρ≈−0.60, global 3-factor model.
- **[[value-momentum-everywhere-deep-dive]]** — Extended AMP: full Table I/II reproduction, alternative bond value measures, liquidity-risk regressions, 3-factor pricing of FF portfolios & hedge funds.
- **[[quant-finance-strategy-hub]]** — Integrated hub: master strategy map, unified pipeline, cross-strategy correlation matrix, 3-factor extensions, risk framework, decision tree, parameter cheat sheet.

## Programming & Computer Science (cross-cutting)

> First-principles CS + the modern builder's mindset, distilled from the 5-video YouTube corpus ([[raw-sources/youtube_transcript.txt]] → `/raw-sources/youtube-transcript-*.txt`). Raw transcript digest: `[[programming/yt info]]`. Summary digest at vault-root `NOTES.md`.

- **[[programming/overview]]** — module synthesis: the 5-video "PROGRAM loop," concept map, and reading order (start here).
- **[[programming/cs50/index]]** — *Harvard CS50x* full course notes: 11-week syllabus (Scratch → C → Arrays → Algorithms → Memory → Data Structures → Python → SQL → Web → Flask → Cybersecurity) + PSet catalog. Start here to turn fundamentals into a practiced curriculum.
- **[[programming/programming-cs-fundamentals]]** — universal language-agnostic CS: syntax, variables, conditionals, arrays, loops, errors, debugging, functions, imports, recursion, searching (Big-O), pseudocode.
- **[[programming/math-for-programming]]** — the ASCII donut case study: rotation matrices, dot-product shading, math's "1% edge" (graphics/ML/crypto).
- **[[programming/mathematics-of-creativity]]** — creativity = attempts × combinations × time × (chaos−order); Simonton, Zipf's law, Boden, exponential growth, edge of chaos.
- **[[programming/winning-in-tech-art-of-winning]]** — spectator vs surfer; short feedback loops; build visibly; stop self-negotiating.
- **[[programming/learn-python-fast-system]]** — concrete 6-step Python fast-track: one course, discomfort, AI-as-tutor, Codewars, 30 Days of Python, SaaS.
- **[[programming/programming-flowcharts]]** — learning / debug / build loops as Mermaid + ASCII state machines.
- **[[programming/SAAS_BUILD_NOTES]]** — complete breakdown of JavaScript Mastery LMS SaaS course (XUkNR-JfHwo): architectural roadmap, error mitigation matrix (14 failure modes), 7-day execution plan, 10 fail-proof micro-SaaS concepts with vertical niches.
- **[[programming/c-programming/index]]** — *Bro Code's C Programming Full Course* (xND0t1pr3KY): beginner's guide (IDE + compiler setup), C essentials for absolute beginners (zero-prior-knowledge), detailed notes (16 topics), Mermaid/ASCII flowcharts, 13 hands-on projects (circle circumference → digital clock), 15 ready-to-run `.c` files, and a 45+ problem solved practice bank with trace tables (basics → operators → conditionals → loops → arrays → sorting → strings → functions → pointers → structs).
- **[[programming/cs50p/final-project-planner]]** — *CS50P (Introduction to Programming with Python)* final project planner for a Terminal Task & Habit Tracker CLI: verified CS50P rules (differ from CS50x — fixed `2022/python/project` slug, ~500-word README, `cs50.me/cs50p` gradebook), `data.json` schema, function designs + pytest test matrix, 5-phase roadmap, submission steps, and master checklist.
- **[[robotics/roadmap|Robotics & AI Engineering Roadmap (2026)]]**: modern, job-ready path combining the classical robotics backbone (math, C++/Python, ROS2, SLAM, control) with the 2026 AI stack (VLA foundation models — GR00T N1.6, π0, Gemini Robotics, SmolVLA — sim-to-real, imitation/RL, edge AI). Includes 8 stages, 12-month timeline, tool cheat-sheet, and master checklist.

## Object-Oriented Programming in Python (cross-cutting)

> Full note library for **object-oriented Python**: mental model → four pillars → inheritance internals → dunders → properties/descriptors → SOLID → design patterns → dataclasses/typing → metaprogramming. Sources: Python official docs (Tutorial §9, Data Model, PEP 557), Real Python, Refactoring Guru, *Fluent Python*.

- **[[object-oriented-programming/overview]]** — module synthesis: OOP definition, the 4 pillars table, concept map, source registry, reading order, golden rules (start here).
- **[[object-oriented-programming/oop-foundations]]** — classes as blueprints, objects as instances, `self`, `__init__`, class vs instance attributes, the 3 method kinds, `__dict__`, namespace diagrams, pitfalls.
- **[[object-oriented-programming/the-four-pillars]]** — encapsulation, abstraction, inheritance, polymorphism as one system; Python-specific delivery (conventions, ABCs, duck typing).
- **[[object-oriented-programming/inheritance]]** — single/multiple inheritance, MRO & C3 linearization, cooperative `super()`, the diamond problem, mixins, ABCs, inheritance-vs-composition decision tree.
- **[[object-oriented-programming/polymorphism]]** — duck typing (EAFP), method overriding, operator overloading, `typing.Protocol` (structural typing), `functools.singledispatch`.
- **[[object-oriented-programming/magic-methods-dunder]]** — complete dunder reference by category (lifecycle, repr, comparison, arithmetic, containers, call/context, attributes, slots) + protocols + idioms.
- **[[object-oriented-programming/properties-and-descriptors]]** — `@property`, `cached_property`, the descriptor protocol, full attribute lookup chain, data vs non-data descriptors, `__slots__`.
- **[[object-oriented-programming/design-principles-solid]]** — SRP, OCP, LSP, ISP, DIP with before/after Python code; composition-over-inheritance; SOLID decision flowchart.
- **[[object-oriented-programming/design-patterns]]** — GoF patterns made Pythonic: Singleton/Factory/Builder, Adapter/Decorator/Facade/Proxy, Strategy/Observer/Template-Method/State; dict-registry & callable idioms.
- **[[object-oriented-programming/modern-oop-dataclasses-typing]]** — `@dataclass` (all flags), `field()`/`default_factory`, `__post_init__`, dataclass-vs-NamedTuple, generics/`Self`/`@final`, `match`/`case` over objects.
- **[[object-oriented-programming/advanced-metaprogramming]]** — `__new__` vs `__init__`, metaclasses (`type`, custom metaclasses), the full attribute lookup chain, `__getattr__`/`__getattribute__`, introspection toolkit.
- **[[object-oriented-programming/cheatsheet]]** — one-page compressed reference (vocabulary, skeleton, method matrix, pillars, inheritance codes, top dunders, dataclass flags, SOLID, patterns).
- **[[object-oriented-programming/flowcharts]]** — master flowcharts: class-design loop, inheritance-vs-composition, method-kind picker, dunder picker, pattern picker, learning loop (Mermaid + ASCII).
- **[[object-oriented-programming/interview-questions]]** — 34 curated Q&A across 5 levels (fundamentals → inheritance → dunders → design → modern Python) + mini coding challenges.

## Excel & VBA (cross-cutting)

> Mac-native Excel VBA financial-modeling workbooks: rebuild notes and standalone templates.

- **[[excel workflows/FinancialAdvisor_RebuildNotes]]** — Financial Advisor cash-flow model rebuild: Scripting.Dictionary → Collection, variance sign-convention fix (Actual − Budget), runtime OS detection, font auto-switching.
- **[[excel workflows/Budget_Tracker_Basic]]** — Standalone budget tracker workbook (simplified from the Financial Advisor model): no ActiveX, no Scripting.Dictionary, runtime OS detection, Indian Rupee (₹) formatting.

## AI / ML (cross-cutting)

> Complete study library for **5 Minutes Engineering's** "Complete AI Artificial Intelligence in One Shot" (9h YouTube course): 6 modules + master notes. ML/quant implementations live in `ai-ml/`.

- **[[ai/index]]** — AI module hub: syllabus map, reading order, video→module mapping (start here).
- **[[ai/AI_MASTER_NOTES]]** — master notes covering all 6 modules (syllabus map, tables, diagrams, quick-revision summary).
- **[[ai/sub-notes/MODULE_1_AI_FOUNDATIONS_AGENTS]]** — AI foundations & agents: definitions, AI⊇ML⊇DL⊇NLP, PEAS, agent architecture, 5 agent types.
- **[[ai/sub-notes/MODULE_2_PROBLEM_SOLVING_SEARCH]]** — problem solving & search: BFS/DFS/UCS/IDDFS, A* & AO*, minimax & alpha-beta, CSP backtracking & AC-3.
- **[[ai/sub-notes/MODULE_3_KNOWLEDGE_REPRESENTATION_LOGIC]]** — knowledge representation & logic: propositional/FOL, resolution & CNF, unification, chaining, semantic networks.
- **[[ai/sub-notes/MODULE_4_FUZZY_LOGIC]]** — fuzzy logic: fuzzy sets, membership functions, FIS, Mamdani vs Sugeno, defuzzification.
- **[[ai/sub-notes/MODULE_5_PLANNING_NEURAL_NETWORKS]]** — planning & neural networks: STRIPS, goal-stack & partial-order planning; perceptrons, MLP, backprop.
- **[[ai/sub-notes/MODULE_6_GENETIC_ALGORITHMS]]** — genetic algorithms: lifecycle, encodings, selection/crossover/mutation, schema theory, worked examples.
- **[[reinforcement-learning-ppo]]** — Policy gradient → GAE → clipped PPO objective (full derivation), actor-critic, PyTorch code.
- **[[transformers-attention-detail]]** — Self-attention math, multi-head, transformer block, causal masking, from-scratch code.
- **[[matching-engine-cpp]]** — C++20 limit-order matching engine design & implementation.
- **[[event-driven-backtesting]]** — Event-driven architecture, look-ahead discipline, cost models, Python + C++ skeleton.


## Data Science & Machine Learning (field module)

> Learning resources, roadmaps, and prep for the DS/ML field. Hub: [[modules/data-science/index|Data Science Field Index]].

- **[[ml-theory-and-moocs]]** - Canonical references + tiered MOOC catalog + concept explainers.
- **[[python-datascience-frameworks]]** - pandas/sklearn, XGBoost/LightGBM/CatBoost, TensorFlow 2 deep-dive, PyTorch.
- **[[python-datascience-topics]]** - Problem-type map: anomaly detection, CV, NLP, time series, recsys, RL environments.
- **[[mlops-production-deployment]]** - Ray, TF serving stack, model interpretation tools.
- **[[curated-reading-list]]** - ~190 high-signal essays distilled by theme.
- **[[math-for-ml-survival-guide]]** - Honest math depth table, quit-proof ordering.
- Roadmaps: **[[roadmap-data-scientist]]**, **[[roadmap-ml-engineer]]** (stages, exit tests, quit points).
- Prep: **[[ml-interview-playbook]]**, **[[kaggle-and-practice-guide]]**.
- Expanded repos: **[[repo-ossu-data-science]]**, **[[repo-ml-roadmaps-mindmaps]]**, **[[repo-ds-interviews-grigorev]]**, **[[repo-mlcourse-ai]]**, **[[repo-awesome-deep-learning-papers]]**, **[[repo-tf-pytorch-learning-stack]]**, **[[repo-data-engineer-roadmap]]**.

## Systems Design & Distributed Systems (field module)

> Hub: [[modules/systems-design/index|Systems Design Index]].

- **[[systems-design-distributed]]** - Patterns, Docker/K8s best practices, workflow engines, infra utilities.
- **[[system-design-interview]]** - 6-step framework, scoring axes, worked design.
- **[[repo-system-design-primer]]** - The canonical study repo expanded (topic index, solved questions, Anki).
- **[[repo-scalability-catalogs]]** - Case-study mining protocol; Netflix/Discord/Uber/Instagram starters.

## Web Development (field module)

> Hub: [[modules/web-development/index|Web Dev Index]].

- **[[web-development-resources]]** - MDN, event loop, CSS conventions, UX, frameworks.
- **[[repo-frontend-learning-resources]]** - Beginner resource list + FrontendMasters handbook expanded.
- **[[repo-fullstack-web-developer-path]]** - Week-by-week fullstack plan with exit tests.

## Careers, Market & Interview Prep (field module)

> Hub: [[modules/careers/index|Careers Index]].

- **[[market-analysis-tech-2026]]** - Sourced 2026 market split + strategy for a BTech student.
- **[[interview-counter-guide]]** - Round anatomy, live-coding script, STAR bank, negotiation.
- **[[build-project-playbook]]** - Portfolio projects: selection matrix, v0.1 rule, failure points.
- **[[example-question-bank]]** - Cross-topic drill bank (~40 questions).
- **[[roadmaps-and-study-guides]]** - Meta-catalog of all major roadmaps.

## Robotics & ROS2 (cross-cutting)

> Deep-researched study library for **robotics fundamentals + ROS 2 (Robot Operating System 2)** — sense–plan–act, sensors/kinematics/control/SLAM/planning, then the full ROS2 stack (nodes · topics · services · actions · DDS/QoS · colcon · tf2 · rviz2 · Gazebo · Nav2). Sources: docs.ros.org, design.ros2.org, docs.nav2.org, The Construct, Kevin Wood / Edouard Renard courses.

- **[[robotics/index]]** — robotics module hub: reading order, module map, autonomy-stack diagram (start here).
- **[[robotics/overview]]** — what robotics is: the sense–plan–act loop, robot anatomy, software stack, vault connections.
- **[[robotics/robotics-fundamentals]]** — engineering core: sensors, actuators & differential drive, kinematics/DH, PID & MPC, Kalman/AMCL, SLAM, motion planning (A*, RRT, DWA/TEB), perception.
- **[[robotics/ros2-architecture]]** — the ROS2 mental model: nodes, topics, services, actions, parameters, executors, lifecycle nodes; ROS1 vs ROS2.
- **[[robotics/ros2-communication]]** — DDS, QoS policies & profiles, discovery, the domain ID, middleware vendors, debugging mismatches.
- **[[robotics/ros2-installation-setup]]** — distro selection (Jazzy recommended), install steps, colcon workspace layout, first package.
- **[[robotics/ros2-beginner-guide]]** — hands-on path with commands: turtlesim → publisher/subscriber → interfaces → services/actions → tf2/URDF → rviz2 → Gazebo → Nav2.
- **[[robotics/worked-example-odom-ekf]]** — **worked example**: differential-drive odometry + 2D EKF fully implemented in rclpy (unicycle integration, Jacobian, innovation wrapping, fake-robot simulator, PlotJuggler verification).
- **[[robotics/ros2-tools-debugging]]** — CLI introspection, rqt/rviz2, rosbag, tf2 tools, Nav2 debug pipeline, gotchas.
- **[[robotics/ros2-cheatsheet]]** — every command on one page (nodes/topics/services/actions/params/colcon/bag/tf2 + Python skeleton + QoS picks).

## Productivity & Systems (cross-cutting)

> How the learning system itself runs: attention, knowledge workflow, habits, task management, and execution heuristics. Cross-links into quant-finance and ai-ml form the meta-layer of the knowledge base.

- **[[overview]]** — the unified productivity theme: 8-pillar operating model + full source registry (September starts here).
- **[[productive-flowchart]]** — the model as a flow chart / state machine (Mermaid + ASCII) for becoming & staying productive.
- **[[deep-work-attention-economics]]** — Deep vs shallow work, attention residue, the 4 execution disciplines (Cal Newport).
- **[[pkm-code-framework]]** — CODE framework + PARA method (Tiago Forte); this wiki is an instance of it.
- **[[atomic-habits-systems]]** — Identity-based habits, Four Laws of Behavior Change (James Clear).
- **[[gtd-task-management]]** — Externalize tasks, 5 workflow stages (David Allen).
- **[[mental-models-for-execution]]** — Pareto, Eisenhower Matrix, Parkinson's Law, Inversion.
- **[[focus-minimalism-babauta]]** — Leo Babauta: Age of Distraction, 3-Most-Important-Tasks, focus rituals, simplicity, single-tasking.
- **[[little-book-productivity-scott-young]]** — Scott Young: 99 tactics — timeboxing, weekly/daily goals, 3-pile organizing, energy, 30-Day Trial, Pareto.
- **[[101-ways-workplace-productivity-fishel]]** — Shelley Fishel: 101 before/during/after-work operating procedures for the workplace.
- **[[apo-handbook-productivity]]** — APO: definition (Output/Input), PDCA management cycle, 31 initiatives (5S, Kaizen, Lean, Six Sigma, JIT, BPR).

## Software Program Management & C Programming (cross-cutting)

> Four-module exam-focused deep dive covering introductory SPM + C, written for beginners: SDLC/project management → program control → arrays → user-defined functions. Each module is plain-English-first, with ASCII flowcharts, production-grade C code, memory maps, dry-run trace tables, complexity analysis, and worked exam drills (5–6 problems per module, all output-prediction style). The **[[SPM/c-programming-master-study-guide]]** is the single-file consolidation (memory → control flow → arrays → functions) with full LaTeX address derivations.

- **[[SPM/c-programming-master-study-guide]]** — Exhaustive one-file cram guide: preprocessor pipeline, Text/Data/BSS/Heap/Stack layout, full operator precedence ladder, all control-flow constructs with where-`continue`-jumps, 1D/2D address derivations (row-major & column-major), binary search, bubble sort, matrix add/multiply, call-by-value vs pointer, recursion stack traces & tail recursion, storage classes. Complete LaTeX derivations + working C code + trap sheet.
- **[[SPM/module-1-spm-c-basics]]** — SDLC models (Waterfall, V-Model, Spiral, Agile), estimation (LOC/FP/COCOMO with mode constants), PERT/CPM & risk; C program structure, 4-phase compilation pipeline with error-to-stage cheat sheet, Stack/Heap/Data/Text memory layout. 6 worked problems.
- **[[SPM/module-2-program-control-functions]]** — operator precedence for conditions, `if`/`else` and the dangling-else, `switch` fall-through vs. jump tables, `while`/`do-while`/`for` semantics, nested loops (triangular counts), `break`/`continue`/`goto`/`return` — including *where* `continue` jumps in each loop type. 6 output-prediction drills with dry-run tables.
- **[[SPM/module-3-arrays]]** — 1D/2D arrays, row-major vs. column-major address formulas (with derivation), array↔pointer decay, traversal, insertion/deletion with shift visualization, linear & binary search, bubble sort, O(n)/O(log n) complexity. 6 worked problems.
- **[[SPM/module-4-user-defined-functions]]** — prototypes/definition/call, pass-by-value vs. pass-by-pointer, storage classes (`auto`/`static`/`extern`), stack frames & the dangling-pointer trap, recursion (linear/tail/tree/mutual) with full stack traces, function pointers, variadic functions. 6 worked problems.

## Engineering Chemistry (cross-cutting)

> Five-module exam-focused deep dive covering the full Engineering Chemistry curriculum: water technology & hardness → surfactants/colloids → electrochemistry & corrosion → spectroscopy → polymers & fuels. Each module has ASCII flowcharts, full derivations, worked exam problems, and engineering applications.

- **[[engineering-chem/module-1-water-technology-hardness]]** — Hardness (temporary/permanent, ppm/°Cl/°Fr units), CaCO₃ equivalency, lime-soda (with dosage calc), zeolite, ion-exchange, RO, the 4 boiler troubles, EDTA hardness titrations. 5 worked problems.
- **[[engineering-chem/module-2-surfactants-interfaces-colloids]]** — Amphiphilic structure, 4 surfactant classes (SDS/CTAB/non-ionic/zwitterionic), micellization thermodynamics, CMC & Kraft point, detergency, emulsification (HLB), solubilization. 5 worked problems.
- **[[engineering-chem/module-3-electrochemistry-corrosion]]** — Nernst equation (full derivation), calomel & glass electrodes, conductometric titration curves, dry vs wet corrosion, galvanic series, differential aeration/pitting, sacrificial anodes, ICCP, electroplating & galvanization. 6 worked problems.
- **[[engineering-chem/module-4-spectroscopy-instrumental]]** — EM spectrum, Beer-Lambert law (derivation & deviations), σ/π/n electronic transitions, chromophores/auxochromes, batho/hypsochromic shifts, IR vibrational modes & functional-group regions. 5 worked problems.
- **[[engineering-chem/module-5-polymers-fuels]]** — Thermoplastics vs thermosets, elastomers & vulcanization, conducting polymers (polyaniline), calorific value (HCV/LCV), Dulong's formula, bomb calorimetry, proximate & ultimate analysis of coal. 5 worked problems.

## German A1 (cross-cutting)

> Complete beginner's guide to **German A1 (CEFR / Goethe Start Deutsch 1)**: pronunciation → full grammar system → vocabulary → practice. Beginner-friendly, exam-aware, free resources included.

- **[[german/overview]]** — module hub: what A1 is, 8-week roadmap, Goethe exam format, free sources (start here).
- **[[german/alphabet-and-pronunciation]]** — alphabet + ä/ö/ü/ß, sound rules (sch/tsch/z/v/w, ei/ie/eu), long vs short vowels, stress, pronunciation traps.
- **[[german/grammar-essentials]]** — quick core: der/die/das & gender, plurals, pronouns, sein/haben, regular conjugation, verb-2nd order, nicht vs kein, nominative & accusative, modals.
- **[[german/nouns-and-cases]]** — FULL noun system: the 4 cases, complete der/die/das & ein/eine declension tables, personal pronouns (nom/acc/dat), gender rules, 5 plural patterns, contractions (am/im/zum).
- **[[german/verbs-conjugation]]** — FULL verb system: regular & strong verbs (du/er change), separable verbs, modal verbs, imperative, Perfekt (spoken past), reflexive verbs + top-25 verb list.
- **[[german/word-order-and-questions]]** — the sentence machine: verb-2nd rule, Satzklammer (sentence bracket), W-questions, negation positions, coordinating vs subordinating conjunctions (denn/weil), TeKaMoLo.
- **[[german/prepositions]]** — 3 families: always-dative (mit/nach/aus/zu/von/bei), always-accusative (durch/für/gegen/ohne/um), two-way with the **Wo?/Wohin? rule**, contractions, time prepositions.
- **[[german/adjectives-and-possessives]]** — adjective endings (the "signal" theory), possessives (mein/dein…), demonstratives (dieser), comparatives (als/am besten).
- **[[german/vocabulary-and-phrases]]** — all A1 exam themes: greetings, self-intro, numbers, time & dates, family, food, shopping, travel, weather, house, body & health, clothes & colors, school & work, animals, survival phrases + top 25 verbs.
- **[[german/phrasebook-cheatsheet]]** — one-page survival phrasebook: essentials, W-questions, numbers, time, shopping, travel, food, emergencies + the "Ich möchte" formula.
- **[[german/practice-and-exercises]]** — 10-part practice test (98 points) with full answer key and a scoring guide.

## Engineering Drawing (cross-cutting)

> Beginner-friendly exam-focused module: the universal language of engineering. Sources: **N.D. Bhatt**, **BIS SP 46:2003** (line types, lettering, dimensioning), Narayana & Kannaiah, Jolhe.

- **[[engineering-drawing/overview]]** — module hub & beginner's guide: what a drawing must be, tools, line types (BIS), sheets & title block, scales (plain/diagonal/vernier), lettering, dimensioning basics (start here).
- **[[engineering-drawing/orthographic-projections]]** — the core topic: glass-box analogy, HP/VP planes & quadrants, **first vs third angle** (with symbols), projection of points → lines → planes → solids, true-length tricks, 3-view drawing & reading.
- **[[engineering-drawing/isometric-and-sections]]** — 3D "picture" views: isometric axes & box method, circles→ellipses, isometric drawing vs projection; then sectional views (cutting plane, 45° hatching, full/half/offset/revolved sections) + dimensioning recap.

## Engineering Physics (cross-cutting)

> Four-module deep dive: wave optics → optoelectronics/lasers → quantum mechanics → semiconductors & electromagnetism. Each module has 10-15 fully worked examples, ASCII flowcharts, and cross-links.

- **[[engineering-physics/module-1-optics-interference-diffraction]]** — Huygens, YDSE, thin films, Newton's rings, single/double slit diffraction, gratings, polarization, Malus/Brewster, Michelson interferometer. 12 worked examples.
- **[[engineering-physics/module-2-optoelectronics-lasers-fiber-optics]]** — Stimulated emission, Einstein coefficients, 3/4-level lasers, He-Ne, semiconductor lasers, optical fibers, TIR, NA, attenuation, EDFA. 15 worked examples.
- **[[engineering-physics/module-3-quantum-mechanics]]** — Photoelectric effect, de Broglie, Schrödinger equation, particle in box, harmonic oscillator, hydrogen atom, spin, tunneling, Compton. 15 worked examples.
- **[[engineering-physics/module-4-semiconductors-electromagnetism]]** — Energy bands, doping, p-n junction, BJT/FET, logic gates, Maxwell's equations, EM waves, Poynting vector, radiation pressure, magnetic materials. 12 worked examples.

## Engineering Mathematics (cross-cutting)

> Five-module applied math deep dive: matrices → partial differentiation → homogeneous functions → linear DEs → complex numbers. Each module has ASCII flowcharts, worked exam problems, proofs, and engineering applications.

- **[[engineering-math/module-1-matrices]]** — Rank, echelon form, Gaussian elimination, systems of linear equations, eigenvalues & eigenvectors, Cayley-Hamilton theorem (with proof). 5 worked problems.
- **[[engineering-math/module-2-partial-differentiation]]** — First & higher order partials, Clairaut's theorem, chain rule, total differentials, Jacobian, Hessian, maxima/minima, Lagrange multipliers. 5 worked problems.
- **[[engineering-math/module-3-homogeneous-functions]]** — Euler's theorem (with proof), degree determination, higher-order deductions, composite homogeneous functions, y=vx substitution. 7 worked problems.
- **[[engineering-math/module-4-linear-differential-equations]]** — First-order LDE, higher-order constant coefficients, complementary function, particular integral methods, variation of parameters, Cauchy-Euler equations. 5 worked problems.
- **[[engineering-math/module-5-complex-numbers]]** — De Moivre's theorem (with proof), nth roots, hyperbolic functions, complex logarithm, separation into real & imaginary parts. 5 worked problems.

## Stock Agent (cross-cutting)

> Deep-analysis module for the **user-built algorithmic trading platform** at `C:\Users\Vijaykumar\stock-agent`: Alpaca paper trading + FastAPI + React, with signals, VectorBT backtests, and an XGBoost/LightGBM ML pipeline. Documents functions, what works, what fails, value, and a fix roadmap.

- **[[stock-agent/overview]]** — module hub: what the app is, tech stack, data flow, status at a glance (start here).
- **[[stock-agent/deep-review-report]]** — **full-depth audit report**: strengths, 18 verified bugs with file:line references, and a 5-phase action plan.
- **[[stock-agent/architecture]]** — every component & how it fits: routers, core, trading/execution, ingestion, ML, frontend, deployment.
- **[[stock-agent/functions-and-features]]** — full feature inventory: paper trading, signals, analysis, backtests, ML, ingestion, data health, streaming.
- **[[stock-agent/what-works-and-fails]]** — honest scorecard: strengths vs failures (dead WS on Py3.14, scheduler disabled, ML missing technical indicators, mislabeled metrics, security gaps).
- **[[stock-agent/value-and-standalone]]** — what it helps you do, where it stands alone vs alternatives, current potential & blocker ranking.
- **[[stock-agent/improvement-roadmap]]** — prioritized P0→P3 fix roadmap with files, execution order, and a "personal platform ready" checklist.

## Self-Mastery (cross-cutting)

> The psychological engine underneath every other module: how the inner system (identity, beliefs, attention, emotions) is the real operating system. Distilled from the 7-slice YouTube corpus (`/raw-sources/slice0*.txt.md`). Summary digest at vault-root `NOTES.md`.

- **[[self-mastery/overview]]** — module synthesis: the "LEVEL" operating loop (Locate belief → Engineer identity → Vitalize direction → Execute with systems → Leverage & ship), the five cross-cutting laws, concept map, source registry, reading order (start here).
- **[[self-mastery/belief-engineering]]** — how belief creates biology & reality first: placebo/nocebo (Crum studies), self-efficacy, the self-fulfilling loop, belief audit, useful-and-untrue, strategic delusion, superposition of self.
- **[[self-mastery/manifestation-quadrant]]** — the Metamorphosis / Desire→Belief→Behavior→Field model: frequency coherence, the vacuum principle, effortless (laminar) achievement, pain-as-fuel, unified life, the two lines, the high-frequency human.
- **[[self-mastery/subconscious-reprogramming]]** — the unseen architecture (hysteresis/compression), theta mental rehearsal, the identity stack & physiology, borrowed state vs true state, the purpose antidote (mission/windows).
- **[[self-mastery/psychological-execution]]** — the internal state layer: stopping overthinking, discipline design (homeostasis, dopamine protocol, identity architecture), craving hard things, boredom tolerance, and the god-mode flow protocol.
- **[[self-mastery/life-systems-design]]** — the systems layer: the thermostat & 1-week/12-month sprint, learner's life (1-hour law), consistency & procrastination (Zeigarnik, 70% rule), hyperfocus, never-zero-days & the winner's loop, subtraction ("the glitch"), and the 24-hour empire one-person business.
- **[[self-mastery/self-mastery-flowcharts]]** — all runbooks as Mermaid + ASCII state machines: belief ladder, meta-program, manifestation quadrant, theta+6-phase, discipline loop, god-mode, winner's loop, thermostat reset, insight engine, 1-week sprint, 24-hour empire, silence→change map.

(End of file - total 86 lines)
