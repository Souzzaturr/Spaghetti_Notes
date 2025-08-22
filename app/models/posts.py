import data_treatment


#---

def iniciar_posts_data ():

    with open("../../data/posts_data.csv", "a+", encoding = "UTF-8") as posts_data:

        posts_data.seek(0)

        if posts_data.read().splitlines() == []:
            posts_data.write("titulo,conteudo,usuario\n")
    
    return

#---

def criar_post (titulo: str, conteudo: str, usuario: str):

    titulo_tratado = data_treatment.tratar_texto_post(titulo)
    conteudo_tratado = data_treatment.tratar_texto_post(conteudo)

    with open("../../data/posts_data.csv", "a", encoding = "UTF-&") as posts_data:

        posts_data.write(f"{titulo_tratado},{conteudo_tratado},{usuario}\n")
    
    return

#---

#melhorado com ajuda de IA
def deletar_post(titulo: str, conteudo: str, usuario: str):

    titulo_tratado = data_treatment.tratar_texto_post(titulo)
    conteudo_tratado = data_treatment.tratar_texto_post(conteudo)
    lista_linhas = []

    # lê o arquivo uma única vez
    with open("../../data/posts_data.csv", "r", encoding="utf-8") as posts_data:
        linhas = posts_data.read().splitlines()

    if linhas:  # verifica se não está vazio
        # mantém o cabeçalho
        lista_linhas.append(linhas[0])

        # filtra os posts que não queremos remover
        for post in linhas[1:]:
            if post.split(",") != [titulo_tratado, conteudo_tratado, usuario]:
                lista_linhas.append(post)

    # reescreve o arquivo
    with open("../../data/posts_data.csv", "w", encoding="utf-8") as posts_data:
        for linha in lista_linhas:
            posts_data.write(linha + "\n")

#---