---
project: flask-swagger-generator
kind: decisions
tier: semantic
pinned: true
updated_at: 2026-11-21
---

# 🏛️ Decisões Arquiteturais — `flask-swagger-generator` (`flask-swagger-init`)

## Cláusulas Pétreas `[PINNED]`
- **Suporte Mínimo Python `>=3.11` (Validado até `3.15`):** `setup.py` exige `python_requires=">=3.11"` (alinhado a `marshmallow 4.x`) e o CI constrói e testa em Python `3.15`.
- **Compatibilidade `marshmallow` v4 (`metadata={"example": ...}`):** Em `SwaggerView.__create_schema_from_class`, exemplos nos campos `marshmallow.fields` DEVEM ser declarados via `metadata={"example": ...}` (nunca via kwarg `example=...`, removido no `marshmallow 4.x`), e `SwaggerMashmallowSchema` deve ler `field.schema` / `field.inner.schema` e tratar `example is None`.
- **Testes Offline com `unittest`:** Não usar `Flask-Testing` (incompatível com Flask 3.x); executar a suíte via `python -B -m unittest discover -s tests -v`.
