# Workshop — Data + GitHub Copilot

Este workshop mostra como usar o GitHub Copilot como parceiro de programação para tarefas de dados: escrever queries **SQL**, manipular **DataFrames** com pandas, conduzir uma **análise exploratória de dados (EDA)** e produzir **visualizações**. Ao longo de quatro módulos práticos você trabalha sobre um dataset de vinhos, aplicando boas práticas de engenharia de dados enquanto delega ao Copilot a geração e refinamento de código — sempre revisando o resultado antes de aceitá-lo.

## Estrutura

```
lab/
├── data/                # Datasets centralizados (train.csv, train_sample.csv, regions.csv)
├── sql_module/          # Módulo 1: Geração de Queries SQL
├── pandas_module/       # Módulo 2: Manipulação de DataFrames
├── eda_module/          # Módulo 3: Análise Exploratória de Dados
├── viz_module/          # Módulo 4: Visualização de Dados
├── outputs/             # Artefatos gerados (gráficos .png)
├── check.py             # Validador modular
└── requirements.txt     # Dependências Python
```

## Dataset

O workshop usa três tabelas, todas em `lab/data/`:

- `train.csv` — 32.780 vinhos, com as colunas `name`, `region`, `variety`, `rating` e `notes`.
- `train_sample.csv` — amostra de 1.000 vinhos, com o mesmo esquema de `train.csv`. É esta amostra que o validador utiliza.
- `regions.csv` — 15 regiões, com as colunas `id`, `region_name`, `country`, `climate`, `avg_temperature` e `soil_type`.

Atenção a um detalhe importante para os joins: a coluna `region` em `train.csv` é **texto livre** e não casa por igualdade exata com `regions.region_name`. Para relacionar as tabelas, use correspondência aproximada (`LIKE`) em vez de igualdade (`=`).

## Pré-requisitos

- Uma conta GitHub com o **GitHub Copilot** ativo.
- Um navegador.

O ambiente já vem pronto via **GitHub Codespaces** (Python 3.12 com `pandas`, `matplotlib`, `seaborn` e `sqlalchemy` instalados).

Para rodar localmente, instale as dependências:

```bash
pip install -r lab/requirements.txt
```

## Como funciona

Este workshop segue o formato **GitHub Skills**: você avança de passo em passo, e uma automação valida cada entrega e publica o próximo passo na issue de acompanhamento. O fluxo de cada passo é:

1. Crie um branch para o passo atual.
2. Complete o módulo correspondente àquele passo.
3. Valide localmente:

   ```bash
   python lab/check.py --module <sql|pandas|eda|viz>
   ```

4. Faça `commit` e `push` do seu branch.
5. A automação (GitHub Actions) valida a entrega e publica o próximo passo na issue de acompanhamento.

Os passos seguem sempre a ordem: **SQL → Pandas → EDA → Visualização**.

## Validação

O `check.py` é um validador modular que executa suas implementações sobre `train_sample.csv`. Ele aceita **qualquer implementação que produza o resultado esperado** — não importa o estilo do código, apenas a corretude do resultado — e devolve feedback em português para orientar as correções.

Para validar todos os módulos de uma vez:

```bash
python lab/check.py --module all
```

## Boas práticas (transversal)

- Sempre **revise o código gerado** pelo Copilot antes de aceitá-lo.
- Prefira **operações vetorizadas** do pandas a laços explícitos.
- Mantenha os **dados centralizados** em `lab/data/`.
- Escreva código **modular e legível**, com funções pequenas.
- Dê **títulos e labels** claros aos gráficos.
- Garanta **reprodutibilidade** (fixe seeds, use caminhos relativos ao projeto).
- Aproveite os comandos do Copilot: `/explain`, `/fix` e `/doc`.

## Guia para instrutores

| Formato | Escopo sugerido |
| --- | --- |
| **Completo** | Os 4 módulos completos: SQL, Pandas, EDA e Visualização. |
| **Reduzido** | Fazer SQL + Pandas na prática e **demonstrar** EDA + Visualização. |

Os gabaritos ficam em `lab/.solutions/` e são de uso do instrutor.

## Recursos

- [GitHub Copilot](https://docs.github.com/copilot)
- [pandas](https://pandas.pydata.org/docs/)
- [Matplotlib](https://matplotlib.org/stable/gallery/index.html)
- [seaborn](https://seaborn.pydata.org/tutorial.html)
