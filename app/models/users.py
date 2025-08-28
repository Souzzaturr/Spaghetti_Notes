from . import security

#---

def iniciar_users_data ():

    with open("data/users_data.csv", "a+", encoding = "UTF-8") as users_data:

        users_data.seek(0)
        
        if users_data.read().splitlines() == []:
            users_data.write("nome,senha\n")
    
    return

#---

def criar_usuario (nome: str, senha: str) -> None:

    hash_senha = security.dar_hash(senha)

    with open("data/users_data.csv", "a", encoding = "UTF-8") as users_data:
        users_data.write(f"{nome},{hash_senha}\n")
    
    return

#---

#verifica se há apenas caracteres permitidos no nome de usuario
def nome_usuario_caracteres_permitidos (usuario: str) -> bool:
    
    for caractere in usuario:

        #verificar se o caractere não é letra, numero ou underline
        if not (caractere.isalnum() or caractere == "_"):

            return False
    
    return True


#---

def listar_usuarios () -> list:

    lista_usuarios = list()

    with open ("data/users_data.csv", "r", encoding = "UTF-8") as users_data:

        for nome in users_data.read().splitlines()[1:]:

            lista_usuarios.append(nome.split(",")[0])
    
    return lista_usuarios