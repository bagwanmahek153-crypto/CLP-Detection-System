import sqlite3

class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect("patients.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            age INTEGER,
            speech_score INTEGER,
            prediction INTEGER
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, age, speech, prediction):
        query = "INSERT INTO patients (age, speech_score, prediction) VALUES (?, ?, ?)"
        self.conn.execute(query, (age, speech, prediction))
        self.conn.commit()