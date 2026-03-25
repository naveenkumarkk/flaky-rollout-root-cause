import os
import sqlite3

DB_PATH = "/app/data/app.db"
APP_VERSION = os.getenv("APP_VERSION", "1.2.3")

os.makedirs("/app/data", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    version TEXT NOT NULL
)
""")

cur.execute("DELETE FROM metadata")
cur.execute("INSERT INTO metadata (version) VALUES (?)", (APP_VERSION,))

conn.commit()
conn.close()

print("Migration completed successfully.")