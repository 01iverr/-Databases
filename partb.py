import psycopg2
import matplotlib.pyplot as plt

# Update connection string information
host = "3190003-3190167.postgres.database.azure.com"
dbname = "postgres"
user = "who_is_the_admin@3190003-3190167"
password = "N00NEGETOVERIT!"
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()
cursor.execute("select genres from movies_metadata;") ##limit 10
genresget = cursor.fetchall()
genres = set()
###############

genres = set()
for i in genresget:
    words = str(i).split("}")
    del words[-1]
    for j in words:
        gen = j.split(":")[2][2:-1:]
        genres.add(gen)

print("\nQuery 1")
cursor.execute("SELECT extract(year from release_date) as year, COUNT(*) FROM MOVIES_METADATA GROUP BY year order by year;")
query1 = cursor.fetchall()
x = []
y = []
k=0
for i in query1:
    x.append(i[0])
    y.append(i[1])
    k += 1
plt.figure(figsize=(14.080, 7.080), dpi = 100)
plt.scatter(x,y, color = "#123456")
plt.title("Query 1", color ="#654321")
plt.xlabel("Year")
plt.ylabel("Number Movies")
plt.savefig("Query 1.png", dpi = 1000)
plt.show()
print("Execute correct")


#########################################################################
print("\nQuery 2")
cat = []
num = []
for i in genres :
    cursor.execute("SELECT COUNT(id) FROM Movies_metadata where genres like '%" + i + "%';")
    cat.append(i)
    num.append(str(cursor.fetchall()[0])[1:-2:])

plt.figure(figsize=(14.080, 7.080), dpi = 100)
plt.scatter(num,cat,color ="#565039")
plt.title("Query 2", color ="#565039")
plt.ylabel("Categories")
plt.xlabel("Number Movies")
plt.savefig("Query 2.png", dpi = 1000)
plt.show()
print("Execute correct")

#################################################################################################
print("\nQuery 3")
b= 105090  #gia allagh xrwmatos 
for i in genres :
    year = []
    num = []
    cursor.execute("SELECT extract (year from release_date) as year ,COUNT(id) FROM Movies_metadata where genres like '%" + i + "%' group by year order by year;")
    q3 = cursor.fetchall()
    for j in q3:
        year.append(j[0])
        num.append(j[1])
    b+=25899 #gia allagh xrwmatos
    plt.figure(figsize=(14.080, 7.080), dpi = 100)
    plt.title("Query 3 "+ str(i), color ="black")
    plt.xlabel("Year")
    plt.ylabel("Number Movies")
    plt.scatter(year,num, color ="#"+str(b))
    plt.savefig("Query 3 "+str(i)+".png", dpi = 1000)
    plt.show()
print("Execute correct")
##
#########################################################################################
print("\nQuery 4")
cat = []
count = []
for i in genres :
    cursor.execute("SELECT round(cast(avg(rating) as numeric), 2) FROM Ratings join links on ratings.movieid = links.movieid join movies_metadata on movies_metadata.imdb_id = links.imdbid where genres like '%" + i + "%';")
    cat.append(i)
    count.append(str(cursor.fetchall()[0])[10:-4:])
plt.figure(figsize=(14.080, 7.080), dpi = 100)
plt.title("Query 4", color = "#894361")
plt.ylabel("Categories")
plt.xlabel("Number Movies")
plt.scatter(count, cat, color = "#894361")
plt.savefig("Query 4.png", dpi = 1000)
plt.show()
print("Execute correct")
##
#####################################################################################
print("\nQuery 5")
cursor.execute("SELECT userid , COUNT(rating) FROM Ratings GROUP BY userid order by userid;")
user_id = []
count = []
for i in cursor.fetchall():
    user_id.append(i[0])
    count.append(i[1])
plt.figure(figsize=(14.080, 7.080), dpi = 100)
plt.title("Query 5", color = "#315182")
plt.ylabel("User")
plt.xlabel("Number Ratings")
plt.scatter(user_id, count, color = "#315182")
plt.savefig("Query 5.png", dpi = 1000)
plt.show()
print("Execute correct")
##
##############################################################################    
print("\nQuery 6")
cursor.execute("SELECT userid , round(cast(avg(rating) as numeric), 2) FROM Ratings GROUP BY userid order by userid;")
user_id = []
avg = []
for i in cursor.fetchall():
    user_id.append(i[0])
    avg.append(i[1])
plt.figure(figsize=(14.080, 7.080), dpi = 100)
plt.title("Query 6", color = "#761325")
plt.xlabel("User")
plt.ylabel("Number AVG Ratings")
plt.scatter(user_id, avg, color = "#761325")
plt.savefig("Query 6.png", dpi = 1000)
plt.show()
print("Execute correct")

#######################################################################
print("Query 7")
cursor.execute("select * from table_view;")
usid = []
avg = []
count = []
q7 = cursor.fetchall()
for i in q7:
    usid.append(i[0])
    avg.append(float(i[2]))
    count.append(i[1])

fig = plt.figure(figsize=(14.080, 7.080), dpi = 100)
ax = fig.add_subplot(projection='3d')
plt.title("Query 7", color = "#268560")
plt.xlabel("User", color = "#157805")
plt.ylabel("Number AVG Ratings", color = "#069351")
ax.set_zlabel("Total Ratings", color = "#057072")
ax.scatter(usid,avg,count, color = "#141293")
plt.savefig("Query 7.png", dpi = 1000)
plt.show() 
print("Execute correct")

# Clean up
conn.commit()
cursor.close()
conn.close()
