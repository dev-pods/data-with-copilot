# Módulo 2 — Manipulação de DataFrames

Neste módulo você vai transformar dados de vinhos usando `pandas`, completando
as funções do arquivo `transformations.py` com a ajuda do GitHub Copilot.

**Objetivo:** aprender o fluxo essencial de manipulação de DataFrames —
leitura, limpeza, agregação, criação de features e manipulação de texto — e
perceber como o Copilot acelera cada etapa.

## O que você vai praticar

- Leitura e limpeza de dados (`read_csv`, conversão de tipos, tratamento de nulos)
- Agregação com `groupby` e `agg`
- Ordenação de resultados com `sort_values`
- Feature engineering com `pd.cut` (criação de faixas/categorias)
- Manipulação de strings em colunas de texto
- Boas práticas ao trabalhar em par com o Copilot

## Como o Copilot ajuda aqui

O Copilot é especialmente útil em tarefas de `pandas`, onde muitas operações
seguem padrões conhecidos:

- **Comentário-para-código:** escreva um comentário descrevendo a transformação
  e deixe o Copilot sugerir a implementação.
- **Autocompletar transformações:** ao começar `df.groupby(...)` ou
  `pd.cut(...)`, o Copilot completa o encadeamento típico.
- **Copilot Chat:** peça explicações de trechos, geração de variações ou
  comparação de abordagens.
- **`/fix`:** selecione o código com erro e peça correção quando um teste falhar.

Prompts prontos para experimentar:

> Complete a função `top_varieties_by_avg_rating` calculando a média de `rating`
> por `variety`, ordenando do maior para o menor e retornando as `n` primeiras
> linhas com as colunas `variety` e `avg_rating`.

> Explique o que `pd.cut` faz e como definir os limites (`bins`) para criar as
> faixas "Baixa", "Média" e "Alta".

> Extraia o país da coluna `region`, pegando o texto após a última vírgula
> (ex: "Mendocino, California" deve virar "California").

## Exercícios

Abra `transformations.py` e complete as funções abaixo. Todas usam
`import pandas as pd`.

### 1. Ler o CSV

Leia o arquivo de vinhos e retorne um `DataFrame`.

```python
def load_wines(path: str) -> pd.DataFrame:
    ...
```

- **O que retornar:** o `DataFrame` com os dados do CSV indicado por `path`.
- **Dica:** use `pd.read_csv`. Depois valide com `df.head()` e `df.info()`.
- **Prompt sugerido:**

> Implemente `load_wines` para ler um arquivo CSV a partir do caminho `path` e
> retornar um DataFrame do pandas.

### 2. Limpar os ratings

Converta a coluna `rating` para numérica e remova as linhas com `rating` nulo.

```python
def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    ...
```

- **O que retornar:** um novo `DataFrame` sem linhas de `rating` inválido/nulo.
- **Dica:** use `pd.to_numeric(..., errors="coerce")` para transformar valores
  inválidos em `NaN` e depois `dropna(subset=["rating"])`. Trabalhe sobre uma
  cópia com `.copy()`.
- **Prompt sugerido:**

> Converta a coluna `rating` para numérico tratando valores inválidos como nulos
> e remova as linhas onde `rating` ficou nulo.

### 3. Top variedades por rating médio

Calcule a média de `rating` por `variety`, ordene de forma decrescente e
retorne as `n` primeiras.

```python
def top_varieties_by_avg_rating(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    ...
```

- **O que retornar:** um `DataFrame` com as colunas `variety` e `avg_rating`,
  ordenado do maior para o menor rating médio, limitado a `n` linhas.
- **Dica:** use `groupby("variety")["rating"].mean()` seguido de `sort_values`
  e `head(n)`. Nomeie a coluna de média como `avg_rating`.
- **Prompt sugerido:**

> Agrupe por `variety`, calcule a média de `rating`, ordene decrescente e
> retorne as `n` primeiras linhas com as colunas `variety` e `avg_rating`.

### 4. Categorizar o rating

Adicione a coluna `rating_category` classificando cada vinho em faixas.

```python
def add_rating_category(df: pd.DataFrame) -> pd.DataFrame:
    ...
```

- **O que retornar:** o `DataFrame` com a nova coluna `rating_category`, usando
  as faixas: "Baixa" (`< 85`), "Média" (`85-90`) e "Alta" (`> 90`).
- **Dica:** use `pd.cut` definindo os `bins` e os `labels` correspondentes.
  Trabalhe sobre uma cópia com `.copy()`.
- **Prompt sugerido:**

> Crie a coluna `rating_category` com `pd.cut`, usando as faixas "Baixa" para
> ratings abaixo de 85, "Média" entre 85 e 90 e "Alta" acima de 90.

### 5. Enriquecer com o país

Adicione a coluna `country` extraindo o último trecho após a vírgula em
`region`.

```python
def enrich_with_country(df: pd.DataFrame) -> pd.DataFrame:
    ...
```

- **O que retornar:** o `DataFrame` com a nova coluna `country` (ex:
  "Mendocino, California" deve resultar em "California").
- **Dica:** use as funções de string do pandas (`str.split(",")` e selecione o
  último elemento com `.str[-1]`), aplicando `.str.strip()` para remover espaços.
- **Prompt sugerido:**

> Adicione a coluna `country` extraindo o texto após a última vírgula da coluna
> `region` e removendo espaços em branco nas pontas.

## Boas práticas (transversal)

- Evite mutar o `df` original: crie uma cópia com `.copy()` antes de alterar.
- Prefira operações vetorizadas do pandas em vez de loops linha a linha.
- Escreva encadeamentos (`method chaining`) legíveis, quebrando em linhas.
- Valide cada etapa com `df.head()` e `df.info()`.
- Peça docstrings ao Copilot com `/doc` para documentar as funções.

## Validação

Rode a verificação do módulo:

```bash
python lab/check.py --module pandas
```

Com a validação passando, faça o `push` das suas alterações — isso libera o
próximo passo do workshop.
