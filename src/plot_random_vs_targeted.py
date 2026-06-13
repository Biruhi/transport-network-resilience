import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/random_vs_targeted.csv"
)

targeted = df[
    df["attack_type"] == "Targeted"
]

random_attack = df[
    df["attack_type"] == "Random"
]

plt.figure(figsize=(10, 6))

plt.plot(
    targeted["nodes_removed"],
    targeted["connectivity_loss"],
    marker="o",
    linewidth=2,
    label="Targeted Attack"
)

plt.plot(
    random_attack["nodes_removed"],
    random_attack["connectivity_loss"],
    marker="s",
    linewidth=2,
    label="Random Attack"
)

plt.xlabel(
    "Nodes Removed"
)

plt.ylabel(
    "Connectivity Loss (%)"
)

plt.title(
    "Random vs Targeted Attack Resilience"
)

plt.legend()

plt.grid(True)

plt.savefig(
    "figures/random_vs_targeted.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()