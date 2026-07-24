# Módulo 4 — Visualização de Dados

Neste módulo você vai transformar números em imagens: gráficos que comunicam
padrões do dataset de forma clara e direta. O objetivo é praticar a criação de
visualizações com `matplotlib` e `seaborn`, completando funções em
`plots.py` com o apoio do GitHub Copilot.

## O que você vai praticar

- Criar um histograma para entender a distribuição de uma variável numérica
- Criar um gráfico de barras horizontais para comparar categorias
- Criar um boxplot para comparar distribuições entre grupos
- Escolher o gráfico certo para cada tipo de pergunta
- Definir títulos e labels de eixos legíveis (em português)
- Salvar figuras em disco como arquivos PNG
- Combinar `matplotlib` + `seaborn` no mesmo fluxo

## Como o Copilot ajuda aqui

O Copilot é ótimo para acelerar a escrita de código de visualização:

- Gera o código de um gráfico a partir de uma descrição em linguagem natural
- Ajusta estilo, cores, títulos e labels sem você lembrar toda a API
- Com `/fix`, corrige erros comuns de plot (eixos, tipos, backend, figuras
  não fechadas)

Alguns prompts prontos para experimentar (escreva como comentário acima da
função ou peça no chat):

> Crie um histograma da coluna `rating` com 20 bins, título e labels de eixos
> em português, e salve a figura em `out_path` como PNG.

> Gere um gráfico de barras horizontais com as 10 variedades mais frequentes
> (coluna `variety`), ordenadas por quantidade, e salve em `out_path`.

> Faça um boxplot de `rating` para as 5 variedades mais frequentes, com labels
> em português, e salve a figura em `out_path`.

## Exercícios

Os exercícios completam as funções em `plots.py`. Cada função recebe um
`DataFrame` (`df`) e um caminho de saída (`out_path`), gera um gráfico, **salva
o PNG em `out_path`** e retorna a figura. Os arquivos são gravados em
`lab/outputs/`.

Importante: o backend do `matplotlib` deve ser o `Agg` (sem interface
gráfica), já configurado no topo do arquivo com `matplotlib.use('Agg')`.
Não use colunas que não existam no dataset. As colunas disponíveis em
`train.csv` / `train_sample.csv` são: `name`, `region`, `variety`, `rating`,
`notes`.

### 1. Distribuição de rating (histograma)

Gere um histograma da coluna `rating` para visualizar como as notas se
distribuem.

```python
def plot_rating_distribution(df, out_path):
    ...
```

- O que gerar: um histograma de `rating` (sugestão: 20 bins).
- O que salvar: a figura em `out_path` como PNG.
- Dica: use `plt.subplots()`, adicione título e labels de eixos em português
  e finalize com `fig.savefig(out_path)`.
- Prompt sugerido:

> Crie um histograma da coluna `rating` com 20 bins, título e labels de eixos
> em português, salve em `out_path` como PNG e retorne a figura.

### 2. Top 10 variedades (barras horizontais)

Gere um gráfico de barras horizontais com as 10 variedades (`variety`) mais
frequentes no dataset.

```python
def plot_top_varieties(df, out_path):
    ...
```

- O que gerar: barras horizontais das top 10 variedades por quantidade.
- O que salvar: a figura em `out_path` como PNG.
- Dica: use `df["variety"].value_counts().head(10)` para obter as contagens e
  `ax.barh(...)` para as barras horizontais.
- Prompt sugerido:

> Gere um gráfico de barras horizontais com as 10 variedades mais frequentes
> da coluna `variety`, ordenadas por quantidade, com título e labels em
> português, e salve em `out_path`.

### 3. Rating por variedade (boxplot)

Gere um boxplot de `rating` para as 5 variedades mais frequentes, comparando
a distribuição das notas entre elas.

```python
def plot_boxplot_by_variety(df, out_path):
    ...
```

- O que gerar: um boxplot de `rating` para as top 5 variedades.
- O que salvar: a figura em `out_path` como PNG.
- Dica: filtre o `df` para manter apenas as 5 variedades mais frequentes antes
  de plotar; use `seaborn.boxplot(data=..., x="variety", y="rating")`.
- Prompt sugerido:

> Faça um boxplot de `rating` para as 5 variedades mais frequentes da coluna
> `variety`, com título e labels em português, e salve em `out_path`.

## Boas práticas (transversal)

- Sempre defina título do gráfico e labels dos eixos
- Evite excesso de cores; use cores apenas quando agregam significado
- Salve as figuras em resolução adequada (defina o `dpi`, ex.: `dpi=100`)
- Feche as figuras após salvar com `plt.close(fig)` para liberar memória
- Escolha o gráfico adequado ao dado: histograma para distribuição, barras
  para comparação de categorias, boxplot para comparar distribuições
- Peça uma revisão ao Copilot: "revise este gráfico e sugira melhorias de
  clareza e legibilidade"

## Validação

Ao concluir as três funções, rode o verificador do módulo. Ele confere se os
PNGs esperados foram gerados em `lab/outputs/`:

```bash
python lab/check.py --module viz
```

Com a validação passando, faça o push das suas alterações — ele libera o
encerramento do workshop.
