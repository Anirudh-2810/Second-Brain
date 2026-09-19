---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Round 1"
unit: "Wings and Control Surfaces"
date: 2026-09-19
description: "Airfoil terms and types, five wing planforms, five mountings, dihedral effect, aspect ratio, angle of attack and stall, aileron-elevator-rudder axes."
tags: [btech, aeromodelling, airfoil, wing, aspect-ratio, stall, control-surfaces]
last_updated: "2026-09-19"
confidence: high
---

## For future agent
Distilled from `[[raw-sources/Aerodynamics_and_Avionics_Study_Material.pdf]]` §3–8 (wing basics → control surfaces). Highest MCQ density of the PDF — planform/mounting/control-surface identification questions come from here.

# Wings and Controls (simple words)

> Parent hub: [[INDEX]] · Prev: [[aerodynamics-foundations]] · Next: [[avionics-rc-stack]]
> This page has the most MCQ questions in it. Read slowly. Every table has a "how to remember" line.

## 1. Airfoil — parts and two types

An airfoil is the side-view cut of a wing. Imagine slicing a wing like a bread loaf and looking at the slice. That curved slice is the airfoil.

The 5 words the test uses:

1. **Leading edge** — the front nose of the slice. It is the most rounded part. Air hits here first.
2. **Trailing edge** — the sharp back end. Air leaves here.
3. **Chord line** — an imaginary straight scale joining nose to tail. Like drawing a straight line on the slice from front to back.
4. **Mean camber line** — an imaginary curved line running in the middle of the slice, halfway between top skin and bottom skin. If the wing is curved a lot, this middle line bends a lot.
5. **Thickness** — how fat the slice is. Measured along the chord, in two ways (against the middle line or against the straight line — test rarely asks which, just remember it is "fatness along the chord").

Two types — this is a favourite MCQ:

| Type | What it looks like | Lift when wing is flat (0° angle)? | Where used + why |
|------|-------------------|-------------------------------------|------------------|
| **Symmetrical** | Top and bottom curves are mirror copies. Middle line and straight line fall on each other. | **Zero lift.** No curve difference, so no pressure difference. | Helicopter rotor blades, vertical tails. Reason: when flying straight, you do NOT want the tail to pull sideways on its own. |
| **Cambered (non-symmetrical)** | Top is more curved than bottom. Middle line sits above the straight line. | **Still gives useful lift even at 0°.** The built-in curve already makes top air faster. | Normal plane wings. Gives more lift at every angle, better lift-to-drag, gentler stall. |

**Memory trick:** "Camber = Curve = Carries lift even when flat."

**MCQ:** "Which airfoil lifts at zero angle of attack?" → cambered. "Which gives no lift at zero?" → symmetrical.

## 2. Wing planforms — the shape seen from top

