import os
from flask import Flask, render_template, request, flash
#database imports
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
#form imports
from flask_wtf.csrf import CSRFProtect
#admin imports
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "zodiac.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'supersecret'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)



#models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    birthday = db.Column(db.String(15), nullable=False)
    birthhour = db.Column(db.String(4))
    ampm = db.Column(db.String(4))
    def __repr__(self):
        return "<User: {} | Birthday: {} {}{}>".format(self.email, self.birthday, self.birthhour, self.ampm)
    

#routes 

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        user = User(email = request.form['email'],
        birthday = request.form['birthday'],
        birthhour = request.form['hour'],
        ampm = request.form['AMPM'])
        db.session.add(user)
        db.session.commit()
        flash('Hold on, we\'re searching for someone with your exact birthday!')
    return render_template('home.html')
    
admin = Admin(app)
admin.add_view(ModelView(User, db.session))



if __name__ == "__main__":
    app.run(debug=True)