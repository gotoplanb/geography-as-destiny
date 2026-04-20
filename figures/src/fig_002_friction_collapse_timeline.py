"""
Figure 002: Friction Collapse Timeline
Effective geographic friction over time — punctuated equilibrium.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

fig, ax = plt.subplots(1, 1, figsize=(12, 5))

# Define friction regimes as step function
events = [
    (-3000, 1.0, 'Overland corridors\n(rivers, valleys, steppe)'),
    (-1500, 0.82, 'Oceanic sail\n(low friction, high latency)'),
    (1400, 0.65, 'Gunpowder\n(fortification collapses)'),
    (1840, 0.45, 'Telegraph\n(information friction collapses)'),
    (1860, 0.25, 'Railroad\n(physical friction collapses)'),
    (1990, 0.10, 'Internet\n(information layer decouples)'),
]

# Draw the step function
for i, (year, friction, label) in enumerate(events):
    # Horizontal line at this friction level
    end_year = events[i+1][0] if i+1 < len(events) else 2030
    ax.plot([year, end_year], [friction, friction], color='#2c3e50', linewidth=2.5)

    # Vertical drop
    if i > 0:
        prev_friction = events[i-1][1]
        ax.plot([year, year], [prev_friction, friction], color='#c0392b', linewidth=2, linestyle='-')
        # Drop marker
        ax.plot(year, friction, 'v', color='#c0392b', markersize=8, zorder=5)

    # Label
    if i == 0:
        ax.annotate(label, xy=(year + 200, friction - 0.02), fontsize=8, color='#7f8c8d', va='top')
    else:
        x_offset = 30 if year > 1800 else 100
        ax.annotate(label, xy=(year + x_offset, friction + 0.02), fontsize=8, color='#c0392b',
                   fontweight='bold', va='bottom')

# Shade the plateaus
for i, (year, friction, _) in enumerate(events):
    end_year = events[i+1][0] if i+1 < len(events) else 2030
    ax.fill_between([year, end_year], 0, friction, alpha=0.06, color='#2c3e50')

# Labels
ax.set_xlabel('Time', fontsize=11)
ax.set_ylabel('Effective Geographic Friction', fontsize=11)
ax.set_title('Friction Collapse as Punctuated Equilibrium\nGeography holds — then technology resets the distribution',
             fontsize=13, fontweight='bold', pad=15)

# Annotations
ax.annotate('Long stable periods\nwhere geography holds',
            xy=(-1000, 0.92), fontsize=9, color='#7f8c8d', style='italic', ha='center')
ax.annotate('Each drop changes\nwho the terrain serves',
            xy=(1920, 0.55), fontsize=9, color='#c0392b', style='italic', ha='center')

ax.set_xlim(-3200, 2050)
ax.set_ylim(0, 1.1)
ax.set_yticks([])

plt.tight_layout()
plt.savefig('figures/output/fig-002-friction-collapse-timeline.png', dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-002-friction-collapse-timeline.svg', bbox_inches='tight')
print("Generated: fig-002-friction-collapse-timeline.png/.svg")
