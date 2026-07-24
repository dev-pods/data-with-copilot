"""Modulo 1 - Geracao de Queries SQL (GABARITO / referencia do instrutor).

NAO compartilhe este arquivo com os participantes durante o workshop.
"""
from __future__ import annotations


def avg_rating_by_variety() -> str:
    return """
        SELECT variety,
               ROUND(AVG(rating), 2) AS avg_rating,
               COUNT(*) AS total
        FROM wines
        GROUP BY variety
        ORDER BY avg_rating DESC
    """


def top10_highest_rated() -> str:
    return """
        SELECT name, variety, rating
        FROM wines
        ORDER BY rating DESC
        LIMIT 10
    """


def varieties_above_overall_avg() -> str:
    return """
        SELECT variety,
               ROUND(AVG(rating), 2) AS avg_rating
        FROM wines
        GROUP BY variety
        HAVING AVG(rating) > (SELECT AVG(rating) FROM wines)
        ORDER BY avg_rating DESC
    """


def wines_by_region_climate() -> str:
    return """
        SELECT r.climate,
               COUNT(w.name) AS total_wines,
               ROUND(AVG(w.rating), 2) AS avg_rating
        FROM regions r
        LEFT JOIN wines w
          ON w.region LIKE '%' || r.region_name || '%'
        GROUP BY r.climate
        ORDER BY total_wines DESC
    """
