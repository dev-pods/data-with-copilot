## Passo 1 — Geração de Queries SQL

Objetivo: usar o Copilot para transformar linguagem natural em **queries SQL** (SQLite) sobre a base de vinhos.

Guia completo do módulo: [`lab/sql_module/README.md`](../../blob/main/lab/sql_module/README.md)

### Suas tarefas

Complete as 4 funções em [`lab/sql_module/queries.py`](../../blob/main/lab/sql_module/queries.py) — cada uma deve **retornar uma string SQL**. As tabelas são `wines` e `regions`.

1. `avg_rating_by_variety()` — média de `rating` por `variety`, com contagem, ordenada desc.
2. `top10_highest_rated()` — os 10 vinhos com maior `rating` (`name`, `variety`, `rating`).
3. `varieties_above_overall_avg()` — variedades com média de `rating` acima da média geral (`HAVING` + subquery).
4. `wines_by_region_climate()` — `LEFT JOIN` de `regions` com `wines` via `LIKE`, contando vinhos e média por `climate`.

> [!TIP]
> Escreva um comentário descrevendo o que a query deve fazer e deixe o Copilot sugerir o SQL. Use `/explain` para revisar antes de confiar no resultado.

### Boas práticas (transversal)

- Prefira nomes de alias claros e evite `SELECT *`.
- Revise sempre o SQL gerado pela IA antes de aceitá-lo.
- Formate/idente a query para facilitar a leitura.

### Validar e avançar

```bash
python lab/check.py --module sql
```

Quando os 4 itens estiverem ✅, faça commit e push do seu branch:

```bash
git add lab/sql_module/queries.py
git commit -m "Modulo SQL concluido"
git push -u origin HEAD
```

A automação valida e publica o **Passo 2** aqui. 🚀
