"""
Figure 017: The Steppe Pressure Engine — where nomadic power projects cheapest.

An ILLUSTRATIVE power-projection field, not measured reach. A nomadic core on the
Pontic–Caspian steppe projects power cheaply along the grass and expensively across
forest, desert, and mountain — and cannot cross open water. The filled bands are
iso-levels of a LEAST-COST spread, so the corridor shape emerges from the ground.

v3 — real data:
  * Ground cost from RESOLVE/WWF terrestrial ecoregions (BIOME_NUM): temperate
    grassland (steppe) is cheap; desert, forest, taiga are costly. Real biome
    geography, not a latitude band.
  * Mountain cost from ETOPO 2022 elevation (60"), read windowed over the frame.
  * Open water (Natural Earth land mask) is impassable.

Pipeline: ecoregions + DEM -> per-cell cost -> least-cost distance from the core
(skimage.graph.MCP_Geometric) -> power = exp(-cost/scale) -> isobands.from_raster()
-> filled contour polygons -> clipped to land -> cartopy parchment base.

Derived inputs are cached to fig_017_inputs.npz (committed, ~small) so the figure
rebuilds offline. Raw downloads live in ./data/ (gitignored). Requires the `geofig`
conda env. Honesty: still ILLUSTRATIVE — the cost weights are a documented model,
the decay is a chosen scale; the figure demonstrates the mechanism, not magnitudes.
"""
from __future__ import annotations

import os
import numpy as np
import xarray as xr

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

import geopandas as gpd
import shapely
from shapely.ops import unary_union
from skimage.graph import MCP_Geometric

import isobands

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
INPUTS_NPZ = os.path.join(HERE, "fig_017_inputs.npz")

# ---- house style ----
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 9
LAND, OCEAN, COAST, RIVER, INK, POWER = (
    "#f5f0e1", "#dbeaf2", "#7f8c8d", "#a9cce3", "#2c3e50", "#c0392b")

# ---- map frame ----
LON0, LON1, LAT0, LAT1 = 12.0, 96.0, 33.0, 60.0
NX, NY = 720, 360

# ---- data sources ----
DEM_URL = ("/vsicurl/https://www.ngdc.noaa.gov/mgg/global/relief/ETOPO2022/"
           "data/60s/60s_surface_elev_gtif/ETOPO_2022_v1_60s_N90W180_surface.tif")
ECO_ZIP = os.path.join(DATA, "Ecoregions2017.zip")
ECO_URL = "https://storage.googleapis.com/teow2016/Ecoregions2017.zip"

# ---- the cost model ----
CORE_LON, CORE_LAT = 47.0, 48.0
# WWF/RESOLVE biome number -> baseline ground cost (steppe is the cheap grass)
BIOME_COST = {
    8: 1.0,    # Temperate Grasslands, Savannas & Shrublands  (the steppe)
    10: 2.5,   # Montane Grasslands & Shrublands (elevation adds the rest)
    9: 2.0,    # Flooded Grasslands & Savannas
    13: 4.5,   # Deserts & Xeric Shrublands
    12: 3.5,   # Mediterranean Forests, Woodlands & Scrub
    4: 6.0,    # Temperate Broadleaf & Mixed Forests
    5: 6.5,    # Temperate Conifer Forests
    3: 6.5,    # Tropical & Subtropical Coniferous Forests
    6: 8.0,    # Boreal Forests/Taiga
    11: 7.0,   # Tundra
}
BIOME_COST_DEFAULT = 5.0
ELEV_ADD = 70.0                 # extra cost across high terrain
ELEV_LO, ELEV_HI = 1200.0, 3500.0   # smoothstep bounds (m): plains free, ranges walled
WATER_COST = np.inf

SCALE_KM = 950.0
LEVELS = [0.09, 0.18, 0.32, 0.50, 0.73]


