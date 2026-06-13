import osmnx as ox
import networkx as nx
import pandas as pd
import random

print("=" * 60)
print("RANDOM VS TARGETED ATTACK ANALYSIS")
print("=" * 60)

# --------------------------------------------------
# LOAD NETWORK
# --------------------------------------------------

G = ox.load_graphml(
    "data/raw/addis_ababa.graphml"
)

G = nx.Graph(G)

largest_before = max(
    nx.connected_components(G),
    key=len
)

size_before = len(largest_before)

print(f"Original Largest Component: {size_before}")

# --------------------------------------------------
# LOAD BETWEenness RESULTS
# --------------------------------------------------

df = pd.read_csv(
    "data/processed/top_betweenness_nodes.csv"
)

attack_sizes = [
    50,
    100,
    200,
    500,
    1000
]

results = []

graph_node_type = type(next(iter(G.nodes)))

# --------------------------------------------------
# TARGETED ATTACK
# --------------------------------------------------

for n_remove in attack_sizes:

    G_attack = G.copy()

    critical_nodes = [
        graph_node_type(x)
        for x in df.head(n_remove)["node"]
    ]

    for node in critical_nodes:

        if node in G_attack:
            G_attack.remove_node(node)

    largest_after = max(
        nx.connected_components(G_attack),
        key=len
    )

    loss = (
        1 -
        len(largest_after) / size_before
    ) * 100

    results.append(
        {
            "attack_type": "Targeted",
            "nodes_removed": n_remove,
            "connectivity_loss": loss
        }
    )

# --------------------------------------------------
# RANDOM ATTACK
# --------------------------------------------------

random.seed(42)

all_nodes = list(G.nodes())

for n_remove in attack_sizes:

    G_attack = G.copy()

    random_nodes = random.sample(
        all_nodes,
        n_remove
    )

    G_attack.remove_nodes_from(
        random_nodes
    )

    largest_after = max(
        nx.connected_components(G_attack),
        key=len
    )

    loss = (
        1 -
        len(largest_after) / size_before
    ) * 100

    results.append(
        {
            "attack_type": "Random",
            "nodes_removed": n_remove,
            "connectivity_loss": loss
        }
    )

# --------------------------------------------------
# SAVE RESULTS
# --------------------------------------------------

results_df = pd.DataFrame(results)

print(results_df)

results_df.to_csv(
    "data/processed/random_vs_targeted.csv",
    index=False
)

print("\nSaved:")
print(
    "data/processed/random_vs_targeted.csv"
)