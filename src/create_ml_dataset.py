import osmnx as ox
import networkx as nx
import pandas as pd

print("Loading network...")

G = ox.load_graphml(
    "data/raw/addis_ababa.graphml"
)

G = nx.Graph(G)

print("Calculating degree...")
degree = nx.degree_centrality(G)

print("Calculating closeness...")
closeness = nx.closeness_centrality(G)

print("Calculating pagerank...")
pagerank = nx.pagerank(G)

print("Loading betweenness...")
bet_df = pd.read_csv(
    "data/processed/top_betweenness_nodes.csv"
)

betweenness = dict(
    zip(
        bet_df["node"].astype(str),
        bet_df["betweenness"]
    )
)

rows = []

top_critical = set(
    bet_df.head(500)["node"]
    .astype(str)
)

for node in G.nodes():

    node_str = str(node)

    rows.append({
        "node": node_str,
        "degree": degree[node],
        "closeness": closeness[node],
        "pagerank": pagerank[node],
        "betweenness":
            betweenness.get(node_str, 0),
        "critical":
            1 if node_str in top_critical else 0
    })

dataset = pd.DataFrame(rows)

dataset.to_csv(
    "data/processed/ml_dataset.csv",
    index=False
)

print(dataset.head())
print(dataset["critical"].value_counts())

print("\nSaved:")
print(
    "data/processed/ml_dataset.csv"
)