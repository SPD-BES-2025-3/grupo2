# ADR-011: Simulação de Integração com Sistema Externo de Câmeras

**Status:** Conceitual (Simulação)

**Data:** 2025-07-29

## Contexto

O projeto do cinema Drive-in precisa simular a integração com um sistema externo (Sistema 2) que controla câmeras e catracas físicas. O Sistema 1 (foco do trabalho acadêmico) deve receber mensagens via MQTT sobre chegada de veículos, processar a imagem da placa usando IA/OCR, validar contra reservas no MongoDB e atualizar o status das reservas.

## Decisão

Implementar uma simulação de integração entre dois sistemas:

**Sistema 1 (Nosso Sistema - Foco do Trabalho):**
- CRUD completo das entidades (Filmes, Sessões, Clientes, Reservas)
- MQTT Broker subscriber para receber mensagens do Sistema 2
- Processamento de IA/OCR para detecção de placas
- Validação de placas contra reservas no MongoDB
- Atualização de status de reserva para "finalizada"

**Sistema 2 (Simulado - Não construído):**
- Sistema externo que controla câmeras e catracas físicas
- Publica mensagens MQTT quando veículo chega
- Envia imagem em base64 da parte frontal do veículo

## Fluxo de Integração Real

1. **Chegada do Veículo**: Sistema 2 detecta veículo se aproximando
2. **Captura de Imagem**: Sistema 2 captura imagem frontal em base64
3. **Publicação MQTT**: Sistema 2 publica mensagem com imagem no tópico
4. **Recebimento**: Sistema 1 recebe mensagem via MQTT subscriber
5. **Processamento IA/OCR**: Sistema 1 extrai placa da imagem usando IA
6. **Validação**: Sistema 1 busca reserva com a placa no MongoDB
7. **Atualização**: Se encontrada, status da reserva vira "finalizada"
8. **Resposta**: Sistema 1 pode enviar confirmação via MQTT (opcional)

## Alternativas Consideradas

1. **Integração Real com Hardware**: Conectar diretamente com câmeras/catracas físicas
2. **Sistema Monolítico**: Incluir controle de hardware dentro do Sistema 1
3. **Simulação via MQTT**: Simular Sistema 2 externo (escolhida)
4. **Mock Local**: Simular entrada sem comunicação externa

## Consequências

**Positivas:**
- **Foco Acadêmico**: Permite concentrar no desenvolvimento do Sistema 1 (CRUD, IA, validações)
- **Realismo**: Simula arquitetura real de sistemas distribuídos
- **Flexibilidade**: MQTT permite fácil substituição por sistema real no futuro
- **Testabilidade**: Possível criar diferentes cenários de teste
- **Aprendizado**: Experiência com comunicação assíncrona e processamento de IA

**Negativas:**
- **Simulação**: Não há integração real com hardware físico
- **Dependência Externa**: Precisa simular Sistema 2 para testes completos
- **Complexidade**: Adiciona camada MQTT que poderia ser evitada em versão simplificada

## Detalhes de Implementação

### Estrutura da Mensagem MQTT (Sistema 2 → Sistema 1)
```json
{
  "gate_id": "entrada_01",
  "event_type": "VEHICLE_ARRIVED", 
  "image_base64": "iVBORw0KGgoAAAANSUhEUgAA...",
  "timestamp": "2025-07-29T10:30:00Z",
  "camera_metadata": {
    "camera_id": "cam_001",
    "resolution": "1920x1080"
  }
}
```

### Tópicos MQTT
- **Entrada**: `cinema/vehicle/arrived` (Sistema 2 → Sistema 1)
- **Saída**: `cinema/access/response` (Sistema 1 → Sistema 2, opcional)

### Processamento no Sistema 1
1. **MQTT Subscriber** recebe mensagem
2. **OCR Service** processa `image_base64`
3. **Reserva Repository** busca por `vehicle_plate` no MongoDB
4. **Reserva Service** atualiza status para "finalizada" se encontrada
