# ADR-008: Implementação do Pipeline de Reconhecimento de Placas em Produção

**Status:** Aprovado

## Contexto

O projeto do cinema Drive-in requer um sistema robusto para o acesso de veículos, que envolve a detecção de placas e reconhecimento de caracteres para validação de reservas. A fase inicial do projeto utilizou simulações de OCR para acelerar o desenvolvimento, mas a evolução exige agora um pipeline de computer vision real e integrado.

## Decisão

Optou-se por implementar um **pipeline de reconhecimento de placas em produção** integrado ao backend, combinando detecção de objetos com IA e reconhecimento óptico de caracteres (OCR). Este pipeline processará imagens de veículos recebidas via eventos e será responsável por extrair e validar os dados da placa.

## Consequências

### Pontos Positivos

-   **Precisão e Realismo:** Permite o reconhecimento real de placas, essencial para o funcionamento do sistema de acesso.
-   **Validação Automatizada:** Habilita a validação automática de reservas com base nas placas detectadas.
-   **Controle Integrado:** Mantém o controle do pipeline de visão computacional internamente ao backend, permitindo otimização e customização.
-   **Preparação para Produção:** Move a funcionalidade central do sistema de uma simulação para uma implementação pronta para ambientes de produção.

### Pontos Negativos

-   **Complexidade Computacional:** Requer recursos significativos (CPU/GPU) para o processamento de modelos de IA e OCR.
-   **Dependências Pesadas:** Introduz dependências de bibliotecas de IA e visão computacional (ex: PyTorch, OpenCV).
-   **Latência Potencial:** O tempo de processamento das imagens pode introduzir latência no fluxo de validação de acesso.