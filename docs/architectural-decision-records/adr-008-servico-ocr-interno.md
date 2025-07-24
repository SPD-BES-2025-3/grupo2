# ADR-008: Manter o Serviço de Reconhecimento de Placas (OCR) Interno ao Backend

**Status:** Aprovado

**Data:** 2025-07-25

## Contexto

O sistema precisa de uma funcionalidade para reconhecer placas de veículos a partir de imagens enviadas na entrada do cinema drive-in. A arquitetura ideal para essa funcionalidade poderia ser um microsserviço dedicado, que encapsularia as dependências pesadas (como bibliotecas de OCR) e poderia ser escalado de forma independente.

## Decisão

Decidimos implementar o serviço de OCR como um módulo interno (`OCRService`) dentro do monolito do backend, em vez de criar um microsserviço separado neste momento.

## Consequências

**Positivas:**
- **Velocidade de Desenvolvimento:** A implementação interna é significativamente mais rápida, pois elimina a necessidade de configurar um novo projeto, pipeline de CI/CD, comunicação entre serviços e infraestrutura separada. Isso é crucial para cumprir os prazos atuais do projeto.
- **Simplicidade Operacional:** Reduz a complexidade de deploy e monitoramento no curto prazo, já que há apenas um serviço para gerenciar.

**Negativas:**
- **Acoplamento:** O backend principal fica acoplado à lógica e às dependências do OCR. Uma falha ou alto consumo de recursos no serviço de OCR pode impactar a performance de toda a aplicação.
- **Escalabilidade Limitada:** Não é possível escalar a funcionalidade de OCR de forma independente das outras APIs do backend.
- **Débito Técnico:** Esta decisão é considerada um débito técnico que deve ser reavaliado caso a funcionalidade de OCR se torne mais complexa, crítica ou um gargalo de performance. O `OCRService` foi projetado com baixo acoplamento para facilitar uma futura extração.