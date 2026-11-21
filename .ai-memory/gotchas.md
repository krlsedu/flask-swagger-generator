---
project: flask-swagger-generator
kind: gotchas
tier: semantic
updated_at: 2026-11-21
---

# ⚠️ Armadilhas Conhecidas (`Gotchas`) — `flask-swagger-generator`

- **Kwarg `example=` removido no `marshmallow` v4:** `fields.String(example=...)` lança `TypeError` em `marshmallow>=4.0`. Usar `metadata={"example": ...}` (compatível com `3.13+` e `4.x`).
- **`fields.Nested.nested` e `val is None`:** Em schemas Marshmallow sem `metadata["example"]`, `get_example_value` recebia `None` e falhava em `int(None)` / `"None"`; além disso, `field.schema` é a interface segura para extrair o schema aninhado na v4.
- **`Flask-Testing` incompatível com Flask 3.x:** `flask_testing` quebra em `Flask 3.1+` e deve permanecer fora de `requirements-test.txt`.
