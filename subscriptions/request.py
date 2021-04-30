import sqlite3
import json
from models import Subscriptions

def get_all_subscriptions():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on,
            s.ended_on
        FROM subscriptions s
        """)

        subscriptions = []
        dataset = db_cursor.fetchall()
        for row in dataset :
            subscription = Subscriptions(row['id'], row['follower_id'], row['author_id'], row['created_on'], row['ended_on'])
            subscriptions.append(subscription.__dict__)
    return json.dumps(subscriptions)

def get_single_subscription(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on,
            s.ended_on
        FROM subscriptions s
        WHERE s.id = ?
        """, (id, ))

        dataset = db_cursor.fetchone()
        subscription = Subscriptions(dataset['id'], dataset['follower_id'], dataset['author_id'], dataset['created_on'], dataset['ended_on'])
    return json.dumps(subscription.__dict__)

def create_subscription(new_subscription):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO subscriptions
            (follower_id, author_id, created_on, ended_on)
        VALUES
            (?, ?, ?, ?)
        """, (new_subscription['follower_id'], new_subscription['author_id'], new_subscription['created_on'], new_subscription['ended_on'], ))
        id = db_cursor.lastrowid
        new_subscription['id'] = id
    return json.dumps(new_subscription)

def delete_subscription(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM subscriptions
        WHERE id = ?
        """,(id,))

# def update_subscription(id, updated_subscription):
#     with sqlite3.connect("./rare.db") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         UPDATE subscriptions
#             SET 
#                 label = ?
#         WHERE id = ?
#         """,(updated_subscription['label'], id, ))
        
#         rows_affected = db_cursor.rowcount
#         if rows_affected == 0:
#             return False
#         else:
#             return True