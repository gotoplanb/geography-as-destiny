"""
Figure 005: The Silk Road Corridor — Terrain Determines Routes (static version)
Simplified matplotlib/cartopy map showing terrain, routes, and nodes.
Interactive Leaflet version available on the website.
"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9

fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Extent: Mediterranean to eastern China, Horn of Africa to Central Siberia
ax.set_extent([20, 120, 10, 55], crs=ccrs.PlateCarree())

# Terrain features
ax.add_feature(cfeature.LAND, facecolor='#f5f0e1', edgecolor='none')
ax.add_feature(cfeature.OCEAN, facecolor='#d4e6f1')
ax.add_feature(cfeature.LAKES, facecolor='#d4e6f1', edgecolor='#aab7c4', linewidth=0.5)
ax.add_feature(cfeature.RIVERS, edgecolor='#85c1e9', linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.3, edgecolor='#cccccc', linestyle=':')
ax.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor='#7f8c8d')

# Add shaded relief-like effect using terrain coloring for key mountain ranges
# (simplified — real shaded relief would need DEM data)
mountain_regions = [
    # Himalayas / Karakoram / Hindu Kush / Pamirs
    {'lon': [65, 70, 75, 80, 85, 90, 95, 100], 'lat': [30, 33, 35, 34, 30, 28, 28, 30],
     'color': '#c9b89e', 'label': None},
    # Tian Shan
    {'lon': [67, 72, 78, 85, 90], 'lat': [40, 42, 43, 43, 42],
     'color': '#c9b89e', 'label': 'Tian Shan'},
    # Kunlun
    {'lon': [74, 80, 86, 92], 'lat': [35, 36, 36, 35],
     'color': '#c9b89e', 'label': 'Kunlun Mts'},
]

# Taklamakan Desert shading
takla_lon = [76, 78, 82, 86, 88, 86, 82, 78, 76]
takla_lat = [38, 40, 40.5, 40, 38, 37, 36.5, 37, 38]
ax.fill(takla_lon, takla_lat, color='#e8dcc8', alpha=0.6, transform=ccrs.PlateCarree())
ax.text(82, 38.5, 'TAKLAMAKAN\nDESERT', ha='center', fontsize=7, color='#a0896c',
        style='italic', transform=ccrs.PlateCarree())

# Karakum Desert
karakum_lon = [54, 58, 62, 64, 62, 58, 54]
karakum_lat = [37, 39, 39.5, 38, 36, 35.5, 37]
ax.fill(karakum_lon, karakum_lat, color='#e8dcc8', alpha=0.4, transform=ccrs.PlateCarree())
ax.text(59, 37.5, 'Karakum', ha='center', fontsize=6, color='#a0896c',
        style='italic', transform=ccrs.PlateCarree())

# === ROUTES ===

# Northern overland route
north_route_lon = [35, 40, 44, 50, 55, 60, 66, 69, 72, 76, 80, 87, 93, 100, 108, 112]
north_route_lat = [32, 37, 38, 37, 38, 40, 40, 39, 40, 41, 42, 42, 43, 42, 38, 35]
ax.plot(north_route_lon, north_route_lat, color='#2980b9', linewidth=2,
        label='Northern overland route', transform=ccrs.PlateCarree(), zorder=3)

# Southern overland route
south_route_lon = [66, 69, 72, 76, 79, 83, 87, 93]
south_route_lat = [40, 39, 38, 37, 36.5, 36, 37, 43]
ax.plot(south_route_lon, south_route_lat, color='#c0392b', linewidth=1.5, linestyle='--',
        label='Southern overland route (fragile)', transform=ccrs.PlateCarree(), zorder=3)

# Maritime route
maritime_lon = [35, 40, 50, 55, 60, 68, 75, 80, 85, 95, 100, 105, 110, 115, 118]
maritime_lat = [30, 25, 22, 20, 22, 20, 15, 12, 10, 12, 13, 12, 15, 20, 25]
ax.plot(maritime_lon, maritime_lat, color='#27ae60', linewidth=2,
        label='Maritime route (monsoon highway)', transform=ccrs.PlateCarree(), zorder=3)

# === NODES ===

# Active nodes
active_nodes = [
    (35, 32, 'Levant', 8),
    (44, 38, 'Baghdad', 7),
    (52, 36, 'Isfahan', 6),
    (60, 40, 'Merv', 6),
    (66.9, 39.6, 'Samarkand', 9),
    (64.4, 39.8, 'Bukhara', 7),
    (76, 40.1, 'Kashgar', 7),
    (89, 42.9, 'Turfan', 6),
    (94.7, 40.1, 'Dunhuang', 8),
    (108, 34.3, "Xi'an", 8),
    (79.5, 37, 'Khotan', 5),
]

for lon, lat, name, size in active_nodes:
    ax.plot(lon, lat, 'o', color='#2c3e50', markersize=size, zorder=5,
            transform=ccrs.PlateCarree())
    ax.text(lon, lat + 1.2, name, ha='center', fontsize=7, fontweight='bold',
            color='#2c3e50', transform=ccrs.PlateCarree(), zorder=5)

# Abandoned nodes (hollow)
abandoned = [
    (82.7, 37.8, 'Niya †'),
    (80, 38.5, 'Miran †'),
]
for lon, lat, name in abandoned:
    ax.plot(lon, lat, 'o', color='#c0392b', markersize=5, markerfacecolor='none',
            markeredgewidth=1.5, zorder=5, transform=ccrs.PlateCarree())
    ax.text(lon, lat - 1.2, name, ha='center', fontsize=6, color='#c0392b',
            style='italic', transform=ccrs.PlateCarree())

# Swahili Coast nodes
swahili = [
    (39.3, -6.2, 'Zanzibar'),
    (39.5, -8.8, 'Kilwa'),
    (41, -2, 'Mombasa'),
]
for lon, lat, name in swahili:
    ax.plot(lon, lat, 's', color='#27ae60', markersize=5, zorder=5,
            transform=ccrs.PlateCarree())
    ax.text(lon + 2, lat, name, ha='left', fontsize=6, color='#27ae60',
            transform=ccrs.PlateCarree())

# === CHOKEPOINT LABELS ===
chokepoints = [
    (70, 36, 'PAMIR\nKNOT', '#8e44ad'),
    (94, 42, 'GANSU\nCORRIDOR', '#8e44ad'),
    (67, 33, 'Afghan\nCorridor', '#8e44ad'),
]
for lon, lat, label, color in chokepoints:
    ax.text(lon, lat, label, ha='center', fontsize=7, color=color,
            fontweight='bold', style='italic', transform=ccrs.PlateCarree(),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=color, alpha=0.7))

# Geographic structure labels
ax.text(30, 35, 'Western\nFan', ha='center', fontsize=8, color='#7f8c8d',
        style='italic', transform=ccrs.PlateCarree())
ax.text(55, 42, 'Iranian\nFunnel', ha='center', fontsize=8, color='#7f8c8d',
        style='italic', transform=ccrs.PlateCarree())
ax.text(66, 43, 'Transoxiana\n(the heart)', ha='center', fontsize=8, color='#7f8c8d',
        style='italic', transform=ccrs.PlateCarree())
ax.text(113, 32, 'Eastern\nFan', ha='center', fontsize=8, color='#7f8c8d',
        style='italic', transform=ccrs.PlateCarree())

# Jade Gate marker
ax.plot(93.5, 40, '*', color='#e67e22', markersize=12, zorder=6,
        transform=ccrs.PlateCarree())
ax.text(93.5, 38.5, 'Jade Gate', ha='center', fontsize=7, color='#e67e22',
        fontweight='bold', transform=ccrs.PlateCarree())

# Legend and title
ax.legend(loc='lower left', fontsize=8, framealpha=0.9)
ax.set_title('The Silk Road — A Relay Network, Not a Road\nTwo funnels, two fans, a knot in the middle — overland and maritime',
             fontsize=13, fontweight='bold', pad=12)

# Subtitle
ax.text(70, 8, '† = abandoned (water table dropped)    ★ = Jade Gate (imperial frontier)',
        ha='center', fontsize=7, color='#7f8c8d', transform=ccrs.PlateCarree())

plt.tight_layout()
plt.savefig('figures/output/fig-005-silk-road-corridor.png', dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-005-silk-road-corridor.svg', bbox_inches='tight')
print("Generated: fig-005-silk-road-corridor.png/.svg")
