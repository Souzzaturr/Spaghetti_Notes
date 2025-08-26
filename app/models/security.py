import hashlib

def dar_hash(senha: str) -> str:
    senha_bytes = senha.encode()
    hash_senha_bytes = hashlib.sha256(senha_bytes)
    hash_senha = hash_senha_bytes.hexdigest(hash_senha_bytes)

    return hash_senha

#---

def verificar_usuario (usuario: str) -> bool:

    lista_usuarios = list()

    with open("data/users_data.csv", "r", encoding = "UTF-8") as users_data:

        for usuario in users_data.read().splitlines()[1:]:
            lista_usuarios.append(usuario[0])
    
    return usuario in lista_usuarios

#---

def verificar_senha (usuario: str, senha: str) -> bool:

    senha_tah_correta = False

    with open ("data/users_data.csv", "r", encoding = "UTF-8") as users_data:

        for user in users_data.read().splitlines()[1:]:
            
            if usuario == user[0]:
                
                senha_tah_correta = dar_hash(senha) == user[1]
            
                break
    
    return senha_tah_correta