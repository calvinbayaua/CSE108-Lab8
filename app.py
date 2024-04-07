from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

@app.route('/')
def start():
    db.create_all()
    return render_template("login.html") 

if __name__ == "__main__":
    app.run()