import sqlite3
import json
from models import Tags, Post_Tags, post_tags

def get_all_tags():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM tags c
        ORDER by label
        """)
        tags = []
        dataset = db_cursor.fetchall()
        for row in dataset :
            tag = Tags(row['id'], row['label'])
            tags.append(tag.__dict__)
    return json.dumps(tags)

def get_single_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM tags c
        WHERE c.id = ?
        """, (id, ))

        dataset = db_cursor.fetchone()
        tag = Tags(dataset['id'], dataset['label'])
    return json.dumps(tag.__dict__)

def create_tag(new_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO tags
            (label)
        VALUES
            (?)
        """, (new_tag['label'],))
        id = db_cursor.lastrowid
        new_tag['id'] = id
    return json.dumps(new_tag)

def delete_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM tags
        WHERE id = ?
        """,(id,))

def update_tag(id, updated_tag):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE tags
            SET 
                label = ?
        WHERE id = ?
        """,(updated_tag['label'], id, ))
        
        rows_affected = db_cursor.rowcount
        if rows_affected == 0:
            return False
        else:
            return True

def get_post_tags():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id
        FROM posttags pt
        """)
        post_tags = []
        dataset = db_cursor.fetchall()
        for row in dataset :
            pt = Post_Tags(row['id'], row['post_id'], row['tag_id'])
            post_tags.append(pt.__dict__)
    return json.dumps(post_tags)