# Sistema de Cinema Drive-in 

#### Discente: Mauro Sérgio

## Relatório - Etapa 01

Nesta etapa, atuei principalmente na documentação e implementação da base do backend do sistema de cinema drive-in, modelagem de entidades e arquitetura do sistema. Também contribuí para a documentação da stack tecnológica e para a configuração de migrações com Alembic.

Entre os commits mais relevantes, destaco: a modelagem da entidade Filme, a configuração do ORM (SQLAlchemy) e ODM (Motor/MongoDB), a organização dos diagramas e decisões arquiteturais, a implementação dos endpoints de filmes e a finalização da configuração de migrações. Essas entregas estruturam a base do backend e facilitam a evolução do projeto.

Alguns pontos ficaram pendentes, como a implementação completa dos testes automatizados para os novos módulos e a documentação detalhada de todos os endpoints. Para as próximas etapas, pretendo avançar na cobertura de testes, integração contínua e detalhamento da documentação técnica.

## Histórico de Commits

#### 1. **Commit:** `476b686` - Versão inicial do diagrama de classes
- **Descrição:** Criação do diagrama de classes inicial do sistema
- **Impacto:** Base para a modelagem das entidades do projeto
- **Arquivos:** 1 arquivo criado

#### 2. **Commit:** `3814a42` - Documentando a stack do projeto
- **Descrição:** Adição da documentação da stack tecnológica utilizada
- **Impacto:** Facilita o entendimento das tecnologias adotadas
- **Arquivos:** 1 arquivo modificado

#### 3. **Commit:** `afdec7f` - Correção de um erro de digitação
- **Descrição:** Pequena correção textual na documentação
- **Impacto:** Melhora a clareza e a apresentação do projeto
- **Arquivos:** 1 arquivo modificado

#### 4. **Commit:** `c4fb8c1` - Adicionando o diagrama de containeres e reorganizando os diretórios
- **Descrição:** Inclusão do diagrama de containers e reorganização da estrutura de diretórios
- **Impacto:** Melhora a organização e a documentação visual da arquitetura
- **Arquivos:** 2 arquivos criados/modificados

#### 5. **Commit:** `253b88f` - Modelando filme
- **Descrição:** Implementação do modelo de filme
- **Impacto:** Estruturação da entidade Filme no backend
- **Arquivos:** 1 arquivo criado/modificado

#### 6. **Commit:** `ed34550` - Configurando ORM e ODM
- **Descrição:** Configuração inicial do ORM (SQLAlchemy) e ODM (Motor/MongoDB)
- **Impacto:** Permite integração com bancos de dados relacional e NoSQL
- **Arquivos:** 2 arquivos criados/modificados

#### 7. **Commit:** `5b33291` - Organizando a disposição dos diagramas com README próprio
- **Descrição:** Organização dos diagramas em diretório próprio e criação de README explicativo
- **Impacto:** Facilita a navegação e compreensão dos diagramas do projeto
- **Arquivos:** 2 arquivos criados/modificados

#### 8. **Commit:** `5cf2a7d` - Implementação inicial de filme
- **Descrição:** Primeira implementação das rotas e lógica para filmes
- **Impacto:** Adiciona endpoints e lógica básica para manipulação de filmes
- **Arquivos:** 2 arquivos criados/modificados

#### 9. **Commit:** `dc6cd91` - feat: Setting movie endpoints
- **Descrição:** Configuração dos endpoints para filmes
- **Impacto:** Disponibiliza operações CRUD para filmes na API
- **Arquivos:** 1 arquivo criado/modificado

#### 10. **Commit:** `ee99272` - Merge branch 'develop' of https://github.com/SPD-BES-2025-3/grupo2 into develop
- **Descrição:** Merge de alterações da branch develop
- **Impacto:** Sincronização do desenvolvimento
- **Arquivos:** Diversos arquivos modificados

#### 11. **Commit:** `9968317` - feat: Implemented movie genres
- **Descrição:** Implementação do suporte a gêneros de filmes
- **Impacto:** Permite associar múltiplos gêneros a um filme
- **Arquivos:** 1 arquivo criado/modificado

#### 12. **Commit:** `3593dc0` - Finalizando a branch Alembic
- **Descrição:** Finalização e merge das configurações de migração com Alembic
- **Impacto:** Permite versionamento e migração do banco de dados relacional
- **Arquivos:** 2 arquivos criados/modificados
