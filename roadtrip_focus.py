# Roadtrip Focus: cross-country focus timer.
# hill color improvements: teal-charcoal sequence with #00e69a accent

# Dark mode hills (teal-charcoal sequence with #00e69a accent undertone)
# These replace the biome-varied charcoal grays for a consistent dark aesthetic
if self.dark_mode:
    hill_defs = [
        ("#051510",  0.22, 420, 22, 0.018, 0),    # dark teal-green charcoal
        ("#0a201a",  0.45, 360, 18, 0.024, 1.1),  # medium teal-charcoal
        ("#153025",  0.85, 300, 14, 0.032, 2.4),  # darkest teal-charcoal
    ]
else:
    # light day - unmuted green
    hill_defs = [
        ("#4a7c59",  0.22, 420, 22, 0.018, 0),    # soft sage green far
        ("#6aa07a",  0.45, 360, 18, 0.024, 1.1),  # medium sage green mid
        ("#8ab59a",  0.85, 300, 14, 0.032, 2.4),  # light sage green near
    ]
PYEOF