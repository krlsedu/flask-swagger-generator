Release Notes - v26.47.001

Abaixo estão as notas de atualização para a versão v26.47.001. Esta versão concentra-se na modernização da infraestrutura do projeto através da atualização do ambiente de suporte para Python 3.15 e da transição para a versão v4 das dependências e esteiras. Além disso, foram introduzidas melhorias na geração e validação de especificações OpenAPI v3, expansão da suíte de testes unitários e atualização das diretrizes e fluxos de automação CI/CD.

## 🚀 Features
*(Nenhuma alteração desta categoria nesta versão)*

## 🐛 Fixes
*(Nenhuma alteração desta categoria nesta versão)*

## 🔧 Chore
* **Ambiente e Compatibilidade:** Atualização de compatibilidade do projeto para suporte ao runtime Python 3.15 e avanço para a versão principal v4 do ecossistema de dependências (`requirements.txt`, `requirements-test.txt` e `setup.py`). A alteração abrange refatorações nos componentes do gerador OpenAPI v3 (`schema_attribute.py`, `schemas.py` e `swagger_view.py`) para garantir conformidade de tipagem e serialização, adição de novos testes para visualização do Swagger (`test_swagger_view.py`), alinhamento dos contratos YAML de teste e reestruturação dos pipelines de automação e notificação CI/CD (`.github/workflows/build.yml` e `.github/workflows/notify-cicd.yml`), mitigando débitos técnicos e prevenindo incompatibilidades futuras (`setup.py`).
  * *Commit: `9030a3d` | Autor: @krlsedu*