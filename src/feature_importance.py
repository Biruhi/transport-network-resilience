import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ----------------------------------
# LOAD DATA
# ----------------------------------

df = pd.read_csv(
    "data/processed/ml_dataset.csv"
)

X = df[
    [
        "degree",
        "closeness",
        "pagerank"
    ]
]

y = df["critical"]

# ----------------------------------
# TRAIN TEST SPLIT
# ----------------------------------

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )
)

# ----------------------------------
# RANDOM FOREST
# ----------------------------------

model = RandomForestClassifier(
    n_estimators=300,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

model.fit(
    X_train,
    y_train
)

# ----------------------------------
# FEATURE IMPORTANCE
# ----------------------------------

importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance":
        model.feature_importances_

})

importance = (
    importance
    .sort_values(
        by="Importance",
        ascending=False
    )
)

print(importance)

# ----------------------------------
# PLOT
# ----------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.ylabel(
    "Importance"
)

plt.title(
    "Feature Importance for Critical Node Prediction"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "figures/feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()