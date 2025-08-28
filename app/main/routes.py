from flask import render_template, current_app, request, session, flash
from ..models import posts
from . import main_bp

#página inicial
@main_bp.route('/', methods = ["GET", "POST"])
def inicial ():

    if request.method == "POST":

        if request.form.get("from_perfil_user") == "logout":

            del session["usuario"]

    lista_posts = posts.exibir_posts_in_lista()

    if "usuario" in session.keys():
        
        return render_template("inicio.html", lista_posts = lista_posts, usuario = session["usuario"])
    
    return render_template("inicio.html", lista_posts = lista_posts)


#página de receitas
@main_bp.route("/receitas/<titulo>")
def receita (titulo: str):

    conteudo = request.args.get("conteudo")
    
    usuario = request.args.get("usuario")

    return render_template("receita.html", titulo = titulo, conteudo = conteudo, usuario = usuario)


@main_bp.route("/sobre")
def sobre ():
    return render_template("sobre.html")
