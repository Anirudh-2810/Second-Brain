---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "Quick Revision (all 6 PDFs, plain words)"
date: 2026-09-24
description: "Read-before-sleep one-pager from all 6 Team Onyx PDFs: numbered plain-word facts with everyday examples, same style as the 19th revision note."
tags: [btech, aeromodelling, team-onyx, interview, quick-revision]
last_updated: "2026-09-24"
confidence: medium
---

## For future agent
One-page bedtime revision built 2026-09-24 from all 6 Team Onyx PDFs (ESCs, Propulsion, both Workshop PPTs, Juniors book, study material) for the interview (Round-1 already cleared). Style contract: numbered `N) fact — one para`, plain words, one everyday example per line. Deep detail lives in [[esc-deep-dive]], [[propulsion-system-deep-dive]], [[workshop-ppts-merged]], [[airplanes-for-juniors-foundations]], [[aerodynamics-foundations]], [[wings-controls]], [[avionics-rc-stack]]; oral+code drill in [[team-onyx-interview-mock-01]]. Hub: [[INDEX]].

# Team Onyx Quick Revision (plain words, read + sleep)

> Tonight: read these 30 lines out loud once, then sleep. Tomorrow drill misses in [[team-onyx-interview-mock-01]].
> New here? Study the 4 proper notes FIRST ([[INDEX#How to study (read this first)]]) — this page is only the last-night list, not the teacher.

## A. ESC bits (from the ESCs PDF)

1) **ESC = the throttle guy.** Your stick talks to the receiver, the receiver sends a tiny PPM signal to the ESC, and the ESC turns that into big power for the motor. Think dimmer switch for a fan — same idea, but it switches ~2000 times per second (MOSFET) instead of burning extra power as heat like the old resistor controllers did.

2) **ESC feeds the receiver too (BEC).** Your battery is 11+ volts, but the receiver and servos only wanna eat 5–6 volts. The BEC inside the ESC steps the voltage down — like a phone charger stepping wall power down to 5V. No BEC? That's called OPTO — then you must power the receiver separately.

3) **Buy the ESC one size BIGGER.** 10 A motor → 15 or 18 A ESC, never 10. Exact match runs hot and dies mid-air — like carrying a school bag exactly at your weight limit vs leaving headroom. Interviewers LOVE this question.

4) **Three wire sets, say them in order:** battery lead → the pack; servo lead → receiver throttle channel; motor leads → the motor. Recite it like a train route and you sound like you built one.

5) **Brushless needs its ESC, always.** Brushless = 3 wires, no touching brushes, 85–90% efficient — the team default. Brushed = 2 wires, old drill-motor stuff, 75–80%. If they ask "which motor", answer brushless + ESC before they finish the sentence.

## B. Propulsion bits (from the Propulsion PDF)

6) **The chain goes: battery → ESC → motor → propeller → thrust.** Say it as one breath. Receiver/radio commands it, servos steer it. If you forget the order, remember B-E-M-P (Big Elephants Make Peanuts).

7) **Outrunner = team default.** Outrunner spins its outer shell around the middle, gives big torque, drives the prop directly — no gearbox. Inrunner spins inside, screams fast RPM, and NEEDS a gearbox to touch a prop. "Direct drive" = outrunner.

8) **Prop stamp 8×5 means 8 inch wide, 5 inch bite.** First number = diameter (tip to tip), second = pitch (how far it screws forward per turn, like a screw in wood). 8×5 needs a STRONGER motor than 8×4 — bigger bite, more muscle. Small prop = fast top speed; big prop = strong punch off the line.

9) **kV is NOT kilovolt — it is rpm PER volt.** 1800 kV on 12 V = 21,600 rpm (just multiply). Trick question factory: 2200 kV on 3S (11.1 V) = 24,420 rpm. And 2S is NOT 2 seconds — it is 2 cells.

10) **LiPo numbers in one line:** one cell = 3.7 V normal, 4.21 full, never below 3.3 or it dies. 3S = 11.1 nominal, ~12.6 fresh, land by ~10.6. Capacity 2200 mAh with 25C = 2.2 × 25 = 55 A max punch. Say the 55 with the math and they stop doubting you.

11) **Match order: prop first, then motor, then ESC.** Pick the prop for the job, pick a motor strong enough to spin it, pick an ESC bigger than the motor. Never backwards — that's the one-line answer to "how do you size a power system".

## C. Build-flow bits (from both Workshop PPTs)

