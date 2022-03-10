import sqlite3
con = sqlite3.connect("my_favourite_movies")

cur = con.cursor()

query = "select * from movies where actor = 'Robert Pattinson'"

cur.execute(query)
data = cur.fetchall()

for d in data:
    print(d)

cur.close()
con.close()
