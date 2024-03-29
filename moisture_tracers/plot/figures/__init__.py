import numpy as np
import cartopy.crs as ccrs
import matplotlib.dates as mdates
import cmcrameri

from twinotter.external import eurec4a


date_format = mdates.DateFormatter("%HZ")

linestyles = dict(
    km1p1="-", km2p2="--", km4p4="-.", D100m_150m="-", D100m_300m="--", D100m_500m="-."
)
alphas = dict(
    km1p1=1.0, km2p2=1.0, km4p4=1.0, D100m_150m=0.5, D100m_300m=0.5, D100m_500m=0.5
)
labels = dict(
    D100m_150m="150 m",
    D100m_300m="300 m",
    D100m_500m="500 m",
    km1p1="1.1 km",
    km2p2="2.2 km",
    km4p4="4.4 km",
)
labels["150m"] = "150 m"
labels["300m"] = "300 m"
labels["500m"] = "500 m"
labels["1p1km"] = "1.1 km"
labels["2p2km"] = "2.2 km"
labels["4p4km"] = "4.4 km"

projection = ccrs.PlateCarree()

lw_flux_plot_kwargs = dict(vmin=260, vmax=300, cmap="cmc.grayC")
satellite_plot_kwargs = dict(vmin=280, vmax=300, cmap="cmc.nuuk_r")

z_levs = 40 * np.array([
    0.000000e+00, 1.250000e-04, 5.416666e-04, 1.125000e-03, 1.875000e-03, 2.791667e-03,
    3.875000e-03, 5.125000e-03, 6.541667e-03, 8.125000e-03, 9.875000e-03, 1.179167e-02,
    1.387500e-02, 1.612500e-02, 1.854167e-02, 2.112500e-02, 2.387500e-02, 2.679167e-02,
    2.987500e-02, 3.312500e-02, 3.654167e-02, 4.012500e-02, 4.387500e-02, 4.779167e-02,
    5.187500e-02, 5.612501e-02, 6.054167e-02, 6.512500e-02, 6.987500e-02, 7.479167e-02,
    7.987500e-02, 8.512500e-02, 9.054167e-02, 9.612500e-02, 1.018750e-01, 1.077917e-01,
    1.138750e-01, 1.201250e-01, 1.265417e-01, 1.331250e-01, 1.398750e-01, 1.467917e-01,
    1.538752e-01, 1.611287e-01, 1.685623e-01, 1.761954e-01, 1.840590e-01, 1.921980e-01,
    2.006732e-01, 2.095645e-01, 2.189729e-01, 2.290236e-01, 2.398690e-01, 2.516917e-01,
    2.647077e-01, 2.791699e-01, 2.953717e-01, 3.136506e-01, 3.343919e-01, 3.580330e-01,
    3.850676e-01, 4.160496e-01, 4.515977e-01, 4.924007e-01, 5.392213e-01, 5.929016e-01,
    6.543679e-01, 7.246365e-01, 8.048183e-01, 8.961251e-01, 1.000000e+00
])


def add_halo_circle(ax):
    eurec4a.add_halo_circle(ax, alpha=1, lw=3, color="w")
    eurec4a.add_halo_circle(ax, alpha=1, lw=2)
