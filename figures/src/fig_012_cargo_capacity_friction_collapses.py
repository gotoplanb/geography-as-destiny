"""
Figure 012: Cargo Capacity Across Plains Transportation Technologies
Step function showing dog (75 lbs) → horse (300 lbs) → railroad (200,000 lbs).
Logarithmic scale. Two discontinuous jumps — each a friction collapse.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

# Data
techs = ['Dog + Travois\n(pre-1700)', 'Horse + Travois\n(~1710)', 'Railroad Freight Car\n(~1870)']
capacities = [75, 300, 200000]
colors = ['#95a5a6', '#e67e22', '#c0392b']
years_approx = [0, 1, 2]

bars = ax.bar(years_approx, capacities, color=colors, width=0.6, edgecolor='#2c3e50', linewidth=1)

# Log scale
ax.set_yscale('log')
ax.set_ylim(30, 500000)

# Labels on bars
for bar, cap, tech in zip(bars, capacities, techs):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height * 1.3,
            f'{cap:,} lbs', ha='center', va='bottom', fontsize=12, fontweight='bold',
            color='#2c3e50')

# Multiplier annotations
ax.annotate('4×', xy=(0.5, 180), fontsize=16, fontweight='bold', color='#e67e22',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#e67e22'))
ax.annotate('', xy=(1, 150), xytext=(0, 150),
            arrowprops=dict(arrowstyle='->', color='#e67e22', linewidth=2))

ax.annotate('667×', xy=(1.5, 8000), fontsize=16, fontweight='bold', color='#c0392b',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#c0392b'))
ax.annotate('', xy=(2, 5000), xytext=(1, 5000),
            arrowprops=dict(arrowstyle='->', color='#c0392b', linewidth=2))

# Friction collapse labels
ax.text(0.5, 50, 'First friction collapse:\nhorse replaces dog', ha='center', fontsize=8,
        color='#e67e22', style='italic')
ax.text(1.5, 400000, 'Second friction collapse:\nrailroad replaces horse', ha='center', fontsize=8,
        color='#c0392b', style='italic')

# Axis labels
ax.set_xticks(years_approx)
ax.set_xticklabels(techs, fontsize=10)
ax.set_ylabel('Cargo Capacity (lbs, log scale)', fontsize=11)
ax.set_title('Two Sequential Friction Collapses on the Same Terrain\nThe horse enabled the Comanche Empire. The railroad ended it.',
             fontsize=13, fontweight='bold', pad=15)

# Additional context
ax.text(2, 40, 'The gap between the second and third bars\nis why no institutional adaptation could bridge it.',
        ha='center', fontsize=8, color='#7f8c8d', style='italic')

plt.tight_layout()
plt.savefig('figures/output/fig-012-cargo-capacity-friction-collapses.png', dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-012-cargo-capacity-friction-collapses.svg', bbox_inches='tight')
print("Generated: fig-012-cargo-capacity-friction-collapses.png/.svg")
