# ADR-009: Arquitetura Event-Driven com MQTT para Processamento de Placas

**Status:** Aprovado

## Contexto

O Sistema de Cinema Drive-in (Backend) precisa receber mensagens assíncronas de um Sistema de Catraca (externo) que controla câmeras e catracas físicas. Quando um veículo chega, o Sistema de Catraca envia uma imagem em base64 via MQTT. O Backend deve processar essa imagem com IA/OCR, extrair a placa, validar contra reservas no MongoDB e atualizar o status da reserva para "finalizada".

## Decisão

Implementar uma arquitetura event-driven usando **MQTT** para a comunicação entre o Sistema de Catraca e o Backend.
-   **Sistema de Catraca (simulado)**: Publica eventos de chegada de veículos via MQTT.
-   **Sistema de Cinema Drive-in (Backend)**: Subscreve a esses eventos, orquestra o processamento IA/OCR e a atualização de reservas.

## Alternativas Consideradas

1.  **HTTP REST API síncrona**: Comunicação direta entre câmeras e backend.
2.  **Filas tradicionais (RabbitMQ/SQS)**: Processamento via filas de mensagens.
3.  **MQTT Pub/Sub**: Comunicação assíncrona via tópicos especializados (escolhida).

## Consequências

### Pontos Positivos

-   **Desacoplamento**: Câmeras, serviço de processamento e validação funcionam independentemente.
-   **Tempo Real/Baixa Latência**: MQTT proporciona comunicação de baixa latência, adequada para eventos de portaria.
-   **Escalabilidade**: Múltiplas câmeras podem publicar simultaneamente, e múltiplos consumidores podem ser adicionados.
-   **Tolerância a Falhas**: O sistema continua funcionando mesmo com componentes offline temporariamente, com mensagens persistindo no broker.
-   **Flexibilidade**: Fácil adição de novos tipos de eventos e processadores.

### Pontos Negativos

-   **Complexidade**: Adiciona uma camada de comunicação assíncrona.
-   **Debugging**: Fluxo assíncrono pode ser mais difícil de rastrear.
-   **Dependência Externa**: Requer um broker MQTT funcional e configurado.
-   **Garantias de Entrega**: Necessita configuração adequada de QoS (Quality of Service) para garantir entrega de mensagens.

## Detalhes de Implementação

### Tópicos MQTT
-   `cinema/plates/images`: Sistema de Catraca publica chegada de veículo com imagem.
-   `cinema/plates/acess`: Backend pode responder com o resultado da validação (opcional, para controle da catraca).
