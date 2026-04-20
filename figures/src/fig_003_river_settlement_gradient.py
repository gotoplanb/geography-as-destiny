"""
Figure 003: Universal River Settlement Gradient
Elevation profile with settlement density overlay — the quantitative heart.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.spines.top'] = False

fig, ax1 = plt.subplots(1, 1, figsize=(11, 5.5))

# Normalized distance along river (0 = headwaters, 1 = coast)
x = np.linspace(0, 1, 500)

# Elevation profile — steep at headwaters, flattening toward delta
elevation = 3000 * np.exp(-3 * x) + 50

# Settlement density — low at headwaters, peak at floodplain/delta
# with Goldilocks zone in middle and asymmetric boundaries
settlement = np.where(x < 0.15, 0.02,  # hard upstream boundary
              np.where(x < 0.3, 0.3 * ((x - 0.15) / 0.15)**0.5,  # Goldilocks ramp
              np.where(x < 0.7, 0.3 + 0.5 * ((x - 0.3) / 0.4),  # floodplain increase
              0.8 + 0.15 * ((x - 0.7) / 0.3))))  # delta maximum

# Smooth the settlement curve
from numpy import convolve
kernel = np.ones(20) / 20
settlement_smooth = np.convolve(settlement, kernel, mode='same')

# Elevation on left axis
color_elev = '#3498db'
ax1.fill_between(x, 0, elevation, alpha=0.15, color=color_elev)
ax1.plot(x, elevation, color=color_elev, linewidth=2, label='Elevation')
ax1.set_xlabel('Distance along river\n← Headwaters                                                                    Coast →',
               fontsize=10, labelpad=10)
ax1.set_ylabel('Elevation (m)', color=color_elev, fontsize=10)
ax1.tick_params(axis='y', labelcolor=color_elev)
ax1.set_ylim(0, 3500)

# Settlement on right axis
ax2 = ax1.twinx()
color_settle = '#e74c3c'
ax2.plot(x, settlement_smooth, color=color_settle, linewidth=2.5, label='Settlement density')
ax2.set_ylabel('Settlement density (predicted)', color=color_settle, fontsize=10)
ax2.tick_params(axis='y', labelcolor=color_settle)
ax2.set_yticks([])
ax2.set_ylim(0, 1.2)

# Zone annotations
zones = [
    (0.07, 'Headwaters\nErosive, sparse\nChokepoints only', '#7f8c8d', 2800),
    (0.22, 'Goldilocks\nZone\nFirst movers', '#27ae60', 2200),
    (0.50, 'Floodplain\nSurplus agriculture\nCities', '#e67e22', 1200),
    (0.88, 'Delta\nMaximum fertility\nHighest density', '#8e44ad', 400),
]

for xpos, label, color, ypos in zones:
    ax1.annotate(label, xy=(xpos, ypos), fontsize=8, color=color,
                ha='center', va='center', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, alpha=0.8))

# Asymmetry annotation
ax1.annotate('Hard upstream\nboundary', xy=(0.14, 500), fontsize=8, color='#c0392b',
            ha='center', style='italic')
ax1.annotate('Soft downstream\nboundary', xy=(0.75, 500), fontsize=8, color='#c0392b',
            ha='center', style='italic')

# Title
ax1.set_title('The River Settlement Gradient\nEnergy dissipation predicts where civilizations form',
              fontsize=13, fontweight='bold', pad=15)

ax1.set_xticks([])

plt.tight_layout()
plt.savefig('figures/output/fig-003-river-settlement-gradient.png', dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-003-river-settlement-gradient.svg', bbox_inches='tight')
print("Generated: fig-003-river-settlement-gradient.png/.svg")
