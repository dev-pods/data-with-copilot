"""Módulo 3 — Análise Exploratória de Dados (EDA).

Complete cada função com o apoio do GitHub Copilot. Use ``/explain`` para
entender fórmulas (como o IQR) antes de confiar no código gerado.

Valide com:  ``python lab/check.py --module eda``
"""
from __future__ import annotations

import pandas as pd


def descriptive_stats(df: pd.DataFrame) -> pd.Series:
    """Retorne as estatísticas descritivas da coluna ``rating`` (count, mean,
    std, min, quartis, max). Dica: ``df['rating'].describe()``."""
    raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def detect_outliers_iqr(df: pd.DataFrame, column: str = "rating") -> pd.DataFrame:
    """Retorne as linhas consideradas outliers em ``column`` pelo método IQR
    (valores abaixo de Q1 - 1.5*IQR ou acima de Q3 + 1.5*IQR)."""
    # Prompt sugerido: "Implemente a detecção de outliers da coluna usando IQR (fator 1.5)."
    raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def missing_values_report(df: pd.DataFrame) -> pd.Series:
    """Retorne a contagem de valores ausentes por coluna. Dica: ``df.isna().sum()``."""
    raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def rating_stats_by_variety(df: pd.DataFrame) -> pd.DataFrame:
    """Agrupe por ``variety`` e retorne count, mean, min e max de ``rating``,
    ordenado pela média decrescente."""
    raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")
