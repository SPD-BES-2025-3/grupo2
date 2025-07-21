# Sistema de Cinema Drive-in 

#### Discente: João Gabel Cavalcante França

## Relatório - Etapa 01


Nesta primeira etapa, atuei principalmente na implementação do backend do sistema de controle de acesso do cinema drive-in, designei-me para estruturar a base do backend com FastAPI e trabalhar na comunicação com dispositivos externos por meio do protocolo MQTT, além de desenvolver um serviço de OCR (Reconhecimento Optico de Caracteres) para identificação de placas de veículos. Também tive participação na definição da arquitetura geral do projeto e na documentação.

Na prática, executei boa parte da infraestrutura do sistema, incluindo a implementação de um adaptador robusto para o broker MQTT, com suporte a reconexão, múltiplos tópicos e handlers personalizados. Desenvolvi também o serviço de OCR, com validação de placas brasileiras por meio de expressões regulares, simulando o comportamento de um reconhecimento real sem depender de serviços externos como Google Vision ou AWS - pelo menos, por enquanto. Além disso, criei o controlador orientado a eventos ```EventDrivenController``` responsável por integrar esses dois serviços (OCR e MQTT) de forma assíncrona, garantindo que o sistema pudesse reagir dinamicamente aos eventos de entrada.

Entre os commits mais relevantes, destaco três: o primeiro foi a implementação completa do serviço de OCR, com tratamento assíncrono e validação de placas; o segundo, a criação do adaptador de infraestrutura para MQTT; e o terceiro, o controlador orientado a eventos, que conecta todos os elementos anteriores. Esses três componentes formam a espinha dorsal do backend atual (não finalizado, depois preciso incluir na main, quando finalizar).

Embora tenha conseguido entregar os principais módulos funcionais, alguns pontos ficaram pendentes. Não consegui implementar testes automatizados para TODOS os módulos desenvolvidos (MQTT-Broker), nem atualizar a documentação da API com as novas classes e endpoints. Além disso, enfrentei desafios técnicos, principalmente na configuração do cliente MQTT para lidar com reconexões e múltiplos tópicos, bem como na estruturação da comunicação assíncrona entre os serviços. Para as próximas etapas, espero finalizar a implementação do sistema de detecção de placas integrado ao OCR finalizado e desenvolver o restante das classes.

## Histórico de Commits

#### 1. **Commit:** `25ce7d3` - Update .gitignore
- **Descrição:** Atualização do arquivo .gitignore para incluir arquivos Python, ambiente e IDE
- **Impacto:** Melhoria na organização do repositório
- **Arquivos:** 1 arquivo modificado (+179 linhas, -18 linhas)

#### 2. **Commit:** `6fd083f` - init backend project
- **Descrição:** Inicialização da estrutura base do projeto backend
- **Impacto:** Criação da arquitetura fundamental do projeto
- **Arquivos:** 10 arquivos criados (+82 linhas)
- **Estrutura criada:**
  - Sistema de configuração
  - Estrutura MVC (controllers, models, services, views)
  - Arquivo principal main.py

#### 3. **Commit:** `0caa4fe` - Add PlateImageEvent model
- **Descrição:** Implementação do modelo para eventos de imagem de placas via MQTT
- **Impacto:** Base para processamento de eventos de reconhecimento de placas
- **Arquivos:** 1 arquivo criado (+40 linhas)

#### 4. **Commit:** `e9d49bc` - feat(dto): Add Gate model
- **Descrição:** Adição do modelo Gate para controle de acesso do cinema
- **Impacto:** Estrutura para gerenciamento de portões/entradas
- **Arquivos:** 1 arquivo criado (+32 linhas)

#### 5. **Commit:** `07f6e78` - feat(ocr): Implement OCR service
- **Descrição:** Implementação completa do serviço de OCR para reconhecimento de placas
- **Impacto:** Funcionalidade core para leitura automática de placas
- **Arquivos:** 1 arquivo criado (+115 linhas)
- **Funcionalidades:**
  - Processamento de imagens
  - Validação de placas brasileiras
  - Tratamento de erros

#### 6. **Commit:** `7a4cac4` - feat(infra-adapters): Implement MQTT broker adapter
- **Descrição:** Implementação do adaptador MQTT com conexão e tratamento de mensagens
- **Impacto:** Infraestrutura para comunicação via MQTT
- **Arquivos:** 2 arquivos modificados (+141 linhas, -1 linha)
- **Funcionalidades:**
  - Conexão com broker MQTT
  - Publicação e subscrição de mensagens
  - Tratamento de reconexão

#### 7. **Commit:** `d813281` - feat(config): Add MQTT configuration
- **Descrição:** Adição de configurações MQTT ao ConfigManager
- **Impacto:** Suporte a configurações MQTT centralizadas
- **Arquivos:** 2 arquivos modificados (+12 linhas, -2 linhas)

#### 8. **Commit:** `91f4a36` - feat(controller): Implement PlateEventDrivenController
- **Descrição:** Implementação do controlador orientado a eventos para processamento de placas
- **Impacto:** Orquestração do fluxo de processamento de eventos de placas
- **Arquivos:** 1 arquivo criado (+25 linhas)
