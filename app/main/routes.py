from flask import render_template, current_app, request
from ..models import posts
from . import main_bp

#página inicial
@main_bp.route('/')
def inicial ():

    lista_posts = posts.exibir_posts_in_lista()

    return render_template("inicio.html", lista_posts = lista_posts)


#página de receitas
@main_bp.route("/receitas/<titulo>")
def receita (titulo: str):

    conteudo = request.args.get("conteudo")
    
    usuario = request.args.get("usuario")

    return render_template("receita.html", titulo = titulo, conteudo = conteudo, usuario = usuario)
