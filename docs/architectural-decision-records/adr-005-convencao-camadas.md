# ADR-005: Convenção de Camadas (Service, Repository, Controller)

**Status:** Aprovado

## Contexto

A organização do backend em camadas facilita a manutenção, testes e evolução do sistema. O projeto adota as camadas Controller, Service e Repository para separar responsabilidades.

## Decisão

- **Controller:** Responsável por receber requisições HTTP, validar dados de entrada e encaminhar para a camada de serviço.
- **Service:** Centraliza a lógica de negócio, validações complexas e orquestra chamadas aos repositórios.
- **Repository:** Realiza operações diretas de acesso ao banco de dados, abstraindo detalhes de persistência.

## Consequências

### Pontos Positivos
- Facilita testes unitários e integração.
- Melhora a clareza e organização do código.
- Permite evolução independente das camadas.

### Pontos Negativos
- Pode aumentar a quantidade de arquivos e complexidade inicial.
- Exige disciplina para manter a separação de responsabilidades.
