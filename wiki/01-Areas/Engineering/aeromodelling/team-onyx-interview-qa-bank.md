---
date: 2026-09-25
description: "Team Onyx interview Q&A bank: every aero+avionics concept in plain words with 2-3 likely interview questions and one-line answers right after each concept, distilled from all 6 source PDFs."
tags: [btech, aeromodelling, team-onyx, interview, qa-bank, avionics, aerodynamics]
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "Interview Q&A Bank"
last_updated: "2026-09-25"
confidence: high
---

## For future agent

Interview Q&A companion to the 4 proper teaching notes ([[esc-deep-dive]], [[propulsion-system-deep-dive]], [[workshop-ppts-merged]], [[airplanes-for-juniors-foundations]]) + Round-1 pages ([[aerodynamics-foundations]], [[wings-controls]], [[avionics-rc-stack]]). Format per concept: **Say it simple** (2-3 lines, simpler than the notes) then **🎤 likely questions** with one-line answers. Drill: cover answers, say aloud, uncover to score. Hub: [[INDEX]] · Code drill: [[team-onyx-interview-mock-01]] · Bedtime: [[team-onyx-quick-revision]].

# Team Onyx Interview Q&A Bank (simple words)

## A. Forces + lift ([[aerodynamics-foundations]])

**A1. The 4 forces.** Say it simple: weight pulls down, lift pushes up, drag pushes back, thrust pushes forward. Level flight = lift ties weight AND thrust ties drag.
🎤 "What must hold for level steady flight?" → Lift = Weight and Thrust = Drag, both at once.
🎤 "Climb? Speed up?" → Climb = lift beats weight. Faster = thrust beats drag.

**A2. Bernoulli half.** Say it simple: fast air pushes less. Wing top is curvier, air there runs faster, so top pressure drops and the wing gets sucked up. Blow over a paper strip — it rises.
🎤 "Where is pressure low on a wing?" → Top. Swapped options are always wrong.
🎤 "State Bernoulli in one line?" → Speed up = pressure down (energy saved, not lost).

**A3. Coanda + downwash.** Say it simple: air hugs the curved top like water hugging a spoon under a tap, then leaves heading downward. That downward exit flow is downwash.
🎤 "What is downwash?" → Air bent downward behind the wing.

**A4. Newton half.** Say it simple: wing shoves air down, air shoves wing up. Same push-back as a balloon flying when air rushes out.
🎤 "Bernoulli or Newton — which explains lift?" → Both together. Either-alone options are traps.

**A5. Equal Transit (the famous wrong theory).** Say it simple: it claims split air particles must re-meet at the back, so top air hurries. False — nobody forces a re-meet; experiments killed it.
🎤 "Air must reach the trailing edge together — true?" → False, that exact sentence marks the wrong option.

**A6. Bluff vs streamlined + drag split.** Say it simple: brick/truck = bluff, air can't hug it, pressure-pattern drag wins. Fish/flat wing = streamlined, rubbing drag wins. Drag = pressure part + friction part.
🎤 "Brick drag is mostly…?" → Pressure (form) drag. "Fish?" → Friction drag.

## B. Wings + controls ([[wings-controls]])

**B1. Airfoil parts.** Say it simple: bread-slice cut of a wing. Round nose = leading edge, sharp tail = trailing edge, straight nose-to-tail scale = chord line, bendy middle line = camber line.
🎤 "Chord line?" → Straight line nose to tail. "Camber line?" → Curved middle line.

