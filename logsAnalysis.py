#!/usr/bin/env python

import psycopg2

dbname = 'news'

db = psycopg2.connect("dbname=news")

c = db.cursor()

# Question 1

c.execute("""
SELECT articles.title, count(*) AS top
FROM articles
JOIN log
ON REPLACE(log.path, '/article/', '') LIKE articles.slug
GROUP BY articles.title
ORDER BY top DESC LIMIT 3
""")

q1 = c.fetchall()

print("\n1. Most popular three articles of all time:")

for article in q1:
    print("{} -- {} views".format(article[0], article[1]))

# Question 2

c.execute("""
SELECT authors.name, count(*) AS top
FROM authors
JOIN articles
ON authors.id = articles.author
JOIN log
ON REPLACE(log.path, '/article/', '') LIKE articles.slug
GROUP BY authors.id
ORDER BY top DESC
""")

q2 = c.fetchall()

print("\n2. Most popular article authors of all time:")

for author, views in q2:
    print("{} -- {} views".format(author, views))


# Question 3

c.execute("""
SELECT error.day, (errors * 100.0 / accesses) AS percent
FROM (SELECT cast(time AS Date) AS day, count(*) AS errors
      FROM log
      WHERE status NOT LIKE '200 %'
      GROUP BY day) AS error
JOIN (SELECT cast(time AS Date) AS day, count(*) AS accesses
      FROM log GROUP BY day) AS access
ON error.day = access.day
WHERE (errors * 100.0 / accesses) > 1
ORDER BY percent DESC
""")

q3 = c.fetchall()

print("\n3. Days when more than 1% of requests lead to errors:")

for day, percent in q3:
    print("{} -- {}%".format(day, percent))

db.close
