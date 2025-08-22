import security

#---

def iniciar_users_data ():

    with open("../../data/users_data.csv", "a+", encoding = "UTF-8") as users_data:

        users_data.seek(0)
        
        if users_data.read().splitlines() == []:
            users_data.write("nome,senha\n")
    
    return

#---

def criar_usuario (nome: str, senha: str) -> None:

    hash_senha = security.dar_hash(senha)

    with open("../../data/users_data.csv", "a", encoding = "UTF-8") as users_data:
        users_data.write(f"{nome},{hash_senha}\n")
    
    return

#---

#def verificar_usuario (usuario: str, senha: str) -> bool: