"""
Figure 014: The Occluded Front — Nomadic Solvent and Sedentary Succession
Two-panel comparison: Texas/Southwest (1820-1845) and Transoxiana (700-900 CE).
Same mechanism: nomadic pressure dissolves incumbent sedentary order;
incoming sedentary empire crystallizes in the dissolved space.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9

DISSOLVE_COLOR   = '#e8d5a3'   # amber — the vacuum / dissolved zone
NOMADIC_COLOR    = '#c0392b'   # red — nomadic pressure system
SEDENTARY_IN_COLOR = '#2980b9' # blue — incoming sedentary empire
SEDENTARY_OUT_COLOR = '#7f8c8d' # grey — retreating sedentary empire
COLLISION_COLOR  = '#8e44ad'   # purple — collision / occluded front zone
LAND_COLOR       = '#f5f0e1'
OCEAN_COLOR      = '#d4e6f1'


def arrow(ax, x0, y0, dx, dy, color, width=0.04, head=0.25, alpha=0.85, zorder=6):
    ax.annotate('', xy=(x0+dx, y0+dy), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f'->,head_width={head},head_length={head*0.7}',
                                color=color, lw=2.5, alpha=alpha),
                xycoords=ccrs.PlateCarree()._as_mpl_transform(ax),
                textcoords=ccrs.PlateCarree()._as_mpl_transform(ax),
                zorder=zorder)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7),
                                subplot_kw={'projection': ccrs.PlateCarree()})

# ============================================================
# LEFT PANEL — North America, ~1820–1845
# Comanche (red) moving SW; Americans (blue) catching up from E
# Dissolved zone = northern Mexico power vacuum
# ============================================================
ax1.set_extent([-113, -88, 17, 42], crs=ccrs.PlateCarree())
ax1.add_feature(cfeature.LAND,      facecolor=LAND_COLOR)
ax1.add_feature(cfeature.OCEAN,     facecolor=OCEAN_COLOR)
ax1.add_feature(cfeature.RIVERS,    edgecolor='#85c1e9', linewidth=0.4)
ax1.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor='#7f8c8d')
ax1.add_feature(cfeature.BORDERS,   linewidth=0.4, edgecolor='#aaaaaa', linestyle=':')

# --- Dissolved zone: northern Mexico power vacuum ---
vacuum_lon = [-113, -105, -100, -97, -97, -104, -113]
vacuum_lat = [  32,   32,   29,  26,  22,   22,   32]
ax1.fill(vacuum_lon, vacuum_lat, color=DISSOLVE_COLOR, alpha=0.55,
         transform=ccrs.PlateCarree(), zorder=2)
ax1.text(-105, 26.5, 'MEXICAN\nPOWER VACUUM\n(dissolved zone)',
         fontsize=7.5, color='#8B6914', ha='center', style='italic',
         transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Comanchería core ---
core_lon = [-104, -100, -97, -96, -98, -102, -104]
core_lat = [  37,   38,  36,  33,  30,   31,   37]
ax1.fill(core_lon, core_lat, color=NOMADIC_COLOR, alpha=0.12,
         transform=ccrs.PlateCarree(), zorder=3)
ax1.plot(core_lon, core_lat, color=NOMADIC_COLOR, linewidth=1.2,
         linestyle='--', transform=ccrs.PlateCarree(), zorder=4)
ax1.text(-100, 34.5, 'COMANCHERÍA', fontsize=8, color=NOMADIC_COLOR,
         ha='center', fontweight='bold', transform=ccrs.PlateCarree(),
         zorder=7, path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Comanche pressure arrows (SW movement) ---
for x0, y0, dx, dy in [
    (-103, 33, -3.5, -3.5),
    (-100, 31, -2.5, -3.0),
    (-97,  30, -3.0, -3.5),
]:
    ax1.annotate('', xy=(x0+dx, y0+dy), xytext=(x0, y0),
                 arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.25',
                                 color=NOMADIC_COLOR, lw=2.5, alpha=0.85),
                 xycoords=ccrs.PlateCarree()._as_mpl_transform(ax1),
                 textcoords=ccrs.PlateCarree()._as_mpl_transform(ax1), zorder=6)

ax1.text(-99, 23.5, 'Comanche\npressure\n(slower front)',
         fontsize=7.5, color=NOMADIC_COLOR, ha='center', fontweight='bold',
         transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- American pressure arrows (W movement, faster) ---
for x0, y0, dx, dy in [
    (-91, 33,  -5.5, -0.5),
    (-91, 30,  -5.0, -1.0),
    (-91, 27,  -4.5, -1.5),
]:
    ax1.annotate('', xy=(x0+dx, y0+dy), xytext=(x0, y0),
                 arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.25',
                                 color=SEDENTARY_IN_COLOR, lw=2.5, alpha=0.85),
                 xycoords=ccrs.PlateCarree()._as_mpl_transform(ax1),
                 textcoords=ccrs.PlateCarree()._as_mpl_transform(ax1), zorder=6)

ax1.text(-89.5, 29, 'American\nexpansion\n(faster front)',
         fontsize=7.5, color=SEDENTARY_IN_COLOR, ha='left', fontweight='bold',
         transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Collision / occluded front zone (Texas–New Mexico) ---
collision_lon = [-107, -100, -97, -96, -100, -107]
collision_lat = [  34,   34,  30,  28,   28,   34]
ax1.fill(collision_lon, collision_lat, color=COLLISION_COLOR, alpha=0.18,
         transform=ccrs.PlateCarree(), zorder=5)
ax1.plot(collision_lon, collision_lat, color=COLLISION_COLOR, linewidth=1.5,
         transform=ccrs.PlateCarree(), zorder=5)
ax1.text(-101.5, 31.2, 'COLLISION ZONE\n(Texas / New Mexico)',
         fontsize=7.5, color=COLLISION_COLOR, ha='center', fontweight='bold',
         transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Mexico City (retreating center) ---
ax1.plot(-99.1, 19.4, 's', color=SEDENTARY_OUT_COLOR, markersize=9, zorder=7,
         transform=ccrs.PlateCarree())
ax1.text(-99.1, 18, 'Mexico City\n(retreating center)', fontsize=7, color=SEDENTARY_OUT_COLOR,
         ha='center', transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

ax1.set_title('North America, ~1820–1845\nComanche dissolves Mexican sovereignty;\nAmerica crystallizes in the dissolved space.',
              fontsize=10, fontweight='bold')

# ============================================================
# RIGHT PANEL — Central Asia, ~700–900 CE
# Turkic / steppe (red) moving W; Abbasid/Samanid (blue) moving NE
# Dissolved zone = Tang grip on Tarim Basin / Transoxiana
# ============================================================
ax2.set_extent([44, 90, 30, 52], crs=ccrs.PlateCarree())
ax2.add_feature(cfeature.LAND,      facecolor=LAND_COLOR)
ax2.add_feature(cfeature.OCEAN,     facecolor=OCEAN_COLOR)
ax2.add_feature(cfeature.RIVERS,    edgecolor='#85c1e9', linewidth=0.4)
ax2.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor='#7f8c8d')
ax2.add_feature(cfeature.BORDERS,   linewidth=0.4, edgecolor='#aaaaaa', linestyle=':')

# --- Dissolved zone: Transoxiana / Tarim Basin ---
vacuum_lon2 = [56, 62, 70, 78, 80, 72, 62, 56]
vacuum_lat2 = [44, 46, 45, 43, 38, 36, 38, 44]
ax2.fill(vacuum_lon2, vacuum_lat2, color=DISSOLVE_COLOR, alpha=0.55,
         transform=ccrs.PlateCarree(), zorder=2)
ax2.text(68, 40.5, 'TRANSOXIANA\n(dissolved zone)',
         fontsize=7.5, color='#8B6914', ha='center', style='italic',
         transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Samarkand ---
ax2.plot(66.9, 39.7, '*', color='#e67e22', markersize=13, zorder=8,
         transform=ccrs.PlateCarree())
ax2.text(66.9, 38.5, 'Samarkand', fontsize=7.5, ha='center', fontweight='bold',
         color='#e67e22', transform=ccrs.PlateCarree(), zorder=8,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Steppe / Turkic pressure (from NE, moving W) ---
for x0, y0, dx, dy in [
    (83, 46, -5, -2.0),
    (80, 43, -5, -1.5),
    (78, 40, -4, -1.0),
]:
    ax2.annotate('', xy=(x0+dx, y0+dy), xytext=(x0, y0),
                 arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.25',
                                 color=NOMADIC_COLOR, lw=2.5, alpha=0.85),
                 xycoords=ccrs.PlateCarree()._as_mpl_transform(ax2),
                 textcoords=ccrs.PlateCarree()._as_mpl_transform(ax2), zorder=6)

ax2.text(84.5, 46.5, 'Steppe / Turkic\npressure\n(slower front)',
         fontsize=7.5, color=NOMADIC_COLOR, ha='center', fontweight='bold',
         transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Abbasid/Samanid expansion (from SW, moving NE) ---
for x0, y0, dx, dy in [
    (50, 32, 4.5, 3.5),
    (54, 33, 4.0, 3.5),
    (57, 32, 3.5, 4.0),
]:
    ax2.annotate('', xy=(x0+dx, y0+dy), xytext=(x0, y0),
                 arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.25',
                                 color=SEDENTARY_IN_COLOR, lw=2.5, alpha=0.85),
                 xycoords=ccrs.PlateCarree()._as_mpl_transform(ax2),
                 textcoords=ccrs.PlateCarree()._as_mpl_transform(ax2), zorder=6)

ax2.text(49, 31, 'Abbasid /\nSamanid\nexpansion\n(faster front)',
         fontsize=7.5, color=SEDENTARY_IN_COLOR, ha='center', fontweight='bold',
         transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Collision zone: Transoxiana ---
collision_lon2 = [58, 66, 72, 68, 60, 58]
collision_lat2 = [42, 44, 42, 37, 37, 42]
ax2.fill(collision_lon2, collision_lat2, color=COLLISION_COLOR, alpha=0.18,
         transform=ccrs.PlateCarree(), zorder=5)
ax2.plot(collision_lon2, collision_lat2, color=COLLISION_COLOR, linewidth=1.5,
         transform=ccrs.PlateCarree(), zorder=5)
ax2.text(65, 43, 'COLLISION ZONE\n(Transoxiana)',
         fontsize=7.5, color=COLLISION_COLOR, ha='center', fontweight='bold',
         transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# --- Chang'an (retreating Tang center — off panel, just label direction) ---
ax2.text(88, 35, 'Chang\'an →\n(retreating center)',
         fontsize=7, color=SEDENTARY_OUT_COLOR, ha='center',
         transform=ccrs.PlateCarree(), zorder=7,
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

ax2.set_title('Central Asia, ~700–900 CE\nTurkic confederations dissolve Tang grip;\nAbbasid / Samanid order crystallizes in Transoxiana.',
              fontsize=10, fontweight='bold')

# ============================================================
# Legend and suptitle
# ============================================================
legend_elements = [
    mpatches.Patch(facecolor=DISSOLVE_COLOR, alpha=0.7,  label='Dissolved zone (power vacuum)'),
    mpatches.Patch(facecolor=NOMADIC_COLOR,  alpha=0.55, label='Nomadic pressure system (solvent)'),
    mpatches.Patch(facecolor=SEDENTARY_IN_COLOR, alpha=0.55, label='Incoming sedentary empire (crystallizing)'),
    mpatches.Patch(facecolor=COLLISION_COLOR, alpha=0.4, label='Collision / occluded front zone'),
    mpatches.Patch(facecolor=SEDENTARY_OUT_COLOR, alpha=0.55, label='Retreating sedentary empire'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=5,
           fontsize=8, framealpha=0.9, bbox_to_anchor=(0.5, -0.04))

fig.suptitle(
    'The Occluded Front: Nomadic Solvent and Sedentary Succession\n'
    '"The nomadic pressure system dissolves the incumbent. The incoming sedentary empire crystallizes in the dissolved space."',
    fontsize=12, fontweight='bold', y=1.02
)

plt.tight_layout()
out_base = 'figures/output/fig-014-occluded-front-nomadic-solvent'
plt.savefig(f'{out_base}.png', dpi=150, bbox_inches='tight')
plt.savefig(f'{out_base}.svg', bbox_inches='tight')
print(f"Generated: {out_base}.png/.svg")
