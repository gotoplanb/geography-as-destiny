"""
Figure 015: Tidal Pressure System vs Breaking Wave
Two-panel comparison: Silk Road (~50 BCE-1200 CE) and Yamnaya expansion (~3300-2500 BCE).

Same gradient-following mechanism, different pressure-system geometry:
- Tidal: two comparable civilization masses generating bidirectional flow,
  producing hybrid culture at relay nodes.
- Breaking wave: one high-pressure source producing outward pulse with
  weak diffuse backwash, producing population/cultural overlay.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9

# Color palette
MASS_EAST_COLOR    = '#b8860b'   # dark gold — Han/Tang China sphere
MASS_WEST_COLOR    = '#8b0000'   # dark red — Rome/Persia sphere
TIDAL_FLOW_COLOR   = '#2c5f8d'   # blue — bidirectional commercial flow
HYBRID_NODE_COLOR  = '#8e44ad'   # purple — hybrid cultural nodes

SOURCE_COLOR       = '#c0392b'   # red — Yamnaya high-pressure source
OVERLAY_COLOR      = '#85b8d4'   # light blue — receiving zone overlay
WAVE_ARROW_COLOR   = '#c0392b'   # red — outgoing wave arrows
BACKWASH_COLOR     = '#7f8c8d'   # grey — weak backwash

LAND_COLOR         = '#f5f0e1'
OCEAN_COLOR        = '#d4e6f1'


def label(ax, x, y, text, color, fontsize=8, weight='bold', italic=False):
    style = 'italic' if italic else 'normal'
    ax.text(x, y, text, fontsize=fontsize, color=color,
            ha='center', fontweight=weight, style=style,
            transform=ccrs.PlateCarree(), zorder=8,
            path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])


def arrow(ax, x0, y0, x1, y1, color, lw=2.5, alpha=0.85, head=0.35, style='->'):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f'{style},head_width={head},head_length={head*0.75}',
                                color=color, lw=lw, alpha=alpha),
                xycoords=ccrs.PlateCarree()._as_mpl_transform(ax),
                textcoords=ccrs.PlateCarree()._as_mpl_transform(ax),
                zorder=6)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7),
                                subplot_kw={'projection': ccrs.PlateCarree()})

# ============================================================
# LEFT PANEL — Silk Road Tidal System (~50 BCE – 1200 CE)
# Two civilization masses on opposite ends generating bidirectional flow.
# Hybrid cultural nodes emerge in the middle zone.
# ============================================================
ax1.set_extent([20, 125, 15, 55], crs=ccrs.PlateCarree())
ax1.add_feature(cfeature.LAND,      facecolor=LAND_COLOR)
ax1.add_feature(cfeature.OCEAN,     facecolor=OCEAN_COLOR)
ax1.add_feature(cfeature.RIVERS,    edgecolor='#85c1e9', linewidth=0.4)
ax1.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor='#7f8c8d')
ax1.add_feature(cfeature.BORDERS,   linewidth=0.4, edgecolor='#aaaaaa', linestyle=':')

# --- Eastern civilization mass (Han/Tang China) ---
china_lon = [102, 115, 122, 122, 115, 105, 102]
china_lat = [42,  42,  38,  28,  22,  28,  42]
ax1.fill(china_lon, china_lat, color=MASS_EAST_COLOR, alpha=0.30,
         transform=ccrs.PlateCarree(), zorder=2)
# Gravity well — concentric circles indicating commercial pull
for r in [3, 5, 7]:
    theta = np.linspace(0, 2*np.pi, 60)
    ax1.plot(112 + r*np.cos(theta), 34 + r*np.sin(theta)*0.6,
             color=MASS_EAST_COLOR, lw=0.6, alpha=0.4,
             transform=ccrs.PlateCarree(), zorder=3)
label(ax1, 112, 34, 'HAN / TANG\nCHINA',
      MASS_EAST_COLOR, fontsize=9.5)
label(ax1, 112, 27, 'civilization mass',
      MASS_EAST_COLOR, fontsize=7, weight='normal', italic=True)

# --- Western civilization mass (Rome / Persia) ---
west_lon = [22, 38, 52, 55, 50, 35, 22]
west_lat = [48, 45, 38, 30, 22, 25, 35]
ax1.fill(west_lon, west_lat, color=MASS_WEST_COLOR, alpha=0.30,
         transform=ccrs.PlateCarree(), zorder=2)
for r in [3, 5, 7]:
    theta = np.linspace(0, 2*np.pi, 60)
    ax1.plot(38 + r*np.cos(theta), 35 + r*np.sin(theta)*0.6,
             color=MASS_WEST_COLOR, lw=0.6, alpha=0.4,
             transform=ccrs.PlateCarree(), zorder=3)
label(ax1, 38, 35, 'ROME /\nPERSIA',
      MASS_WEST_COLOR, fontsize=9.5)
label(ax1, 38, 28, 'civilization mass',
      MASS_WEST_COLOR, fontsize=7, weight='normal', italic=True)

# --- Bidirectional corridor flow ---
# Eastward arrows (W → E) — Western goods to China
for y in [42, 38, 34, 30]:
    arrow(ax1, 50, y, 100, y, TIDAL_FLOW_COLOR, lw=2.0, alpha=0.7, head=0.3)

# Westward arrows (E → W) — Eastern goods to Rome/Persia
for y in [44, 40, 36, 32]:
    arrow(ax1, 100, y, 50, y, TIDAL_FLOW_COLOR, lw=2.0, alpha=0.7, head=0.3)

# --- Hybrid cultural nodes in the middle ---
hybrid_nodes = [
    (65, 40, 'SOGDIANA',     'Persian-speaking\ncommercial broker'),
    (72, 35, 'GANDHARA',     'Greek-Indian\nBuddhist art'),
    (94, 40, 'DUNHUANG',     'multilingual\narchive node'),
]
for lon, lat, name, desc in hybrid_nodes:
    ax1.plot(lon, lat, 'o', color=HYBRID_NODE_COLOR, markersize=10,
             markeredgecolor='white', markeredgewidth=1.5,
             transform=ccrs.PlateCarree(), zorder=7)
    label(ax1, lon, lat-1.8, name, HYBRID_NODE_COLOR, fontsize=7.5)
    label(ax1, lon, lat-3.6, desc, HYBRID_NODE_COLOR,
          fontsize=6.5, weight='normal', italic=True)

# --- Panel title and caption ---
ax1.set_title('Tidal System — Silk Road (~50 BCE – 1200 CE)',
              fontsize=11, fontweight='bold', pad=10)
ax1.text(0.5, -0.10,
         'Two comparable civilization masses generate continuous bidirectional flow.\n'
         'Hybrid cultural forms emerge at relay nodes where the two flows meet.',
         transform=ax1.transAxes, ha='center', fontsize=8.5, style='italic')

# ============================================================
# RIGHT PANEL — Yamnaya Breaking Wave (~3300–2500 BCE)
# Single source generating outward pulse in three directions.
# Receiving zones absorb the wave; weak diffuse backwash.
# ============================================================
ax2.set_extent([-10, 100, 30, 65], crs=ccrs.PlateCarree())
ax2.add_feature(cfeature.LAND,      facecolor=LAND_COLOR)
ax2.add_feature(cfeature.OCEAN,     facecolor=OCEAN_COLOR)
ax2.add_feature(cfeature.RIVERS,    edgecolor='#85c1e9', linewidth=0.4)
ax2.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor='#7f8c8d')
ax2.add_feature(cfeature.BORDERS,   linewidth=0.4, edgecolor='#aaaaaa', linestyle=':')

# --- Yamnaya source: Pontic-Caspian high-pressure zone ---
source_lon = [38, 55, 60, 55, 38, 32, 38]
source_lat = [52, 52, 48, 44, 44, 48, 52]
ax2.fill(source_lon, source_lat, color=SOURCE_COLOR, alpha=0.50,
         transform=ccrs.PlateCarree(), zorder=4)
# Gravity well — concentric pressure rings (radiating outward)
for r in [4, 7, 10]:
    theta = np.linspace(0, 2*np.pi, 60)
    ax2.plot(46 + r*np.cos(theta), 48 + r*np.sin(theta)*0.7,
             color=SOURCE_COLOR, lw=0.5, alpha=0.35,
             transform=ccrs.PlateCarree(), zorder=3)
label(ax2, 46, 48, 'YAMNAYA',
      SOURCE_COLOR, fontsize=10)
label(ax2, 46, 45, 'Pontic-Caspian\nhigh-pressure source',
      SOURCE_COLOR, fontsize=7, weight='normal', italic=True)

# --- Receiving zones (cultural overlay) ---
# Western Europe overlay (Corded Ware, Bell Beaker)
europe_lon = [-5,  20, 25,  20,  10,  -5, -5]
europe_lat = [55,  58, 52,  46,  44,  48, 55]
ax2.fill(europe_lon, europe_lat, color=OVERLAY_COLOR, alpha=0.40,
         transform=ccrs.PlateCarree(), zorder=2)
label(ax2, 10, 52, 'EUROPEAN OVERLAY',
      '#2c5d7a', fontsize=7.5)
label(ax2, 10, 49, '(Corded Ware,\nBell Beaker)',
      '#2c5d7a', fontsize=6.5, weight='normal', italic=True)

# Eastern Altai overlay (Afanasievo)
altai_lon = [78, 92, 95, 90, 80, 78]
altai_lat = [54, 55, 50, 46, 48, 54]
ax2.fill(altai_lon, altai_lat, color=OVERLAY_COLOR, alpha=0.40,
         transform=ccrs.PlateCarree(), zorder=2)
label(ax2, 87, 51, 'ALTAI OVERLAY',
      '#2c5d7a', fontsize=7.5)
label(ax2, 87, 48, '(Afanasievo,\nleapfrog outpost)',
      '#2c5d7a', fontsize=6.5, weight='normal', italic=True)

# Southeastern Iranian plateau overlay
iran_lon = [50, 70, 70, 60, 50, 50]
iran_lat = [40, 40, 33, 30, 32, 40]
ax2.fill(iran_lon, iran_lat, color=OVERLAY_COLOR, alpha=0.40,
         transform=ccrs.PlateCarree(), zorder=2)
label(ax2, 60, 36, 'IRANIAN OVERLAY',
      '#2c5d7a', fontsize=7.5)
label(ax2, 60, 33, '(Indo-Iranian\nbranch)',
      '#2c5d7a', fontsize=6.5, weight='normal', italic=True)

# --- Outward wave arrows (strong, red) ---
# West to Europe
for x0, y0, x1, y1 in [
    (40, 51, 12, 55),
    (38, 49, 8,  50),
    (38, 47, 5,  46),
]:
    arrow(ax2, x0, y0, x1, y1, WAVE_ARROW_COLOR, lw=3.0, alpha=0.85, head=0.4)

# East to Altai
for x0, y0, x1, y1 in [
    (52, 50, 82, 53),
    (54, 48, 85, 50),
]:
    arrow(ax2, x0, y0, x1, y1, WAVE_ARROW_COLOR, lw=3.0, alpha=0.85, head=0.4)

# Southeast to Iranian plateau
for x0, y0, x1, y1 in [
    (50, 45, 58, 38),
    (52, 46, 62, 36),
]:
    arrow(ax2, x0, y0, x1, y1, WAVE_ARROW_COLOR, lw=3.0, alpha=0.85, head=0.4)

# --- Weak backwash arrows (thin, dashed, grey) ---
# From Europe back to Yamnaya
arrow(ax2, 12, 53, 36, 50, BACKWASH_COLOR, lw=1.0, alpha=0.5,
      head=0.2, style='->')
# From Altai back to Yamnaya
arrow(ax2, 82, 51, 54, 49, BACKWASH_COLOR, lw=1.0, alpha=0.5,
      head=0.2, style='->')
# From Iranian plateau back to Yamnaya
arrow(ax2, 60, 38, 48, 45, BACKWASH_COLOR, lw=1.0, alpha=0.5,
      head=0.2, style='->')

# Backwash label
ax2.text(28, 58, 'weak diffuse backwash →',
         fontsize=7, color=BACKWASH_COLOR, style='italic',
         transform=ccrs.PlateCarree(), zorder=8,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Panel title and caption ---
ax2.set_title('Breaking Wave — Yamnaya Expansion (~3300–2500 BCE)',
              fontsize=11, fontweight='bold', pad=10)
ax2.text(0.5, -0.10,
         'Single high-pressure source generates outward pulse in three directions.\n'
         'Receiving zones absorb the overlay; backwash is weak and diffuse.',
         transform=ax2.transAxes, ha='center', fontsize=8.5, style='italic')

# ============================================================
# Master title and legend
# ============================================================
fig.suptitle('Pressure-System Geometry Determines Cultural Outcome',
             fontsize=13, fontweight='bold', y=1.00)

# Legend below both panels
legend_elements = [
    mpatches.Patch(facecolor=MASS_EAST_COLOR, alpha=0.30, label='Civilization mass (sedentary)'),
    mpatches.Patch(facecolor=SOURCE_COLOR, alpha=0.50, label='High-pressure source (pastoralist)'),
    mpatches.Patch(facecolor=OVERLAY_COLOR, alpha=0.40, label='Cultural overlay zone'),
    mpatches.Patch(facecolor=HYBRID_NODE_COLOR, alpha=0.7, label='Hybrid cultural node'),
    mpatches.Patch(facecolor=TIDAL_FLOW_COLOR, alpha=0.7, label='Bidirectional commercial flow'),
    mpatches.Patch(facecolor=WAVE_ARROW_COLOR, alpha=0.85, label='Outward wave (strong)'),
    mpatches.Patch(facecolor=BACKWASH_COLOR, alpha=0.5, label='Backwash (weak)'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=4,
           bbox_to_anchor=(0.5, -0.05), fontsize=8, frameon=False)

plt.tight_layout(rect=[0, 0.04, 1, 0.97])

# Save outputs
output_dir = '/Users/davestanton/geography-as-destiny/figures/output'
plt.savefig(f'{output_dir}/fig-015-tidal-vs-breaking-wave.png',
            dpi=200, bbox_inches='tight', facecolor='white')
plt.savefig(f'{output_dir}/fig-015-tidal-vs-breaking-wave.svg',
            bbox_inches='tight', facecolor='white')

print('Saved: fig-015-tidal-vs-breaking-wave.{png,svg}')
