from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

#setup flask
app = Flask(__name__)

#link db
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

@app.route('/login/')
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


