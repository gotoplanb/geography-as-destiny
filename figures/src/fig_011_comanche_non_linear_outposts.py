"""
Figure 011: Comanche Non-Linear Outposts vs. Gansu Corridor Linear Infrastructure
Two-panel comparison showing why the terrain determines the organizational form.
"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6),
                                subplot_kw={'projection': ccrs.PlateCarree()})

# === LEFT PANEL: Comanchería — scattered, non-linear ===
ax1.set_extent([-108, -95, 28, 40], crs=ccrs.PlateCarree())
ax1.add_feature(cfeature.LAND, facecolor='#f5f0e1')
ax1.add_feature(cfeature.OCEAN, facecolor='#d4e6f1')
ax1.add_feature(cfeature.RIVERS, edgecolor='#85c1e9', linewidth=0.5)
ax1.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor='#7f8c8d')
ax1.add_feature(cfeature.BORDERS, linewidth=0.3, edgecolor='#cccccc', linestyle=':')

# Comanchería boundary (approximate)
comanche_lon = [-108, -105, -100, -97, -96, -97, -100, -104, -108]
comanche_lat = [37, 39, 38, 36, 33, 30, 29, 32, 37]
ax1.fill(comanche_lon, comanche_lat, color='#e74c3c', alpha=0.1, transform=ccrs.PlateCarree())
ax1.plot(comanche_lon, comanche_lat, color='#e74c3c', linewidth=1.5, linestyle='--',
         transform=ccrs.PlateCarree())

# Scattered outpost/camp locations (approximate seasonal positions)
np.random.seed(42)
n_camps = 25
camp_lons = np.random.uniform(-106, -97, n_camps)
camp_lats = np.random.uniform(30, 38, n_camps)
ax1.scatter(camp_lons, camp_lats, c='#c0392b', s=30, zorder=5,
            transform=ccrs.PlateCarree(), edgecolors='#2c3e50', linewidth=0.5)

# Arkansas River (approximate)
ark_lon = [-106, -104, -102, -100, -98, -96]
ark_lat = [38.5, 38, 37.5, 37.5, 37, 36.5]
ax1.plot(ark_lon, ark_lat, color='#3498db', linewidth=1.5, transform=ccrs.PlateCarree())
ax1.text(-101, 38.5, 'Arkansas R.', fontsize=7, color='#3498db',
         transform=ccrs.PlateCarree(), style='italic')

# Big Timbers trade center
ax1.plot(-103.5, 38, '*', color='#e67e22', markersize=12, zorder=6,
         transform=ccrs.PlateCarree())
ax1.text(-103.5, 37, 'Big Timbers\n(seasonal trade)', fontsize=7, color='#e67e22',
         ha='center', transform=ccrs.PlateCarree(), fontweight='bold')

ax1.set_title('Comanchería (~1750)\nScattered camps, no linear spine\nNo permanent urban nodes',
              fontsize=10, fontweight='bold')
ax1.text(-101, 29, 'COMANCHERÍA', fontsize=11, color='#c0392b', ha='center',
         transform=ccrs.PlateCarree(), fontweight='bold', alpha=0.5)

# === RIGHT PANEL: Gansu Corridor — linear, organized ===
ax2.set_extent([88, 108, 34, 44], crs=ccrs.PlateCarree())
ax2.add_feature(cfeature.LAND, facecolor='#f5f0e1')
ax2.add_feature(cfeature.OCEAN, facecolor='#d4e6f1')
ax2.add_feature(cfeature.RIVERS, edgecolor='#85c1e9', linewidth=0.5)
ax2.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor='#7f8c8d')
ax2.add_feature(cfeature.BORDERS, linewidth=0.3, edgecolor='#cccccc', linestyle=':')

# Gansu Corridor route (approximate)
gansu_lon = [90, 93, 95, 97, 99, 101, 103, 105, 107]
gansu_lat = [40, 40, 40.5, 40, 39.5, 39, 38, 37, 35]
ax2.plot(gansu_lon, gansu_lat, color='#2980b9', linewidth=3, transform=ccrs.PlateCarree(),
         zorder=3)

# Linear nodes along the corridor
corridor_nodes = [
    (90, 40.1, 'Hami'),
    (93, 42.9, 'Turfan'),
    (94.7, 40.1, 'Dunhuang'),
    (98, 39.7, 'Zhangye'),
    (101, 38.5, 'Wuwei'),
    (104, 37, 'Lanzhou'),
]
for lon, lat, name in corridor_nodes:
    ax2.plot(lon, lat, 'o', color='#2c3e50', markersize=8, zorder=5,
             transform=ccrs.PlateCarree())
    ax2.text(lon, lat + 0.8, name, fontsize=7, ha='center', fontweight='bold',
             color='#2c3e50', transform=ccrs.PlateCarree())

# Jade Gate marker
ax2.plot(93.5, 40, '*', color='#e67e22', markersize=12, zorder=6,
         transform=ccrs.PlateCarree())
ax2.text(93.5, 38.8, 'Jade Gate', fontsize=7, color='#e67e22', ha='center',
         transform=ccrs.PlateCarree(), fontweight='bold')

# Taklamakan label
ax2.text(92, 38, 'TAKLAMAKAN', fontsize=8, color='#a0896c', ha='center',
         style='italic', transform=ccrs.PlateCarree())

# Great Wall approximate line
wall_lon = [94, 97, 100, 103, 106]
wall_lat = [40.5, 40.5, 39.8, 38.5, 37.5]
ax2.plot(wall_lon, wall_lat, color='#7f8c8d', linewidth=1, linestyle=':',
         transform=ccrs.PlateCarree())
ax2.text(100, 41, 'Great Wall', fontsize=6, color='#7f8c8d', ha='center',
         style='italic', transform=ccrs.PlateCarree())

ax2.set_title('Gansu Corridor (~750 CE)\nLinear nodes along a geographic spine\nPermanent cities with archives',
              fontsize=10, fontweight='bold')

# Suptitle
fig.suptitle('The Terrain Determines the Organizational Form\nNo spine → no permanent nodes. Linear spine → cities with institutions.',
             fontsize=13, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('figures/output/fig-011-comanche-non-linear-outposts.png', dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-011-comanche-non-linear-outposts.svg', bbox_inches='tight')
print("Generated: fig-011-comanche-non-linear-outposts.png/.svg")
