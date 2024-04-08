from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = SQLAlchemy(app)
admin = Admin(app)

#This table will be student view of classes
class Student_table(db.Model):
    courseName = db.Column(db.String, primary_key=True)
    teacher = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    
    #This could be pulled from a different table
    #enrollment = db.Column(db.String, unique=True, nullable=False)
    
@app.route('/')
def start():
    db.create_all()
    return render_template("login.html")

@app.route('/student')
def Student():
    return render_template("student.html")

@app.route('/admin')
def Admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run()