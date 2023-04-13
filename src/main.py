from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

#setup flask
app = Flask(__name__)

#link db
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

#make database tables
class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.String(100),unique=True,primary_key=True,nullable=False)
    organisation_id = db.Column(db.String(100),nullable=False)
    room_number = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(100),nullable=False)

    def __init__(self,customer_id,organisation_id,room_number,name):
        self.customer_id = customer_id
        self.organisation_id = organisation_id
        self.room_number = room_number
        self.name = name

class Manager(db.Model):
    __tablename__ = 'managers'
    organisation_id = db.Column(db.String(100),unique=True,primary_key=True,nullable=False)
    password = db.Column(db.String(100),nullable=False)

    def __init__(self,organisation_id,password):
        self.organisation_id = organisation_id
        self.password = password

@app.route('/login/',methods=["GET","POST"])
def login():
    #login page
    return render_template('login.html')

@app.route('/')
def root():
    #redirect website url to login page by default
    return redirect(url_for('login'))

if __name__ == '__main__':
    print("=> Starting flask app")
    with app.app_context():
        # create database
        db.create_all()
        print("=> Database created")
    app.run(debug=True)
    print("=> Unmessed is running")
