# Visão Geral

O projeto consiste no desenvolvimento de um sistema para gerenciamento de um cinema Drive-in, com funcionalidades como o cadastro de clientes, controle de sessões de filmes, reservas de vagas e exibição de filmes. A modelagem inicial foi baseada em um diagrama de classes que representa as principais entidades do domínio: Cliente, Filme, Gênero, Sessão, Vaga e Reserva.

## Sumário

1. [Introdução](#1-introdução)  
   1.1 [Justificativa](#11-justificativa)  
   1.2 [Descrição do Problema](#12-descrição-do-problema)  
   1.3 [Motivação](#13-motivação)

2. [Plano do Projeto](#2-plano-do-projeto)  
   2.1 [Objetivo Geral](#21-objetivo-geral)  
   2.2 [Objetivos Específicos](#22-objetivos-específicos)  
   2.3 [Tecnologias e Ferramentas Utilizadas](#23-tecnologias-e-ferramentas-utilizadas)

## 1. Introdução

### 1.1 Justificativa

Com a crescente demanda por experiências de entretenimento inovadoras e personalizadas os cinemas Drive-in voltaram a ganhar popularidade como alternativa nostálgica para o consumo de filmes. Nesse contexto, surge a necessidade de um sistema informatizado que gerencie eficientemente as sessões, reservas e ocupação de vagas em um cinema Drive-in, de forma ágil e confiável.

Sistematizar eesse processo otimiza o controle operacional do negócio e melhora a experiência do cliente final, reduzindo falhas humanas, facilitando o processo de reservas e permitindo a gestão em tempo real das sessões, veículos e vagas disponíveis.

### 1.2 Descrição do Problema

A gestão manual de cinemas Drive-in, ou qualquer sistema de reservas em geral, enfrenta diversos desafios:

- Impossibilidade de realizar reservas online e fora do horário comercial;
- Atendimento demorado e mais propício ao erro;
- Dificuldade em controlar reservas simultâneas;
- Falta de visibilidade em tempo real das vagas disponíveis;
- Impossibilidade de integrar diferentes sistemas (reserva, controle de acesso, histórico de sessões);
- Risco de conflitos ou inconsistências entre dados de clientes, sessões e filmes exibidos.

Diante desses desafios, torna-se essencial o desenvolvimento de um sistema confiável, com integração assíncrona entre seus componentes e interface amigável para a operação.

### 1.3 Motivação

O projeto é motivado por quatro principais fatores:

1. **Relevância Prática:** O desenvolvimento de um sistema para cinema Drive-in representa um problema do mundo real com múltiplas entidades, relações e operações CRUD, ideal para aplicação prática dos conhecimentos adquiridos na disciplina.

2. **Integração Tecnológica:** A utilização de múltiplas tecnologias proporciona a oportunidade de aprendizado em arquitetura de software moderna, tanto no contexto relacional quanto não relacional.

3. **Formação Profissional:** A entrega do projeto em etapas simula a realidade de desenvolvimento ágil, estimulando a organização do trabalho em grupo, uso de versionamento com Git, documentação técnica e testes.

4. **Domínio da Persistência de Dados:** O projeto permite explorar diferentes abordagens de persistência de dados, incluindo bancos relacionais com ORM e bancos NoSQL com ODM, proporcionando maior compreensão sobre modelagem de dados, operações CRUD, mapeamento objeto-relacional/documental, e estratégias de integração de dados entre sistemas.

## 2. Plano do Projeto

### 2.1 Objetivo Geral

Desenvolver um sistema para gerenciamento de um cinema Drive-in, com funcionalidades para administração de sessões, reservas, filmes, clientes e vagas. O sistema será dividido em backend, frontend e camadas de persistência, explorando tecnologias relacionais e não relacionais.

### 2.2 Objetivos Específicos

- Desenvolver uma API RESTful para gerenciar as operações do cinema (filmes, sessões, reservas, etc.).
- Criar uma interface de usuário web reativa para interação dos clientes e administradores.
- Implementar um sistema de persistência de dados robusto, utilizando a melhor abordagem para cada tipo de informação (relacional e NoSQL).
- Garantir a qualidade do código através de testes unitários e documentação técnica.

### 2.3 Sistema de Reconhecimento de Placas com IA

O projeto inclui um sistema inteligente de reconhecimento de placas veiculares que automatiza o processo de entrada no cinema Drive-in. Este sistema combina tecnologias de OCR (Optical Character Recognition) com processamento assíncrono via MQTT para proporcionar uma experiência fluida aos clientes.

**Características Principais:**
- **OCR Inteligente**: Reconhecimento automático de placas brasileiras (formatos antigo e Mercosul)
- **Processamento Assíncrono**: Integração via MQTT para comunicação em tempo real entre câmeras e sistema
- **Validação Automática**: Verificação de formato e associação com reservas existentes
- **Controle de Acesso**: Liberação automática baseada na validação da placa detectada

**Fluxo de Funcionamento:**
1. Câmera na entrada captura imagem do veículo
2. Sistema OCR processa a imagem e extrai a placa
3. Placa é validada contra reservas ativas via MQTT
4. Acesso é liberado automaticamente se reserva válida for encontrada
5. Logs detalhados são mantidos para auditoria

### 2.4 Arquitetura e Decisões Técnicas

As principais decisões arquiteturais, incluindo a escolha de tecnologias, padrões e estratégias, estão documentadas em `Architectural Decision Records` (ADRs). Essa documentação centraliza o contexto, as justificativas e as consequências de cada escolha importante feita no projeto.

Para detalhes sobre a stack (FastAPI, React, PostgreSQL, MongoDB, etc.) e outras decisões, consulte a [**Documentação Arquitetural**](docs/README.md).

## 3. Cronograma de Desenvolvimento

|Iteração|Descrição|Data Início|Data Fim|Responsável|Situação|
|---|---|---|---|---|---|
|1|Configuração inicial do projeto e estrutura base|16/07/2025|17/07/2025|João|✅ Concluído|
|2|Modelagem de dados e diagramas UML|17/07/2025|19/07/2025|Mauro/José|✅ Concluído|
|3|Setup do ambiente e configuração de banco de dados|19/07/2025|20/07/2025|Joseppe|✅ Concluído|
|4|Implementação do CRUD de Clientes|20/07/2025|21/07/2025|Joseppe|✅ Concluído|
|5|Sistema de OCR e integração MQTT|21/07/2025|21/07/2025|João|✅ Concluído|
|6|Implementação do módulo de Filmes e Gêneros|21/07/2025|22/07/2025|Mauro|✅ Concluído|
|7|Desenvolvimento do Frontend React|21/07/2025|21/07/2025|Felipe|✅ Concluído|
|8|Implementação do CRUD de Sessões|22/07/2025|22/07/2025|Mauro|✅ Concluído|
|9|Configuração final de migrações Alembic|22/07/2025|22/07/2025|Joseppe/Mauro|✅ Concluído|
|10|Implementação do CRUD de Reservas|22/07/2025|23/07/2025|Mauro|✅ Concluído|
|11|Sistema de Reconhecimento de Placas com IA|22/07/2025|27/07/2025|João|⏳ Pendente|
|11.1|• Implementação do OCR Service com validação brasileira|22/07/2025|24/07/2025|João|⏳ Pendente|
|11.2|• Integração MQTT para eventos assíncronos|24/07/2025|25/07/2025|João|⏳ Pendente|
|11.3|• Simuladores de hardware e testes de integração|25/07/2025|27/07/2025|João|⏳ Pendente|
|12|Implementação do middleware|22/07/2025|27/07/2025|Indefinido|⏳ Pendente|
|13|Finalização do Frontend|22/07/2025|27/07/2025|Felipe|⏳ Pendente|
|14|Dockerização completa do projeto|22/07/2025|28/07/2025|Joseppe|⏳ Pendente|
|15|Hospedagem na OCI(Oracle Cloud Infrastructure)|22/07/2025|28/07/2025|Joseppe|⏳ Pendente|

## 4. Como Rodar o Projeto

### 4.1 Pré-requisitos

Para executar este projeto, é necessário ter instalado em sua máquina:

- **Git**: Para clonar o repositório
- **Docker**: Para orquestração dos containers do projeto

### 4.2 Instruções de Execução

Execute os seguintes comandos, em ordem, para inicializar o projeto:

```bash

# 1. Clone o repositório
git clone https://github.com/SPD-BES-2025-3/grupo2.git

# 2. Navegue até o diretório do projeto
cd grupo2

# 3. Inicie o projeto com Docker Compose
docker compose up -d --build

```

Após executar esses comandos, o sistema estará disponível em `http://localhost:8000`.

### 4.3 Executando os Testes Unitários

O projeto inclui uma suíte completa de testes unitários para validar as operações CRUD de todas as entidades do sistema. Para executar os testes:

```bash
# 1. Navegue até o diretório de testes do backend
cd backend-cinema/tests

# 2. Execute todos os testes unitários
python run_all_tests.py
```

**Cobertura dos Testes:**

- **Cliente Service**: 10 testes CRUD (CREATE, READ, UPDATE, DELETE)
- **Filme Service**: 9 testes CRUD com validações de título e dados
- **Sessão Service**: 11 testes CRUD incluindo validações de filme e horário
- **Reserva Service**: 8 testes CRUD assíncronos com validações de cliente/sessão

**Total**: 38 testes cobrindo todos os cenários essenciais (sucesso, erro, validações).

### 4.4 Acessando a Documentação da API

O FastAPI gera automaticamente a documentação interativa da API. Após iniciar o servidor, você pode acessar:

- **Swagger UI**: `http://localhost:8000/docs` - Interface interativa para testar os endpoints
- **ReDoc**: `http://localhost:8000/redoc` - Documentação detalhada da API
