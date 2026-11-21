---
project: flask-swagger-generator
kind: handoff
tier: working
updated_at: 2026-11-21
---

# 🤝 Handoff Ativo — `flask-swagger-generator`

> **Escopo do Projeto:** Biblioteca `flask-swagger-init` no PyPI para geração automática de especificação OpenAPI 3.0 e publicação da Swagger UI para aplicações Flask.

## 1. Onde Paramos / Contexto Atual (`WIP`)
- **[2026-11-21] Correção de build PyPI (`MANIFEST.in` + `setup.cfg`) após falha na tag `v26.47.001` (`Por Publicar`):**
  - Na tag `v26.47.001` (`run 44943778566` no GitHub Actions), os testes em Python `3.15` passaram, mas o passo `python -m build` falhou com `ModuleNotFoundError: No module named 'version'` porque o `sdist` não incluía `version.py`, `version.txt` e `requirements.txt` sem `MANIFEST.in`.
  - Adicionado `MANIFEST.in` na raiz (`version.py`, `version.txt`, `requirements.txt`, `README.md`, `LICENSE`), ajustado `setup.cfg` (`description_file = README.md`) e validado `python -m build` + `6/6` testes offline localmente em Python `3.15.2`.
- **[2026-11-21] Implementação base da ID 95 (`6/6` testes offline OK em Python `3.15.2`):**
  - Atualizado `requirements.txt` (`flask>=3.1,<4`, `marshmallow>=3.13,<5`, `flask-swagger-ui>=4.11,<6`), removido `setuptools` de runtime e atualizado `requirements-test.txt`.
  - Atualizado `setup.py` para `python_requires=">=3.11"`, `encoding="utf-8"` e classifiers `3.11`–`3.15`.
  - Corrigida compatibilidade com `marshmallow 4.x` e literais de array em `swagger_view.py` (`metadata={"example": ...}`), `schemas.py` (`field.schema`, `field.inner.schema`, `if val is None: return None`) e `schema_attribute.py` (`self.value[0]` para listas não vazias + guarda `and self.reference`).
  - Migrados os testes de `Flask-Testing` para `unittest.TestCase`, alinhada a linha `version: 1.0.0.` nas 5 fixtures YAML, adicionado `test_swagger_view.py`, atualizado `.github/workflows/build.yml` (Python `3.15` + testes) e provisionados `.agents/`, `.ai-memory/`, `.junie/` e `notify-cicd.yml`.

## 2. Tentativas Descartadas / O que Falhou (`Failed Approaches`)
- **Tag `v26.47.001` (`run 44943778566`):** `python -m build` sem `MANIFEST.in` falhou ao construir o wheel a partir do sdist (`ModuleNotFoundError: No module named 'version'`). Resolvido com `MANIFEST.in`.

## 3. Estado dos Arquivos / Branch / Build
- **Fonte Primária:** GitHub (`main`, com espelho `.zip` em `projects/repositorys/flask-swagger-generator/`).
- **Testes e Build offline:** `python -B -m unittest discover -s tests -v` (`6/6` passando) e `python -m build` OK em Python `3.15.2`.

## 4. Próximos Passos / Pendências Abertas
- Configurar secret `TOKEN_CSCTRACKER` (e opcionalmente `CICD_WEBHOOK_URL`) no GitHub Actions do repositório para o workflow `notify-cicd.yml`.
- Publicar nova versão de `flask-swagger-init` no PyPI para desbloquear a **ID 94** (`CscTrackerPyCore`).
