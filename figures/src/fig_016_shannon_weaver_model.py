"""
Figure 016: The Shannon-Weaver Communication Model
The canonical 1948/1949 block diagram: information source through transmitter,
channel (subject to noise), receiver, to destination. The framework reads
historical sources as messages produced by this process.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11

fig, ax = plt.subplots(1, 1, figsize=(12, 5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')

# Color palette consistent with other figures in the project
box_edge = '#2c3e50'
box_fill = '#ecf0f1'
noise_fill = '#fadbd8'
noise_edge = '#c0392b'
arrow_color = '#2c3e50'
label_color = '#34495e'

# Box positions (x_center, y_center, width, height, label)
boxes = [
    (1.0, 3.5, 1.6, 1.0, 'Information\nSource'),
    (3.4, 3.5, 1.6, 1.0, 'Transmitter'),
    (6.0, 3.5, 1.6, 1.0, 'Channel'),
    (8.6, 3.5, 1.6, 1.0, 'Receiver'),
    (11.0, 3.5, 1.6, 1.0, 'Destination'),
]

for x, y, w, h, label in boxes:
    rect = patches.FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.05",
        edgecolor=box_edge, facecolor=box_fill, linewidth=1.5
    )
    ax.add_patch(rect)
    ax.text(x, y, label, ha='center', va='center', fontsize=10,
            color=box_edge, fontweight='bold')

# Noise source box below the channel
noise_x, noise_y, noise_w, noise_h = 6.0, 1.2, 1.6, 1.0
noise_rect = patches.FancyBboxPatch(
    (noise_x - noise_w/2, noise_y - noise_h/2), noise_w, noise_h,
    boxstyle="round,pad=0.05",
    edgecolor=noise_edge, facecolor=noise_fill, linewidth=1.5
)
ax.add_patch(noise_rect)
ax.text(noise_x, noise_y, 'Noise\nSource', ha='center', va='center',
        fontsize=10, color=noise_edge, fontweight='bold', style='italic')

# Arrows between adjacent boxes, with labels above
arrow_pairs = [
    (1.8, 2.6, 'message'),
    (4.2, 5.0, 'signal'),
    (6.8, 7.4, 'received\nsignal'),
    (9.4, 10.2, 'message'),
]

for x_start, x_end, label in arrow_pairs:
    arrow = FancyArrowPatch(
        (x_start, 3.5), (x_end, 3.5),
        arrowstyle='->', mutation_scale=18,
        color=arrow_color, linewidth=1.4
    )
    ax.add_patch(arrow)
    ax.text((x_start + x_end) / 2, 4.25, label,
            ha='center', va='bottom', fontsize=9,
            color=label_color, style='italic')

# Arrow from noise source up into the channel
noise_arrow = FancyArrowPatch(
    (noise_x, noise_y + noise_h/2), (noise_x, 3.0),
    arrowstyle='->', mutation_scale=18,
    color=noise_edge, linewidth=1.4
)
ax.add_patch(noise_arrow)

# Title
ax.text(6.0, 5.7, 'The Shannon-Weaver Communication Model',
        ha='center', va='center', fontsize=13, fontweight='bold',
        color=box_edge)
ax.text(6.0, 5.25,
        'A message survives encoding, channel noise, and decoding before the receiver reconstructs it',
        ha='center', va='center', fontsize=10, style='italic',
        color=label_color)

# Bottom caption tying it to the framework
ax.text(6.0, 0.15,
        'The framework reads historical sources as messages produced by this process — encoded by senders, '
        'distorted by channels, reconstructed by receivers.',
        ha='center', va='center', fontsize=9, style='italic',
        color=label_color, wrap=True)

plt.tight_layout()
plt.savefig('figures/output/fig-016-shannon-weaver-model.png',
            dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-016-shannon-weaver-model.svg',
            bbox_inches='tight')
print("Generated: fig-016-shannon-weaver-model.png/.svg")
