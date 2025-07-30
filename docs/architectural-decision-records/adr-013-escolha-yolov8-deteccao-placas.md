# ADR-013: Escolha do YOLOv8 para Detecção de Placas

**Status:** Aprovado

## Contexto

O sistema de cinema Drive-in necessita detectar placas de veículos em imagens capturadas pelas câmeras de entrada. Esta detecção é o primeiro passo do pipeline de reconhecimento que posteriormente utiliza OCR para extrair o texto da placa. A solução deve ser precisa, rápida e robusta para diferentes condições de iluminação e ângulos.

## Decisão

Optou-se por utilizar o **YOLOv8** (You Only Look Once version 8) da Ultralytics como modelo de detecção de placas.

- **Modelo customizado**: LP-detection.pt treinado especificamente para placas brasileiras
- **Biblioteca Ultralytics**: ultralytics==8.3.170 para inferência
- **Suporte GPU/CPU**: Detecção automática do melhor dispositivo disponível
- **Funcionalidade de crop**: Extração automática da região da placa detectada

## Consequências

### Pontos Positivos

- Alta precisão e performance otimizada para detecção em tempo real.
- Flexibilidade para GPU e CPU com auto-detecção de dispositivo.
- API simples da Ultralytics com funcionalidade de crop integrada.
- Customização permite modelos específicos para placas brasileiras.

### Pontos Negativos

- Modelo relativamente grande (~50MB) e dependências pesadas (PyTorch).
- Consumo intensivo de recursos GPU/CPU.
- Dependência externa da manutenção da biblioteca Ultralytics.
