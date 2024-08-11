import sqlite3
from flask import Flask

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT)')
    # conn.commit()
    conn.row_factory = sqlite3.Row
    return conn

# Flask routes
@app.route('/')
def index():
    return "Welcome to data pirates!"

@app.route('/create', methods=(['GET']))
def create():
    return "implement create"

@app.route('/read', methods=(['GET']))
def read():
    return "implemnet read"

@app.route('/update/<int:id>', methods=(['GET']))
def update_task(id):
    return "implement update"

@app.route('/delete/<int:id>')
def delete_task(id):
    return "implement delete"

if __name__ == '__main__':
    connect_db()
    app.run(debug=True)
