import requests
import time
from datetime import datetime, timedelta

BASE_URL = "http://backend:8000"

cliente_payload = {
    "nome": "Cleiton João",
    "email": "cleiton@joao.com",
    "placa": "ONT3060"
}
cliente_id = requests.post(f"{BASE_URL}/clientes", json=cliente_payload).json().get("id")

filmes = [
    {
        "titulo": "Gente Grande",
        "diretor": "Dennis Dugan",
        "generos": ["Comédia", "Drama"],
        "duracao_minutos": 120,
        "classificacao_indicativa": "12"
    },
    {
        "titulo": "Gato de Botas 2: O Último Pedido",
        "diretor": "Joel Crawford",
        "generos": ["Animação", "Comédia", "Aventura", "Fantasia", "Drama"],
        "duracao_minutos": 102,
        "classificacao_indicativa": "L"
    },
    {
        "titulo": "Psicopata Americano",
        "diretor": "Mary Harron",
        "generos": ["Terror", "Suspense", "Comédia"],
        "duracao_minutos": 102,
        "classificacao_indicativa": "18"
    }
]

filme_ids = []
for f in filmes:
    response = requests.post(f"{BASE_URL}/filmes", json=f)
    filme_id = response.json().get("id")
    filme_ids.append(filme_id)
    print(f"🚀🚀🚀🚀🚀🚀🚀🚀🚀 filme_id: {filme_id}")

base_time = datetime.utcnow().replace(microsecond=0)

for i, filme_id in enumerate(filme_ids):
    data = (base_time + timedelta(days=i)).date().isoformat()
    hora = (base_time + timedelta(hours=i)).time().isoformat(timespec="milliseconds") + "Z"
    sessao_payload = {
        "filme_id": filme_id,
        "data": data,
        "hora": hora,
        "preco_por_veiculo": 10 + (i * 2)
    }
    print(f"🚀🚀🚀🚀🚀🚀🚀🚀🚀 sessao_payload: {sessao_payload} 🎬")
    requests.post(f"{BASE_URL}/sessoes", json=sessao_payload)
