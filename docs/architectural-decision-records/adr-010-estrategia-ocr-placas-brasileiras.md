# ADR-010: Estratégia de Processamento OCR para Placas Brasileiras

**Status:** Aprovado

## Contexto

O sistema precisa processar imagens de placas veiculares brasileiras com alta precisão, considerando os dois formatos oficiais: formato antigo (ABC1234) e formato Mercosul (ABC1A23). A solução deve ser robusta, eficiente e preparada para diferentes condições de iluminação e qualidade de imagem.

## Decisão

Implementar uma estratégia de processamento OCR que combina:
1.  **Pré-processamento** de imagem para melhoria de qualidade.
2.  **Validação** baseada em padrões regex para formatos brasileiros.
3.  **Score de confiança** para determinar a precisão da detecção, permitindo filtragem ou reprocessamento de detecções duvidosas.

*(Nota: A decisão sobre as ferramentas específicas de IA/OCR, como YOLOv8 e EasyOCR, é tratada em ADRs separadas, como `adr-013` e `adr-014`.)*

## Alternativas Consideradas

1.  **Tesseract OCR Local**: Processamento totalmente local.
2.  **AWS Rekognition**: Serviço de OCR na nuvem da Amazon.
3.  **Google Vision API**: Serviço de OCR do Google.
*(A decisão atual foca em solução local para menor latência e custo inicial, permitindo futuras integrações com serviços de nuvem para maior precisão ou escalabilidade, se necessário.)*

## Consequências

### Pontos Positivos

-   **Precisão Aprimorada**: A validação específica para padrões brasileiros aumenta a acurácia do reconhecimento.
-   **Controle de Qualidade**: O score de confiança permite tratar detecções duvidosas (ex: requerer revisão humana ou tentativa de reprocessamento).
-   **Adaptabilidade**: A estratégia permite a integração futura de múltiplas técnicas ou provedores de OCR para aumentar a robustez.

### Pontos Negativos

-   **Complexidade da Lógica**: A implementação da validação e do tratamento de confiança adiciona complexidade ao serviço.
-   **Qualidade da Imagem**: A performance final do OCR é altamente dependente da qualidade da imagem de entrada.
-   **Otimização**: Requer otimização contínua dos modelos e do pré-processamento para garantir performance e acurácia.

### Threshold de Confiança
-   **Mínimo aceitável**: 0.80 (80%) para considerar a placa válida.
-   **Ideal**: 0.90+ (90%+) para garantir alta confiabilidade.
-   **Ações para < 0.80**: Registrar para análise, acionar processo manual, ou requerer nova imagem.