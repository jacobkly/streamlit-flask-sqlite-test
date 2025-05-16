from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/add', methods=['POST'])
def add_user():
    name = request.json.get('name')
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'successfully added a new user {name}'})

@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('SELECT name FROM users;')
    names = [row[0] for row in c.fetchall()]
    conn.close()
    return jsonify(names)

if __name__ == '__main__':
    app.run(debug=True, port=5000)