Stand above the plane and look down. The outline of the wing is the **planform**. Planform area = wing skin area + the hidden middle bit inside the fuselage (imagine extending the front and back edges until they meet at the plane's centre line).

| Planform | Simple picture | Good and bad |
|----------|---------------|--------------|
| **Rectangular** | Like a ruler — same width from root to tip. | Easiest and cheapest to build. But not very efficient. Beginner RC planes use this. |
| **Tapered straight** | Like a ruler squeezed at the tips — wide at root, narrow at tip. | A middle path. Tries to copy the efficient elliptical lift pattern, but stays easy to build. |
| **Elliptical** | Like a flattened rugby ball / leaf edge. Spitfire wing. | **Best efficiency — lowest induced drag** (drag made by making lift). But curved edges are hard and costly to manufacture. So not every plane uses it. |
| **Swept** | Wings point backward like a paper dart. | Made for fast, near-sound-speed (**transonic**) flight. Sweeping back reduces the drag felt by the air hitting the wing straight on. |
| **Delta** | Big triangle like a dosa / kite. Very short and wide (low aspect ratio). | Works okay in ALL speeds — slow, near-sound, and supersonic. Used on supersonic jets, many European designs (Concorde, Mirage). |

**Memory trick:** "Rectangle = easy. Ellipse = efficient. Sweep = speed. Delta = does everything."

**MCQ:** "Lowest induced drag" → always elliptical. "Efficient in all regimes" → delta. "Reduces transonic drag" → swept.

## 3. Wing mounting — where the wing sits on the body

Monoplane = plane with one set of wings. Where that wing joins the tube (fuselage):

- **Low wing** — joined near the belly (bottom) of the plane. Like most passenger jets you board. Good for visibility above, easy landing gear.
- **Mid wing** — joined at the middle of the tube, halfway up. Common on aerobatic stunt planes.
- **Shoulder wing** — joined at the "shoulder", just below the roof. A half-step below a high wing.
- **High wing** — joined on the roof / cabin top, above the tube. Like a Cessna or cargo plane. Good ground clearance, stable.
- **Parasol** — held CLEAR above the roof on sticks (called cabane struts / pylon). Like an umbrella (parasol = umbrella) held over the plane. Old warbirds look like this.

**Memory trick:** Parasol = **para**chute + **sol** (sun shade) — wing as a sunshade on sticks. If the MCQ mentions struts/pylon/pedestal above the fuselage → parasol, not high wing.

## 4. Dihedral and anhedral — upward or downward tilt

Hold your arms out like wings:

- Arms tilted **up** (V shape) = **dihedral** (upward angle from flat).
- Arms flat = zero dihedral.
- Arms drooping **down** (inverted V) = **anhedral**.
- More than one bend along the wing = **polyhedral** (poly = many).

Why tilt matters — **dihedral effect**:

When wind hits the plane slightly from the side (called **sideslip**), a dihedral wing automatically creates a rolling push that levels the plane again. So:

- MORE upward tilt → STRONGER auto-levelling → MORE stable in spiral flight, but HARDER to turn sharply.
- LESS tilt (or downward anhedral) → WEAKER auto-levelling → LESS stable, but EASIER to twist and turn fast.

Who uses what:

- **Fighter jets** want fast turns, so they use near-zero or even **anhedral** (drooped). They happily give up stability to gain agility.
- **Big high-wing cargo planes** (Antonov An-124, Lockheed Galaxy) get free stability because their wing sits ABOVE the heavy centre — like a pendulum hanging down (also called **keel effect**). That alone gives too much stability, making turns sluggish. So designers ADD a little anhedral to cancel the extra and make the giant turnable again.

**Memory trick:** "Up = stable. Down = agile." Fighters droop to dance; giants droop to stop being too stiff.

## 5. Aspect ratio — long-skinny vs short-fat

Aspect ratio (AR) tells how long and skinny a wing is. Glider wings (long like a ruler) = high AR. Fighter/delta wings (short and fat) = low AR.

- If the wing is a rectangle/square: $AR = span / chord$ (length tip-to-tip divided by width front-to-back).
- For ANY shape: $$AR = span^2 / wing\ area$$ (span times span, divided by area).

Worked example (test loves this): span = 12 m, area = 24 m².
$AR = 12 × 12 / 24 = 144 / 24 = 6.$ Answer: **6** (no units).

Why care: high AR (gliders) = less induced drag = glides far. Low AR (deltas) = strong, good at high speed, but draggier at slow speed.

## 6. Angle of attack and stall — tilt vs airflow, in plain words

**Angle of attack (AoA, alpha)** = angle between the wing's straight chord line and the air coming at it. NOT the angle vs the ground — vs the **airflow**.

- Nose tilted up (climb) → AoA grows.
- Nose tilted down (dive) → AoA shrinks.
- Bigger AoA (up to a point) → more lift. Like tilting your palm out of a car window — tilt more, feel more push.

**Stall** = tilting too far. Past a **critical angle** (about **16°** in the PDF picture), lift suddenly DROPS instead of rising. The plane feels like it "lets go" and sinks.

Why stall happens — the chain in 4 steps:

1. At high tilt, air must flow against rising pressure on the wing top (uphill battle).
2. Tired air gives up and peels off the surface. This peeling is **flow separation**. The peel point (separation point) slides **forward** from the back as AoA rises.
3. The peeled, messy zone on top grows into a big **turbulent wake** (churning air).
4. Messy top = no smooth pressure difference = **lift falls, pressure drag jumps**.

Also remember: a curved (cambered) wing still lifts a little even at 0° AoA. A symmetrical wing lifts nothing at 0° — which is why tails use symmetrical sections (no surprise turns while cruising straight).

**MCQ:** "Lift decreases beyond ___ angle" → critical angle of attack. "Stall is caused by" → flow separation (air flowing against rising pressure).

## 7. Control surfaces — steering the plane

Three main flaps. Each turns the plane around ONE axis. Learn them as pairs:

| Surface | Where + how it moves | What the pilot feels | Axis (imagine a rod through the plane) |
|---------|---------------------|---------------------|----------------------------------------|
| **Ailerons** (roll) | Small flaps near both **wingtips**. They always move **opposite**: right up → left down, and reverse. Up-flap = that wing loses lift (pushed down). Down-flap = that wing gains lift (extra curve + more downwash, pushed up). | Plane **rolls / banks** sideways, like a bike leaning into a turn. Right aileron up → right wing drops → roll RIGHT. | **Longitudinal axis** (nose-to-tail rod). |
| **Elevators** (pitch) | Flaps on the **horizontal tail**. Both move **together** (both up or both down). They tilt the tail's lift up or down, making a turning push (moment) around the plane's heavy centre (CG). Elevator up → tail pushed down → nose goes UP (climb). Elevator down → nose goes DOWN. Tail itself is an upside-down airfoil. | Nose climbs or dives. | **Lateral axis** (wingtip-to-wingtip rod). |
| **Rudder** (yaw) | Flap on the **vertical tail fin**. Swings left/right like a boat rudder. Deflect right → air pushes tail left → nose points RIGHT. It is a slice of a symmetrical airfoil, so it only pulls when you move it. | Nose swings left/right, like shaking your head "no". Normally used **together with roll** to make a clean turn. | **Vertical axis** (floor-to-roof rod). |

**Memory tricks:**
- Aileron = **A**ileron = **A**rms-ends = opposite dance → roll.
- Elevator = **E**levator = **E**levates the nose → pitch (both flaps together, like an elevator door pair).
- Rudder = **R**udder = **R**ear fin, **R**otates nose left-right → yaw.

**MCQ:** "Roll about which axis?" → longitudinal. "Pitch?" → lateral. "Yaw?" → vertical. "Which surfaces move opposite?" → ailerons. "Which move together?" → elevators.

## Quick self-check

1. Which planform has lowest induced drag, and why isn't everything built that way?
2. Which mounting sits on struts above the fuselage?
3. Why do fighters use anhedral and heavy high-wings too?
4. $AR$ for span 12 m, area 24 m²?
5. Aileron up on the right wing → roll which way? Rudder alone turns nose about which axis?
