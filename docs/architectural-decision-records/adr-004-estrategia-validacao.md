# ADR-004: Estratégia de Validação de Dados

**Status:** Aprovado

## Contexto

A validação de dados é fundamental para garantir a integridade das informações processadas pelo sistema. O projeto apresenta diferentes necessidades de validação, como formato, obrigatoriedade e existência de entidades no banco de dados.

## Decisão

Foi decidido separar a validação em duas etapas:

- **Validação de formato e obrigatoriedade:** Realizada via Pydantic nos Schemas, garantindo que os dados recebidos estejam no padrão esperado.
- **Validação de existência no banco:** Realizada nas camadas de serviço, evitando que Schemas acessem diretamente o banco de dados e mantendo a separação de responsabilidades.

## Consequências

### Pontos Positivos
- Facilita testes unitários e reutilização dos Schemas.
- Mantém o código desacoplado e organizado.
- Reduz riscos de dependências circulares e facilita manutenção.

### Pontos Negativos
- Exige disciplina para manter a separação entre validação de formato e de existência.
- Pode aumentar o número de etapas no fluxo de validação.
