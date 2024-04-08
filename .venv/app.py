from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import json

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
    
#This table will allow teachers to see their classes
class TeacherClasses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String, unique=True, nullable=False)
    teacher = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)
    
#This table will allow teachers to see the student and grade of a class
class TeacherView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String, unique=True, nullable=False)
    teacher = db.Column(db.String, unique=True, nullable=False)
    time = db.Column(db.String, unique=True, nullable=False)

# # Define Flask-Admin views for each model
admin.add_view(ModelView(StudentClasses, db.session))
admin.add_view(ModelView(AvailableClasses, db.session))
admin.add_view(ModelView(TeacherClasses, db.session))
admin.add_view(ModelView(TeacherView, db.session))
    
@app.route('/')
def start():
    # print_database_schema() # <- Used to view what tables have been created 
    # db.drop_all() # <- Used to delete every UNCOMENTED table (must do if you resturcture tables or will cause issues in flask admin)
    db.create_all()
    return render_template("login.html")

@app.route('/student')
def Student():
    return render_template("student.html")

# @app.route('/admin') # Flask Admin Build the route for us so we do not need to specify a route


if __name__ == "__main__":
    app.run()