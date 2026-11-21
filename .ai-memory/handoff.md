---
project: flask-swagger-generator
kind: handoff
tier: working
updated_at: 2026-11-21
---

# 🤝 Handoff Ativo — `flask-swagger-generator`

> **Escopo do Projeto:** Biblioteca `flask-swagger-init` no PyPI para geração automática de especificação OpenAPI 3.0 e publicação da Swagger UI para aplicações Flask.

## 1. Onde Paramos / Contexto Atual (`WIP`)
- **[2026-11-21] Implementação da ID 95 (`Por Publicar`, `6/6` testes offline OK em Python `3.15.2`):**
  - Atualizado `requirements.txt` (`flask>=3.1,<4`, `marshmallow>=3.13,<5`, `flask-swagger-ui>=4.11,<6`), removido `setuptools` de runtime e atualizado `requirements-test.txt`.
  - Atualizado `setup.py` para `python_requires=">=3.11"`, `encoding="utf-8"` e classifiers `3.11`–`3.15`.
  - Corrigida compatibilidade com `marshmallow 4.x` e literais de array em `swagger_view.py` (`metadata={"example": ...}`), `schemas.py` (`field.schema`, `field.inner.schema`, `if val is None: return None`) e `schema_attribute.py` (`self.value[0]` para listas não vazias + guarda `and self.reference`).
  - Migrados os testes de `Flask-Testing` para `unittest.TestCase`, alinhada a linha `version: 1.0.0.` nas 5 fixtures YAML, adicionado `test_swagger_view.py`, atualizado `.github/workflows/build.yml` (Python `3.15` + testes) e provisionados `.agents/`, `.ai-memory/`, `.junie/` e `notify-cicd.yml`.

## 2. Tentativas Descartadas / O que Falhou (`Failed Approaches`)
- *(Nenhuma pendência ativa — todas as incompatibilidades de `marshmallow` v4 e fixtures foram resolvidas).*

## 3. Estado dos Arquivos / Branch / Build
- **Fonte Primária:** GitHub (`main`, com espelho `.zip` em `projects/repositorys/flask-swagger-generator/`).
- **Testes offline:** `python -B -m unittest discover -s tests -v` (`6/6` passando em Python `3.15.2`).

## 4. Próximos Passos / Pendências Abertas
- Configurar secret `TOKEN_CSCTRACKER` (e opcionalmente `CICD_WEBHOOK_URL`) no GitHub Actions do repositório para o workflow `notify-cicd.yml`.
- Publicar nova versão de `flask-swagger-init` no PyPI para desbloquear a **ID 94** (`CscTrackerPyCore`).
