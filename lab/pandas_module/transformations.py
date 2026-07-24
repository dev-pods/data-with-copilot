"""Módulo 2 — Manipulação de DataFrames com pandas.

Complete cada função com o apoio do GitHub Copilot. Prefira operações
vetorizadas e evite alterar o DataFrame original (use ``.copy()``).

Valide com:  ``python lab/check.py --module pandas``
"""
from __future__ import annotations

import pandas as pd


def load_wines(path: str) -> pd.DataFrame:
    """Leia o CSV em ``path`` e retorne um DataFrame do pandas."""
    # Prompt sugerido: "Leia o arquivo CSV em path com pandas e retorne o DataFrame."
    raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Converta a coluna ``rating`` para numérico e remova as linhas cujo
    ``rating`` seja nulo. Retorne o DataFrame limpo."""
    raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def top_varieties_by_avg_rating(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Retorne as ``n`` variedades com maior média de ``rating`` (colunas:
    variety, avg_rating), ordenadas da maior para a menor."""
    raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def add_rating_category(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``rating_category`` com as faixas: "Baixa" (< 85),
    "Média" (85 a 90) e "Alta" (> 90). Dica: use ``pd.cut``."""
    raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def enrich_with_country(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``country`` extraindo o último trecho após a vírgula de
    ``region`` (ex.: "Mendocino, California" -> "California")."""
    raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")
