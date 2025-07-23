# Documentação Arquitetural

Este diretório consolida toda a documentação relevante do projeto, organizada para facilitar o entendimento e o acompanhamento das decisões arquiteturais, bem como da estrutura e dos principais componentes. Cada seção aborda um aspecto específico do projeto, desde decisões críticas de design até representações visuais que apoiam a arquitetura.

## Registros de Decisão Arquitetural (ADRs)

A pasta `adr` documenta as principais decisões arquiteturais tomadas ao longo do projeto, detalhando o contexto, as motivações e as consequências de cada escolha. As decisões estão organizadas da seguinte forma:

| ADR Id      | Descrição                                                      | Status    |
|-------------|----------------------------------------------------------------|-----------|
| [`adr-001`](adr/adr-001-uso-de-postgres-e-mongodb.md) | Detalha a decisão de adotar PostgreSQL para dados menos voláteis e MongoDB para reservas. | Aprovado  |
| [`adr-002`](adr/adr-002-uso-de-fastapi-e-react.md) | Justifica a escolha de FastAPI para o backend e React para o frontend. | Aprovado  |
| [`adr-004`](adr/adr-004-estrategia-validacao.md) | Define a estratégia de validação de dados, separando formato e existência. | Aprovado   |
| [`adr-005`](adr/adr-005-convencao-camadas.md) | Estabelece a convenção de camadas: Controller, Service e Repository. | Aprovado   |
| [`adr-006`](adr/adr-006-gerenciamento-configuracao-env.md) | Gerenciamento de configuração via arquivos .env. | Aprovado   |

## Diagramas

A pasta `diagrams` contém representações visuais, como fluxogramas e diagramas UML, que ajudam a ilustrar e compreender a estrutura do projeto e as interações entre seus componentes.

---

Manter este documento atualizado é essencial para garantir que todos os envolvidos no projeto possam acompanhar as principais decisões e a evolução da arquitetura. Ele serve como referência central para uma comunicação clara e eficiente dentro da equipe.