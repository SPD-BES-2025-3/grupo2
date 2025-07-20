# ADR-001: Escolha da Stack de Bancos de Dados

**Status:** A ser revisado

## Contexto

O sistema de gerenciamento do cinema Drive-in exige o armazenamento de diferentes tipos de dados, com características e necessidades distintas de acesso e atualização.

## Decisão

Optou-se por utilizar dois bancos de dados:

- **PostgreSQL**: banco de dados relacional utilizado para armazenar informações menos voláteis e de atualização menos frequente, como dados de filmes e clientes.
- **MongoDB**: banco de dados NoSQL utilizado para armazenar dados de escrita mais frequente, como as reservas, proporcionando maior flexibilidade e performance para esse tipo de operação.

## Consequências

### Pontos Positivos

- Mantém a integridade e estrutura relacional dos dados principais do negócio (filmes, clientes, etc.) no PostgreSQL.
- Permite otimizar o desempenho do sistema, utilizando cada banco para o tipo de dado mais adequado.
- Facilita a escalabilidade e manutenção dos dados de reservas, que tendem a ter maior volume e frequência de escrita.

### Pontos Negativos

- Aumenta a complexidade da arquitetura, exigindo integração entre dois bancos de dados distintos.
- Pode demandar maior esforço de manutenção e conhecimento técnico da equipe.
