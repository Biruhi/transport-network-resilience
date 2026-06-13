import osmnx as ox
import pandas as pd
import matplotlib.pyplot as plt

# Load graph
G = ox.load_graphml(
    "data/raw/addis_ababa.graphml"
)

# Load betweenness results
df = pd.read_csv(
    "data/processed/top_betweenness_nodes.csv"
)

# Select top 50 nodes
top_nodes = df.head(50)["node"].astype(str)

# Get node coordinates
nodes, edges = ox.graph_to_gdfs(
    G,
    nodes=True,
    edges=True
)

critical_nodes = nodes.loc[
    nodes.index.astype(str).isin(top_nodes)
]

# Plot
fig, ax = plt.subplots(figsize=(12, 12))

edges.plot(
    ax=ax,
    linewidth=0.5
)

critical_nodes.plot(
    ax=ax,
    markersize=20
)

plt.title(
    "Top 50 Critical Intersections in Addis Ababa"
)

plt.savefig(
    "figures/top50_critical_nodes.png",
    dpi=300,
    bbox_inches="tight"
)

print("Map saved.")