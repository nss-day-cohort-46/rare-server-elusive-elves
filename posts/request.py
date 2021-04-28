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