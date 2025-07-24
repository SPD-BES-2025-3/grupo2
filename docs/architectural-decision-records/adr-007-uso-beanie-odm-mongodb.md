# ADR-007: Uso do Beanie como ODM para MongoDB

**Status:** Aprovado

## Contexto

O projeto utiliza MongoDB para armazenar dados de alta frequência de escrita, como as reservas, conforme definido na [ADR-002](./adr-002-uso-de-postgre-e-mongo.md). Para interagir com o banco de dados de forma orientada a objetos e alinhada com as práticas do Python, é necessário um ODM (Object-Document Mapper).

Considerando que o backend é desenvolvido com FastAPI, um framework assíncrono, é fundamental que o ODM escolhido tenha suporte nativo a `asyncio` para não bloquear a *event loop* e comprometer a performance da aplicação. As principais alternativas analisadas foram o **Beanie** e o **MongoEngine**.

## Decisão

Foi decidido adotar o **Beanie** como ODM para o MongoDB.

O fator determinante para esta escolha foi o **suporte nativo e de primeira classe a operações assíncronas**. O Beanie foi projetado para ser `async-first`, integrando-se perfeitamente com o ecossistema do FastAPI. Todas as operações de banco de dados são `awaitable`, o que permite um código mais limpo e performático.

Em contrapartida, o **MongoEngine**, embora seja uma biblioteca robusta e com mais tempo de mercado, possui uma API síncrona. Para utilizá-lo em um ambiente assíncrono, seria necessário encapsular suas chamadas em executores de threads (como o `run_in_executor` do asyncio), o que adiciona complexidade, sobrecarga de performance e vai contra os princípios de uma aplicação não-bloqueante.

## Consequências

### Pontos Positivos

- **Performance Aprimorada:** A natureza assíncrona nativa do Beanie garante que as operações de I/O com o banco não bloqueiem a aplicação, maximizando a vazão de requisições.
- **Integração com Pydantic:** O Beanie utiliza modelos Pydantic para definir os documentos. Isso elimina a duplicação de código entre os modelos de banco de dados e os schemas da API, simplificando a validação e a serialização de dados.
- **Código Moderno e Simplificado:** A sintaxe para consultas é intuitiva e alinhada com as práticas modernas de desenvolvimento em Python, facilitando a manutenção.
- **Ecossistema Coerente:** A escolha mantém a coerência tecnológica do projeto, utilizando ferramentas assíncronas em todas as camadas do backend.

### Pontos Negativos

- **Maturidade Relativa:** Por ser uma biblioteca mais recente que o MongoEngine, sua comunidade é menor, o que pode significar menos recursos e exemplos disponíveis para casos de uso muito específicos.
- **Curva de Aprendizagem:** A equipe precisará se familiarizar com a API e as convenções específicas do Beanie.