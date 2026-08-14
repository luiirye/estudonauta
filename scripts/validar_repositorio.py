"""Valida a sintaxe e as convenções estruturais do repositório."""

from __future__ import annotations

import ast
import re
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
PASTA_PYTHON = RAIZ / "python"
PADRAO_MUNDO = re.compile(r"mundo_\d{2}_[a-z0-9_]+$")
PADRAO_AULA = re.compile(r"aula_\d{2}$")
PADRAO_EXERCICIO = re.compile(r"exercicio_\d{3}(?:_v\d+)?(?:\.(?:py|mp3))?$")
PADRAO_LINK = re.compile(r"\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)")


def validar_sintaxe(erros: list[str]) -> None:
    for arquivo in sorted(PASTA_PYTHON.rglob("*.py")):
        try:
            ast.parse(arquivo.read_text(encoding="utf-8"), filename=str(arquivo))
        except (SyntaxError, UnicodeDecodeError) as erro:
            erros.append(f"Sintaxe inválida em {arquivo.relative_to(RAIZ)}: {erro}")


def validar_estrutura(erros: list[str]) -> None:
    mundos = [pasta for pasta in PASTA_PYTHON.iterdir() if pasta.is_dir()]
    for mundo in sorted(mundos):
        if not PADRAO_MUNDO.fullmatch(mundo.name):
            erros.append(f"Nome de mundo fora do padrão: {mundo.relative_to(RAIZ)}")
        for obrigatorio in ("README.md", "aulas", "exercicios"):
            if not (mundo / obrigatorio).exists():
                erros.append(f"Item obrigatório ausente: {(mundo / obrigatorio).relative_to(RAIZ)}")

        for aula in (mundo / "aulas").iterdir():
            if aula.is_dir() and aula.name != "__pycache__" and not PADRAO_AULA.fullmatch(aula.name):
                erros.append(f"Nome de aula fora do padrão: {aula.relative_to(RAIZ)}")

        for exercicio in (mundo / "exercicios").iterdir():
            if exercicio.name in {"README.md", "utilidadesCeV", "__pycache__", "cores_ansi.txt"}:
                continue
            if exercicio.suffix not in {"", ".py", ".mp3", ".txt"}:
                continue
            if not PADRAO_EXERCICIO.fullmatch(exercicio.name):
                erros.append(f"Nome de exercício fora do padrão: {exercicio.relative_to(RAIZ)}")


def validar_links(erros: list[str]) -> None:
    for documento in sorted(RAIZ.rglob("*.md")):
        if ".git" in documento.parts:
            continue
        conteudo = documento.read_text(encoding="utf-8")
        for destino in PADRAO_LINK.findall(conteudo):
            if "://" in destino or destino.startswith("mailto:"):
                continue
            caminho = (documento.parent / destino).resolve()
            if not caminho.exists():
                erros.append(
                    f"Link local inválido em {documento.relative_to(RAIZ)}: {destino}"
                )


def main() -> int:
    erros: list[str] = []
    validar_sintaxe(erros)
    validar_estrutura(erros)
    validar_links(erros)

    if erros:
        print("Validação encontrou problemas:")
        for erro in erros:
            print(f"- {erro}")
        return 1

    quantidade = sum(1 for _ in PASTA_PYTHON.rglob("*.py"))
    print(f"Tudo certo: {quantidade} arquivos Python válidos e estrutura consistente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
