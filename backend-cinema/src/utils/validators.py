import re

# ==================== VALIDAÇÕES DE CLIENTE ====================

def validar_placa_brasileira(placa: str) -> bool:
    if not placa or len(placa) not in [7, 8]:
        return False
    
    placa = placa.upper().strip()
    
    padrao_antigo = r'^[A-Z]{3}\d{4}$'
    
    padrao_mercosul = r'^[A-Z]{3}\d[A-Z]\d{2}$'
    
    return (re.match(padrao_antigo, placa) is not None or 
            re.match(padrao_mercosul, placa) is not None)

validar_placa = validar_placa_brasileira

def formatar_placa_brasileira(placa: str) -> str:
    if not placa:
        return ""
    return placa.upper().strip()

def validar_email(email: str) -> bool:
    if not email or '@' not in email:
        return False
    
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao_email, email) is not None

def validar_nome_cliente(nome: str) -> bool:
    if not nome:
        return False
    
    nome = nome.strip()
    return 2 <= len(nome) <= 100

# ==================== VALIDAÇÕES DE FILME ====================
def validar_titulo_filme(titulo: str) -> bool:
    if not titulo or len(titulo) < 1:
        return False
    return True

def validar_diretor_filme(diretor: str) -> bool:
    if not diretor or len(diretor) < 1:
        return False
    return True

def validar_generos_filme(generos: list) -> tuple:
    if not generos or not isinstance(generos, list):
        return False, "A lista de gêneros está vazia ou não é uma lista."
    for idx, genero in enumerate(generos):
        if not isinstance(genero, str) or len(genero) < 1:
            return False, f"Gênero inválido no índice {idx}: '{genero}'"
    return True, ""

def validar_duracao_filme(duracao: int) -> bool:
    if not isinstance(duracao, int) or duracao <= 0:
        return False
    return True

def validar_nota_filme(nota: float) -> bool:
    if not isinstance(nota, float) or nota < 0.0 or nota > 10.0:
        return False
    return True