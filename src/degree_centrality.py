import osmnx as ox
import networkx as nx
import pandas as pd

G = ox.load_graphml(
    "data/raw/addis_ababa.graphml"
)

degree = nx.degree_centrality(G)

df = pd.DataFrame({
    "node": list(degree.keys()),
    "degree": list(degree.values())
})

df = df.sort_values(
    by="degree",
    ascending=False
)

print(df.head(20))

df.to_csv(
    "data/processed/top_degree_nodes.csv",
    index=False
)

print("Results saved.")