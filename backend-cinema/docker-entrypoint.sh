#!/bin/bash

RUN_SEEDER=${RUN_SEEDER:-true}

run_seeder_background() {
    echo "Aguardando backend estar pronto..."

    until curl -f http://localhost:8000/health > /dev/null 2>&1; do
        echo "Backend ainda não está pronto, aguardando..."
        sleep 5
    done
    
    echo "Backend está rodando! Executando data seeder..."
    
    python src/utils/seed.py
    
    if [ $? -eq 0 ]; then
        echo "Data seeder executado com sucesso!"
    else
        echo "Erro ao executar data seeder"
    fi
}

echo "Iniciando servidor..."
uvicorn src.main:app --host 0.0.0.0 --port 8000 &
SERVER_PID=$!

if [ "$RUN_SEEDER" = "true" ]; then
    run_seeder_background &
else
    echo "Seeder desabilitado via RUN_SEEDER=false"
fi

wait $SERVER_PID
