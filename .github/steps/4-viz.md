## Passo 4 — Visualização de Dados

Objetivo: usar o Copilot para criar gráficos claros com **matplotlib** e **seaborn**.

Guia completo do módulo: [`lab/viz_module/README.md`](../../blob/main/lab/viz_module/README.md)

### Suas tarefas

Complete as funções em [`lab/viz_module/plots.py`](../../blob/main/lab/viz_module/plots.py). Cada função **gera e salva** um PNG em `out_path` (dentro de `lab/outputs/`):

1. `plot_rating_distribution(df, out_path)` — histograma da distribuição de `rating`.
2. `plot_top_varieties(df, out_path)` — barras horizontais das top 10 variedades por quantidade.
3. `plot_boxplot_by_variety(df, out_path)` — boxplot de `rating` das top 5 variedades.

> [!TIP]
> Descreva o gráfico em linguagem natural e deixe o Copilot gerar o código. Mantenha `matplotlib.use("Agg")` para funcionar no ambiente do CI.

### Boas práticas (transversal)

- Sempre inclua **título** e **labels** dos eixos.
- Escolha o gráfico adequado ao tipo de dado.
- Feche as figuras com `plt.close()` e salve com `dpi` adequado.

### Validar e concluir

```bash
python lab/check.py --module viz
```

Faça commit e push do seu branch. Esse é o **último módulo** — a automação encerra o workshop. 🎉
