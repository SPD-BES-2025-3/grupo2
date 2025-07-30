# ADR-014: Migração para EasyOCR Real

**Status:** Aprovado

## Contexto

O sistema inicialmente utilizava uma simulação de OCR que retornava placas fictícias para desenvolvimento e testes. Com a evolução do projeto, tornou-se necessário implementar reconhecimento real de caracteres para extrair texto das placas detectadas pelo YOLOv8. A precisão na leitura de placas brasileiras é crítica para o funcionamento correto do sistema de validação de reservas.

## Decisão

Optou-se por migrar da simulação para o **EasyOCR** como solução de reconhecimento óptico de caracteres.

- **EasyOCR 1.7.2**: Biblioteca Python para OCR
- **Suporte multilíngue**: Configurado para português e inglês (`['pt', 'en']`)
- **Otimização GPU**: Tentativa automática de usar GPU, fallback para CPU
- **Validação brasileira**: Regex para formatos antigo (ABC1234) e Mercosul (ABC1A23)
- **Pipeline assíncrono**: Integração com FastAPI async/await

## Consequências

### Pontos Positivos

- Precisão adequada para placas brasileiras com suporte offline.
- API simples com suporte GPU e fallback automático para CPU.
- Solução gratuita sem dependência de serviços externos pagos.
- Validação específica para formatos brasileiro antigo e Mercosul.

### Pontos Negativos

- Dependências pesadas (OpenCV, PyTorch) aumentam tamanho da aplicação.
- Inicialização lenta devido ao carregamento dos modelos.
- Performance variável dependente da qualidade da imagem de entrada.
