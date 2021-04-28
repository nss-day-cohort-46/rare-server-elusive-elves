import sqlite3
import json
from models import Categories

def get_all_categories():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        ORDER by label
        """)
        categories = []
        dataset = db_cursor.fetchall()
        for row in dataset :
            category = Categories(row['id'], row['label'])
            categories.append(category.__dict__)
    return json.dumps(categories)

def get_single_category(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        WHERE c.id = ?
        """, (id, ))

        dataset = db_cursor.fetchone()
        category = Categories(dataset['id'], dataset['label'])
    return json.dumps(category.__dict__)

def create_category(new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Categories
            (label)
        VALUES
            (?)
        """, (new_category['label'],))
        id = db_cursor.lastrowid
        new_category['id'] = id
    return json.dumps(new_category)

def delete_category(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Categories
        WHERE id = ?
        """,(id,))

def update_category(id, updated_category):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Categories
            SET 
                label = ?
        WHERE id = ?
        """,(updated_category['label'], id, ))
        
        rows_affected = db_cursor.rowcount
        if rows_affected == 0:
            return False
        else:
            return True