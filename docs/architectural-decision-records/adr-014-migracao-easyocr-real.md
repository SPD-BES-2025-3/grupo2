# ADR-014: Uso do EasyOCR para Reconhecimento de Caracteres

**Status:** Aprovado

## Contexto

Como parte do pipeline de reconhecimento de placas (`adr-008`), é necessário um componente de Reconhecimento Óptico de Caracteres (OCR) para extrair o texto das placas veiculares detectadas pelo modelo de IA (YOLOv8, conforme `adr-013`). A precisão na leitura de placas brasileiras é crítica, e a solução deve ser eficiente e viável para implementação local.

## Decisão

Optou-se por utilizar o **EasyOCR 1.7.2** como a solução principal para o reconhecimento óptico de caracteres dentro do serviço de processamento de placas.

-   **EasyOCR 1.7.2**: Biblioteca Python para OCR.
-   **Suporte multilíngue**: Configurado para português e inglês (`['pt', 'en']`) para otimizar o reconhecimento de caracteres em placas brasileiras (antigas e Mercosul).
-   **Otimização GPU**: Tenta automaticamente utilizar GPU para inferência, com fallback para CPU em caso de indisponibilidade ou erro, garantindo flexibilidade de ambiente.
-   **Integração com pipeline assíncrono**: Será integrado com o fluxo de processamento assíncrono do FastAPI.

## Alternativas Consideradas

*(As alternativas de serviços de nuvem ou outras bibliotecas foram consideradas em um nível mais estratégico de OCR, conforme `adr-010`, mas o EasyOCR foi escolhido para esta implementação específica local.)*

## Consequências

### Pontos Positivos

-   **Precisão para Placas Brasileiras**: Oferece precisão adequada para os formatos de placas brasileiras, com a vantagem de funcionar offline.
-   **API Simples**: Possui uma API Python simples para integração.
-   **Custo Zero (On-premise)**: Solução gratuita e de código aberto, sem dependência de serviços externos pagos ou faturamento por uso.
-   **Flexibilidade de Hardware**: Suporte automático a GPU e fallback para CPU.

### Pontos Negativos

-   **Dependências Pesadas**: Requer dependências como OpenCV e PyTorch, que podem aumentar o tamanho da imagem Docker e o consumo de recursos.
-   **Inicialização Lenta**: A primeira execução pode ser lenta devido ao carregamento dos modelos de IA/OCR na memória.
-   **Performance Variável**: A precisão e performance dependem da qualidade da imagem de entrada (resolução, iluminação, ângulo).