def smoothstep(x, a, b):
    t = np.clip((x - a) / (b - a), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def build_inputs(x, y):
    """Return (elevation[NY,NX], biome[NY,NX]) on the model grid, from cache or source."""
    if os.path.exists(INPUTS_NPZ):
        d = np.load(INPUTS_NPZ)
        return d["elevation"], d["biome"]

    import rioxarray  # noqa: F401
    from rasterio.features import rasterize
    from affine import Affine

    os.makedirs(DATA, exist_ok=True)
    os.environ.setdefault("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")
    os.environ.setdefault("CPL_VSIL_CURL_ALLOWED_EXTENSIONS", ".tif")

    # elevation: windowed read of the global DEM, linearly resampled to the grid
    import rioxarray
    dem = rioxarray.open_rasterio(DEM_URL, masked=True).squeeze()
    dem = dem.rio.clip_box(minx=LON0, miny=LAT0, maxx=LON1, maxy=LAT1)
    elevation = dem.interp(x=x, y=y).values.astype("float32")
    elevation = np.nan_to_num(elevation, nan=0.0)

    # biomes: rasterize BIOME_NUM onto the grid (row 0 == y[0] == south)
    if not os.path.exists(ECO_ZIP):
        import urllib.request
        urllib.request.urlretrieve(ECO_URL, ECO_ZIP)
    shp = "/vsizip/" + os.path.abspath(ECO_ZIP) + "/Ecoregions2017.shp"
    eco = gpd.read_file(shp, bbox=(LON0, LAT0, LON1, LAT1))
    dlon = (x[-1] - x[0]) / (NX - 1)
    dlat = (y[-1] - y[0]) / (NY - 1)
    transform = Affine(dlon, 0, x[0] - dlon / 2, 0, dlat, y[0] - dlat / 2)
    biome = rasterize(
        ((geom, int(b)) for geom, b in zip(eco.geometry, eco["BIOME_NUM"])),
        out_shape=(NY, NX), transform=transform, fill=0, dtype="int16",
    )
    np.savez_compressed(INPUTS_NPZ, elevation=elevation, biome=biome)
    return elevation, biome


def build_cost(elevation, biome, onland):
    cost = np.full(biome.shape, BIOME_COST_DEFAULT, dtype=float)
    for b, c in BIOME_COST.items():
        cost[biome == b] = c
    cost += ELEV_ADD * smoothstep(elevation, ELEV_LO, ELEV_HI)
    cost[~onland] = WATER_COST
    return cost


def least_cost_distance(cost, x, y):
    dy_km = (y[1] - y[0]) * 111.0
    dx_km = (x[1] - x[0]) * 111.0 * np.cos(np.deg2rad(CORE_LAT))
    mcp = MCP_Geometric(cost, sampling=(dy_km, dx_km))
    iy = int(np.argmin(np.abs(y - CORE_LAT)))
    ix = int(np.argmin(np.abs(x - CORE_LON)))
    cum, _ = mcp.find_costs([[iy, ix]])
    return cum


def load_land():
    shp = shpreader.natural_earth(resolution="50m", category="physical", name="land")
    return unary_union(list(shpreader.Reader(shp).geometries()))


def main():
    outdir = os.path.normpath(os.path.join(HERE, "..", "output"))
    os.makedirs(outdir, exist_ok=True)

    x = np.linspace(LON0, LON1, NX)
    y = np.linspace(LAT0, LAT1, NY)
    LONg, LATg = np.meshgrid(x, y)

    land = load_land()
    onland = shapely.contains_xy(land, LONg, LATg)

    elevation, biome = build_inputs(x, y)
    cost = build_cost(elevation, biome, onland)
    cum = least_cost_distance(cost, x, y)
    power = np.where(np.isfinite(cum), np.exp(-cum / SCALE_KM), 0.0)
    # light smoothing so contours read as organic isolines, not rasterized biome edges
    from scipy.ndimage import gaussian_filter
    power = gaussian_filter(power, sigma=1.4)

    da = xr.DataArray(power, coords={"y": y, "x": x}, dims=("y", "x"))
    bands = isobands.from_raster(da, levels=LEVELS, crs="EPSG:4326")
    bands = bands.sort_values("min_value").reset_index(drop=True)
    bands = gpd.clip(bands, land)
    bands = bands[~bands.geometry.is_empty & bands.geometry.notna()]

    # ---- render ----
    fig = plt.figure(figsize=(13, 6.2), dpi=150)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([LON0, LON1, LAT0, LAT1], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.OCEAN, facecolor=OCEAN)
    ax.add_feature(cfeature.LAND, facecolor=LAND)
    ax.add_feature(cfeature.RIVERS, edgecolor=RIVER, linewidth=0.3)
    ax.add_feature(cfeature.LAKES, facecolor=OCEAN, edgecolor="none")
    ax.add_feature(cfeature.COASTLINE, linewidth=0.4, edgecolor=COAST)

    n = len(bands)
    for i, (_, row) in enumerate(bands.iterrows()):
        frac = (i + 1) / n
        ax.add_geometries(
            [row.geometry], crs=ccrs.PlateCarree(),
            facecolor=to_rgba(POWER, 0.10 + 0.20 * frac),
            edgecolor=to_rgba(POWER, 0.30), linewidth=0.25, zorder=3,
        )

    ax.plot(CORE_LON, CORE_LAT, marker="*", markersize=16, color="#7b241c",
            transform=ccrs.PlateCarree(), zorder=6)
    ax.text(CORE_LON + 1.2, CORE_LAT + 0.9, "Pontic–Caspian core", color="#7b241c",
            fontsize=9, fontweight="bold", transform=ccrs.PlateCarree(), zorder=6)

    anchors = [
        (19.5, 47.0, "Great Hungarian Plain"),
        (24.0, 49.8, "Carpathians"),
        (44.0, 42.6, "Caucasus"),
        (68.0, 49.5, "Kazakh steppe"),
        (73.5, 39.8, "Tien Shan"),
        (88.0, 51.6, "Altai"),
    ]
    for lon, lat, label in anchors:
        ax.text(lon, lat, label, fontsize=7.5, style="italic", color=INK,
                ha="center", transform=ccrs.PlateCarree(), zorder=6)

    ax.set_title(
        "The Steppe Pressure Engine — where nomadic power projects cheapest",
        fontsize=13, fontweight="bold", pad=10,
    )
    fig.text(0.5, 0.03,
             "Illustrative least-cost model over real biomes (WWF ecoregions) and terrain (ETOPO): "
             "power spreads cheaply over grass, is dammed by mountains, and cannot cross open water.",
             ha="center", fontsize=8, color=INK)

    base = os.path.join(outdir, "fig-017-steppe-pressure-engine")
    fig.savefig(base + ".png", bbox_inches="tight", facecolor="white")
    fig.savefig(base + ".svg", bbox_inches="tight", facecolor="white")
    print("bands drawn:", n, "| reachable land cells:",
          int(np.isfinite(cum).sum()), "of", int(onland.sum()))
    print("wrote", base + ".png / .svg")


if __name__ == "__main__":
    main()
