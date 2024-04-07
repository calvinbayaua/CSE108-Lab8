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
class StudentClasses(db.Model):
    courseName = db.Column(db.String, primary_key=True)
    teacher = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    enrollment = db.Column(db.String, unique=True, nullable=False)
    
#This table will allow students to add classes
class AvailableClasses(db.Model):
    courseName = db.Column(db.String, primary_key=True)
    teacher = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    
#This table will allow teachers to see their classes
class TeacherClasses(db.Model):
    courseName = db.Column(db.String, primary_key=True)
    teacher = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    
#This table will allow teachers to see the student and grade of a class
class TeacherView(db.Model):
    courseName = db.Column(db.String, primary_key=True)
    teacher = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    
@app.route('/')
def start():
    db.create_all()
    return render_template("login.html") 

if __name__ == "__main__":
    app.run()