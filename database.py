# database.py
import sqlite3

# Name der SQLite-Datenbank
DB = "fundbuero.db"

def create_items_table():
    """
    Erstellt die Tabelle für Fundgegenstände, falls sie noch nicht existiert.
    Spalten: id, name, image_path, date
    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            image_path TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_item(name, image_path, date):
    """
    Fügt einen neuen Fundgegenstand in die Datenbank ein.
    - name: Vorhersage der KI (Schuh, Hose, Shirt)
    - image_path: Dateiname oder 'camera_photo' bei Kameraaufnahme
    - date: Funddatum (als String)
    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO items (name, image_path, date) VALUES (?, ?, ?)",
              (name, image_path, date))
    conn.commit()
    conn.close()


def search_items(query):
    """
    Sucht in der Datenbank nach Items, die den Suchbegriff enthalten.
    - query: z.B. 'Schuh', 'Hose'
    Returns: Liste der gefundenen Einträge
    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM items WHERE name LIKE ?", ('%' + query + '%',))
    rows = c.fetchall()
    conn.close()
    return rows
