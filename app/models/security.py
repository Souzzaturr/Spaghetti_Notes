import hashlib

def dar_hash(senha: str) -> str:
    senha_bytes = senha.encode()
    hash_senha_bytes = hashlib.sha256(senha_bytes)
    hash_senha = hash_senha_bytes.hexdigest()

    return hash_senha

#---

def verificar_usuario (usuario: str) -> bool:

    lista_usuarios = list()

    with open("data/users_data.csv", "r", encoding = "UTF-8") as users_data:

        for nome_senha in users_data.read().splitlines()[1:]:
            if usuario == nome_senha.split(",")[0]:
                return True
    
    return False

#---

def verificar_senha (usuario: str, senha: str) -> bool:

    senha_tah_correta = False

    with open ("data/users_data.csv", "r", encoding = "UTF-8") as users_data:

        for user in users_data.read().splitlines()[1:]:
            
            if usuario == user.split(",")[0]:
                
                senha_tah_correta = dar_hash(senha) == user.split(",")[1]
            
                break
    
    return senha_tah_correta