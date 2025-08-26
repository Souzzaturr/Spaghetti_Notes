from flask import render_template, current_app
from . import main_bp

#página inicial
@main_bp.route('/')
def inicial ():
    return render_template("inicio.html")
