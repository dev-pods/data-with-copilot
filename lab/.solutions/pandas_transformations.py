"""Modulo 2 - Manipulacao de DataFrames (GABARITO / referencia do instrutor)."""
from __future__ import annotations

import pandas as pd


def load_wines(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    return df.dropna(subset=["rating"]).reset_index(drop=True)


def top_varieties_by_avg_rating(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    return (
        df.groupby("variety")["rating"]
        .mean()
        .sort_values(ascending=False)
        .head(n)
        .reset_index(name="avg_rating")
    )


def add_rating_category(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["rating_category"] = pd.cut(
        df["rating"],
        bins=[-float("inf"), 85, 90, float("inf")],
        labels=["Baixa", "Média", "Alta"],
    )
    return df


def enrich_with_country(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["country"] = df["region"].astype(str).str.split(",").str[-1].str.strip()
    return df
