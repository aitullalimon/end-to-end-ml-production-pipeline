from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import pandas as pd


@dataclass
class DatasetSpec:
    name: str
    path: Path
    target_col: str = "target"


def load_csv(spec: DatasetSpec) -> pd.DataFrame:
    if not spec.path.exists():
        raise FileNotFoundError(f"Dataset not found: {spec.path}")

    df = pd.read_csv(spec.path)

    if spec.target_col not in df.columns:
        raise ValueError(f"Target column '{spec.target_col}' not found in columns: {list(df.columns)[:20]}...")

    if df.empty:
        raise ValueError(f"Dataset is empty: {spec.path}")

    return df


def basic_data_report(df: pd.DataFrame, target_col: str = "target") -> dict:
    report = {
        "n_rows": int(df.shape[0]),
        "n_cols": int(df.shape[1]),
        "missing_cells": int(df.isna().sum().sum()),
        "missing_by_col_top10": df.isna().sum().sort_values(ascending=False).head(10).to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "target_value_counts_top10": df[target_col].value_counts(dropna=False).head(10).to_dict(),
    }
    return report
