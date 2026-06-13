import osmnx as ox

place = "Bole, Addis Ababa, Ethiopia"

G = ox.graph_from_place(
    place,
    network_type="drive"
)

ox.save_graphml(
    G,
    filepath="data/raw/addis_ababa.graphml"
)

print("Network saved successfully.")