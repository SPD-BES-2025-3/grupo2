# Sistema de Cinema Drive-in 

#### Discente: Mauro Sérgio

## Relatório - Versão final

Durante esta etapa, meu papel foi central na **arquitetura e documentação** do sistema de cinema drive-in, atuando como responsável pela modelagem técnica, decisões arquiteturais e estruturação da base do backend. Minhas contribuições focaram em três frentes principais:

### 🏗️ **Arquitetura e Documentação Técnica**
Liderei a criação e evolução da documentação arquitetural, incluindo diagramas UML, ADRs (Architecture Decision Records) e estruturação técnica do projeto. Fui responsável por estabelecer padrões de desenvolvimento e documentar decisões críticas.

### 🎬 **Modelagem de Domínio e Backend**  
Implementei a modelagem completa do domínio de filmes, sessões e reservas, configurando a infraestrutura de dados com ORM/ODM dual (PostgreSQL + MongoDB) e estabelecendo os padrões de desenvolvimento do backend.

### 🚗 **Sistema de Reconhecimento de Placas (IA/OCR)**
Contribuí significativamente na **documentação e comunicação técnica** do sistema de computer vision, traduzindo as decisões do especialista em IA em documentação clara e acessível para toda a equipe. Meu foco foi facilitar o entendimento e manutenção futura do sistema.

## Principais Contribuições por Área

### 1. 📐 **Arquitetura e Documentação (Jul 17-30)**
**Commits:** `476b686`, `3814a42`, `c4fb8c1`, `5b33291`, `6988aec`, `1a99ec1`, `337d590`, `dff6647`, `d1d35ca`

- **Criação da documentação arquitetural completa:** Desenvolvi todos os diagramas UML (classes, containers, sequência) que definem a estrutura do sistema
- **Estabelecimento de ADRs:** Documentei e aprovei decisões arquiteturais críticas (ADRs 1-16), incluindo stack tecnológica, padrões de desenvolvimento e arquitetura de microserviços
- **Definição da arquitetura de containerização:** Especifiquei a estratégia Docker com health checks e orquestração via Docker Compose
- **Documentação do sistema de placas:** Elaborei diagramas de sequência específicos para o pipeline OCR/IA, facilitando o entendimento do fluxo complexo

### 2. 🎬 **Modelagem de Domínio e Backend (Jul 20-24)**
**Commits:** `253b88f`, `ed34550`, `5cf2a7d`, `dc6cd91`, `996831799`, `7896cc74`, `40f5c55`

- **Modelagem da entidade Filme:** Implementei modelo completo com suporte a múltiplos gêneros, classificação etária e metadados
- **Configuração dual ORM/ODM:** Estabeleci integração PostgreSQL (SQLAlchemy) + MongoDB (Beanie) para dados relacionais e documentos
- **Sistema de sessões e reservas:** Modelei entidades complexas com relacionamentos e validações de negócio
- **Migrações automáticas:** Configurei Alembic para versionamento e evolução do schema do banco relacional
- **APIs REST completas:** Implementei endpoints CRUD com validação, paginação e tratamento de erros

### 3. 🚗 **Sistema de Reconhecimento de Placas (Jul 28-30)**
**Commits:** `6fcc1bf`, `ec6af12`, `46fdc6b`, `337d590`, `d1d35ca`

- **Documentação da arquitetura OCR:** Traduzi as decisões técnicas do especialista em IA em documentação clara do pipeline YOLOv8 → EasyOCR → Validação
- **Especificação da integração MQTT:** Documentei a arquitetura event-driven para processamento assíncrono de imagens, facilitando a implementação
- **Diagramas de sequência especializados:** Criei representações visuais do fluxo OCR/MQTT para comunicação eficaz com a equipe

### 4. 🖥️ **Stack Frontend e DevOps (Jul 30)**
**Commits:** `dff6647`, `d1d35ca`

- **Definição da stack frontend:** Documentei decisão por Vite + Material-UI + Zustand para interface moderna
- **Estratégia de health checks:** Estabeleci monitoramento de serviços Docker para garantir disponibilidade
- **Organização da documentação:** Estruturei documentação técnica para facilitar manutenção e onboarding

## Impacto Técnico e Resultados

### 🎯 **Entregas Principais**
- **16 ADRs aprovadas** documentando decisões arquiteturais críticas
- **3 diagramas UML completos** (classes, containers, sequência OCR)
- **Arquitetura dual de dados** PostgreSQL + MongoDB funcional
- **Documentação técnica do pipeline OCR/IA** facilitando compreensão e manutenção
- **Backend base estruturado** com padrões de desenvolvimento estabelecidos

### 🔄 **Metodologia de Trabalho**
- **Documentação como código:** Todas as decisões arquiteturais foram formalizadas via ADRs
- **Arquitetura evolutiva:** Diagramas e documentação atualizados conforme evolução do sistema
- **Padrões consistentes:** Estabeleci convenções de camadas (Controller → Service → Repository)
- **Versionamento de schema:** Configurei migrações automáticas para evolução do banco
