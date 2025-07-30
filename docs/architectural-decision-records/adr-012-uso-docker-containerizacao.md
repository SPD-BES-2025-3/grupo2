# ADR-012: Uso do Docker para Containerização

**Status:** Aprovado

## Contexto

O sistema de cinema Drive-in é composto por múltiplos serviços interdependentes: PostgreSQL, MongoDB, MQTT Broker (Mosquitto), e backend FastAPI. Cada serviço possui suas próprias dependências, configurações e requisitos de ambiente, apresentando desafios de configuração inconsistente entre ambientes e complexidade no setup inicial.

## Decisão

Optou-se por adotar **Docker** e **Docker Compose** como estratégia de containerização para todo o projeto.

- **Containerização completa**: PostgreSQL, MongoDB, Mosquitto MQTT, Backend FastAPI
- **Docker Compose**: Orquestração dos serviços com dependências
- **Health checks**: Verificação de saúde para todos os containers
- **Volumes persistentes**: Dados dos bancos mantidos entre reinicializações
- **Rede isolada**: `cinema_network` para comunicação interna entre serviços

## Consequências

### Pontos Positivos

- Consistência de ambiente garantindo mesmas versões e configurações.
- Setup simplificado com comando único (`docker compose up`).
- Isolamento completo evitando conflitos entre serviços.
- Portabilidade funcionando identicamente em qualquer sistema operacional.
- Resiliência com health checks e reinicialização automática.

### Pontos Negativos

- Overhead de recursos com maior consumo de RAM e CPU.
- Curva de aprendizagem exigindo conhecimento de Docker e Docker Compose.
- Complexidade adicional no debugging dentro de containers.