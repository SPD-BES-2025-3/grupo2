# ADR-013: Escolha do YOLOv8 para Detecção de Placas

**Status:** Aprovado

## Contexto

O Sistema de Cinema Drive-in necessita detectar a localização de placas de veículos em imagens capturadas pelas câmeras de entrada (simuladas via MQTT). Esta detecção é o primeiro passo crucial do pipeline de reconhecimento que posteriormente utiliza OCR para extrair o texto da placa. A solução deve ser precisa, rápida e robusta para diferentes condições de iluminação e ângulos das imagens recebidas.

## Decisão

Optou-se por utilizar o **YOLOv8** (You Only Look Once version 8) da Ultralytics como o modelo de IA para detecção de placas veiculares.

-   **Modelo customizado**: Será utilizado um modelo (`LP-detection.pt`) treinado ou adaptado especificamente para placas brasileiras.
-   **Biblioteca Ultralytics**: Será utilizada a biblioteca `ultralytics==8.3.170` para a inferência do modelo.
-   **Suporte GPU/CPU**: A detecção automática do melhor dispositivo disponível (GPU ou CPU) será configurada para otimizar a performance.
-   **Funcionalidade de crop**: A funcionalidade de extração automática da região da placa detectada será utilizada para alimentar o serviço de OCR.

## Alternativas Consideradas

*(Outras alternativas de modelos de detecção de objetos como Faster R-CNN, SSD, etc., foram consideradas, mas o YOLOv8 foi escolhido pela sua combinação de velocidade e precisão para detecção em tempo real.)*

## Consequências

### Pontos Positivos

-   **Alta Precisão e Performance**: Conhecido por sua alta acurácia e velocidade em detecção de objetos em tempo real.
-   **Otimização de Hardware**: Flexibilidade para GPU e CPU com auto-detecção de dispositivo.
-   **API Simplificada**: A biblioteca Ultralytics oferece uma API simples, facilitando a integração no backend.
-   **Customização**: Permite o uso de modelos customizados para especificidades de placas brasileiras.

### Pontos Negativos

-   **Tamanho do Modelo e Dependências**: O modelo pode ser relativamente grande (~50MB) e possui dependências pesadas (como PyTorch), aumentando o tamanho da aplicação e o consumo de recursos.
-   **Consumo de Recursos**: É uma operação computacionalmente intensiva, podendo consumir significativamente recursos de GPU/CPU.
-   **Dependência de Biblioteca**: Existe uma dependência da manutenção e evolução da biblioteca Ultralytics.