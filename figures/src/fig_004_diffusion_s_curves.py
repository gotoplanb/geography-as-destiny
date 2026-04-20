"""
Figure 004: Islam's Two Diffusion Curves (+ Manichaeism)
Conquest step function vs. trade-route S-curve vs. Manichaeism collapse.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

fig, ax = plt.subplots(1, 1, figsize=(11, 5.5))

# Time axis
t = np.linspace(200, 1500, 1000)

# Conquest curve — step function at ~630-730 CE
conquest = np.where(t < 630, 0,
           np.where(t < 640, (t - 630) / 10 * 0.3,
           np.where(t < 660, 0.3 + (t - 640) / 20 * 0.3,
           np.where(t < 730, 0.6 + (t - 660) / 70 * 0.35,
           0.95))))

# Trade-route curve — classic S-curve, slower, starting later
def s_curve(t, t_mid, k, ceiling=1.0):
    return ceiling / (1 + np.exp(-k * (t - t_mid)))

trade = s_curve(t, t_mid=1000, k=0.008, ceiling=0.9)
trade = np.where(t < 700, 0, trade)  # doesn't start until trade networks form

# Manichaeism — rise then collapse
mani_rise = s_curve(t, t_mid=350, k=0.02, ceiling=0.35)
mani_collapse = np.where(t > 500, 0.35 * np.exp(-0.003 * (t - 500)), 0)
mani = np.where(t < 400, mani_rise, mani_collapse)
mani = np.where(t > 900, 0.01, mani)  # essentially gone by 900

# Plot
ax.plot(t, conquest, color='#c0392b', linewidth=2.5, label='Islam — conquest (step function)')
ax.plot(t, trade, color='#2980b9', linewidth=2.5, label='Islam — trade routes (S-curve)')
ax.plot(t, mani, color='#95a5a6', linewidth=2, linestyle='--', label='Manichaeism (rise then collapse)')

# Shade the gap between conquest and trade
ax.fill_between(t, trade, conquest,
                where=(conquest > trade) & (t > 650),
                alpha=0.1, color='#e74c3c')

# Annotations
ax.annotate('Political Islam\nprecedes cultural Islam\nby centuries',
            xy=(850, 0.5), fontsize=9, color='#c0392b', style='italic', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#c0392b', alpha=0.7))

ax.annotate('Mani designed for\nmaximum diffusion.\nNo boundaries = no survival.',
            xy=(600, 0.15), fontsize=8, color='#7f8c8d', style='italic', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#95a5a6', alpha=0.7))

# Rogers categories on the trade curve
rogers_points = [
    (800, 'Innovators', 0.02),
    (900, 'Early adopters', 0.1),
    (1000, 'Early majority', 0.45),
    (1150, 'Late majority', 0.75),
    (1350, 'Laggards', 0.88),
]
for year, label, y_approx in rogers_points:
    y_val = 0.9 / (1 + np.exp(-0.008 * (year - 1000)))
    ax.plot(year, y_val, 'o', color='#2980b9', markersize=5, zorder=5)
    ax.annotate(label, xy=(year, y_val), xytext=(year - 20, y_val + 0.06),
               fontsize=7, color='#2980b9', ha='right', rotation=0)

# Labels
ax.set_xlabel('Year (CE)', fontsize=10)
ax.set_ylabel('Adoption level', fontsize=10)
ax.set_title("Two Curves for One Religion — and One That Failed\nSame corridor, opposite boundary strategies, opposite outcomes",
             fontsize=13, fontweight='bold', pad=15)
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)

ax.set_xlim(200, 1500)
ax.set_ylim(-0.02, 1.05)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(['0%', '25%', '50%', '75%', '100%'])

plt.tight_layout()
plt.savefig('figures/output/fig-004-diffusion-s-curves.png', dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-004-diffusion-s-curves.svg', bbox_inches='tight')
print("Generated: fig-004-diffusion-s-curves.png/.svg")
