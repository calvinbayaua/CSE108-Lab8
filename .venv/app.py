from doctest import debug
from imghdr import tests
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
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    time = db.Column(db.String(50))
    teacher = db.Column(db.String(100))
    students = db.relationship('Student', secondary=student_class_association, backref=db.backref('classes', lazy='dynamic'))

    
@app.route('/')
def start():   
    db.create_all()
    # #all_students = Student.query.all()

    # # Print details of each student
    # for student in all_students:
    #     print(f"Student ID: {student.id}, Name: {student.name}, Username: {student.username}, Password: {student.password}")
        
    return render_template("login.html") 
    
@app.route('/login', methods=['POST'])
def login():
    # Receive the JSON data sent from the JavaScript code
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Query the database for the provided username
    student = Student.query.filter_by(username=username).first()

    # Check if a student with the provided username exists and verify the password
    if student and student.password == password:
        # Redirect to the student's home page URL
        return redirect(url_for('student_home', student_id=student.id))
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

if __name__ == "__main__":
    db.create_all()
    testStudent = Student(1, "Roj", "roj1", "Roger1")
    db.session.add(testStudent)
    db.session.commit()
    
    all_students = Student.query.all()

    # Print details of each student
    for student in all_students:
        print(f"Student ID: {student.id}, Name: {student.name}, Username: {student.username}, Password: {student.password}")
    
    print("Hello World")
        
    app.run(debug=True)