12) **The 5-step design order:** problem → pick airfoil → size the wing → size the tail → check stability. Like cooking: recipe first, then ingredients, then taste-test. Memorise the order — "walk me through a build" starts here.

13) **Plane types in one breath:** by use = passenger/cargo/military; by wings = one/two/many (mono/bi/multi); by landing = land/sea/both; by speed = slow (< sound), fast (> sound, Concorde), crazy fast (> 5× sound). Pick any two axes and you can classify any plane they name.

14) **Wright brothers flew 1903.** da Vinci dreamed it, Cayley built the first glider (1853), the Wrights actually flew (17 Dec 1903). One history line is enough colour for "tell me about aviation".

15) **Want to climb? Push harder than weight.** Thrust ÷ Weight > 1 = you accelerate straight up. Flaps = extra lift for take-off, extra drag for landing slowdown — same flap, two jobs.

16) **Battery ladder:** lead-acid → NiCad → NiMH → Li-ion → Li-poly. LiPo wins because it is light, thin, punchy, and shaped however you want — like upgrading from a brick phone to a smartphone battery.

17) **Servo = a motor that holds an angle.** Not spinning round and round — it moves to an exact position and stays (flaps, landing gear). Speed is measured over 60 degrees at full load. Say "closed-loop angle holder" and move on.

## D. Juniors-book colour (from Understanding Airplanes)

18) **Double the speed → QUADRUPLE the push.** Dynamic pressure grows with speed SQUARED. That is why take-off and landing speeds are the whole game — small speed change, huge force change. Like running into rain vs cycling into rain.

19) **Vortices leak off the edges.** Air spills from the high-pressure side over the wingtip to the low-pressure side and curls into a swirl — that swirl IS induced drag. Works as your one-breath answer to "what is induced drag".

20) **The drag-fix ladder: clean it, stretch it, thin it.** Streamline the shape (less separation), stretch the wing long-skinny (less angle drag — high aspect ratio), thin the section and sweep it (less wave drag at speed). Three words, in order.

21) **We bank to turn because forces must line up.** Tighter turn → more bank, so gravity + turning push still point straight down through your seat. Uncoordinated = skid/slip, like a car sliding sideways on a turn.

22) **Wing-tail angle gap sets the mood (decalage).** Gap too small = twitchy and nervous; just right = stable hands-off; too big = lazy and sluggish. Quote it when they ask "what makes a model stable".

23) **Tube truss = cheap and stiff.** A frame of thin steel tubes gives lots of strength for little weight — the jugaad answer before carbon fibre. Cite it for "how to build a light stiff fuselage".

## E. Numbers you already know (from the study-material PDF)

24) **Level flight = everything balanced:** Lift = Weight AND Thrust = Drag. Climb = lift wins, speed up = thrust wins. Start every aero answer here.

25) **Lift needs BOTH Bernoulli AND Newton.** Fast air on top pushes less (low pressure sucks the wing up) AND the wing shoves air down so air shoves it up. Any option saying only one = wrong. "Equal Transit" (air must meet at the back) = the famous WRONG theory.

26) **Symmetrical wings lift NOTHING when flat.** Curved (cambered) wings still lift at zero tilt; mirror-flat (symmetrical) ones need a tilt — that is why tails and helicopter blades use them, so they don't pull on their own.

27) **Shapes cheat-sheet:** rectangular = easiest to build; elliptical = most efficient; swept = fast planes; delta triangle = okay at all speeds. Positions: low/mid/high, and parasol = held ABOVE the body on sticks (struts mentioned → parasol).

28) **Dihedral up = stable, anhedral down = agile.** Wings tilted up auto-level you (trainers); tilted down turn fast (fighters). Stall = past ~16° tilt the air peels off the top, lift drops, drag jumps.

29) **Controls:** ailerons (wingtips, opposite ways) = roll; elevator (tail, together) = nose up/down; rudder (fin) = nose left/right. Aspect ratio = span² ÷ area (12 span, 24 area → 6).

30) **Radio in one line:** 2.4 GHz, 6 channels (rudder, elevator, ailerons, throttle + 2 spare), receiver binds to ONE protocol only. Trap answers: kV ≠ kilovolt, 2S ≠ 2 seconds, ESC rating ≠ motor current.

## Tonight's close

- Read A→E once, out loud, no stopping. Star the lines you stumbled on.
- Tomorrow: drill stumbles in [[team-onyx-interview-mock-01]] (Set A = same facts as questions, Set B = live Python).
- Sleep now — the notice said basics only, and basics are all above.
