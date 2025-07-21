# Visão Geral

O projeto consiste no desenvolvimento de um sistema para gerenciamento de um cinema Drive-in, com funcionalidades como o cadastro de clientes, controle de sessões de filmes, reservas de vagas e exibição de filmes. A modelagem inicial foi baseada em um diagrama de classes que representa as principais entidades do domínio: Cliente, Filme, Gênero, Sessão, Vaga e Reserva.

# Sumário 

1. [Introdução](#1-introdução)  
   1.1 [Justificativa](#11-justificativa)
   1.2 [Descrição do Problema](#12-descrição-do-problema)  
   1.3 [Motivação](#13-motivação) 

2. [Stack Tecnológica](#2-stack-tecnológica)

# 1. Introdução

## 1.1 Justificativa

Com a crescente demanda por experiências de entretenimento inovadoras e personalizadas os cinemas Drive-in voltaram a ganhar popularidade como alternativa nostálgica para o consumo de filmes. Nesse contexto, surge a necessidade de um sistema informatizado que gerencie eficientemente as sessões, reservas e ocupação de vagas em um cinema Drive-in, de forma ágil e confiável.

Sistematizar eesse processo otimiza o controle operacional do negócio e melhora a experiência do cliente final, reduzindo falhas humanas, facilitando o processo de reservas e permitindo a gestão em tempo real das sessões, veículos e vagas disponíveis.

## 1.2 Descrição do Problema

A gestão manual de cinemas Drive-in, ou qualquer sistema de reservas em geral, enfrenta diversos desafios:

- Impossibilidade de realizar reservas online e fora do horário comercial;
- Atendimento demorado e mais propício ao erro;
- Dificuldade em controlar reservas simultâneas;
- Falta de visibilidade em tempo real das vagas disponíveis;
- Impossibilidade de integrar diferentes sistemas (reserva, controle de acesso, histórico de sessões);
- Risco de conflitos ou inconsistências entre dados de clientes, sessões e filmes exibidos.

Diante desses desafios, torna-se essencial o desenvolvimento de um sistema confiável, com integração assíncrona entre seus componentes e interface amigável para a operação.

## 1.3 Motivação

O projeto é motivado por quatro principais fatores:

1. **Relevância Prática:** O desenvolvimento de um sistema para cinema Drive-in representa um problema do mundo real com múltiplas entidades, relações e operações CRUD, ideal para aplicação prática dos conhecimentos adquiridos na disciplina.

2. **Integração Tecnológica:** A utilização de múltiplas tecnologias proporciona a oportunidade de aprendizado em arquitetura de software moderna, tanto no contexto relacional quanto não relacional.

3. **Formação Profissional:** A entrega do projeto em etapas simula a realidade de desenvolvimento ágil, estimulando a organização do trabalho em grupo, uso de versionamento com Git, documentação técnica e testes.

4. **Domínio da Persistência de Dados:** O projeto permite explorar diferentes abordagens de persistência de dados — incluindo bancos relacionais com ORM e bancos NoSQL com ODM, proporcionando maior compreensão sobre modelagem de dados, operações CRUD, mapeamento objeto-relacional/documental, e estratégias de integração de dados entre sistemas.


# 2. Stack Tecnológica

O projeto utiliza a seguinte stack tecnológica:

- **Backend:** Python com FastAPI
- **Frontend:** React
- **Banco de Dados Relacional:** PostgreSQL
- **Banco de Dados NoSQL:** MongoDB 

