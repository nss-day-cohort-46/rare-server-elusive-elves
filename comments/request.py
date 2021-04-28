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

def create_comment(comment):
    # Get the id value of the last comment in the list
    max_id = COMMENTS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the comment dictionary
    comment["id"] = new_id

    # Add the comment dictionary to the list
    COMMENTS.append(comment)

    # Return the dictionary with `id` property added
    return comment

  
def delete_comment(id):
   with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))
        


def update_comment(id, new_comment):
    # Iterate the COMMENTS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, comment in enumerate(COMMENTS):
        if comment["id"] == id:
            # Found the comment. Update the value.
            COMMENTS[index] = new_comment
            break