from flask import render_template, session, current_app, request, redirect, flash, url_for
from ..models import users, security
from . import usuario_bp



@usuario_bp.route("/login", methods = ["GET", "POST"])
def login ():

    if request.method == "POST":

        usuario = request.form.get("nome")

        senha = request.form.get("senha")


        if security.verificar_usuario(usuario):

            if security.verificar_senha(usuario, senha):

                session["usuario"] = usuario

                flash("Login realizado com sucesso!", "success")

                return redirect(url_for('main.inicial'))
            
            
            flash("Senha incorreta", "danger")
            
            return redirect(url_for("usuario.login"))
        
        
        flash("Não foram encontrados usuários com esse nome, gostaria de criar um novo usuário?", "danger")

        return redirect(url_for("usuario.login"))
    
    
    return render_template('login.html')


#---


@usuario_bp.route("/cadastro", methods = ["GET", "POST"])
def cadastro ():

    if request.method == "POST":

        usuario = request.form.get("nome")

        senha = request.form.get("senha")

        print(usuario)


        if users.nome_usuario_caracteres_permitidos(usuario):
            
            if not security.verificar_usuario(usuario):

                users.criar_usuario(usuario, senha)

                flash("Usuario cadastrado com sucesso!!", "success")

                return redirect(url_for("usuario.login"))
            

            flash("Já existe um usuário com esse mesmo nome, gostaria de fazer login?", "danger")

            return redirect(url_for("usuario.cadastro"))

        
        flash("Um nome de usuario pode conter apenas letras, números, e underline!", "danger")

        return redirect(url_for("usuario.cadastro"))
    

    return render_template("cadastro.html")