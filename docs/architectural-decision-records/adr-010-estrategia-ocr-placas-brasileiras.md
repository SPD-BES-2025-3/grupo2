# ADR-010: Estratégia de Processamento OCR para Placas Brasileiras

**Status:** Proposto

**Data:** 2025-07-29

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

### Pipeline de Processamento (Implementação Real)
1. **Recebimento**: Mensagem MQTT com imagem em base64 do Sistema 2
2. **Decodificação**: Conversão de base64 para bytes da imagem  
3. **OCR/IA**: Extração da placa usando modelo de IA + OCR
4. **Validação**: Verificação do formato brasileiro (ABC1234 ou ABC1A23)
5. **Limpeza**: Remoção de caracteres inválidos
6. **Busca**: Consulta no MongoDB por reserva com `vehicle_plate`
7. **Atualização**: Se encontrada, status vira "finalizada"

### Threshold de Confiança
- **Mínimo aceitável**: 0.80 (80%)
- **Ideal**: 0.90+ (90%+)
- **Backup necessário**: < 0.85 (85%)