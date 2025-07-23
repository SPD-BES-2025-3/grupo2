# ADR-006: Uso de DTOs e Schemas para Transferência e Validação de Dados

**Status:** Aprovado

## Contexto

A manipulação de dados entre camadas do sistema exige padronização e validação para garantir integridade e facilitar manutenção. O projeto utiliza DTOs (Data Transfer Objects) e Schemas (Pydantic) para esse fim.

## Decisão

- **DTOs:** Utilizados para transportar dados entre camadas internas do backend, evitando exposição direta dos modelos de banco.
- **Schemas (Pydantic):** Utilizados para validação de dados recebidos e enviados via API, garantindo formato e regras de negócio básicas.

## Consequências

### Pontos Positivos
- Facilita evolução dos modelos sem impactar contratos externos.
- Melhora a segurança e integridade dos dados trafegados.
- Permite validação automática e documentação das rotas.

### Pontos Negativos
- Exige manutenção dos DTOs e Schemas conforme o sistema evolui.
- Pode gerar duplicidade de estruturas se não houver padronização.
