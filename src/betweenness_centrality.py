import osmnx as ox
import networkx as nx
import pandas as pd

print("Loading network...")

G = ox.load_graphml(
    "data/raw/addis_ababa.graphml"
)

print("Calculating betweenness centrality...")

betweenness = nx.betweenness_centrality(
    G,
    k=100,
    seed=42
)

df = pd.DataFrame({
    "node": list(betweenness.keys()),
    "betweenness": list(betweenness.values())
})

df = df.sort_values(
    by="betweenness",
    ascending=False
)

df.to_csv(
    "data/processed/top_betweenness_nodes.csv",
    index=False
)

print(df.head(20))

print("Results saved.")