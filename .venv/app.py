from flask import Flask, jsonify, redirect, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)
app.secret_key = '123'

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

@app.route('/')
def index():
    db.create_all()
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    student = Student.query.filter_by(username=username, password=password).first()

    if student:
        # Store the student ID in the session
        session['student_id'] = student.id
        return jsonify({'redirect_url': url_for('student')})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/student', methods=['GET'])
def student():
    student_id = session.get('student_id')
    if student_id:
        student = Student.query.get(student_id)
        if student:
            return render_template('student.html', yourCoursesTH=True, courses=[])
    return jsonify({'message': 'Unauthorized'}), 401

if __name__ == "__main__":
    app.run()
