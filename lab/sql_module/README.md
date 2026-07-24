# Módulo 1 — Geração de Queries SQL

Objetivo: usar o GitHub Copilot para transformar descrições em linguagem natural em queries SQL (dialeto SQLite) que exploram um dataset de vinhos.

## O que você vai praticar 🍷

- Traduzir linguagem natural em SQL com ajuda do Copilot
- Escrever agregações (`AVG`, `COUNT`) e ordenação (`ORDER BY`)
- Agrupar dados com `GROUP BY` e filtrar grupos com `HAVING`
- Usar subqueries para comparar valores contra uma média geral
- Fazer `JOIN` aproximado entre tabelas usando `LIKE`
- Aproveitar recursos do Copilot como comentário-para-código, inline chat e `/explain`

## Como o Copilot ajuda aqui

Neste módulo você completa 4 funções no arquivo `queries.py`. Cada função deve retornar uma **string SQL**. O Copilot pode acelerar bastante esse trabalho:

- **Comentário-para-código**: escreva um comentário descrevendo a query em português e deixe o Copilot sugerir a string SQL correspondente na linha seguinte.
- **Copilot Chat inline (`Cmd+I`)**: selecione o corpo da função e peça a query diretamente no editor, sem sair do contexto do código.
- **`/explain`**: selecione uma query SQL já gerada e use `/explain` para entender o que cada cláusula faz antes de aceitá-la.
- **Prompts em linguagem natural**: descreva o resultado esperado (colunas, agregação, ordenação) e o dialeto (SQLite).

Exemplos de prompts prontos para colar no Copilot Chat:

> Gere uma query SQLite que calcule a média de `rating` por `variety`, com a contagem de vinhos, ordenada da maior para a menor.

> Escreva uma query SQLite que retorne os 10 vinhos com maior `rating`, mostrando `name`, `variety` e `rating`.

> Preciso de uma query SQLite que faça `LEFT JOIN` entre `regions` e `wines` usando `LIKE`, agrupando por `climate`.

## Exercícios

Complete as 4 funções em `queries.py`. As tabelas disponíveis no banco SQLite são:

- `wines` — carregada de `train_sample.csv`, com as colunas `name`, `region`, `variety`, `rating`, `notes`.
- `regions` — carregada de `regions.csv`, com as colunas `id`, `region_name`, `country`, `climate`, `avg_temperature`, `soil_type`.

> Observação importante: `regions.region_name` (ex: `"Bordeaux"`) **não** casa por igualdade com `wines.region` (texto livre, ex: `"Mendocino, California"`). Para relacionar as tabelas, use `LIKE '%' || region_name || '%'`.

### 1. `avg_rating_by_variety()`

- **O que retornar**: a média de `rating` por `variety`, junto com a quantidade de vinhos de cada variedade, ordenada da maior média para a menor.
- **Colunas esperadas**: `variety`, média de rating (ex: `avg_rating`), contagem (ex: `total`).
- **Dica**: use `GROUP BY variety` com `AVG(rating)` e `COUNT(*)`, e finalize com `ORDER BY avg_rating DESC`.
- **Prompt sugerido**:

> Gere uma query SQLite sobre a tabela `wines` que retorne `variety`, a média de `rating` como `avg_rating` e a contagem como `total`, agrupando por `variety` e ordenando pela média em ordem decrescente.

### 2. `top10_highest_rated()`

- **O que retornar**: os 10 vinhos com maior `rating`.
- **Colunas esperadas**: `name`, `variety`, `rating`.
- **Dica**: ordene por `rating DESC` e limite o resultado com `LIMIT 10`.
- **Prompt sugerido**:

> Escreva uma query SQLite que selecione `name`, `variety` e `rating` da tabela `wines`, ordene por `rating` em ordem decrescente e retorne apenas os 10 primeiros.

### 3. `varieties_above_overall_avg()`

- **O que retornar**: as variedades cuja média de `rating` é maior que a média geral de `rating` de todos os vinhos.
- **Colunas esperadas**: `variety`, média da variedade (ex: `avg_rating`).
- **Dica**: agrupe por `variety` e use `HAVING AVG(rating) > (SELECT AVG(rating) FROM wines)`.
- **Prompt sugerido**:

> Gere uma query SQLite que retorne as `variety` cuja média de `rating` seja maior que a média geral de `rating`, usando `GROUP BY` e `HAVING` com uma subquery.

### 4. `wines_by_region_climate()`

- **O que retornar**: um `LEFT JOIN` de `regions` com `wines`, contando quantos vinhos existem e a média de `rating` por `climate`.
- **Colunas esperadas**: `climate`, contagem de vinhos (ex: `total_wines`), média de rating (ex: `avg_rating`).
- **Dica**: junte as tabelas com `wines.region LIKE '%' || regions.region_name || '%'` e agrupe por `climate`. Use `LEFT JOIN` para manter regiões mesmo sem vinhos correspondentes.
- **Prompt sugerido**:

> Escreva uma query SQLite que faça `LEFT JOIN` entre `regions` e `wines` usando `wines.region LIKE '%' || regions.region_name || '%'`, e retorne `climate`, o total de vinhos e a média de `rating`, agrupando por `climate`.

## Boas práticas (transversal)

- **Revise o SQL gerado**: nunca aceite uma sugestão do Copilot sem ler. Use `/explain` para confirmar que cada cláusula faz o que você espera.
- **Nomeie aliases com clareza**: prefira `avg_rating` e `total_wines` a `a` ou `c`, para que o resultado seja legível.
- **Formate e idente**: quebre a query em linhas por cláusula (`SELECT`, `FROM`, `WHERE`, `GROUP BY`, `ORDER BY`) para facilitar a leitura e a revisão.
- **Evite `SELECT *`**: selecione apenas as colunas necessárias, garantindo que o resultado tenha exatamente as colunas esperadas.
- **Valide o resultado**: rode a validação local (abaixo) antes de considerar o exercício concluído.

## Validação

Rode o script de verificação local para validar as suas queries deste módulo:

```bash
python lab/check.py --module sql
```

Ao fazer `commit` e `push` das alterações, o GitHub Actions executa a mesma verificação no repositório e libera o próximo passo do workshop automaticamente.
