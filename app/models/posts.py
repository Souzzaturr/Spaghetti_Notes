from . import data_treatment


#---

def iniciar_posts_data ():

    with open("data/posts_data.csv", "a+", encoding = "UTF-8") as posts_data:

        posts_data.seek(0)

        if posts_data.read().splitlines() == []:
            posts_data.write("titulo,conteudo,usuario\n")
    
    return

#---

def criar_post (titulo: str, conteudo: str, usuario: str):

    titulo_tratado = data_treatment.tratar_texto_post(titulo)
    conteudo_tratado = data_treatment.tratar_texto_post(conteudo)

    with open("data/posts_data.csv", "a", encoding = "UTF-8") as posts_data:

        posts_data.write(f"{titulo_tratado},{conteudo_tratado},{usuario}\n")
    
    return

#---

#melhorado com ajuda de IA
def deletar_post(titulo: str, conteudo: str, usuario: str):

    titulo_tratado = data_treatment.tratar_texto_post(titulo)
    conteudo_tratado = data_treatment.tratar_texto_post(conteudo)
    lista_linhas = []

    # lê o arquivo uma única vez
    with open("data/posts_data.csv", "r", encoding="UTF-8") as posts_data:
        linhas = posts_data.read().splitlines()

    if linhas:  # verifica se não está vazio
        # mantém o cabeçalho
        lista_linhas.append(linhas[0])

        # filtra os posts que não queremos remover
        for post in linhas[1:]:
            if post.split(",") != [titulo_tratado, conteudo_tratado, usuario]:
                lista_linhas.append(post)

    # reescreve o arquivo
    with open("data/posts_data.csv", "w", encoding="UTF-8") as posts_data:
        for linha in lista_linhas:
            posts_data.write(linha + "\n")

#---

def exibir_posts_in_lista () -> list:
    
    lista_posts = list()

    with open("data/posts_data.csv", "r", encoding = "UTF-8") as posts_data:
        
        for post in posts_data.read().splitlines()[1:]:
            post = post.split(",")
            
            for i in range(2):
                post[i] = data_treatment.reverter_tratamento_texto_post(post[i])
            
            lista_posts.append(post)
    
    return lista_posts

#---

def exibir_posts_usuario (usuario: str) -> list:
    
    lista_posts = list()

    with open("data/posts_data.csv", "r", encoding = "UTF-8") as posts_data:
        
        for post in posts_data.read().splitlines()[1:]:
            post = post.split(",")
            
            for i in range(2):
                post[i] = data_treatment.reverter_tratamento_texto_post(post[i])
            
            if post[2] == usuario:
                lista_posts.append(post)
    
    return lista_posts

#---

def posts_por_usuario () -> dict:

    usuarios = dict()

    with open("data/posts_data.csv", "r", encoding = "UTF-8") as posts_data:

        for post in posts_data.read().splitlines()[1:]:

            if post.split(",")[2] in usuarios.keys():
                usuarios[post.split(",")[2]] += 1
            
            else:
                usuarios[post.split(",")[2]] = 1
    
    return usuarios