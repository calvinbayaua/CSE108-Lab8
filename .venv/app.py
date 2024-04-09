from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    enrolled_students = db.relationship('Student', secondary='enrollment', backref='courses')

enrollment = db.Table('enrollment',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

# @app.route('/')
# def start():
#     db.create_all()
#     # new_student = Student(1, username='stud1', password='123', name='Student Test')
#     # db.session.add(new_student)
#     # db.session.commit()

#     return render_template('login.html') 

# @app.route('/login', methods=['POST'])
# def login():
#     db.create_all()
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#     print("Goodie")
#     student = Student.query.filter_by(username='stud1').first()
#     print("Baddie")
#     if student:
#         return jsonify({'message': 'Login successful'}), 200
#     else:
#         return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == "__main__":
    db.create_all()
    new_student = Student(1, username='stud1', password='123', name='Student Test')
    db.session.add(new_student)
    db.session.commit()
    
    print("hi")
    print(Student.query.all())
    print("bye")
    app.run() 
