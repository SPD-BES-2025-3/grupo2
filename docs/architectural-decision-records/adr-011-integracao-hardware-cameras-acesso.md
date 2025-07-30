# ADR-011: Simulação de Integração com Sistema de Catraca

**Status:** Conceitual (Simulação)

## Contexto

O projeto do cinema Drive-in tem como objetivo principal o desenvolvimento do Backend (Sistema de Cinema Drive-in) que interage com um sistema externo (Sistema de Catraca) responsável por câmeras e catracas físicas. Para fins do trabalho acadêmico e para permitir o desenvolvimento do Sistema de Cinema Drive-in sem a necessidade de hardware real, é preciso definir como essa integração será simulada.

## Decisão

Implementar uma **simulação da integração** entre o Sistema de Catraca (Sistema externo) e o Sistema de Cinema Drive-in (Backend) utilizando **MQTT** como protocolo de comunicação.

-   **Sistema de Cinema Drive-in (Backend - Nosso Foco):**
    -   CRUD completo das entidades (Filmes, Sessões, Clientes, Reservas).
    -   Consumirá mensagens MQTT publicadas pelo sistema simulado.
    -   Realizará o processamento de IA/OCR para detecção de placas e validação de reservas no MongoDB.
    -   Atualizará o status da reserva para "finalizada" e poderá enviar uma resposta de acesso.
-   **Sistema de Catraca (Simulado - Não construído):**
    -   Representará o hardware físico (câmeras/catracas).
    -   Publicará mensagens MQTT simulando eventos de chegada de veículos (com imagem em base64 da placa frontal).

## Alternativas Consideradas

1.  **Integração Real com Hardware**: Conectar diretamente com câmeras/catracas físicas (descartado por complexidade e escopo acadêmico).
2.  **Sistema Monolítico**: Incluir controle de hardware dentro do Sistema de Cinema Drive-in (descartado para simular arquitetura distribuída).
3.  **Simulação via MQTT**: Simular o Sistema de Catraca externo via MQTT (escolha atual).
4.  **Mock Local**: Simular entrada de dados diretamente no backend sem comunicação externa (descartado para maior realismo na comunicação assíncrona).

## Consequências

### Pontos Positivos

-   **Foco Acadêmico**: Permite concentrar os esforços no desenvolvimento do Sistema de Cinema Drive-in (CRUD, IA, validações) sem a complexidade de hardware.
-   **Realismo Arquitetural**: Simula uma arquitetura real de sistemas distribuídos e comunicação assíncrona.
-   **Flexibilidade**: O uso de MQTT permite fácil substituição por um sistema de hardware real no futuro, se necessário.
-   **Testabilidade**: Facilita a criação de diferentes cenários de teste para o processamento de eventos de placa.
-   **Aprendizado**: Proporciona experiência prática com comunicação assíncrona e processamento de IA em um cenário de integração.

### Pontos Negativos

-   **Abstração do Hardware**: Não há integração real com hardware físico, limitando alguns testes de ponta a ponta.
-   **Dependência da Simulação**: Para testes completos, o sistema de simulação do Sistema de Catraca precisa estar funcional.
-   **Complexidade Adicional**: A camada MQTT adiciona uma complexidade que não existiria em uma versão puramente local ou síncrona.

## Detalhes de Implementação

### Estrutura da Mensagem MQTT (Sistema de Catraca → Backend)
*(Para detalhes da estrutura da mensagem, consulte o `README.md` arquitetural ou o Diagrama de Sequência do fluxo de placas.)*