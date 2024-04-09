from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import json
from sqlalchemy.orm import relationship

########## TESTING ########## <- Required for print_database_schema()

from sqlalchemy import create_engine, MetaData

########## TESTING ##########

app = Flask(__name__)

app.config['SECRET_KEY'] = 'CSE108'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = SQLAlchemy()
admin = Admin()

db.init_app(app)
admin.init_app(app)


########## TESTING ########## <-- Used for Veiwing what tables have been created


def print_database_schema():
    engine = db.get_engine()
    inspector = db.inspect(engine)
    print("Tables in the database:")
    for table_name in inspector.get_table_names():
        print(table_name)

########## TESTING ##########


#This table will be student view of classes
class StudentClasses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    enrollment = db.Column(db.String, nullable=False)
    
#This table will allow students to add classes
class AvailableClasses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String, unique=True, nullable=False)
    teacher = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    enrollment = db.Column(db.String, unique=True, nullable=False)
    
    
#This table will allow teachers to see their classes
class TeacherClasses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String, unique=True, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    enrollment = db.Column(db.String, nullable=False)
    class_id = db.Column(db.Integer, unique=True, nullable=False)
    
# #This table will allow teachers to see the student and grade of a class
# class TeacherView(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     courseName = db.Column(db.String, unique=True, nullable=False)
#     teacher = db.Column(db.String, unique=True, nullable=False)
#     time = db.Column(db.String, unique=True, nullable=False)
#     enrollment = db.Column(db.String, unique=True, nullable=False)

#This allows teacher to veiw and edit student names and grades
class TeacherClassInspect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, nullable=False)
    courseName = db.Column(db.String, nullable=False)
    student = db.Column(db.String, unique=True, nullable=False)
    grade = db.Column(db.Float, nullable=False)

# # Define Flask-Admin views for each model
admin.add_view(ModelView(StudentClasses, db.session))
admin.add_view(ModelView(AvailableClasses, db.session))
admin.add_view(ModelView(TeacherClasses, db.session))
# admin.add_view(ModelView(TeacherView, db.session))
admin.add_view(ModelView(TeacherClassInspect, db.session))

@app.route('/')
def start():
    # print_database_schema() # <- Used to view what tables have been created 
    # db.drop_all() # <- Used to delete every UNCOMENTED table (must do if you resturcture tables or will cause issues in flask admin)
    db.create_all()
    return render_template("login.html")

@app.route('/student')
def Student():
    return render_template("student.html")

@app.route('/teacher')
def Teacher():
    return render_template("teacher.html")

# @app.route('/admin') # Flask Admin Build the route for us so we do not need to specify a route

@app.route('/get-teacher-courses')
def get_teacher_courses():
    # Fetch data from the TeacherClasses table
    teacher_courses = TeacherClasses.query.all()
    # Convert the data to a dictionary
    courses_data = [{"courseName": course.courseName, "teacher": course.teacher, "time": course.time, "enrollment": course.enrollment, "class_id": course.class_id} for course in teacher_courses]
    # Return the data as JSON response
    return jsonify(courses_data)

# @app.route('/get-teacher-view')
# def get_teacher_view():
#     # Fetch data from the TeacherClassInspect table
#     teacher_view = TeacherClassInspect.query.all()

#     # Convert the data to a dictionary
#     view_data = [{"course_id": view.course_id, "course_name": view.courseName, "grade": view.grade} for view in teacher_view]
#     # Return the data as JSON response
#     return jsonify(view_data)

@app.route('/get-teacher-view')  # Renamed the endpoint
def get_teacher_view():
    # Fetch data from the TeacherClassInspect table
    teacher_view = TeacherClassInspect.query.all()
    # Convert the data to a dictionary
    view_data = [{"course_id": view.course_id, "courseName": view.courseName, "student": view.student, "grade": view.grade} for view in teacher_view]
    # Return the data as JSON response
    return jsonify(view_data)

@app.route('/class/<int:class_id>')
def class_detail(class_id):
    # Query TeacherClasses based on class_id
    teacher_class = TeacherClasses.query.filter_by(class_id=class_id).first()
    # Query TeacherClassInspect based on class_id
    class_inspects = TeacherClassInspect.query.filter_by(course_id=class_id).all()
    return render_template("class1.html", teacher_class=teacher_class, class_inspects=class_inspects)


if __name__ == "__main__":
    app.run()