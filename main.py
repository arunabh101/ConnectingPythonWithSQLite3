import sqlite3

con = sqlite3.connect("my_favourite_movies")

print("Enter the name of the movie: ")
nm = input()
print("Enter the name of the actor: ")
ac = input()
print("Enter the name of the actress: ")
acc = input()
print("Enter the name of the director: ")
dc = input()
print("Enter the year in which the movie was released: ")
yr = input()

query = "insert into movies(name,actor,actress,director,year) values(" + "'" + nm + "','" + ac + "','" + acc + "','" + dc + "'," + yr + ")"
con.execute(query)
con.commit()
con.close()
print("Data saved...")
