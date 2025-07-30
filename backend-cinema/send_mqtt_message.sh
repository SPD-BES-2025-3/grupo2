#!/bin/bash

# =============================
# CONFIGURAÇÃO
# =============================
BROKER_HOST="localhost"
BROKER_PORT="1883"
MQTT_TOPIC="cinema/plates/images"
GATE_ID="portao1"
IMAGE_PATH="./examples/test_car6.jpg"  # Caminho para a imagem que será convertida em base64
TIMESTAMP=$(date -Iseconds)  # ISO 8601 (e.g., 2025-07-30T23:59:00-03:00)
TEMP_PAYLOAD_FILE="payload.json"

# =============================
# GERANDO BASE64 DA IMAGEM
# =============================
if [ ! -f "$IMAGE_PATH" ]; then
  echo "❌ Imagem '$IMAGE_PATH' não encontrada."
  exit 1
fi

IMAGE_BASE64=$(base64 -w 0 "$IMAGE_PATH")  # -w 0 evita quebras de linha

# =============================
# MONTANDO O PAYLOAD
# =============================
cat > "$TEMP_PAYLOAD_FILE" <<EOF
{
  "gate_id": "$GATE_ID",
  "image_base64": "$IMAGE_BASE64",
  "timestamp": "$TIMESTAMP"
}
EOF

echo "✅ Payload criado em $TEMP_PAYLOAD_FILE"

# =============================
# ENVIANDO VIA MQTT
# =============================
mosquitto_pub -h "$BROKER_HOST" -p "$BROKER_PORT" -t "$MQTT_TOPIC" -f "$TEMP_PAYLOAD_FILE"

# =============================
# LIMPEZA (opcional)
# =============================
rm "$TEMP_PAYLOAD_FILE"

echo "📨 Mensagem enviada para $MQTT_TOPIC"
