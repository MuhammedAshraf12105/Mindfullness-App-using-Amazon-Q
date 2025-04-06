import sqlite3
from datetime import datetime

class MoodTracker:
    def __init__(self):
        self.conn = sqlite3.connect('mindfulness.db')
        self.create_mood_table()
    
    def create_mood_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS mood_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            mood_level INTEGER,
            notes TEXT,
            timestamp DATETIME,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        ''')
        self.conn.commit()
    
    def record_mood(self, user_id, mood_level, notes=''):
        cursor = self.conn.cursor()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            'INSERT INTO mood_entries (user_id, mood_level, notes, timestamp) VALUES (?, ?, ?, ?)',
            (user_id, mood_level, notes, timestamp)
        )
        self.conn.commit()
    
    def get_mood_history(self, user_id, limit=30):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT mood_level, notes, timestamp FROM mood_entries WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?',
            (user_id, limit)
        )
        return cursor.fetchall()
    
    def get_wellness_tips(self, mood_level):
        tips = {
            1: "Consider talking to a friend or professional. Remember, it's okay to seek help.",
            2: "Try some deep breathing exercises or go for a walk in nature.",
            3: "Practice gratitude by writing down three things you're thankful for.",
            4: "Keep up the positive energy! Share your joy with others.",
            5: "Wonderful! Document what made today special to reference on harder days."
        }
        return tips.get(mood_level, "Take a moment to practice mindfulness.")
    
    def __del__(self):
        self.conn.close()