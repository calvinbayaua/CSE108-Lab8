from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import json
from sqlalchemy.orm import relationship
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user

########## TESTING ########## <- Required for print_database_schema()

from sqlalchemy import create_engine, MetaData

########## TESTING ##########

app = Flask(__name__)

app.config['SECRET_KEY'] = 'CSE108'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

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
    class_id = db.Column(db.Integer, nullable=False)
    courseName = db.Column(db.String, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    enrollment = db.Column(db.String, nullable=False)
    
#This table will allow students to add classes
class AvailableClasses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, nullable=False)
    courseName = db.Column(db.String, unique=True, nullable=False)
    teacher = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    enrollment = db.Column(db.String, unique=True, nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    
#This table will allow teachers to see their classes
class TeacherClasses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String, unique=True, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    enrollment = db.Column(db.String, nullable=False)
    class_id = db.Column(db.Integer, unique=True, nullable=False)

#This allows teacher to veiw and edit student names and grades
class TeacherClassInspect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, nullable=False)
    courseName = db.Column(db.String, nullable=False)
    student = db.Column(db.String, unique=True, nullable=False)
    grade = db.Column(db.Float, nullable=False)

# Define Flask-Admin views for each model
admin.add_view(ModelView(StudentClasses, db.session))
admin.add_view(ModelView(AvailableClasses, db.session))
admin.add_view(ModelView(TeacherClasses, db.session))
admin.add_view(ModelView(TeacherClassInspect, db.session))
admin.add_view(ModelView(User, db.session))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def login():
    # db.drop_all()
    print("Route '/' Called")
    db.create_all()
    if request.method == 'POST':
        print("POST Received")
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        print("Username:" + username)
        print("Password: " + password)

        # user = User.authenticate(username, password)
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            print("IF USER Received")
            login_user(user)
            print("User role: " + user.role)
            if user.role == 'teacher':
                return redirect("/teacher")
            elif user.role == 'student':
                return redirect("/student")
        return jsonify({'message': 'Invalid username or password'}), 401
    else:
        return render_template("login.html")


@app.route('/student')
@login_required
def Student():
    student_id = current_user.id
    student_courses = StudentClasses.query.filter_by(id=student_id).all()
    courses_data = [{"name": course.courseName, "teacher": course.teacher, "time": course.time, "enrollment": course.enrollment} for course in student_courses]
    return render_template('student.html', yourCoursesTH=True, courses=courses_data)

@app.route('/student/your-courses', methods=['GET'])
@login_required
def get_student_courses():
    student_id = current_user.id
    student_courses = StudentClasses.query.filter_by(id=student_id).all()
    courses_data = [{"name": course.courseName, "teacher": course.teacher, "time": course.time, "enrollment": course.enrollment} for course in student_courses]
    return jsonify(courses_data)


@app.route('/student/add-courses', methods=['GET'])
@login_required
def get_available_courses():
    student_id = current_user.id
    student_courses = StudentClasses.query.filter_by(id=student_id).all()
    enrolled_courses = [{"name": course.courseName} for course in student_courses]

    available_courses = AvailableClasses.query.all()
    courses_data = [{"id": course.id, "name": course.courseName, "teacher": course.teacher, "time": course.time, "enrollment": course.enrollment} for course in available_courses]
    return jsonify({"enrolled_courses": enrolled_courses, "courses": courses_data})


@app.route('/student/add-courses/enroll', methods=['PUT'])
@login_required
def enroll_course():
    data = request.get_json()
    course_id = data.get('courseId')

    course = AvailableClasses.query.filter_by(id=course_id).first()
    if not course:
        return jsonify({'message': 'Course not found'}), 404
    
    student_id = current_user.id
    enrolled_course = StudentClasses.query.filter_by(id=student_id, class_id=course_id).first()
    if enrolled_course:
        return jsonify({'message': 'You are already enrolled in this course'}), 400
    
    new_enrollment = StudentClasses(id=student_id, class_id=course_id, courseName=course.courseName, teacher=course.teacher, time=course.time, enrollment=course.enrollment)
    db.session.add(new_enrollment)
    # Increment enrollment count for the course
    course.enrollment = str(int(course.enrollment) + 1)
    db.session.commit()

    return jsonify({'message': 'Enrolled successfully'}), 200


@app.route('/student/add-courses/unenroll', methods=['DELETE'])
@login_required
def unenroll_course():
    data = request.get_json()
    course_id = data.get('courseId')

    # Find the enrolled course for the current user
    student_id = current_user.id
    enrolled_course = StudentClasses.query.filter_by(id=student_id, class_id=course_id).first()
    if not enrolled_course:
        return jsonify({'message': 'You are not enrolled in this course'}), 400

    # Remove the course from the StudentClasses table
    db.session.delete(enrolled_course)
    # Decrement enrollment count for the course
    course = AvailableClasses.query.filter_by(id=course_id).first()
    course.enrollment = str(int(course.enrollment) - 1)
    db.session.commit()

    return jsonify({'message': 'Unenrolled successfully'}), 200




@app.route('/teacher')
def Teacher():
    return render_template("teacher.html")

# @app.route('/admin') # Flask Admin Build the route for us so we do not need to specify a route



@app.route('/get-teacher-courses')
def get_teacher_courses():
    teacher_courses = TeacherClasses.query.all()
    courses_data = [{"courseName": course.courseName, "teacher": course.teacher, "time": course.time, "enrollment": course.enrollment, "class_id": course.class_id} for course in teacher_courses]
    return jsonify(courses_data)

@app.route('/get-teacher-view')  # Renamed the endpoint
def get_teacher_view():
    teacher_view = TeacherClassInspect.query.all()
    view_data = [{"course_id": view.course_id, "courseName": view.courseName, "student": view.student, "grade": view.grade} for view in teacher_view]
    return jsonify(view_data)

@app.route('/class/<int:class_id>')
def class_detail(class_id):
    teacher_class = TeacherClasses.query.filter_by(class_id=class_id).first()
    class_inspects = TeacherClassInspect.query.filter_by(course_id=class_id).all()
    return render_template("class1.html", teacher_class=teacher_class, class_inspects=class_inspects)


if __name__ == "__main__":
    app.run()