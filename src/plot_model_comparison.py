import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    "data/processed/model_comparison.csv"
)

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1"
]

x = np.arange(len(df))

width = 0.2

plt.figure(figsize=(12, 6))

for i, metric in enumerate(metrics):

    plt.bar(
        x + i * width,
        df[metric],
        width,
        label=metric
    )

plt.xticks(
    x + width * 1.5,
    df["Model"]
)

plt.ylabel("Score")

plt.title(
    "Machine Learning Model Performance Comparison"
)

plt.legend()

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "figures/model_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()