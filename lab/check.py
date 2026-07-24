#!/usr/bin/env python3
"""Validador modular do workshop **Data + GitHub Copilot**.

Executa verificacoes leves (porem significativas) sobre o codigo que voce
implementa em cada modulo e devolve feedback em portugues com dicas.

Uso:
    python lab/check.py --module sql
    python lab/check.py --module pandas
    python lab/check.py --module eda
    python lab/check.py --module viz
    python lab/check.py --module all

O mesmo comando roda no GitHub Actions para liberar o proximo passo do
exercicio. Rode localmente antes de fazer push para ter feedback rapido.
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent  # .../lab
DATA_DIR = ROOT / "data"
OUTPUTS_DIR = ROOT / "outputs"
SAMPLE_CSV = DATA_DIR / "train_sample.csv"
REGIONS_CSV = DATA_DIR / "regions.csv"

# Garante que os modulos (sql_module, pandas_module, ...) sejam importaveis.
sys.path.insert(0, str(ROOT))

OK = "\u2705"      # check verde
FAIL = "\u274c"    # x vermelho
TIP = "\U0001f4a1"  # lampada


def _read_sample():
    import pandas as pd

    return pd.read_csv(SAMPLE_CSV)


def _run_check(name, fn):
    """Executa uma verificacao isolada e retorna (nome, passou, mensagem)."""
    try:
        fn()
        return (name, True, "")
    except NotImplementedError:
        return (name, False, "ainda nao implementada - peca ajuda ao GitHub Copilot Chat.")
    except AssertionError as exc:
        return (name, False, str(exc) or "resultado fora do esperado.")
    except Exception as exc:  # noqa: BLE001 - feedback amigavel para o aluno
        return (name, False, f"erro ao executar: {exc}")


# --------------------------------------------------------------------------- #
# Modulo 1 - SQL
# --------------------------------------------------------------------------- #
def check_sql():
    import pandas as pd

    from sql_module import queries  # type: ignore

    conn = sqlite3.connect(":memory:")
    pd.read_csv(SAMPLE_CSV).to_sql("wines", conn, index=False)
    pd.read_csv(REGIONS_CSV).to_sql("regions", conn, index=False)

    specs = [
        ("avg_rating_by_variety", 2, None),
        ("top10_highest_rated", 3, 10),
        ("varieties_above_overall_avg", 1, None),
        ("wines_by_region_climate", 2, None),
    ]
    results = []
    for fn_name, min_cols, max_rows in specs:
        def _check(fn_name=fn_name, min_cols=min_cols, max_rows=max_rows):
            fn = getattr(queries, fn_name)
            sql = fn()
            assert isinstance(sql, str) and sql.strip(), "a funcao deve retornar uma string SQL."
            df = pd.read_sql_query(sql, conn)
            assert len(df.columns) >= min_cols, f"esperado ao menos {min_cols} colunas no resultado."
            assert len(df) >= 1, "a query nao retornou nenhuma linha."
            if max_rows is not None:
                assert len(df) <= max_rows, f"esperado no maximo {max_rows} linhas."

        results.append(_run_check(fn_name, _check))
    conn.close()
    return results


# --------------------------------------------------------------------------- #
# Modulo 2 - Pandas
# --------------------------------------------------------------------------- #
def check_pandas():
    import pandas as pd

    from pandas_module import transformations as T  # type: ignore

    results = []
    state = {}

    def c_load_wines():
        df = T.load_wines(str(SAMPLE_CSV))
        assert hasattr(df, "columns"), "load_wines deve retornar um DataFrame."
        assert len(df) > 0, "o DataFrame carregado esta vazio."
        assert {"name", "region", "variety", "rating"}.issubset(set(df.columns)), \
            "faltam colunas esperadas (name, region, variety, rating)."
        state["df"] = df

    results.append(_run_check("load_wines", c_load_wines))
    base = state.get("df")
    if base is None:
        base = pd.read_csv(SAMPLE_CSV)

    def c_clean_ratings():
        out = T.clean_ratings(base.copy())
        assert "rating" in out.columns, "a coluna rating deve continuar existindo."
        assert out["rating"].notna().all(), "ainda existem ratings nulos."
        assert pd.api.types.is_numeric_dtype(out["rating"]), "rating deve ser numerico."

    results.append(_run_check("clean_ratings", c_clean_ratings))

    def c_top_varieties():
        out = T.top_varieties_by_avg_rating(base.copy(), n=10)
        assert len(out) >= 1, "o resultado nao deve ser vazio."
        assert len(out) <= 10, "esperado no maximo 10 linhas (n=10)."

    results.append(_run_check("top_varieties_by_avg_rating", c_top_varieties))

    def c_rating_category():
        out = T.add_rating_category(base.copy())
        assert "rating_category" in out.columns, "faltou a coluna rating_category."
        valores = set(out["rating_category"].dropna().unique())
        assert valores.issubset({"Baixa", "Média", "Alta"}), \
            "rating_category deve conter apenas Baixa / Média / Alta."

    results.append(_run_check("add_rating_category", c_rating_category))

    def c_enrich_country():
        out = T.enrich_with_country(base.copy())
        assert "country" in out.columns, "faltou a coluna country."
        assert out["country"].notna().mean() > 0.5, "a maioria das linhas deveria ter country preenchido."

    results.append(_run_check("enrich_with_country", c_enrich_country))
    return results


# --------------------------------------------------------------------------- #
# Modulo 3 - EDA
# --------------------------------------------------------------------------- #
def check_eda():
    import pandas as pd

    from eda_module import analysis as A  # type: ignore

    base = pd.read_csv(SAMPLE_CSV)
    results = []

    def c_descriptive():
        out = A.descriptive_stats(base.copy())
        texto = " ".join(str(x) for x in (list(getattr(out, "index", [])) or list(out.keys()) if hasattr(out, "keys") else [out]))
        assert "mean" in texto or "mean" in str(out), "as estatisticas devem incluir a media (mean)."

    results.append(_run_check("descriptive_stats", c_descriptive))

    def c_outliers():
        out = A.detect_outliers_iqr(base.copy(), column="rating")
        assert hasattr(out, "columns"), "detect_outliers_iqr deve retornar um DataFrame."

    results.append(_run_check("detect_outliers_iqr", c_outliers))

    def c_missing():
        out = A.missing_values_report(base.copy())
        rotulos = set(getattr(out, "index", [])) | set(out.keys() if hasattr(out, "keys") else [])
        assert "notes" in rotulos or len(rotulos) >= 3, "o relatorio deve cobrir as colunas do DataFrame."

    results.append(_run_check("missing_values_report", c_missing))

    def c_by_variety():
        out = A.rating_stats_by_variety(base.copy())
        assert len(out) >= 1, "o resultado por variety nao deve ser vazio."

    results.append(_run_check("rating_stats_by_variety", c_by_variety))
    return results


# --------------------------------------------------------------------------- #
# Modulo 4 - Visualizacao
# --------------------------------------------------------------------------- #
def check_viz():
    import matplotlib

    matplotlib.use("Agg")  # backend sem interface grafica (CI)
    import pandas as pd

    from viz_module import plots as P  # type: ignore

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    base = pd.read_csv(SAMPLE_CSV)
    results = []

    specs = [
        ("plot_rating_distribution", OUTPUTS_DIR / "rating_distribution.png"),
        ("plot_top_varieties", OUTPUTS_DIR / "top_varieties.png"),
        ("plot_boxplot_by_variety", OUTPUTS_DIR / "boxplot_by_variety.png"),
    ]
    for fn_name, out_path in specs:
        def _check(fn_name=fn_name, out_path=out_path):
            if out_path.exists():
                out_path.unlink()
            fn = getattr(P, fn_name)
            fn(base.copy(), str(out_path))
            assert out_path.exists(), f"o arquivo {out_path.name} nao foi gerado."
            assert out_path.stat().st_size > 0, f"o arquivo {out_path.name} esta vazio."

        results.append(_run_check(fn_name, _check))
    return results


CHECKS = {
    "sql": check_sql,
    "pandas": check_pandas,
    "eda": check_eda,
    "viz": check_viz,
}


def run_module(module: str) -> bool:
    print(f"\n=== Modulo: {module} ===")
    try:
        results = CHECKS[module]()
    except Exception:  # noqa: BLE001
        print(f"{FAIL} Nao foi possivel importar o modulo '{module}'.")
        traceback.print_exc()
        return False

    all_ok = True
    for name, passed, msg in results:
        if passed:
            print(f"{OK} {name}")
        else:
            all_ok = False
            print(f"{FAIL} {name}: {msg}")
            print(f"   {TIP} Dica: abra o arquivo do modulo e complete a funcao com o Copilot.")
    return all_ok


def main() -> int:
    parser = argparse.ArgumentParser(description="Validador do workshop Data + GitHub Copilot.")
    parser.add_argument(
        "--module",
        required=True,
        choices=[*CHECKS.keys(), "all"],
        help="Modulo a validar (sql, pandas, eda, viz) ou 'all'.",
    )
    args = parser.parse_args()

    modules = list(CHECKS.keys()) if args.module == "all" else [args.module]
    ok = all([run_module(m) for m in modules])

    print()
    if ok:
        print(f"{OK} Tudo certo! Voce pode fazer commit e push para liberar o proximo passo.")
        return 0
    print(f"{FAIL} Ainda ha itens pendentes. Ajuste com o Copilot e rode novamente.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
