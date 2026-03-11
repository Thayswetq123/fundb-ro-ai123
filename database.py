import sqlite3
import datetime

def get_connection():
    return sqlite3.connect("fundbuero.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT UNIQUE,
            password BLOB
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS items(
            username TEXT,
            image BLOB,
            label TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_item(username, image, label):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO items VALUES (?,?,?,?)",
        (username, image, label, datetime.date.today())
    )
    conn.commit()
    conn.close()

def get_items():
    conn = get_connection()
    c = conn.cursor()
    rows = c.execute("SELECT * FROM items").fetchall()
    conn.close()
    return rows
