## Passo 3 — Análise Exploratória de Dados (EDA)

Objetivo: usar o Copilot para gerar estatísticas, detectar outliers e resumir os dados.

Guia completo do módulo: [`lab/eda_module/README.md`](../../blob/main/lab/eda_module/README.md)

### Suas tarefas

Complete as funções em [`lab/eda_module/analysis.py`](../../blob/main/lab/eda_module/analysis.py):

1. `descriptive_stats(df)` — estatísticas descritivas de `rating` (inclui `mean`).
2. `detect_outliers_iqr(df, column="rating")` — linhas outliers pelo método **IQR** (fator 1.5).
3. `missing_values_report(df)` — contagem de valores ausentes por coluna.
4. `rating_stats_by_variety(df)` — `count`, `mean`, `min`, `max` de `rating` por `variety`.

> [!TIP]
> Use `/explain` para entender a fórmula do IQR antes de aceitar o código. Peça ao Copilot para **interpretar** os resultados no chat.

### Boas práticas (transversal)

- Documente as premissas da análise.
- Cuidado ao interpretar correlação como causalidade.
- Garanta reprodutibilidade (mesma entrada → mesma saída).

### Validar e avançar

```bash
python lab/check.py --module eda
```

Faça commit e push do seu branch para liberar o **Passo 4**. 🚀
