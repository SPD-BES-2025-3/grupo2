# ADR-002: Escolha de FastAPI e React para Backend e Frontend

**Status:** Aprovado

## Contexto

O desenvolvimento do sistema para o cinema Drive-in demanda tecnologias modernas, eficientes e com boa aceitação no mercado para a construção do backend e frontend.

## Decisão

Optou-se por utilizar:

- **FastAPI** para o backend: framework Python moderno, rápido e com suporte a APIs RESTful, facilitando o desenvolvimento, documentação automática e validação de dados.
- **React** para o frontend: biblioteca JavaScript amplamente utilizada para construção de interfaces de usuário dinâmicas, reativas e de fácil manutenção.

## Consequências

### Pontos Positivos

- FastAPI proporciona alta performance, tipagem forte e documentação automática das rotas.
- React permite criação de interfaces ricas, responsivas e com grande comunidade de suporte.
- Separação clara entre backend e frontend, facilitando manutenção e escalabilidade.

### Pontos Negativos

- Exige conhecimento em múltiplas tecnologias e linguagens (Python e JavaScript/TypeScript).
- Pode aumentar a complexidade do deploy e integração entre as camadas.
