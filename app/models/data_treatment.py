#funcoes de tratamento de texto

def tratar_texto_post (texto: str) -> str:
    texto_tratado = texto.replace("\r\n", "\n")
    texto_tratado = texto_tratado.replace(",", ";;")
    texto_tratado = texto_tratado.replace("\n", " bR3@klIn3z ")

    return texto_tratado

#---

def reverter_tratamento_texto_post (texto_tratado: str) -> str:
    texto = texto_tratado
    texto = texto.replace(";;", ",")

    return texto

#---

def remover_espacos (texto: str) -> str:
    
    texto2 = texto[0]

    for i in range(1, len(texto[1:])):

        if texto[i] == " ":
            
            if texto[i - 1] != " ":
                texto2 = texto2 + texto[i]
        
        else:
            texto2 = texto2 + texto[i]
    
    return texto2.strip()