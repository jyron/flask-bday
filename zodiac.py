import os
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "zodiac.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#models

class User(db.Model):
    email = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    birthday = db.Column(db.String(15), nullable=False)
    birthhour = db.Column(db.String(2))


#routes 

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')
    

#create db after models

db.create_all

if __name__ == "__main__":
    app.run(debug=True)