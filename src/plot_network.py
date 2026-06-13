import osmnx as ox
import matplotlib.pyplot as plt

G = ox.load_graphml(
    "data/raw/addis_ababa.graphml"
)

fig, ax = ox.plot_graph(
    G,
    node_size=0,
    edge_linewidth=0.6,
    bgcolor="white",
    show=False,
    close=False
)

plt.savefig(
    "figures/bole_network.png",
    dpi=300,
    bbox_inches="tight"
)