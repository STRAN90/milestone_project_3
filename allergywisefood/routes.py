from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from allergywisefood import app, db 
from allergywisefood.models import Category, Users

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")