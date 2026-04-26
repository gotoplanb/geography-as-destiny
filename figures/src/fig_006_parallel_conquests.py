"""
Figure 006: The Parallel Conquests — Static Version
2x3 grid: American West (top) and Central Asian steppe (bottom) at 1865, 1875, 1885.
Shows railroad advance and territory change simultaneously.
"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 8

fig, axes = plt.subplots(2, 3, figsize=(16, 9),
                          subplot_kw={'projection': ccrs.PlateCarree()})

years = [1865, 1875, 1885]

# === TOP ROW: American West ===
for i, (ax, year) in enumerate(zip(axes[0], years)):
    ax.set_extent([-112, -92, 28, 44], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, facecolor='#f5f0e1')
    ax.add_feature(cfeature.RIVERS, edgecolor='#85c1e9', linewidth=0.3)
    ax.add_feature(cfeature.COASTLINE, linewidth=0.3, edgecolor='#7f8c8d')
    ax.add_feature(cfeature.BORDERS, linewidth=0.2, edgecolor='#cccccc', linestyle=':')

    # Comanchería shrinking over time
    if year == 1865:
        com_lon = [-108, -105, -100, -97, -96, -97, -100, -104, -108]
        com_lat = [37, 39, 38, 36, 33, 30, 29, 32, 37]
        ax.fill(com_lon, com_lat, color='#e74c3c', alpha=0.2, transform=ccrs.PlateCarree())
        ax.text(-101, 33, 'Comanchería', fontsize=8, color='#c0392b', ha='center',
                transform=ccrs.PlateCarree(), fontweight='bold')
    elif year == 1875:
        com_lon = [-106, -103, -100, -98, -97, -99, -103, -106]
        com_lat = [36, 37, 36, 34, 32, 31, 32, 36]
        ax.fill(com_lon, com_lat, color='#e74c3c', alpha=0.15, transform=ccrs.PlateCarree())
        ax.text(-101, 33, 'Shrinking', fontsize=7, color='#c0392b', ha='center',
                transform=ccrs.PlateCarree(), style='italic')
    else:  # 1885
        ax.text(-101, 33, 'Reservations\nonly', fontsize=7, color='#c0392b', ha='center',
                transform=ccrs.PlateCarree(), style='italic')

    # Railroad extending westward
    if year == 1865:
        rail_lon = [-92, -96]
        rail_lat = [41, 41]
    elif year == 1875:
        rail_lon = [-92, -96, -100, -104, -108]
        rail_lat = [41, 41, 41, 40, 39]
    else:
        rail_lon = [-92, -96, -100, -104, -108, -112]
        rail_lat = [41, 41, 41, 40, 39, 38]
        # Add southern lines
        ax.plot([-96, -100, -104], [35, 35, 34], color='#2c3e50', linewidth=1.5,
                transform=ccrs.PlateCarree())

    ax.plot(rail_lon, rail_lat, color='#2c3e50', linewidth=2,
            transform=ccrs.PlateCarree(), zorder=4)

    # US controlled shading (expanding)
    if year >= 1875:
        us_lon = [-112, -108, -100, -92, -92, -112]
        us_lat = [44, 44, 44, 44, 40 if year == 1875 else 28, 40 if year == 1875 else 28]
        ax.fill(us_lon, us_lat, color='#2980b9', alpha=0.08, transform=ccrs.PlateCarree())

    ax.set_title(f'American West — {year}', fontsize=10, fontweight='bold')

# === BOTTOM ROW: Central Asian Steppe ===
for i, (ax, year) in enumerate(zip(axes[1], years)):
    ax.set_extent([50, 72, 35, 48], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, facecolor='#f5f0e1')
    ax.add_feature(cfeature.RIVERS, edgecolor='#85c1e9', linewidth=0.3)
    ax.add_feature(cfeature.COASTLINE, linewidth=0.3, edgecolor='#7f8c8d')
    ax.add_feature(cfeature.BORDERS, linewidth=0.2, edgecolor='#cccccc', linestyle=':')

    # Caspian Sea
    casp_lon = [50, 51, 52, 54, 53, 51, 50]
    casp_lat = [37, 39, 42, 44, 46, 47, 37]
    ax.fill(casp_lon, casp_lat, color='#d4e6f1', transform=ccrs.PlateCarree())

    # Aral Sea (shrinking less in this era)
    aral_lon = [58, 59, 60, 61, 60, 59, 58]
    aral_lat = [44, 45, 46, 45, 44, 43.5, 44]
    ax.fill(aral_lon, aral_lat, color='#d4e6f1', transform=ccrs.PlateCarree())

    # Kazakh/Turkmen territory shrinking
    if year == 1865:
        nom_lon = [54, 60, 68, 72, 72, 68, 60, 54]
        nom_lat = [38, 37, 37, 38, 45, 46, 46, 45]
        ax.fill(nom_lon, nom_lat, color='#e74c3c', alpha=0.2, transform=ccrs.PlateCarree())
        ax.text(63, 41, 'Kazakh &\nTurkmen\nTerritory', fontsize=7, color='#c0392b',
                ha='center', transform=ccrs.PlateCarree(), fontweight='bold')
    elif year == 1875:
        nom_lon = [56, 62, 68, 72, 72, 68, 62, 56]
        nom_lat = [38, 37, 38, 40, 45, 46, 46, 45]
        ax.fill(nom_lon, nom_lat, color='#e74c3c', alpha=0.15, transform=ccrs.PlateCarree())
        ax.text(64, 41, 'Shrinking', fontsize=7, color='#c0392b', ha='center',
                transform=ccrs.PlateCarree(), style='italic')
    else:
        ax.text(64, 41, 'Russian\ncontrol', fontsize=7, color='#c0392b', ha='center',
                transform=ccrs.PlateCarree(), style='italic')

    # Transcaspian Railway extending eastward
    if year == 1865:
        # No railway yet
        pass
    elif year == 1875:
        rail_lon = [53, 56, 58]
        rail_lat = [39, 38, 37.5]
        ax.plot(rail_lon, rail_lat, color='#2c3e50', linewidth=2,
                transform=ccrs.PlateCarree(), zorder=4)
    else:
        rail_lon = [53, 56, 58, 62, 64, 67]
        rail_lat = [39, 38, 37.5, 38, 39, 39.5]
        ax.plot(rail_lon, rail_lat, color='#2c3e50', linewidth=2,
                transform=ccrs.PlateCarree(), zorder=4)

    # Key cities
    cities = [
        (66.9, 39.6, 'Samarkand'),
        (64.4, 39.8, 'Bukhara'),
        (58, 42, 'Geok Tepe'),
    ]
    for lon, lat, name in cities:
        ax.plot(lon, lat, 'o', color='#2c3e50', markersize=4, zorder=5,
                transform=ccrs.PlateCarree())
        ax.text(lon, lat + 0.7, name, fontsize=6, ha='center',
                transform=ccrs.PlateCarree())

    # Russian controlled shading
    if year >= 1875:
        rus_lon = [50, 56, 64 if year == 1875 else 72, 72, 72, 50]
        rus_lat = [48, 48, 48, 45, 38 if year == 1875 else 36, 38 if year == 1875 else 36]
        ax.fill(rus_lon, rus_lat, color='#2980b9', alpha=0.08, transform=ccrs.PlateCarree())

    ax.set_title(f'Central Asian Steppe — {year}', fontsize=10, fontweight='bold')

# Legend
fig.text(0.5, 0.01, '━━ Railroad advance     ██ Nomadic territory (shrinking)     ██ Imperial control (expanding)',
         ha='center', fontsize=9, color='#2c3e50')

fig.suptitle('The Parallel Conquests — Same Technology, Same Decade, Opposite Sides of the Planet\nNeither empire aware of the other\'s campaign',
             fontsize=14, fontweight='bold', y=1.01)

plt.tight_layout()
plt.savefig('figures/output/fig-006-parallel-conquests.png', dpi=150, bbox_inches='tight')
plt.savefig('figures/output/fig-006-parallel-conquests.svg', bbox_inches='tight')
print("Generated: fig-006-parallel-conquests.png/.svg")
