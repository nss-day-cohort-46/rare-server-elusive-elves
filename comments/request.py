import sqlite3
import json
from models import Comments



def get_all_comments():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.created_on
        FROM comments as c
        """)

        # Initialize an empty list to hold all comment representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an comment instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Comment class above.
            comment = Comments(row['id'], row['post_id'], row['author_id'], row['content'], row['created_on'])

            comments.append(comment.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(comments)


def get_single_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.created_on
        FROM comments as c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an comment instance from the current row
        comment = Comments(data['id'], data['post_id'], data['author_id'], data['content'], data['created_on'])


        return json.dumps(comment.__dict__)

def create_comment(new_comment):
    with sqlite3.connect("./rare.db") as conn:
        
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO comments
            (post_id, author_id, content, created_on)
        VALUES
            (?, ?, ?, ?);
        """, (new_comment["post_id"], new_comment["author_id"], 
          new_comment["content"], new_comment["created_on"], ))
        
        id = db_cursor.lastrowid

        new_comment["id"] = id

    return json.dumps(new_comment)
  




def delete_comment(id):
   with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))
        


def update_comment(id, new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comments
            SET
                post_id = ?,
                author_id = ?,
                content = ?,
                created_on = ?
        WHERE id = ?
        """, (new_comment["post_id"], new_comment["author_id"], 
          new_comment["content"], new_comment["created_on"], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True