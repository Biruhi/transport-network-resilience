import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/resilience_results.csv"
)

plt.figure(figsize=(10, 6))

plt.plot(
    df["nodes_removed"],
    df["connectivity_loss_percent"],
    marker="o",
    linewidth=2
)

for x, y in zip(
    df["nodes_removed"],
    df["connectivity_loss_percent"]
):
    plt.annotate(
        f"{y:.2f}",
        (x, y)
    )

plt.xlabel(
    "Critical Nodes Removed"
)

plt.ylabel(
    "Connectivity Loss (%)"
)

plt.title(
    "Transportation Network Resilience Under Targeted Attack"
)

plt.grid(True)

plt.savefig(
    "figures/resilience_curve.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()