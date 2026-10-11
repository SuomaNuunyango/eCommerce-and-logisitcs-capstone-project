"""Shared utilities for training return-prediction models."""
from pathlib import Path
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    f1_score, precision_score, recall_score, roc_auc_score,
)

TARGET = "return"
RANDOM_STATE = 42
TEST_SIZE = 0.20

# These are the intended engineered input columns from the feature-engineering notebook.
# Names are normalized to lowercase so Delivery_method/Delivery_status also work.
EXPECTED_FEATURES = [
    "customer_age_years",
    "delivery_method",
    "delivery_status",
    "insurance_status",
    "order_item_id",
    "item_id",
    "item_size",
    "item_color",
    "brand_id",
    "item_price",
    "user_state",
]

# Do not silently include IDs, dates, raw source fields, or other columns.
# The model only uses the explicitly approved feature list above.
NUMERIC_FEATURES = [
    "customer_age_years", "order_item_id", "item_id", "brand_id", "item_price"
]
CATEGORICAL_FEATURES = [
    "delivery_method", "delivery_status", "insurance_status",
    "item_size", "item_color", "user_state"
]


def make_one_hot_encoder():
    """Support scikit-learn versions before and after sparse_output was introduced."""
    try:
        return OneHotEncoder(handle_unknown="ignore", sparse_output=True)
    except TypeError:
        return OneHotEncoder(handle_unknown="ignore", sparse=True)


def load_model_data(path):
    """Load engineered CSV, normalize column names, validate target/features."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Could not find dataset: {path.resolve()}\n"
            "Export the engineered dataset to this path before training."
        )

    df = pd.read_csv(path)
    # The feature notebook uses inconsistent capitalization for some derived fields.
    df.columns = [str(c).strip().lower() for c in df.columns]

    missing = [c for c in [TARGET, *EXPECTED_FEATURES] if c not in df.columns]
    if missing:
        raise ValueError(
            f"Missing required columns in {path}: {missing}\n"
            f"Available columns: {df.columns.tolist()}"
        )

    # Only rows without a known target cannot be used for supervised training.
    # Do not drop rows because feature values are missing; imputers handle those.
    df[TARGET] = pd.to_numeric(df[TARGET], errors="coerce")
    missing_target = int(df[TARGET].isna().sum())
    if missing_target:
        print(
            f"Excluding {missing_target} row(s) with missing/invalid '{TARGET}' "
            "because supervised training requires a known target."
        )
        df = df.loc[df[TARGET].notna()].copy()

    observed = set(df[TARGET].unique())
    if not observed.issubset({0, 1}) or len(observed) < 2:
        raise ValueError(
            f"'{TARGET}' must contain both binary classes 0 and 1; found {sorted(observed)}."
        )

    # Coerce numeric columns. Invalid values become NaN and are imputed inside the pipeline.
    for col in NUMERIC_FEATURES:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert categorical columns to consistent strings while preserving missing values.
    for col in CATEGORICAL_FEATURES:
        df[col] = df[col].astype("string").str.strip()
        df[col] = df[col].replace({"": pd.NA, "nan": pd.NA, "None": pd.NA, "<NA>": pd.NA})

    X = df[EXPECTED_FEATURES].copy()
    y = df[TARGET].astype(int)

    if y.value_counts().min() < 2:
        raise ValueError(
            "Each target class needs at least two rows for a stratified train/test split."
        )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )
    return X_train, X_test, y_train, y_test


def make_preprocessor(scale_numeric=False):
    numeric_steps = [("imputer", SimpleImputer(strategy="median"))]
    if scale_numeric:
        numeric_steps.append(("scaler", StandardScaler()))

    numeric_pipeline = Pipeline(numeric_steps)
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", make_one_hot_encoder()),
    ])

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, NUMERIC_FEATURES),
            ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
        ],
        remainder="drop",
    )


def report_results(name, model, X_test, y_test):
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    print(f"\n{name} — held-out test results")
    print(f"Accuracy:  {accuracy_score(y_test, predictions):.4f}")
    print(f"Precision: {precision_score(y_test, predictions, zero_division=0):.4f}")
    print(f"Recall:    {recall_score(y_test, predictions, zero_division=0):.4f}")
    print(f"F1:        {f1_score(y_test, predictions, zero_division=0):.4f}")
    try:
        print(f"ROC-AUC:   {roc_auc_score(y_test, probabilities):.4f}")
    except ValueError as exc:
        print(f"ROC-AUC unavailable: {exc}")

    print("\nConfusion matrix (rows=true, columns=predicted; order 0, 1):")
    print(confusion_matrix(y_test, predictions, labels=[0, 1]))
    print("\nClassification report:")
    print(classification_report(
        y_test, predictions, labels=[0, 1],
        target_names=["not returned (0)", "returned (1)"],
        zero_division=0,
    ))
