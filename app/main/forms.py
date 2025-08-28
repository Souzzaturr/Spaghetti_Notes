from flask import Flask, request, url_for, render_template, session, flash, redirect
from . import main_bp
from ..models import posts



@main_bp.route("/postar_receita", methods = ["GET", "POST"])
def postar_receita ():

    if request.method == "POST":

        if "usuario" in session.keys():

            titulo = request.form.get("titulo")

            conteudo = request.form.get("receita")

            posts.criar_post(titulo, conteudo, session["usuario"])

            flash("Post de receita criado com sucesso!!", "success")

            return redirect(url_for("main.inicial"))

        
        flash("Você precisa estar logado para criar um post de receita!!", "danger")

        return redirect(url_for("main.postar_receita"))
    
    
    if "usuario" in session.keys():

        return render_template("postar_receita.html",usuario = session["usuario"])
    
    return render_template("postar_receita.html")