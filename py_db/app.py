import sqlite3

conn = sqlite3.connect("test.db")

#create db
conn.row_factory = sqlite3.Row
conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    ''')

#insert
conn.execute('''
        INSERT INTO users (name, age)
        VALUES (?, ?)
    ''', ("name", 10))

#read
conn.execute('SELECT * FROM users')
rows = conn.fetchall()

#update
conn.execute('''
        UPDATE users
        SET name = ?, age = ?
        WHERE id = ?
    ''', ("update", 11, 1))

#delete
conn.execute('''
        DELETE FROM users
        WHERE id = ?
    ''', (1,))
conn.commit()
conn.close()
