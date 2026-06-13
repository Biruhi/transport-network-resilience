import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier
)

# ==================================================
# LOAD DATA
# ==================================================

print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

df = pd.read_csv(
    "data/processed/ml_dataset.csv"
)

print("\nDataset Shape:")
print(df.shape)

print("\nCritical Node Distribution:")
print(df["critical"].value_counts())

# ==================================================
# FEATURES
# ==================================================

X = df[
    [
        "degree",
        "closeness",
        "pagerank"
    ]
]

y = df["critical"]

# ==================================================
# TRAIN TEST SPLIT
# ==================================================

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )
)

# ==================================================
# MODELS
# ==================================================

models = {

    "Logistic Regression":
        LogisticRegression(
            class_weight="balanced",
            max_iter=1000,
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=300,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        ),

    "Extra Trees":
        ExtraTreesClassifier(
            n_estimators=300,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        )
}

# ==================================================
# TRAIN & EVALUATE
# ==================================================

results = []

for name, model in models.items():

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    model.fit(
        X_train,
        y_train
    )

    pred = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        pred
    )

    precision = precision_score(
        y_test,
        pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        pred,
        zero_division=0
    )

    print(
        classification_report(
            y_test,
            pred,
            zero_division=0
        )
    )

    results.append({

        "Model": name,

        "Accuracy":
            round(accuracy, 4),

        "Precision":
            round(precision, 4),

        "Recall":
            round(recall, 4),

        "F1":
            round(f1, 4)
    })

results_df = pd.DataFrame(
    results
)

print("\n")
print("=" * 60)
print("FINAL COMPARISON")
print("=" * 60)

print(results_df)

results_df.to_csv(
    "data/processed/model_comparison.csv",
    index=False
)

print(
    "\nSaved: data/processed/model_comparison.csv"
)