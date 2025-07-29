# Documentação Arquitetural

Este diretório consolida toda a documentação relevante do projeto, organizada para facilitar o entendimento e o acompanhamento das decisões arquiteturais, bem como da estrutura e dos principais componentes. Cada seção aborda um aspecto específico do projeto, desde decisões críticas de design até representações visuais que apoiam a arquitetura.

## Registros de Decisão Arquitetural (ADRs)

A pasta `adr` documenta as principais decisões arquiteturais tomadas ao longo do projeto, detalhando o contexto, as motivações e as consequências de cada escolha. As decisões estão organizadas da seguinte forma:

| ADR Id      | Descrição                                                      | Status    |
|-------------|----------------------------------------------------------------|-----------|
| [`adr-001`](architectural-decision-records/adr-001-uso-de-python-fastapi-e-react.md) | Justifica a escolha de FastAPI para o backend e React para o frontend. | Aprovado  |
| [`adr-002`](architectural-decision-records/adr-002-uso-de-postgre-e-mongo.md) | Detalha a decisão de adotar PostgreSQL e MongoDB. | Aprovado  |
| [`adr-003`](architectural-decision-records/adr-003-uso-de-alembic-para-migracoes.md) | Define o uso do Alembic para migrações do banco de dados PostgreSQL. | Aprovado  |
| [`adr-004`](architectural-decision-records/adr-004-estrategia-validacao.md) | Define a estratégia de validação de dados, separando formato e existência. | Aprovado  |
| [`adr-005`](architectural-decision-records/adr-005-convencao-camadas.md) | Estabelece a convenção de camadas: Controller, Service e Repository. | Aprovado  |
| [`adr-006`](architectural-decision-records/adr-006-uso-dtos-schemas.md) | Define o uso de DTOs e Schemas para transferência e validação de dados. | Aprovado  |
| [`adr-007`](architectural-decision-records/adr-007-uso-beanie-odm-mongodb.md) | Define o uso do ODM Beanie para interação com MongoDB. | Aprovado  |
| [`adr-008`](architectural-decision-records/adr-008-servico-ocr-interno.md) | Estabelece a implementação de um serviço OCR interno ao backend. | Aprovado  |
| [`adr-009`](architectural-decision-records/adr-009-arquitetura-evento-mqtt-placas.md) | Define arquitetura event-driven com MQTT para processamento assíncrono de placas. | Proposto   |
| [`adr-010`](architectural-decision-records/adr-010-estrategia-ocr-placas-brasileiras.md) | Estabelece estratégia híbrida de OCR para reconhecimento de placas brasileiras. | Proposto   |
| [`adr-011`](architectural-decision-records/adr-011-integracao-hardware-cameras-acesso.md) | Define integração com hardware de câmeras e sistemas de controle de acesso. | Proposto   |

## Sistema de Reconhecimento de Placas com IA

O projeto inclui um sistema inteligente de reconhecimento de placas que representa uma das principais inovações técnicas do cinema Drive-in. Este sistema combina múltiplas tecnologias para automatizar completamente o processo de entrada:

### Componentes Principais

**OCR Service (`adr-008`, `adr-010`):**
- Reconhecimento de placas brasileiras (formatos antigo e Mercosul)
- Estratégia híbrida com múltiplos provedores de OCR
- Validação automática de formato e score de confiança
- Processamento assíncrono com fallback para maior robustez

**Arquitetura Event-Driven (`adr-009`):**
- Comunicação assíncrona via MQTT entre componentes
- Processamento em tempo real de eventos de placa
- Desacoplamento entre captura, processamento e validação
- Tolerância a falhas e escalabilidade horizontal

**Integração de Hardware (`adr-011`):**
- Interface padronizada para câmeras de diferentes fabricantes
- Controle automatizado de cancelas e sistemas de acesso
- Monitoramento em tempo real via dashboard
- Simuladores para desenvolvimento e testes

### Fluxo Técnico

```
Câmera → [MQTT] → OCR Service → [MQTT] → Validation Service → [MQTT] → Access Control
    ↓                ↓                        ↓                        ↓
Captura         Processa              Valida Reserva           Libera Acesso
Imagem           Placa                                        
```

Este sistema foi projetado para ser facilmente extensível, permitindo a adição de novos algoritmos de IA, integração com diferentes fornecedores de OCR e expansão para múltiplos pontos de entrada.

## Diagramas

A pasta `diagrams` contém representações visuais, como fluxogramas e diagramas UML, que ajudam a ilustrar e compreender a estrutura do projeto e as interações entre seus componentes.

---

Manter este documento atualizado é essencial para garantir que todos os envolvidos no projeto possam acompanhar as principais decisões e a evolução da arquitetura. Ele serve como referência central para uma comunicação clara e eficiente dentro da equipe.