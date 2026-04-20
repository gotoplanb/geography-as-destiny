"""
Figure 009: Process Knowledge vs. Commodity Diffusion
Paper (process) vs. Silk (commodity) — two fundamentally different curves.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

fig, ax = plt.subplots(1, 1, figsize=(11, 5))

t = np.linspace(0, 1300, 1000)

# Silk (commodity) — gradual, continuous, proportional to supply chain
silk = 0.6 * (1 - np.exp(-0.003 * t))  # logarithmic growth, continuous
silk = np.where(t < 100, silk * t / 100, silk)  # ramp in

# Paper (process) — flat for 650 years, then rapid self-replicating spread
paper_delay = np.where(t < 750, 0.02, 0)  # exists in China, not spreading
paper_spread = np.where(t >= 750, 0.8 / (1 + np.exp(-0.02 * (t - 900))), 0)
paper = paper_delay + paper_spread

ax.plot(t, silk, color='#e67e22', linewidth=2.5, label='Silk (commodity) — continuous supply chain')
ax.plot(t, paper, color='#2980b9', linewidth=2.5, label='Paper (process knowledge) — single threshold, then self-replicates')

# 650-year gap annotation
ax.annotate('', xy=(105, 0.05), xytext=(750, 0.05),
           arrowprops=dict(arrowstyle='<->', color='#7f8c8d', linewidth=1.5))
ax.text(427, 0.08, '~650-year gap\nKnowledge exists in China\nbut hasn\'t transferred west',
        ha='center', fontsize=8, color='#7f8c8d', style='italic')

# Talas marker
ax.axvline(751, color='#c0392b', linewidth=1.5, linestyle=':', alpha=0.7)
ax.annotate('Battle of Talas\n751 CE\nThreshold event', xy=(751, 0.65), fontsize=9,
           color='#c0392b', ha='right', fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#c0392b', alpha=0.8))

# Post-Talas spread annotations
spread_points = [
    (760, 'Samarkand\n~750s'),
    (795, 'Baghdad\n~790s'),
    (900, 'Egypt\n~900s'),
    (1100, 'Europe\n~1100s'),
]
for year, label in spread_points:
    y_val = 0.8 / (1 + np.exp(-0.02 * (year - 900)))
    ax.plot(year, y_val, 'o', color='#2980b9', markersize=6, zorder=5)
    ax.annotate(label, xy=(year, y_val), xytext=(year, y_val + 0.07),
               fontsize=7, color='#2980b9', ha='center')

# Key insight
ax.annotate('The idea is its own supply chain.\nOnce you have the recipe,\nyou don\'t need the trade route.',
            xy=(1050, 0.25), fontsize=9, color='#2980b9', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#2980b9', alpha=0.7))

ax.set_xlabel('Year (CE)', fontsize=10)
ax.set_ylabel('Geographic extent of adoption', fontsize=10)
ax.set_title('Process Knowledge vs. Commodity Diffusion\nTwo transmission mechanisms, two curve shapes, same corridor',
             fontsize=13, fontweight='bold', pad=15)
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)

ax.set_xlim(-50, 1300)
ax.set_ylim(-0.02, 1.0)
ax.set_yticks([])

plt.tight_layout()
plt.savefig('figures/output/fig-009-process-vs-commodity-diffusion.png', dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-009-process-vs-commodity-diffusion.svg', bbox_inches='tight')
print("Generated: fig-009-process-vs-commodity-diffusion.png/.svg")
