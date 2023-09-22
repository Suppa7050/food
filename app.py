from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Replace 'mysql://username:password@localhost/dbname' with your MySQL connection string.
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{os.environ["USER"]}:{os.environ["PASSWORD"]}@localhost/food'

db = SQLAlchemy(app)

# Define a model for your database table.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, username):
        self.username = username

# Create the database and tables.
def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    user = User(username)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    print(os.environ["PASSWORD"],os.environ["USER"])
    create_tables()
    app.run(debug=True)
