import osmnx as ox
import networkx as nx
import pandas as pd

print("=" * 60)
print("TRANSPORTATION NETWORK RESILIENCE ANALYSIS")
print("=" * 60)

# --------------------------------------------------
# LOAD NETWORK
# --------------------------------------------------

G = ox.load_graphml(
    "data/raw/addis_ababa.graphml"
)

print(f"\nOriginal Nodes: {G.number_of_nodes():,}")
print(f"Original Edges: {G.number_of_edges():,}")

# Convert to undirected network
G = nx.Graph(G)

largest_before = max(
    nx.connected_components(G),
    key=len
)

size_before = len(largest_before)

print(
    f"Largest Component Before Attack: {size_before:,}"
)

# --------------------------------------------------
# LOAD BETWENNESS RESULTS
# --------------------------------------------------

df = pd.read_csv(
    "data/processed/top_betweenness_nodes.csv"
)

print("\nTop Betweenness Nodes:")
print(df.head())

# --------------------------------------------------
# DETECT NODE TYPE
# --------------------------------------------------

sample_graph_node = next(iter(G.nodes))

graph_node_type = type(sample_graph_node)

print("\nGraph Node Example:")
print(sample_graph_node)

print("\nGraph Node Type:")
print(graph_node_type)

# --------------------------------------------------
# ATTACK LEVELS
# --------------------------------------------------

attack_sizes = [
    50,
    100,
    200,
    500,
    1000
]

results = []

# --------------------------------------------------
# RESILIENCE ANALYSIS
# --------------------------------------------------

for n_remove in attack_sizes:

    print("\n" + "=" * 50)
    print(f"ATTACK SIZE = {n_remove}")
    print("=" * 50)

    G_attack = G.copy()

    critical_nodes = [
        graph_node_type(node)
        for node in df.head(n_remove)["node"]
    ]

    removed = 0

    for node in critical_nodes:

        if node in G_attack:

            G_attack.remove_node(node)

            removed += 1

    print(f"Nodes Actually Removed: {removed}")

    print(
        f"Nodes Remaining: {G_attack.number_of_nodes():,}"
    )

    largest_after = max(
        nx.connected_components(G_attack),
        key=len
    )

    size_after = len(largest_after)

    connectivity_loss = (
        1
        - size_after / size_before
    )

    print(
        f"Largest Component After: {size_after:,}"
    )

    print(
        f"Connectivity Loss: {connectivity_loss:.2%}"
    )

    results.append(
        {
            "nodes_removed": n_remove,
            "actually_removed": removed,
            "largest_component": size_after,
            "connectivity_loss_percent":
                round(connectivity_loss * 100, 4)
        }
    )

# --------------------------------------------------
# SAVE RESULTS
# --------------------------------------------------

results_df = pd.DataFrame(results)

print("\n")
print("=" * 60)
print("FINAL RESULTS")
print("=" * 60)

print(results_df)

results_df.to_csv(
    "data/processed/resilience_results.csv",
    index=False
)

print(
    "\nSaved: data/processed/resilience_results.csv"
)