import geopandas as gpd
import matplotlib.pyplot as plt
import h3
import contextily as cx
import matplotlib.colors as mcolors

def plot_df(df, column=None, ax=None,legend=None):
    "Plot based on the `geometry` column of a GeoPandas dataframe"
    df = df.copy()
    df = df.to_crs(epsg=4326)  # WGS 84

    # Define color map with 5 colors
    cmap = mcolors.ListedColormap(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

    if ax is None:
        _, ax = plt.subplots(figsize=(8, 8))

    df.plot(
        ax=ax,
        # cmap=cmap,
        alpha=0.5, 
        edgecolor='black',
        column=column, 
        # categorical=True,
        # legend=legend,
        legend_kwds={
        'loc': 'lower right',
        'bbox_to_anchor': (1, 0),  # Controls position (x, y)
        'frameon': True,  # Optional: add a frame around the legend
        'orientation': 'vertical',
        'colorbar': False
        },
        cmap = "RdYlGn_r",
        categorical = True,
        scheme  =  "FisherJenks"
    )
    cx.add_basemap(ax, crs=df.crs, source=cx.providers.CartoDB.Positron)


def plot_shape(shape, ax=None):
    df = gpd.GeoDataFrame({'geometry': [shape]}, crs='EPSG:4326')
    plot_df(df, ax=ax)


def plot_cells(cells, ax=None):
    shape = h3.cells_to_h3shape(cells)
    plot_shape(shape, ax=ax)


def plot_shape_and_cells(shape, res=9):
    fig, axs = plt.subplots(1,2, figsize=(10,5), sharex=True, sharey=True)
    plot_shape(shape, ax=axs[0])
    plot_cells(h3.h3shape_to_cells(shape, res), ax=axs[1])
    fig.tight_layout()