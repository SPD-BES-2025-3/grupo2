# ADR-010: Estratégia de Processamento OCR para Placas Brasileiras

**Status:** Proposto

**Date:** 2025-07-29

## Contexto

O sistema precisa processar imagens de placas veiculares brasileiras com alta precisão, considerando os dois formatos oficiais: formato antigo (ABC1234) e formato Mercosul (ABC1A23). A solução deve ser robusta, eficiente e preparada para diferentes condições de iluminação e qualidade de imagem.

## Decisão

Implementar uma estratégia híbrida de OCR que combina:
1. **Pré-processamento** de imagem para melhoria de qualidade
2. **Validação** baseada em padrões regex para formatos brasileiros
3. **Múltiplas tentativas** com diferentes técnicas de OCR
4. **Score de confiança** para determinar a precisão da detecção

## Alternativas Consideradas

1. **Tesseract OCR Local**: Processamento totalmente local
2. **AWS Rekognition**: Serviço de OCR na nuvem da Amazon
3. **Google Vision API**: Serviço de OCR do Google
4. **Azure Computer Vision**: Serviço de OCR da Microsoft
5. **Solução Híbrida**: Combinação de múltiplas abordagens

## Consequências

**Positivas:**
- **Precisão**: Validação específica para padrões brasileiros aumenta acurácia
- **Flexibilidade**: Possibilidade de alternar entre diferentes provedores de OCR
- **Controle de Qualidade**: Score de confiança permite filtrar detecções duvidosas
- **Robustez**: Múltiplas tentativas aumentam taxa de sucesso

**Negativas:**
- **Complexidade**: Implementação de múltiplas estratégias
- **Performance**: Múltiplas tentativas podem aumentar tempo de processamento
- **Custo**: Uso de APIs externas pode gerar custos
- **Dependência**: APIs externas podem ter indisponibilidade

### Pipeline de Processamento
1. **Recebimento**: Imagem em base64
2. **Pré-processamento**: Normalização, contraste, filtros
3. **OCR Principal**: Tentativa com provider principal
4. **OCR Backup**: Tentativa com provider alternativo (se confiança < threshold)
5. **Validação**: Verificação do formato brasileiro
6. **Limpeza**: Remoção de caracteres inválidos
7. **Resposta**: Placa limpa + score de confiança

### Threshold de Confiança
- **Mínimo aceitável**: 0.80 (80%)
- **Ideal**: 0.90+ (90%+)
- **Backup necessário**: < 0.85 (85%)