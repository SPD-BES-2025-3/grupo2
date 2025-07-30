# ADR-009: Arquitetura Event-Driven com MQTT para Processamento de Placas

**Status:** Proposto

**Data:** 2025-07-29

## Contexto

O sistema de cinema Drive-in (Sistema 1) precisa receber mensagens assíncronas de um sistema externo (Sistema 2) que controla câmeras e catracas. Quando um veículo chega, o Sistema 2 envia uma imagem em base64 via MQTT. O Sistema 1 deve processar essa imagem com IA/OCR, extrair a placa, validar contra reservas no MongoDB e atualizar o status da reserva para "finalizada".

## Decisão

Implementar uma arquitetura event-driven usando MQTT onde:
- **Sistema 2** (não construído): Publica eventos de chegada de veículos  
- **Sistema 1** (nosso foco): Subscreve eventos, processa IA/OCR e atualiza reservas

## Alternativas Consideradas

1. **HTTP REST API síncrona**: Comunicação direta entre câmeras e backend
2. **Filas tradicionais (RabbitMQ/SQS)**: Processamento via filas de mensagens
3. **MQTT Pub/Sub**: Comunicação assíncrona via tópicos especializados

## Consequências

**Positivas:**
- **Desacoplamento**: Câmeras, OCR e validação funcionam independentemente
- **Tempo Real**: MQTT proporciona comunicação de baixa latência
- **Escalabilidade**: Múltiplas câmeras podem publicar simultaneamente
- **Tolerância a Falhas**: Sistema continua funcionando mesmo com componentes offline temporariamente
- **Flexibilidade**: Fácil adição de novos tipos de eventos e processadores

**Negativas:**
- **Complexidade**: Adiciona camada de comunicação assíncrona
- **Debugging**: Fluxo assíncrono pode ser mais difícil de rastrear
- **Dependência Externa**: Requer broker MQTT funcional
- **Garantias de Entrega**: Necessita configuração adequada de QoS

## Detalhes de Implementação

### Tópicos MQTT
- `cinema/vehicle/arrived`: Sistema 2 publica chegada de veículo com imagem
- `cinema/access/response`: Sistema 1 responde com resultado da validação (opcional)

### Fluxo de Eventos  
1. Sistema 2 detecta veículo e publica em `cinema/vehicle/arrived` com imagem base64
2. Sistema 1 recebe mensagem via MQTT subscriber
3. OCR Service processa imagem e extrai placa
4. Sistema 1 valida placa contra reservas no MongoDB  
5. Se encontrada, atualiza status da reserva para "finalizada"
6. (Opcional) Sistema 1 publica resposta em `cinema/access/response`