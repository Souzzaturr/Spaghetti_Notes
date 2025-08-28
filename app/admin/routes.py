from flask import Blueprint, request, redirect, url_for, render_template, current_app, session, flash
from ..models import posts
from . import admin_bp

@admin_bp.route("/admin")
def admin ():

    if "usuario" in session.keys():
        if session["usuario"] == "Artur_ADM" or session["usuario"] == "Josue_ADM" or session["usuario"] == "Gerson_ADM":

            usuarios_posts = posts.posts_por_usuario()

            flash("Seja bem vindo... ADM SUPREMO!!", "success")

            return render_template("admin.html", usuarios_posts = usuarios_posts, usuario = session["usuario"])


    flash("Você não tem acesso à essa pagina!!", "danger")

    return redirect(url_for("main.inicial"))