Release Notes - v26.47.002

Abaixo estão as notas de atualização para a versão v26.47.002. Esta versão tem como foco aprimorar o processo de empacotamento e distribuição do projeto por meio da configuração explícita de inclusão de arquivos estáticos e de suporte no artefato de build. Além disso, foram atualizados os registros de contexto operacional e documentação interna de engenharia para assegurar a consistência dos processos de deploy e desenvolvimento contínuo.

## 🚀 Features
*(Nenhuma alteração desta categoria nesta versão)*

## 🐛 Fixes
*(Nenhuma alteração desta categoria nesta versão)*

## 🔧 Chore
* **Build & Packaging:** Implementação do arquivo de manifesto de distribuição (`MANIFEST.in`) e ajuste de versionamento no `setup.cfg`, garantindo que arquivos estáticos, templates e artefatos de documentação necessários sejam devidamente empacotados na geração do pacote distribuível (sdist/wheel). A alteração previne falhas de dependência em tempo de execução causadas pela ausência de arquivos não Python no artefato final, complementando a mudança com o alinhamento das documentações de handoff e contexto em `.ai-memory/` (`MANIFEST.in`).
  * *Commit: `8803b61` | Autor: @krlsedu*