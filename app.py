from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()