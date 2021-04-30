CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "username" varchar,
  "password" varchar,
  "is_staff" bit,
  "bio" varchar,
  "created_on" date,
  "active" bit
);

INSERT INTO users
    VALUES(1, "Caleb", "James", "calebsjames@gmail.com", "caleb", "123", 1, "I am Caleb", 4/28/2021, 1);
INSERT INTO users
    VALUES(2, "Dylan", "Morris", "dm@gmail.com", "dylan", "123", 1, "I am Dylan, my bio is fine.", 4/26/2021, 1);
INSERT INTO users
    VALUES(3, "Nathan", "Hamilton", "nate@nss.com", "nate", "123", 1, "Nate does not care", 4/25/2021, 1);
INSERT INTO users
    VALUES(4, "Calvin", "Courter", "calvin@gmail.com", "calvin", "123", 1, "I am Calvin, I love bitcoin", 4/24/2021, 1);


CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" DATE,
  "ended_on" DATE,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

INSERT INTO Subscriptions
    VALUES (1, 1, 2, 4/21/2021, 4/28/2021);
INSERT INTO Subscriptions
    VALUES (2, 2, 3, 4/21/2021, 4/28/2021);
INSERT INTO Subscriptions
    VALUES (3, 3, 1, 4/21/2021, 4/28/2021);
INSERT INTO Subscriptions
    VALUES (4, 1, 4, 4/21/2021, 4/28/2021);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" VARCHAR,
  "publication_date" DATE,
  "content" VARCHAR
);

INSERT INTO Posts
    VALUES (1, 1, 1, "This is a title", 4/21/2021, "This is content");
INSERT INTO Posts
    VALUES (2, 1, 1, "This is a another title", 4/21/2021, "This is more content");

UPDATE Posts
SET publication_date = "2021-21-4"
WHERE id = 1;
UPDATE Posts
SET publication_date = "2021-21-4"
WHERE id = 3;

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" VARCHAR,
  "created_on" DATETIME,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

INSERT INTO Comments
    VALUES (1, 1, 1, "This is comment content", 4/28/2021);
INSERT INTO Comments
    VALUES (2, 2, 2, "This is also comment content", 4/28/2021);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" VARCHAR,
  "image_url" VARCHAR
);

INSERT INTO Reactions
    VALUES (1, "Happy", "img_url");
INSERT INTO Reactions
    VALUES (2, "incendiary", "img_url");

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "post_id" INTEGER,
  "reaction_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

INSERT INTO PostReactions
    VALUES (1, 1, 1, 1);
INSERT INTO PostReactions
    VALUES (2, 2, 2, 2);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" VARCHAR
);

INSERT INTO Tags
    VALUES (1, "Tag 1");
INSERT INTO Tags
    VALUES (2, "Tag 2");


CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);


INSERT INTO PostTags
    VALUES (3, 2, 2);
INSERT INTO PostTags
    VALUES (4, 2, 7);
    INSERT INTO PostTags
    VALUES (5, 1, 12);
INSERT INTO PostTags
    VALUES (6, 2, 14);    

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" VARCHAR
);

INSERT INTO Categories
    VALUES (1, "Category A");
INSERT INTO Categories
    VALUES (2, "Category B");


SELECT
    u.id user_id,
    u.first_name,
    u.last_name,
    u.email,
    u.username,
    u.password,
    u.is_staff,
    u.bio,
    u.created_on,
    u.active,
    p.id post_id,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.content,
    s.id subscription_id,
    s.follower_id,
    s.author_id,
    s.created_on,
    s.ended_on,
    c.id comment_id,
    c.post_id,
    c.author_id,
    c.content,
    c.created_on,
    pr.id post_reaction_id,
    pr.user_id,
    pr.post_id,
    pr.reaction_id

FROM Users u

JOIN Posts p
ON p.user_id = u.id

JOIN Subscriptions s
ON s.author_id = u.id

JOIN Comments c
ON c.author_id = u.id

JOIN PostReactions pr
ON pr.user_id = u.id

-- JOIN Subscriptions s
-- ON s.follower_id = u.id



SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content,
            pt.id as pt_id,
            pt.tag_id,
            pt.post_id
        FROM posts p
        JOIN posttags pt on pt.post_id = p.id
        WHERE p.category_id = ?

SELECT 
        pt.id,
        pt.tag_id,
        pt.post_id
    FROM posttags pt        

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
            u.active


        FROM Users as u
    