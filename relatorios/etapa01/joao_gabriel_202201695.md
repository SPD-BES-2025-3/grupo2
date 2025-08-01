# Sistema de Cinema Drive-in 

#### Discente: João Gabriel Cavalcante França

## Relatório - Etapa 01

Nesta primeira etapa, atuei principalmente na implementação do backend do sistema de controle de acesso do cinema drive-in, focando na estruturação da base do backend com FastAPI e desenvolvendo um sistema completo de processamento de placas veiculares. Meu trabalho abrangeu desde a comunicação com dispositivos externos via protocolo MQTT até a implementação de serviços avançados de OCR (Reconhecimento Óptico de Caracteres) e detecção de placas usando machine learning. Também participei ativamente da definição da arquitetura geral do projeto e na documentação técnica.

Na prática, desenvolvi toda a infraestrutura crítica do sistema, incluindo a implementação de um adaptador robusto para o broker MQTT com suporte a reconexão automática, múltiplos tópicos e handlers personalizados para processamento assíncrono. Criei um pipeline completo de processamento de placas que integra detecção via YOLOv8, extração de regiões de interesse com OpenCV, e reconhecimento de texto usando EasyOCR. Além disso, desenvolvi o controlador orientado a eventos `PlateEventDrivenController` responsável por orquestrar todo o fluxo de processamento de forma assíncrona, garantindo que o sistema pudesse reagir dinamicamente aos eventos de entrada de veículos.

O trabalho evoluiu significativamente durante a etapa, partindo de uma implementação simulada do OCR para uma solução completa e funcional. Implementei a integração com EasyOCR para reconhecimento real de texto, desenvolvi um serviço de detecção de placas usando YOLOv8 e OpenCV para identificar e extrair regiões de placas em imagens completas de veículos, e criei o `PlateProcessingService` que orquestra todo o pipeline: detecção → extração → OCR → validação de clientes → verificação de reservas.

Entre os commits mais relevantes, destaco a evolução do sistema: inicialmente com a implementação básica do OCR simulado, seguida pela criação do adaptador MQTT, depois pela implementação do OCR real com EasyOCR, a adição do modelo de detecção YOLOv8, e finalmente a integração completa no `PlateEventDrivenController` e `PlateProcessingService`. Esses componentes formam um sistema end-to-end funcional para automatização do controle de acesso do cinema drive-in.

Os principais desafios técnicos enfrentados incluíram a configuração adequada do cliente MQTT (principalmente com a parte do Mosquitto no Docker, pois nunca havia configurado antes) para lidar com reconexões e múltiplos tópicos simultaneamente, a integração entre diferentes bibliotecas de machine learning (PyTorch para YOLOv8, OpenCV para processamento de imagem, EasyOCR para reconhecimento de texto), e a criação de um pipeline assíncrono eficiente que otimiza o uso de recursos computacionais ao processar apenas regiões relevantes das imagens.

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
- **Descrição:** Implementação inicial do serviço de OCR para reconhecimento de placas
- **Impacto:** Funcionalidade base para leitura automática de placas (simulada)
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
- **Descrição:** Implementação inicial do controlador orientado a eventos para processamento de placas
- **Impacto:** Base para orquestração do fluxo de processamento de eventos de placas
- **Arquivos:** 1 arquivo criado (+25 linhas)

#### 9. **Commit:** `c27cbad` - feat: Enhance OCRService with EasyOCR integration and performance testing
- **Descrição:** Substituição da simulação por implementação real usando EasyOCR
- **Impacto:** OCR funcional para reconhecimento real de texto em placas
- **Arquivos:** 1 arquivo modificado (+228 linhas, -22 linhas)
- **Funcionalidades adicionadas:**
  - Integração com biblioteca EasyOCR
  - Suporte a múltiplos idiomas (português e inglês)
  - Testes de performance e benchmark
  - Processamento otimizado de imagens

