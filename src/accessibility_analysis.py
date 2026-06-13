import osmnx as ox
import networkx as nx
import pandas as pd
import random

print("=" * 60)
print("ACCESSIBILITY ANALYSIS")
print("=" * 60)

# ----------------------------------
# LOAD NETWORK
# ----------------------------------

G = ox.load_graphml(
    "data/raw/addis_ababa.graphml"
)

G = nx.Graph(G)

print(
    f"Nodes: {G.number_of_nodes():,}"
)

print(
    f"Edges: {G.number_of_edges():,}"
)

# ----------------------------------
# SAMPLE NODES
# ----------------------------------

random.seed(42)

sample_nodes = random.sample(
    list(G.nodes()),
    100
)

# ----------------------------------
# BASELINE ACCESSIBILITY
# ----------------------------------

baseline_lengths = []

for source in sample_nodes:

    lengths = nx.single_source_shortest_path_length(
        G,
        source,
        cutoff=20
    )

    baseline_lengths.extend(
        lengths.values()
    )

baseline_accessibility = (
    sum(baseline_lengths)
    / len(baseline_lengths)
)

print(
    f"\nBaseline Accessibility: "
    f"{baseline_accessibility:.2f}"
)

# ----------------------------------
# LOAD CRITICAL NODES
# ----------------------------------

df = pd.read_csv(
    "data/processed/top_betweenness_nodes.csv"
)

graph_node_type = type(
    next(iter(G.nodes()))
)

critical_nodes = [
    graph_node_type(x)
    for x in df.head(200)["node"]
]

# ----------------------------------
# ATTACK NETWORK
# ----------------------------------

G_attack = G.copy()

removed = 0

for node in critical_nodes:

    if node in G_attack:

        G_attack.remove_node(node)

        removed += 1

print(
    f"\nRemoved {removed} critical nodes"
)

# ----------------------------------
# ACCESSIBILITY AFTER ATTACK
# ----------------------------------

attack_lengths = []

valid_sources = [
    n
    for n in sample_nodes
    if n in G_attack
]

for source in valid_sources:

    lengths = nx.single_source_shortest_path_length(
        G_attack,
        source,
        cutoff=20
    )

    attack_lengths.extend(
        lengths.values()
    )

attack_accessibility = (
    sum(attack_lengths)
    / len(attack_lengths)
)

print(
    f"Post-Attack Accessibility: "
    f"{attack_accessibility:.2f}"
)

# ----------------------------------
# CHANGE
# ----------------------------------

change = (
    (attack_accessibility
     - baseline_accessibility)
    / baseline_accessibility
) * 100

print(
    f"\nAccessibility Change: "
    f"{change:.2f}%"
)