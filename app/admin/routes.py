from flask import Blueprint, request, redirect, url_for, render_template, current_app
from . import admin_bp

@admin_bp.route("/")