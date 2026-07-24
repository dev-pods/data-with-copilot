# Instruções do projeto - Data + GitHub Copilot (workshop)

Estas instruções são aplicadas automaticamente pelo GitHub Copilot em todas as
interações neste repositório. Use-as como contexto de engenharia para gerar
código consistente com o conteúdo e as convenções do workshop.

## Visão geral

Workshop para usar o GitHub Copilot em tarefas de dados, em
quatro módulos, sobre uma base de vinhos:

1. Geração de Queries SQL
2. Manipulação de DataFrames (pandas)
3. Análise Exploratória de Dados (EDA)
4. Visualização de Dados

Boas práticas são trabalhadas de forma transversal em todos os módulos.

## Stack

- Python 3.12
- pandas, numpy, matplotlib, seaborn, SQLAlchemy
- SQLite (via `sqlite3`) para o módulo de SQL
- Validação: `lab/check.py` (runner modular próprio)

## Dataset (centralizado)

Sempre em `lab/data/`:

- `train.csv` (32.780) e `train_sample.csv` (1.000): `name`, `region`,
  `variety`, `rating`, `notes`
- `regions.csv` (15): `id`, `region_name`, `country`, `climate`,
  `avg_temperature`, `soil_type`
- `region` (em train) é texto livre (ex.: "Mendocino, California") e **não**
  casa por igualdade com `regions.region_name`; para juntar, use
  `LIKE '%' || region_name || '%'`.

Use `train_sample.csv` em validações rápidas; `train.csv` para análises completas.

## Estrutura dos módulos

Cada módulo fica em `lab/<módulo>_module/` com um `README.md` (teoria,
exercícios e prompts sugeridos) e um arquivo Python com funções a completar:

- `sql_module/queries.py` — funções que retornam strings SQL
- `pandas_module/transformations.py` — transformações que retornam DataFrames
- `eda_module/analysis.py` — funções de estatística/EDA
- `viz_module/plots.py` — funções que geram e salvam gráficos PNG

## Convenções de código

- Nomes de símbolos de código em inglês; comentários e docstrings em português.
- Funções pequenas, com responsabilidade única e legíveis.
- Prefira operações vetorizadas do pandas a loops explícitos.
- Não mute o DataFrame de entrada; trabalhe sobre `.copy()`.
- Em SQL, evite `SELECT *`, use aliases claros e formate/idente a query.
- Em gráficos, sempre inclua título e labels; use `matplotlib.use("Agg")` para
  compatibilidade com o CI e feche as figuras com `plt.close()`.

## Boas práticas com IA (transversal)

- Reveja sempre o código gerado pelo Copilot — a responsabilidade é de quem
  aceita a sugestão.
- Prefira prompts específicos; itere com `/explain`, `/fix` e `/doc`.
- Garanta reprodutibilidade (mesma entrada → mesma saída).

## Restrições gerais

- Não use provedores de dados externos; o dataset é local ao repositório.
- Não quebre o contrato das funções validado por `lab/check.py`.
- Os gabaritos em `lab/.solutions/` são apenas referência do instrutor.
