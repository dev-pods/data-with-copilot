## Passo 2 — Manipulação de DataFrames

Objetivo: usar o Copilot para carregar, limpar e transformar dados com **pandas**.

Guia completo do módulo: [`lab/pandas_module/README.md`](../../blob/main/lab/pandas_module/README.md)

### Suas tarefas

Complete as funções em [`lab/pandas_module/transformations.py`](../../blob/main/lab/pandas_module/transformations.py):

1. `load_wines(path)` — lê o CSV e retorna um DataFrame.
2. `clean_ratings(df)` — converte `rating` para numérico e remove linhas nulas.
3. `top_varieties_by_avg_rating(df, n=10)` — top `n` variedades por média de `rating`.
4. `add_rating_category(df)` — coluna `rating_category`: `Baixa` (<85), `Média` (85–90), `Alta` (>90).
5. `enrich_with_country(df)` — coluna `country` extraída de `region` (texto após a última vírgula).

> [!TIP]
> Peça ao Copilot operações **vetorizadas** (sem loops) e use `.copy()` para não alterar o DataFrame original. Experimente `/fix` quando algo der erro.

### Boas práticas (transversal)

- Não mute o DataFrame de entrada; trabalhe sobre uma cópia.
- Valide o resultado com `df.head()` e `df.info()`.
- Peça docstrings ao Copilot com `/doc`.

### Validar e avançar

```bash
python lab/check.py --module pandas
```

Faça commit e push do seu branch para liberar o **Passo 3**. 🚀
