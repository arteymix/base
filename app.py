from flask import Flask, render_template, g, request
from quick_orm.core import Database
from sqlalchemy import Column, String, Text

__metaclass__ = Database.DefaultMeta

class User:
    username = Column(Text)
    password = Column(Text)
    lol = Column(String)

Database.register()

app = Flask(__name__)

@app.before_first_request
def cleanup():
    import os
    os.unlink('database.sqlite3')

@app.before_request
def setup_db():
    g.db = Database('sqlite:///database.sqlite3')
    g.db.create_tables()

@app.route('/')
def home():
    user = User(username='test')
    g.db.session.add_then_commit(user)
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if g.db.session.query(User).filter(User.username == request.form['username'] and User.password == request._form['password']).exists():
            print "login"
        else:
            print "no login"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
