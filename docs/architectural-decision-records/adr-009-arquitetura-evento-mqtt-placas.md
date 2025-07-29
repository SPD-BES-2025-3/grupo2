# ADR-009: Arquitetura Event-Driven com MQTT para Processamento de Placas

**Status:** Proposto

**Date:** 2025-07-29

## Contexto

O sistema de cinema Drive-in precisa processar imagens de placas veiculares capturadas por câmeras na entrada de forma assíncrona e em tempo real. A comunicação entre o sistema de câmeras, o processamento OCR e a validação de reservas deve ser eficiente, desacoplada e escalável.

## Decisão

Implementar uma arquitetura event-driven utilizando MQTT como broker de mensagens para coordenar o fluxo de processamento de placas veiculares.

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
- `camera/plate/detected`: Imagem capturada pela câmera
- `ocr/plate/processed`: Resultado do processamento OCR  
- `validation/plate/checked`: Resultado da validação da reserva
- `access/gate/control`: Comando para liberação/negação de acesso

### Fluxo de Eventos
1. Câmera publica imagem no tópico `camera/plate/detected`
2. Serviço OCR consome evento, processa imagem e publica em `ocr/plate/processed`
3. Serviço de validação verifica reserva e publica em `validation/plate/checked`
4. Sistema de controle recebe validação e publica comando em `access/gate/control`