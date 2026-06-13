import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import (
    classification_report,
    accuracy_score
)

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

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
)

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

print(
    "Accuracy:",
    accuracy_score(
        y_test,
        predictions
    )
)

print(
    classification_report(
        y_test,
        predictions
    )
)

importance = pd.DataFrame({
    "feature": X.columns,
    "importance":
        model.feature_importances_
})

print("\nFeature Importance")

print(
    importance.sort_values(
        by="importance",
        ascending=False
    )
)