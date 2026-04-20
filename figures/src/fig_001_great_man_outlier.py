"""
Figure 001: The Great Man as Outlier
Normal distribution with historical figures plotted as standard deviations.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Style
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

fig, ax = plt.subplots(1, 1, figsize=(10, 5))

# Normal distribution
x = np.linspace(-4, 4, 1000)
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# Fill the distribution
ax.fill_between(x, y, alpha=0.15, color='#2c3e50')
ax.plot(x, y, color='#2c3e50', linewidth=2)

# Mean line
ax.axvline(0, color='#7f8c8d', linewidth=1, linestyle='--', alpha=0.7)

# Plot historical figures
figures = [
    (-2.2, 'Tecumseh', 'Extended resistance\n~a generation', '#c0392b'),
    (-1.8, 'Kenesary\nQasymov', 'Coalition builder\nkilled by rivals', '#e74c3c'),
    (0, '', 'Structural outcome\n(geography determines this)', '#7f8c8d'),
    (2.0, 'Peter the\nGreat', 'Compressed timeline\n~a generation', '#2980b9'),
]

for sigma, name, label, color in figures:
    y_pos = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * sigma**2)
    ax.plot(sigma, y_pos, 'o', color=color, markersize=10, zorder=5)
    if name:
        ax.annotate(
            f'{name}\n({sigma:+.1f}σ)',
            xy=(sigma, y_pos),
            xytext=(sigma, y_pos + 0.08),
            ha='center', va='bottom',
            fontsize=9, color=color, fontweight='bold',
            arrowprops=dict(arrowstyle='-', color=color, alpha=0.5)
        )

# Labels
ax.set_xlabel('Timing shift from geographic mean\n← Extended resistance          Compressed timeline →',
              fontsize=10, labelpad=10)
ax.set_ylabel('Frequency of historical outcomes', fontsize=10)
ax.set_title('Great Men Are Outliers on a Distribution Geography Defined',
             fontsize=13, fontweight='bold', pad=15)

# Annotation for the mean
ax.annotate('Geographic mean:\nthe outcome that occurs\nregardless of the individual',
            xy=(0, 0.4), xytext=(1.5, 0.35),
            ha='left', fontsize=9, color='#7f8c8d', style='italic',
            arrowprops=dict(arrowstyle='->', color='#7f8c8d', alpha=0.7))

# Remove y-axis ticks (conceptual, not measured)
ax.set_yticks([])
ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
ax.set_xticklabels(['-3σ', '-2σ', '-1σ', 'mean', '+1σ', '+2σ', '+3σ'])

ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.5)

plt.tight_layout()
plt.savefig('figures/output/fig-001-great-man-outlier.png', dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-001-great-man-outlier.svg', bbox_inches='tight')
print("Generated: fig-001-great-man-outlier.png/.svg")
