"""Módulo 1 — Geração de Queries SQL.

Complete cada função para que ela **retorne uma string SQL** (dialeto SQLite).
As tabelas disponíveis são:

- ``wines``   → colunas: name, region, variety, rating, notes
- ``regions`` → colunas: id, region_name, country, climate, avg_temperature, soil_type

Dica: use o GitHub Copilot Chat (inline, Cmd/Ctrl+I) ou escreva um comentário
descrevendo a query e deixe o Copilot sugerir o SQL. Sempre revise o resultado.

Valide com:  ``python lab/check.py --module sql``
"""
from __future__ import annotations


def avg_rating_by_variety() -> str:
    """Média de ``rating`` por ``variety``, com a contagem de vinhos, ordenada da
    maior média para a menor. Retorne colunas como: variety, avg_rating, total."""
    # Prompt sugerido ao Copilot:
    # "Gere uma query SQLite que calcule a média de rating por variety na tabela
    #  wines, incluindo a contagem de vinhos, ordenada da maior média para a menor."
    raise NotImplementedError("Implemente a query com o apoio do GitHub Copilot.")


def top10_highest_rated() -> str:
    """Os 10 vinhos com maior ``rating``. Retorne as colunas: name, variety, rating."""
    raise NotImplementedError("Implemente a query com o apoio do GitHub Copilot.")


def varieties_above_overall_avg() -> str:
    """Variedades cuja média de ``rating`` é MAIOR que a média geral de todos os
    vinhos. Use ``HAVING`` com uma subquery que calcula a média geral."""
    raise NotImplementedError("Implemente a query com o apoio do GitHub Copilot.")


def wines_by_region_climate() -> str:
    """Para cada ``climate`` da tabela ``regions``, conte quantos vinhos existem e a
    média de rating. Faça um ``LEFT JOIN`` de ``regions`` com ``wines`` usando
    ``LIKE`` (wines.region é texto livre, ex: "Mendocino, California")."""
    # Dica de junção:  ON w.region LIKE '%' || r.region_name || '%'
    raise NotImplementedError("Implemente a query com o apoio do GitHub Copilot.")