**B2. Symmetrical vs cambered.** Say it simple: mirror-flat wings lift NOTHING when flat (tails use them so they don't pull alone); curved-top wings lift even at zero tilt (all normal wings).
🎤 "Which lifts at 0°?" → Cambered. "Why tails symmetrical?" → No self-pull while cruising straight.

**B3. Planforms.** Say it simple: rectangle = easy to build (trainers). Ellipse = most efficient, lowest lift-making drag (Spitfire, costly). Sweep = fast near-sound flight. Delta triangle = okay at every speed (Concorde, Mirage).
🎤 "Lowest induced drag?" → Elliptical, always. "All speeds?" → Delta. "Fast transonic?" → Swept.

**B4. Mountings.** Say it simple: low = belly (airliners), mid = middle (stunt), shoulder = below roof, high = roof (Cessna, cargo), parasol = umbrella on sticks ABOVE the roof.
🎤 "Struts holding wing above fuselage?" → Parasol, not high wing. Trap word: struts/pylon.

**B5. Dihedral/anhedral.** Say it simple: arms-up V = stable, auto-levels, turns lazy. Arms-down = agile, turns fast, needs pilot work. Fighters droop to dance; giant high-wings droop to cancel excess stiffness.
🎤 "Up or down for stability?" → Up (dihedral). "Why anhedral on fighters AND Antonovs?" → Fighters buy agility; giants cancel pendulum excess.

**B6. Aspect ratio.** Say it simple: how long-skinny the wing is. $AR = span^2 \div area$. Glider = high, fighter delta = low.
🎤 "Span 12, area 24?" → $144 \div 24 = 6$. "High AR buys what?" → Less lift-making drag, glides farther.

**B7. AoA + stall.** Say it simple: tilt vs the AIRFLOW (not ground). More tilt = more lift until ~16°, then air peels off the top (separation), wake goes messy, lift falls and drag jumps.
🎤 "Stall caused by?" → Flow separation past critical AoA (~16°). "AoA measured against?" → Airflow, never ground.

**B8. Controls.** Say it simple: ailerons (wingtips, opposite dance) = roll about nose-to-tail rod. Elevators (tail pair, together) = nose up/down about wingtip-to-wingtip rod. Rudder (fin, left/right) = nose swing about floor-to-roof rod.
🎤 "Which move opposite? Together?" → Ailerons opposite, elevators together. "Roll axis?" → Longitudinal. "Pitch?" → Lateral. "Yaw?" → Vertical.

## C. Avionics chain ([[avionics-rc-stack]])

**C1. Prop numbers.** Say it simple: stamp 8×5 = 8 inch wide, 5 inch bite per turn (like a screw in wood). Bigger second number = stronger motor needed. Small prop = top speed; big prop = punch. Flat blades = take-off; steep = cruise.
🎤 "8×5 vs 8×4?" → 8×5 hungrier. "Pusher prop?" → Sits at back, pushes.

**C2. Brushed vs brushless.** Say it simple: old = 2 wires, rubbing brushes, wasteful (drills, toys). Modern = 3 wires, no rubbing, needs ESC, 85-90% (every RC plane).
🎤 "Team default?" → Brushless + ESC, answer before they finish asking.

**C3. kV.** Say it simple: RPM per 1 volt, no prop attached. NOT kilovolt. Multiply: 1800 kV × 12 V = 21,600 rpm.
🎤 "2200 kV on 3S (11.1V)?" → 24,420 rpm. "kV = kilovolt?" → No — RPM per volt.

**C4. LiPo.** Say it simple: 2S = 2 cells, 3.7V each. 3S = 11.1 normal, ~12.6 fresh, land by ~10.6, never under 3.3/cell or it dies. C-rating × amps = max punch (2.2A × 25C = 55A).
🎤 "2200mAh 25C gives?" → 55A. "Why land early?" → Drain less = lives longer.

**C5. ESC + BEC + headroom.** Say it simple: middleman with 3 wire sets (battery in, receiver orders in, motor power out). Steps 11V down to 5V for receiver (BEC = no second battery). Always buy BIGGER than motor draw (10A motor → 15/18A) so it stays cool.
🎤 "OPTO means?" → No BEC — power receiver separately. "Exact-match ESC?" → Burns mid-flight, never.

**C6. Tx/Rx.** Say it simple: 2.4GHz box, 6 channels (rudder, elevator, ailerons, throttle + 2 spares). Receiver binds ONE protocol only, runs on 5V from ESC.
🎤 "Mix any Tx with any Rx?" → No — protocol must match.

**C7. Servos.** Say it simple: tiny angle-holding muscles for flaps/gear. Strength = torque, speed = seconds per 60° at full load. Fast for surfaces, slow-gentle for gear.
🎤 "0.12s/60° means?" → Swings 60° in 0.12s pushing max load.

## D. ESC depth ([[esc-deep-dive]])

**D1. PPM path.** Say it simple: receiver taps the ESC down the throttle wire — quick taps = slow, long presses = fast. Same tap language as servos.
🎤 "Full path one breath?" → Stick → Tx → 2.4GHz → Rx → throttle channel → PPM → ESC → motor.

**D2. MOSFET vs resistor.** Say it simple: old controllers rode the brake (burnt extra as heat); modern flick ON/OFF ~2000×/sec and recycle energy through a one-way valve (flyback diode) — cool and smooth.
🎤 "Why did resistor types fail?" → Cooked themselves at part throttle.

**D3. BEC family.** Say it simple: built-in phone charger for the receiver. BEC = inside ESC, UBEC = separate clean unit, SBEC = efficient switching type, OPTO = none at all.
🎤 "Big plane, many servos — which?" → Separate UBEC/SBEC, not the tiny built-in.

## E. Propulsion depth ([[propulsion-system-deep-dive]])

**E1. BEMP chain.** Say it simple: battery → ESC → motor → propeller → thrust. Radio commands, servos steer.
🎤 "Order?" → B-E-M-P, "Big Elephants Make Peanuts."

**E2. Outrunner vs inrunner.** Say it simple: ceiling fan (outer spins, prop bolts straight on) vs mixer motor (inner screams, needs gears). Team flies outrunners.
🎤 "Direct drive?" → Outrunner — torque-rich, no gearbox.

**E3. Sizing order.** Say it simple: prop first (pick for the job), motor second (strong enough to spin it), ESC last (bigger than motor). Never backwards.
🎤 "Size a power system?" → Prop → motor → oversized ESC, one line.

## F. Build flow ([[workshop-ppts-merged]])

**F1. History.** Say it simple: dreamed (da Vinci) → glided (Cayley 1853) → jumped (Lilienthal) → flew (Wrights, 17 Dec 1903).
🎤 "First powered? First glider?" → Wrights 1903; Cayley 1853.

**F2. Classification axes.** Say it simple: don't memorise planes — sort them: use, weight-vs-air, wing count, landing, mount, stability tilt, speed.
🎤 "Classify a floatplane fighter?" → Military + heavier-than-air + sea landing + read mount/speed off the picture.

**F3. 5-step design.** Say it simple: recipe → knife → ingredients → tail → taste-test. Problem, airfoil, wing size, tail size, stability check.
🎤 "Walk me through a trainer?" → Cambered wing, high mount + dihedral, generous tail, stability check. 60 seconds.

**F4. F/W + flaps.** Say it simple: thrust heavier than weight = rocket-climb. Same flap gives lift for take-off, drag for landing.
🎤 "F/W > 1?" → Accelerates straight up.

**F5. Battery ladder + final connections.** Say it simple: lead → NiCad → NiMH → Li-ion → LiPo (light, punchy, any shape). Before flight: plugs seated, directions right, prop tight, battery strapped, range checked.
🎤 "Pre-flight in one line?" → Surfaces, screws, straps, signal — then fly.

## G. Juniors colour ([[airplanes-for-juniors-foundations]])

**G1. Speed squared.** Say it simple: double speed = 4× push (10→20 m/s turns 100 push into 400). Rain stings on a cycle, not on foot.
🎤 "Why do small speed changes explode?" → Dynamic pressure goes as velocity squared — lift AND drag quadruple.

**G2. Vortices.** Say it simple: high-pressure air spills over wingtips and curls into swirls — that lost energy is induced drag, the price of lift.
🎤 "Induced drag one breath?" → Wingtip spill swirls. "Fix?" → Long skinny wings.

**G3. Drag ladder.** Say it simple: clean it (streamline), stretch it (long wings), thin it (sharp + swept for speed).
🎤 "Cut drag — three in order?" → Never answer with just one; ladder order scores.

**G4. Banking.** Say it simple: tilt lift sideways to pull around the turn; rudder-alone skids like a car on ice. Seat-arrow straight down = coordinated.
🎤 "Why not rudder-only?" → Skid. Coordinated = ?

**G5. Decalage.** Say it simple: wing-tail angle gap sets pitch mood — tiny gap twitchy, right gap hands-off stable, huge gap lazy.
🎤 "Stable vs twitchy pitch?" → Decalage gap. Name all three moods.

**G6. Tube truss.** Say it simple: triangles can't squash, squares fold — so welded triangle-tube skeletons (bamboo scaffolding!) give max stiffness per gram before carbon.
🎤 "Light + stiff on student budget?" → Triangulated tube truss.

## How to drill this bank

1. Cover the 🎤 lines, read only **Say it simple** aloud.
2. Uncover one Q at a time — answer before reading the arrow.
3. Star misses → re-read that concept's source page (linked in headings).
4. Clean run = Set A of [[team-onyx-interview-mock-01]] next, timed.
