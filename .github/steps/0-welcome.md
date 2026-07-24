## Preparando o ambiente

Olá, @{{ login }}! Bem-vindo(a) ao workshop **Data + GitHub Copilot para soluções de dados**. 🍷📊

Neste treinamento você vai usar o GitHub Copilot como copiloto de dados em 4 módulos, aplicando **boas práticas** de forma transversal:

| Módulo | Tema | Duração |
| ------ | ---- | ------- |
| 1 | Geração de Queries **SQL** | ~25 min |
| 2 | Manipulação de **DataFrames** (pandas) | ~30 min |
| 3 | **EDA** — Análise Exploratória de Dados | ~30 min |
| 4 | **Visualização** de Dados | ~25 min |

### 1. Abra o ambiente

Abra o projeto em um Codespace (ou clone localmente):

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

- Recomendado: clique em **Code → Codespaces → Create codespace on main**. O ambiente já vem com Python 3.12, pandas, matplotlib, seaborn e as extensões do Copilot. As dependências são instaladas automaticamente.
- Alternativa local: clone o repositório e rode `pip install -r lab/requirements.txt`.

### 2. Conheça o dataset (centralizado)

Todos os módulos usam a mesma base, em `lab/data/`:

- `train.csv` — 32.780 vinhos (colunas: `name`, `region`, `variety`, `rating`, `notes`)
- `train_sample.csv` — amostra de 1.000 registros (usada na validação, mais rápida)
- `regions.csv` — 15 regiões (`id`, `region_name`, `country`, `climate`, `avg_temperature`, `soil_type`)

> [!TIP]
> Manter os dados em um único lugar (`lab/data/`) é uma boa prática: evita cópias divergentes e facilita a reprodutibilidade.

### 3. Recursos do Copilot que vamos usar

- **Autocompletar** a partir de comentários (comentário → código)
- **Copilot Chat inline** (`Cmd/Ctrl + I`) para gerar e ajustar trechos
- Comandos de barra: **`/explain`**, **`/fix`**, **`/doc`**
- **`@workspace`** para perguntas com contexto do repositório

### 4. Como o workshop avança

1. Crie um **branch** para trabalhar (ex.: `git checkout -b modulo-sql`).
2. Complete o módulo do passo atual em `lab/<módulo>/`.
3. Valide localmente: `python lab/check.py --module <sql|pandas|eda|viz>`.
4. Faça **commit** e **push** do branch. A automação valida seu trabalho e publica o próximo passo **aqui nesta issue**.

> [!NOTE]
> A validação roda sobre `train_sample.csv` para ser rápida. Há mais de uma solução correta — o importante é o resultado esperado.
