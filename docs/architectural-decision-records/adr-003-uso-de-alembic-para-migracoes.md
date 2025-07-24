# ADR-003: Uso do Alembic para Migrações de Banco de Dados

**Status:** Aprovado

## Contexto

Com a evolução do sistema, torna-se necessário realizar alterações estruturais no banco de dados relacional (PostgreSQL), como criação de novas tabelas, adição de colunas, alteração de tipos de dados, entre outros. Gerenciar essas mudanças manualmente pode gerar inconsistências, dificultar o versionamento e impactar negativamente o trabalho em equipe.

## Decisão

Foi decidido adotar o Alembic como ferramenta de controle de versões e migrações do banco de dados PostgreSQL. O Alembic permite:

- Gerar scripts de migração automaticamente a partir das alterações nos modelos ORM.
- Aplicar e reverter migrações de forma controlada e rastreável.
- Manter o histórico de mudanças estruturais do banco de dados no repositório de código.

## Consequências

### Pontos Positivos

- Facilita o versionamento e a rastreabilidade das mudanças no banco de dados.
- Permite que diferentes membros da equipe sincronizem facilmente o estado do banco de dados local com o do projeto.
- Reduz o risco de inconsistências e erros em alterações estruturais.
- Integra-se facilmente ao SQLAlchemy, já utilizado no projeto.

### Pontos Negativos

- Exige aprendizado inicial da ferramenta por parte da equipe.
- Requer disciplina para sempre gerar e aplicar migrações ao alterar os modelos.

## Referências
- [Documentação oficial do Alembic](https://alembic.sqlalchemy.org/)
- [Documentação oficial do SQLAlchemy](https://docs.sqlalchemy.org/)
