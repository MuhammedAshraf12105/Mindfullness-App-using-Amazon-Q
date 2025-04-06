import sqlite3
from passlib.hash import pbkdf2_sha256

class AuthManager:
    def __init__(self):
        self.conn = sqlite3.connect('mindfulness.db')
        self.create_users_table()
    
    def create_users_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        ''')
        self.conn.commit()
    
    def register_user(self, username, password, email):
        try:
            hashed_password = pbkdf2_sha256.hash(password)
            cursor = self.conn.cursor()
            cursor.execute(
                'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                (username, hashed_password, email)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def verify_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        
        if result:
            stored_password = result[0]
            return pbkdf2_sha256.verify(password, stored_password)
        return False
    
    def __del__(self):
        self.conn.close()