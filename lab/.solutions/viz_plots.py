"""Modulo 4 - Visualizacao de Dados (GABARITO / referencia)."""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["rating"].dropna(), bins=20, kde=True, ax=ax)
    ax.set_title("Distribuição das notas (rating)")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Frequência")
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    plt.close(fig)
    return fig


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    top = df["variety"].value_counts().head(10).sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(top.index, top.values, color="#7b1e3b")
    ax.set_title("Top 10 variedades por quantidade de vinhos")
    ax.set_xlabel("Quantidade")
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    plt.close(fig)
    return fig


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    top = df["variety"].value_counts().head(5).index
    subset = df[df["variety"].isin(top)]
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.boxplot(data=subset, x="variety", y="rating", ax=ax)
    ax.set_title("Distribuição de rating por variedade (top 5)")
    ax.set_xlabel("Variedade")
    ax.set_ylabel("Rating")
    plt.xticks(rotation=20, ha="right")
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    plt.close(fig)
    return fig
