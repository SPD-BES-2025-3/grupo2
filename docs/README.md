# Documentação Arquitetural

Este diretório consolida toda a documentação relevante do projeto, organizada para facilitar o entendimento e o acompanhamento das decisões arquiteturais, bem como da estrutura e dos principais componentes. Cada seção aborda um aspecto específico do projeto, desde decisões críticas de design até representações visuais que apoiam a arquitetura.

## Registros de Decisão Arquitetural (ADRs)

A pasta `adr` documenta as principais decisões arquiteturais tomadas ao longo do projeto, detalhando o contexto, as motivações e as consequências de cada escolha. As decisões estão organizadas da seguinte forma:

| ADR Id | Descrição | Status |
|---|---|---|
| [`adr-001`](architectural-decision-records/adr-001-uso-de-python-fastapi-e-react.md) | Justifica a escolha de FastAPI para o backend e React para o frontend. | Aprovado |
| [`adr-002`](architectural-decision-records/adr-002-uso-de-postgre-e-mongo.md) | Detalha a decisão de adotar PostgreSQL e MongoDB. | Aprovado |
| [`adr-003`](architectural-decision-records/adr-003-uso-de-alembic-para-migracoes.md) | Define o uso do Alembic para migrações do banco de dados PostgreSQL. | Aprovado |
| [`adr-004`](architectural-decision-records/adr-004-estrategia-validacao.md) | Define a estratégia de validação de dados, separando formato e existência. | Aprovado |
| [`adr-005`](architectural-decision-records/adr-005-convencao-camadas.md) | Estabelece a convenção de camadas: Controller, Service e Repository. | Aprovado |
| [`adr-006`](architectural-decision-records/adr-006-uso-dtos-schemas.md) | Define o uso de DTOs e Schemas para transferência e validação de dados. | Aprovado |
| [`adr-007`](architectural-decision-records/adr-007-uso-beanie-odm-mongodb.md) | Define o uso do ODM Beanie para interação com MongoDB. | Aprovado |
| [`adr-008`](architectural-decision-records/adr-008-servico-ocr-interno.md) | Estabelece a implementação de um serviço OCR interno ao backend. | **Obsoleto** |
| [`adr-009`](architectural-decision-records/adr-009-arquitetura-evento-mqtt-placas.md) | Define arquitetura event-driven com MQTT para processamento assíncrono de placas. | Proposto |
| [`adr-010`](architectural-decision-records/adr-010-estrategia-ocr-placas-brasileiras.md) | Estabelece estratégia híbrida de OCR para reconhecimento de placas brasileiras. | Proposto |
| [`adr-011`](architectural-decision-records/adr-011-integracao-hardware-cameras-acesso.md) | Define integração com hardware de câmeras e sistemas de controle de acesso. | Proposto |
| [`adr-012`](architectural-decision-records/adr-012-uso-docker-containerizacao.md) | Define o uso do Docker e Docker Compose para containerização dos serviços. | Aprovado |
| [`adr-013`](architectural-decision-records/adr-013-escolha-yolov8-deteccao-placas.md) | Escolha do YOLOv8 como modelo de computer vision para detecção de placas. | Aprovado |
| [`adr-014`](architectural-decision-records/adr-014-migracao-easyocr-real.md) | Migração da simulação OCR para implementação real com EasyOCR. | Aprovado |
| [`adr-015`](architectural-decision-records/adr-015-stack-frontend-vite-mui-zustand.md) | Define stack frontend com Vite, Material-UI e Zustand para gerenciamento de estado. | Aprovado |
| [`adr-016`](architectural-decision-records/adr-016-estrategia-healthchecks-microservicos.md) | Estabelece estratégia de health checks para monitoramento de serviços Docker. | Aprovado |
| [`adr-017`](architectural-decision-records/adr-017-arquitetura-pipeline-ocr-yolov8-easyocr.md) | Define arquitetura de pipeline OCR integrada com YOLOv8 e EasyOCR. | Aprovado |


## Visão Geral do Sistema de Acesso de Veículos (IA)

O projeto simula a integração entre dois sistemas para automatizar o acesso ao cinema Drive-in:

- **Sistema de Cinema Drive-in (Backend)**: Backend com funcionalidades de CRUD, processamento de imagens (IA/OCR) e validação de reservas.
- **Sistema de Catraca (Simulado)**: Sistema externo que controla câmeras e catracas físicas, interagindo com o Backend via eventos.

### Arquitetura de Integração Central

O acesso de veículos é orquestrado por um fluxo assíncrono baseado em eventos, garantindo desacoplamento entre os sistemas. O Sistema de Catraca publica eventos de chegada de veículo, que são consumidos pelo Backend para processamento e validação de acesso.

Sistema de Catraca: Captura Evento → [MQTT Broker] → Backend: Processamento IA/OCR → Validação de Reserva → Atualização de Status

### Componentes Chave no Processo de Acesso

* **Comunicação Assíncrona (MQTT):** Conforme `adr-009`, o `Sistema de Catraca` publica eventos de chegada de veículo em um tópico MQTT. O `Backend` subscreve a este tópico para processamento assíncrono, permitindo uma comunicação robusta e desacoplada.

* **Pipeline de Computer Vision (IA/OCR):** Implementado através da arquitetura integrada (`adr-017`), combinando:
  - **Detecção de Placas (YOLOv8):** Modelo de deep learning para detectar e extrair regiões de placas (`adr-013`)
  - **Reconhecimento de Texto (EasyOCR):** Extração de caracteres das placas com validação para formatos brasileiros (`adr-014`)
  - **Processamento Assíncrono:** Pipeline integrado que processa imagens em tempo real

* **Containerização (Docker):** Todos os serviços são orquestrados via Docker Compose (`adr-012`) com health checks (`adr-016`) para garantir disponibilidade e facilitar o deployment.

* **Stack Frontend Moderna:** Interface desenvolvida com Vite, Material-UI e Zustand (`adr-015`) para uma experiência de usuário moderna e responsiva.

* **Validação e Atualização de Reservas:** Após o reconhecimento da placa, o Backend busca a reserva correspondente no MongoDB. Caso a reserva seja encontrada e válida, seu status é atualizado para "finalizada", automatizando o processo de acesso.

## Diagramas

A pasta `diagrams` contém representações visuais, como fluxogramas e diagramas UML, que ajudam a ilustrar e compreender a estrutura do projeto e as interações entre seus componentes. Para detalhes sobre o fluxo de processamento de placas, consulte o Diagrama de Sequência específico.

---

Manter este documento atualizado é essencial para garantir que todos os envolvidos no projeto possam acompanhar as principais decisões e a evolução da arquitetura. Ele serve como referência central para uma comunicação clara e eficiente dentro da equipe.