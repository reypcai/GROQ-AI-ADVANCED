import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT,
    ai_response TEXT
)
""")
conn.commit()

def save_memory(user_input, ai_response):
    cursor.execute(
        "INSERT INTO conversations (user_input, ai_response) VALUES (?, ?)",
        (user_input, ai_response)
    )
    conn.commit()

def get_last_messages(limit=5):
    cursor.execute(
        "SELECT user_input, ai_response FROM conversations ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    return cursor.fetchall()