from flask import render_template
from allergywisefood import app, db 
from allergywisefood.models import Category, Users

@app.route("/")
def home():
    return render_template("index.html")