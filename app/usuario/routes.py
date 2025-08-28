from flask import render_template, request, session, flash, redirect, url_for
from . import usuario_bp
from ..models import posts

@usuario_bp.route("/perfil")
def perfil ():

    if not "usuario" in session.keys():
        flash("Para acessar essa rota é preciso estar logado!!", "danger")

        return redirect(url_for("usuario.login"))

    lista_posts = posts.exibir_posts_usuario(session["usuario"])

    return render_template("perfil.html", lista_posts = lista_posts, usuario = session["usuario"])