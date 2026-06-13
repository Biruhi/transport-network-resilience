import osmnx as ox

G = ox.load_graphml(
    "data/raw/addis_ababa.graphml"
)

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())