import os
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

DB_PATH = "/app/data/app.db"


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/version")
def version():
    if not os.path.exists(DB_PATH):
        return jsonify({"error": "database not initialized"}), 500

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT version FROM metadata LIMIT 1")
    row = cur.fetchone()
    conn.close()

    if row is None:
        return jsonify({"error": "version not found"}), 500

    return jsonify({"version": row[0]}), 200


if __name__ == "__main__":
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", "5000"))
    app.run(host=host, port=port)