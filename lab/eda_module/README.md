# Módulo 3 — Análise Exploratória de Dados (EDA)

Neste módulo você vai explorar o dataset de avaliações usando `pandas` para
extrair estatísticas, identificar anomalias e formular hipóteses. O objetivo é
transformar dados brutos em entendimento, apoiado pelo GitHub Copilot para
acelerar cálculos e interpretações.

## O que você vai praticar

- Calcular estatísticas descritivas de uma coluna numérica (`rating`).
- Detectar outliers com o método IQR (fator 1.5).
- Gerar relatório de valores ausentes por coluna.
- Fazer agregações por grupo (estatísticas de `rating` por `variety`).
- Gerar e testar hipóteses sobre os dados com o apoio da IA.

## Como o Copilot ajuda aqui

O Copilot é útil para escrever cálculos estatísticos a partir de uma descrição
em linguagem natural, poupando você de lembrar a sintaxe exata do `pandas`.

- Descreva o cálculo desejado em um comentário e deixe o Copilot sugerir a
  implementação (por exemplo, "estatísticas descritivas da coluna rating").
- Use `/explain` no Copilot Chat para entender uma fórmula, como o cálculo do
  IQR e por que o fator 1.5 é usado para delimitar outliers.
- Use o Copilot Chat para interpretar resultados: cole a saída de uma função e
  pergunte o que os números indicam sobre a distribuição dos dados.

Prompts prontos para experimentar:

> Implemente a detecção de outliers da coluna rating usando o método IQR com
> fator 1.5.

> Explique passo a passo como o IQR identifica valores atípicos e o que
> representa o fator 1.5.

> Interprete estas estatísticas descritivas de rating e sugira duas hipóteses
> que eu poderia investigar.

## Exercícios

Complete as funções em `analysis.py`. Os dados estão em `lab/data/`
(`train.csv` com 32.780 linhas e `train_sample.csv` com 1.000; use a amostra
para iterar mais rápido). As colunas relevantes são `name`, `region`,
`variety`, `rating` e `notes`.

### 1. Estatísticas descritivas de `rating`

Retorne as estatísticas descritivas da coluna `rating`, incluindo a média
(`mean`).

```python
def descriptive_stats(df):
    ...
```

- O que retornar: o resultado de `df['rating'].describe()` (contém `count`,
  `mean`, `std`, `min`, quartis e `max`).
- Dica: `Series.describe()` já entrega tudo o que você precisa em uma linha.
- Prompt sugerido:

> Retorne as estatísticas descritivas da coluna rating usando pandas,
> incluindo a média.

### 2. Detecção de outliers por IQR

Retorne um `DataFrame` com as linhas consideradas outliers da coluna informada,
usando o método IQR com fator 1.5.

```python
def detect_outliers_iqr(df, column='rating'):
    ...
```

- O que retornar: um `DataFrame` contendo apenas as linhas cujo valor em
  `column` está abaixo de `Q1 - 1.5 * IQR` ou acima de `Q3 + 1.5 * IQR`.
- Dica: calcule `Q1` e `Q3` com `quantile(0.25)` e `quantile(0.75)`; o
  `IQR` é `Q3 - Q1`.
- Prompt sugerido:

> Implemente a detecção de outliers da coluna rating usando o método IQR com
> fator 1.5, retornando as linhas atípicas.

### 3. Relatório de valores ausentes

Retorne a contagem de valores ausentes por coluna.

```python
def missing_values_report(df):
    ...
```

- O que retornar: o resultado de `df.isna().sum()`, com a contagem de valores
  nulos de cada coluna.
- Dica: combine `isna()` com `sum()` para contar os nulos por coluna.
- Prompt sugerido:

> Gere um relatório com a contagem de valores ausentes por coluna do
> DataFrame.

### 4. Estatísticas de `rating` por `variety`

Agregue a coluna `rating` por `variety`, calculando contagem, média, mínimo e
máximo, ordenando pela média em ordem decrescente.

```python
def rating_stats_by_variety(df):
    ...
```

- O que retornar: um `DataFrame` agrupado por `variety` com as colunas
  `count`, `mean`, `min` e `max` de `rating`, ordenado por `mean` desc.
- Dica: use `groupby('variety')['rating'].agg([...])` e depois
  `sort_values('mean', ascending=False)`.
- Prompt sugerido:

> Agrupe rating por variety calculando count, mean, min e max, ordenando pela
> média em ordem decrescente.

## Boas práticas (transversal)

- Documente as premissas da análise (o que você assumiu sobre os dados e por
  quê).
- Valide o tamanho da amostra antes de generalizar conclusões.
- Tenha cuidado ao interpretar correlação versus causalidade: correlação não
  implica causa.
- Peça ao Copilot para explicar o método usado com `/explain` sempre que a
  lógica não estiver clara.
- Garanta reprodutibilidade: fixe sementes quando houver aleatoriedade e
  registre as etapas da análise.

## Validação

Rode a verificação do módulo:

```bash
python lab/check.py --module eda
```

Ao concluir os exercícios, faça o push das suas alterações. O push libera o
próximo passo do workshop.
