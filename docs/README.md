# Documentação Arquitetural

Este diretório consolida toda a documentação relevante do projeto, organizada para facilitar o entendimento e o acompanhamento das decisões arquiteturais, bem como da estrutura e dos principais componentes. Cada seção aborda um aspecto específico do projeto, desde decisões críticas de design até representações visuais que apoiam a arquitetura.

## Registros de Decisão Arquitetural (ADRs)

A pasta `adr` documenta as principais decisões arquiteturais tomadas ao longo do projeto, detalhando o contexto, as motivações e as consequências de cada escolha. As decisões estão organizadas da seguinte forma:

| ADR Id      | Descrição                                                      | Status    |
|-------------|----------------------------------------------------------------|-----------|
| `adr-001` | Justifica a escolha de FastAPI para o backend e React para o frontend. | Aprovado  |
| `adr-002` | Detalha a decisão de adotar PostgreSQL e MongoDB. | Aprovado  |
| `adr-003` | Define o uso do Alembic para migrações do banco de dados PostgreSQL. | Aprovado  |
| `adr-004` | Define a estratégia de validação de dados, separando formato e existência. | Aprovado  |
| `adr-005` | Estabelece a convenção de camadas: Controller, Service e Repository. | Aprovado  |
| `adr-006` | Define o uso de DTOs e Schemas para transferência e validação de dados. | Aprovado  |
| `adr-007` | Define o uso do ODM Beanie para interação com MongoDB. | Aprovado  |
| `adr-008` | Estabelece a implementação de um serviço OCR interno ao backend. | Aprovado  |

## Diagramas

A pasta `diagrams` contém representações visuais, como fluxogramas e diagramas UML, que ajudam a ilustrar e compreender a estrutura do projeto e as interações entre seus componentes.

---

Manter este documento atualizado é essencial para garantir que todos os envolvidos no projeto possam acompanhar as principais decisões e a evolução da arquitetura. Ele serve como referência central para uma comunicação clara e eficiente dentro da equipe.