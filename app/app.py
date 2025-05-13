from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    conn = psycopg2.connect(
        host="db", database="postgres", user="postgres", password="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    return f'Hello from Flask! PostgreSQL version: {db_version}'
