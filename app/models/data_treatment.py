

#---

def tratar_texto_post (texto: str) -> str:
    texto_tratado = texto.replace("\r\n", "\n")
    texto_tratado = texto_tratado.replace(",", ";;").replace("\n", "/////")

    return texto_tratado

#---

def reverter_tratamento_texto_post (texto_tratado: str) -> str:
    texto = texto_tratado.replace("/////", "\n")
    texto = texto.replace(";;", ",")

    return texto

#---

