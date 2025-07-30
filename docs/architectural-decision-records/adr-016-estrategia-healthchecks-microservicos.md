# ADR-016: Estratégia de HealthChecks em Microserviços

**Status:** Aprovado

**Data:** 2025-07-30

## Contexto

O sistema de cinema Drive-in é composto por múltiplos serviços interdependentes (PostgreSQL, MongoDB, MQTT Broker, Backend FastAPI) executados via Docker Compose. A dependência entre serviços exige uma estratégia para garantir que cada componente esteja funcionalmente pronto antes que outros serviços dependentes sejam iniciados.

## Decisão

Decidimos implementar **health checks** em todos os containers Docker para monitoramento e gerenciamento de dependências.

A estratégia inclui:
- **Health checks individuais**: Cada serviço define sua própria verificação de saúde
- **Dependency management**: Backend aguarda saúde dos bancos via `depends_on.condition`
- **Retry logic**: Configuração de tentativas e timeouts específicos
- **Graceful degradation**: Reinicialização automática de containers não saudáveis

## Alternativas Consideradas

1. **Wait-for-it scripts**: Scripts shell para aguardar portas
2. **Init containers**: Containers dedicados para verificação de dependências
3. **Aplicação sem health checks**: Inicialização sem validação de dependências
4. **Health checks externos**: Monitoramento via Kubernetes probes

## Consequências

### Pontos Positivos

- **Inicialização Confiável**: Garante ordem correta de startup dos serviços
- **Recuperação Automática**: Containers não saudáveis são reiniciados automaticamente
- **Detecção Precoce**: Problemas são identificados rapidamente
- **Observabilidade**: Status de saúde visível via `docker ps`
- **Resiliência**: Sistema se recupera automaticamente de falhas temporárias

### Pontos Negativos

- **Overhead**: Health checks consomem recursos adicionais
- **Complexidade**: Adiciona lógica de verificação em cada serviço
- **Tempo de Startup**: Inicialização pode ser mais lenta devido às verificações
