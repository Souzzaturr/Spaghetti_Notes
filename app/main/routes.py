from flask import render_template, current_app
from ..models import posts
from . import main_bp

#página inicial
@main_bp.route('/')
def inicial ():

    lista_posts = posts.exibir_posts_in_lista()

    return render_template("inicio.html", lista_posts = lista_posts)
