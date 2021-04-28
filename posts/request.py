import sqlite3
import json
from models import Posts

def get_single_post(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content
        FROM posts p
        WHERE p.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an post instance from the current row
        post = Posts(data["id"], data["user_id"], data["category_id"], data["title"], data["publication_date"], data["content"])

    return json.dumps(post.__dict__)

def get_all_posts():    
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT  
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content
        FROM posts p
        """)

        posts = []

        #convert rows into a python list
        dataset = db_cursor.fetchall()

        #Iterate through list of data returned
        for row in dataset:

            post = Posts(row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"], row["content"])


            #add post to posts
            posts.append(post.__dict__)


        return json.dumps(posts)


def get_posts_by_user_id(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content
        FROM posts p
        WHERE p.id = ?
        """, ( id, ))

        
        posts = []

        #convert rows into a python list
        dataset = db_cursor.fetchall()

        #Iterate through list of data returned
        for row in dataset:

            post = Posts(row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"], row["content"])


            #add post to posts
            posts.append(post.__dict__)


        return json.dumps(posts)




# Create
def create_post(new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Posts
                ( user_id, category_id, title, publication_date, content )
            VALUES 
                ( ?, ?, ?, ?, ?);
        """, (
            new_post['user_id'],
            new_post['category_id'],
            new_post['title'],
            new_post['publication_date'],
            new_post['content'],
            ))

        id = db_cursor.lastrowid

        new_post['id'] = id

    return json.dumps(new_post)


def get_post_by_category(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


    # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content
        FROM posts p
        WHERE p.category_id = ?
        """, ( id, ))

        
        posts = []

        #convert rows into a python list
        dataset = db_cursor.fetchall()

        #Iterate through list of data returned
        for row in dataset:

            post = Posts(row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"], row["content"])


            #add post to posts
            posts.append(post.__dict__)


        return json.dumps(posts)
        



# Delete
def delete_post(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM posts
            where id = ?
        """, (id,))




# Edit

def update_post(id, new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE posts
                SET
                    user_id = ?,
                    category_id = ?,
                    title = ?,
                    publication_date = ?,
                    content = ?
            WHERE id = ?
        """, (
            new_post['user_id'],
            new_post['category_id'],
            new_post['title'],
            new_post['publication_date'],
            new_post['content'],
            id,
            ))

        # Were any rows affected?
        # Did the client send an id that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response
        return True


def get_posts_by_tags(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


    # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content
        FROM posts p
        WHERE p.category_id = ?
        """, ( id, ))

        
        posts = []

        #convert rows into a python list
        dataset = db_cursor.fetchall()

        #Iterate through list of data returned
        for row in dataset:

            post = Posts(row["id"], row["user_id"], row["category_id"], row["title"], row["publication_date"], row["content"])


            #add post to posts
            posts.append(post.__dict__)


        return json.dumps(posts)
        