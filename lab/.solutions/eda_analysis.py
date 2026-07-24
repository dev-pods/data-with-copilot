"""Modulo 3 - Analise Exploratoria de Dados (GABARITO / referencia)."""
from __future__ import annotations

import pandas as pd


def descriptive_stats(df: pd.DataFrame) -> pd.Series:
    return df["rating"].describe()


def detect_outliers_iqr(df: pd.DataFrame, column: str = "rating") -> pd.DataFrame:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return df[(df[column] < lower) | (df[column] > upper)]


def missing_values_report(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum()


def rating_stats_by_variety(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("variety")["rating"]
        .agg(["count", "mean", "min", "max"])
        .sort_values("mean", ascending=False)
    )
