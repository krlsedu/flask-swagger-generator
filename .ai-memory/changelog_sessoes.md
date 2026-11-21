---
project: flask-swagger-generator
kind: changelog
tier: episodic
updated_at: 2026-11-21
---

# 📜 Changelog de Sessões — `flask-swagger-generator`

## 2026-11-21 — ID 95: Suporte ao Python 3.15, `marshmallow` v4, `flask` 3.1+ e CI Moderno
- Liberadas dependências para `flask>=3.1,<4`, `marshmallow>=3.13,<5`, `flask-swagger-ui>=4.11,<6` e removido `setuptools` de runtime.
- Migrado `SwaggerView` para `metadata={"example": ...}`, corrigido `SwaggerMashmallowSchema` para `marshmallow 4.x`, removida dependência de `Flask-Testing` nos testes e adicionado `test_swagger_view.py`.
- Atualizado `.github/workflows/build.yml` para Python `3.15` com execução da suíte de testes e provisionada governança (`/csctracker`).
- Adicionado `MANIFEST.in` (`version.py`, `version.txt`, `requirements.txt`, `README.md`, `LICENSE`) e ajustado `description_file = README.md` no `setup.cfg` após falha de build na tag `v26.47.001`, validado localmente com `python -m build` em Python `3.15.2`.
