# ADR-011: Integração com Hardware de Câmeras e Controle de Acesso

**Status:** Proposto

**Date:** 2025-07-29

## Contexto

O sistema de cinema Drive-in precisa se integrar com hardware físico incluindo câmeras de captura de placa, catracas de controle de acesso e sistemas de iluminação. A integração deve ser robusta, permitir múltiplos pontos de entrada e fornecer feedback em tempo real.

## Decisão

Implementar uma arquitetura de integração baseada em:
1. **Padrão de Adaptadores** para diferentes tipos de hardware
2. **Comunicação via MQTT** para comandos e status
3. **APIs REST** para configuração e monitoramento
4. **WebSockets** para feedback em tempo real

## Alternativas Consideradas

1. **HTTP Polling**: Consulta periódica aos dispositivos
2. **TCP/UDP Direto**: Comunicação de baixo nível com hardware
3. **Serial/RS485**: Protocolo serial para dispositivos industriais
4. **WebRTC**: Streaming de vídeo em tempo real
5. **MQTT + REST**: Solução híbrida (escolhida)

## Consequências

**Positivas:**
- **Padronização**: Interface uniforme para diferentes fabricantes
- **Escalabilidade**: Fácil adição de novos pontos de entrada
- **Flexibilidade**: Suporta diferentes protocolos de hardware
- **Monitoramento**: Visibilidade completa do status dos dispositivos
- **Manutenção**: Isolamento de falhas por dispositivo

**Negativas:**
- **Complexidade**: Múltiplas camadas de abstração
- **Latência**: Overhead de comunicação via broker
- **Dependências**: Necessita infraestrutura de rede robusta
- **Debugging**: Rastreamento complexo entre hardware e software

## Detalhes de Implementação

### Componentes de Hardware

#### Câmeras de Placa
```python
class PlateCamera:
    def __init__(self, camera_id: str, ip_address: str):
        self.camera_id = camera_id
        self.ip_address = ip_address
        
    async def capture_image(self) -> bytes:
        """Captura imagem da placa"""
        
    async def get_status(self) -> CameraStatus:
        """Status da câmera (online/offline/erro)"""
```

#### Sistema de Controle de Acesso
```python
class AccessController:
    async def open_gate(self, gate_id: str) -> bool:
        """Abre cancela de entrada"""
        
    async def close_gate(self, gate_id: str) -> bool:
        """Fecha cancela de entrada"""
        
    async def get_gate_status(self, gate_id: str) -> GateStatus:
        """Status da cancela"""
```

### Tópicos MQTT para Hardware

#### Comandos
- `hardware/camera/{camera_id}/capture`: Solicita captura de imagem
- `hardware/gate/{gate_id}/open`: Comando para abrir cancela
- `hardware/gate/{gate_id}/close`: Comando para fechar cancela
- `hardware/lights/{area_id}/control`: Controle de iluminação

#### Status
- `hardware/camera/{camera_id}/status`: Status da câmera
- `hardware/gate/{gate_id}/status`: Status da cancela
- `hardware/system/heartbeat`: Heartbeat geral do sistema

### Configuração de Dispositivos

```json
{
  "cameras": [
    {
      "id": "cam_entrada_01",
      "name": "Câmera Entrada Principal",
      "ip": "192.168.1.100",
      "type": "hikvision_ds2cd",
      "settings": {
        "resolution": "1920x1080",
        "fps": 15,
        "night_mode": true
      }
    }
  ],
  "gates": [
    {
      "id": "gate_entrada_01", 
      "name": "Cancela Entrada Principal",
      "controller_ip": "192.168.1.101",
      "type": "barrier_pro_x1"
    }
  ]
}
```

### Fluxo de Integração

1. **Detecção de Veículo**: Sensor detecta aproximação
2. **Captura Automática**: Câmera captura imagem da placa
3. **Processamento**: OCR processa e identifica placa
4. **Validação**: Sistema verifica reserva válida
5. **Controle de Acesso**: Cancela abre automaticamente
6. **Confirmação**: Sistema registra entrada no log
7. **Timeout**: Cancela fecha após tempo configurado

### Monitoramento e Alertas

#### Dashboard em Tempo Real
- Status de todas as câmeras
- Estado das cancelas (aberta/fechada)
- Fila de processamento OCR
- Histórico de acessos recentes

#### Alertas Automáticos
- Câmera offline por > 5 minutos
- Cancela não respondendo
- Fila de OCR com mais de 10 itens
- Taxa de erro > 10% em período

### Configuração de Rede

```yaml
# docker-compose.yml - Rede para hardware
networks:
  hardware_network:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.100.0/24
```

## Segurança

- **Autenticação**: Certificados TLS para MQTT
- **Autorização**: ACLs por tópico/dispositivo
- **Criptografia**: Payloads criptografados
- **Isolamento**: VLAN separada para hardware
- **Auditoria**: Log de todos os comandos enviados