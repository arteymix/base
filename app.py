from flask import Flask, render_template, g
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
    return "Hello world!"

if __name__ == '__main__':
    app.run(debug=True)
