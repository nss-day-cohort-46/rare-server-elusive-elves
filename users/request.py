import json
import sqlite3
from models import Users
from models import Posts
from models import Comments
from models import Subscriptions
# from models import PostReactions


def get_all_users():
    #open connection
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #SQL query
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.username,
            u.password,
            u.is_staff,
            u.bio,
            u.created_on,
            u.active,
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content,
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on,
            s.ended_on,
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.created_on


        FROM Users as u

        JOIN Posts p
        ON p.user_id = u.id

        JOIN Subscriptions s
        ON s.author_id = u.id

        JOIN Comments c
        ON c.author_id = u.id


        """)

        #Initialize an empty list for users
        users = []

        #convert rows into a python list
        dataset = db_cursor.fetchall()

        #Iterate through list of data returned
        for row in dataset:

            #create a user instance from current row
            user = Users(row['id'], row['first_name'], row['last_name'], row['email'],
                            row['username'], row['password'], row['is_staff'], row['bio'], row['created_on'], row['active'])

            #created joined instances
            post = Posts(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['content'])
            comment = Comments(row['id'], row['id'], row['author_id'], row['content'], row['created_on'])
            subscription = Subscriptions(row['id'], row['follower_id'], row['author_id'], row['created_on'], row['ended_on'])
            # postReaction = PostReaction(row['postReaction_id'], row['postReaction_user_id'], row['postReaction_post_id'], row['postReaction_reaction_id'])
           
            #add the new dictionaries to user instance
            user.post = post.__dict__
            user.comment = comment.__dict__
            user.subscription = subscription.__dict__
            # user.postReaction = postReaction.__dict__
           
            #add user to users
            users.append(user.__dict__)

        #return the data
        return json.dumps(users)





# def get_all_users():
#     #open connection
#     with sqlite3.connect("./rare.db") as conn:

#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         #SQL query
#         db_cursor.execute("""
#         SELECT
#             u.id user_id,
#             u.first_name,
#             u.last_name,
#             u.email,
#             u.username,
#             u.password,
#             u.is_staff,
#             u.bio,
#             u.created_on,
#             u.active,
#             p.id post_id,
#             p.user_id,
#             p.category_id,
#             p.title,
#             p.publication_date,
#             p.content,
#             s.id subscription_id,
#             s.follower_id,
#             s.author_id,
#             s.created_on,
#             s.ended_on,
#             c.id comment_id,
#             c.post_id,
#             c.author_id,
#             c.content,
#             c.created_on,
#             pr.id post_reaction_id,
#             pr.user_id,
#             pr.post_id,
#             pr.reaction_id

#         FROM Users u

#         JOIN Posts p
#         ON p.user_id = u.id

#         JOIN Subscriptions s
#         ON s.author_id = u.id

#         JOIN Comments c
#         ON c.author_id = u.id

#         JOIN PostReactions pr
#         ON pr.user_id = u.id
#         """)

#         #Initialize an empty list for users
#         users = []

#         #convert rows into a python list
#         dataset = db_cursor.fetchall()

#         #Iterate through list of data returned
#         for row in dataset:

#             #create a user instance from current row
#             user = Users(row['id'], row['first_name'], row['last_name'], row['email'],
#                             row['username'], row['password'], row['is_staff'], row['bio'], row['created_on'], row['active'])

#             #created joined instances
#             post = Post(row['post_id'], row['post_user_id'], row['post_category_id'], row['title'], row['publication_date'], row['content'])
#             comment = Comment(row['comment_id'], row['post_id'], row['author_id'], row['content'], row['created_on'])
#             subscription = Subscription(row['subscription_id'], row['subscription_follower_id'], row['subscription_author_id'], row['subscription_created_on'], row['subscription_ended_on'])
#             postReaction = PostReaction(row['postReaction_id'], row['postReaction_user_id'], row['postReaction_post_id'], row['postReaction_reaction_id'])

#             #add the new dictionaries to user instance
#             user.post = post.__dict__
#             user.comment = comment.__dict__
#             user.subscription = subscription.__dict__
#             user.postReaction = postReaction.__dict__

#             #add user to users
#             users.append(user.__dict__)

#         #return the data
#         return json.dumps(users)