#### 10. **Commit:** `c7e197a` - feat: Add LP-detection model for license plate detection
- **Descrição:** Adição do modelo YOLOv8 para detecção de placas veiculares
- **Impacto:** Capacidade de detectar placas em imagens completas de veículos
- **Arquivos:** Modelo YOLOv8 adicionado ao projeto
- **Funcionalidades:**
  - Detecção automática de placas em imagens
  - Extração de bounding boxes
  - Modelo pré-treinado otimizado

#### 11. **Commit:** `a5244ce` - feat: Implement plate detection service using YOLOv8 and OpenCV
- **Descrição:** Implementação do serviço de detecção de placas integrando YOLOv8 e OpenCV
- **Impacto:** Pipeline completo de detecção e extração de placas
- **Arquivos:** Novo serviço PlateDetectionService criado
- **Funcionalidades:**
  - Conversão entre formatos de imagem (base64, OpenCV, PIL)
  - Detecção de placas usando YOLOv8
  - Extração de regiões de interesse
  - Pré-processamento de imagens

#### 12. **Commit:** `1c3082c` - feat: Add script to send MQTT messages with image payload
- **Descrição:** Script para teste de envio de mensagens MQTT com imagens
- **Impacto:** Ferramenta de teste e validação do sistema MQTT
- **Funcionalidades:**
  - Simulação de câmeras enviando imagens
  - Teste de payload MQTT
  - Validação de comunicação

#### 13. **Commit:** `e98373e` - feat: Add test images for vehicle plate detection
- **Descrição:** Adição de imagens de teste para validação do sistema
- **Impacto:** Base de dados para testes e desenvolvimento
- **Recursos:**
  - Imagens de veículos com placas visíveis
  - Casos de teste diversos
  - Validação de precisão do sistema

#### 14. **Commit:** `d1ad34e` - feat: Implement application lifecycle management with logging and plate processing endpoint
- **Descrição:** Implementação do gerenciamento de ciclo de vida da aplicação
- **Impacto:** Sistema robusto de inicialização e logging
- **Funcionalidades:**
  - Gerenciamento de lifecycle
  - Sistema de logging estruturado
  - Endpoints de processamento de placas

#### 15. **Commit:** `ff8df11` - feat: Implement PlateEventDrivenController for processing plate events via MQTT
- **Descrição:** Implementação completa do controlador orientado a eventos
- **Impacto:** Orquestração completa do processamento de eventos de placas
- **Funcionalidades:**
  - Processamento assíncrono via MQTT
  - Integração com todos os serviços
  - Tratamento de erros robusto

#### 16. **Commit:** `949fb5a` - feat: Add PlateProcessingService for processing plate image events and managing reservations
- **Descrição:** Implementação do serviço central de processamento de placas
- **Impacto:** Pipeline completo integrado: detecção → OCR → validação → reservas
- **Funcionalidades:**
  - Pipeline completo de processamento
  - Integração com sistema de reservas
  - Validação de clientes e reservas
  - Decisões automáticas de acesso

## Resumo Técnico

### Tecnologias Implementadas:
- **FastAPI** - Framework web assíncrono
- **MQTT** - Comunicação com dispositivos IoT
- **YOLOv8** - Detecção de objetos (placas)
- **OpenCV** - Processamento de imagens
- **EasyOCR** - Reconhecimento óptico de caracteres
- **PyTorch** - Framework de machine learning
- **MongoDB/PostgreSQL** - Persistência de dados

### Arquitetura Implementada:
1. **Camada de Comunicação** - Adaptador MQTT
2. **Camada de Processamento** - Pipeline ML (YOLOv8 + OCR)  
3. **Camada de Negócio** - Validação de clientes e reservas
4. **Camada de Controle** - Controlador orientado a eventos

### Métricas de Desenvolvimento:
- **Commits:** 16 commits principais
- **Linhas de código:** ~1.500+ linhas implementadas
- **Arquivos criados:** 15+ arquivos de código
- **Serviços implementados:** 5 serviços principais
- **Funcionalidades:** Sistema end-to-end funcional
