from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = SQLAlchemy(app)
admin = Admin(app)

# Intermediate table for many-to-many relationship between students and classes
student_class_association = db.Table('student_class_association',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('class_id', db.Integer, db.ForeignKey('class.id'), primary_key=True)
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    time = db.Column(db.String(50))
    teacher = db.Column(db.String(100))
    students = db.relationship('Student', secondary=student_class_association, backref=db.backref('classes', lazy='dynamic'))

    
@app.route('/')
def start():
    db.create_all()
    return render_template("student.html") 

if __name__ == "__main__":
    app.run()