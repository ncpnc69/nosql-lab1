import mysql.connector
from pymongo import MongoClient
from time import perf_counter
import random

start = perf_counter()

mydb = mysql.connector.connect(
  host="10.100.100.120",
  user="root",
  passwd="root",
  database="bababanych"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM znaki")

print("Pobieranie danych z MariaDb")

fetchStart = perf_counter()

stringsTable1 = mycursor.fetchall()

fetchEnd = perf_counter()

print("Czas pobierania: " + str(fetchEnd - fetchStart) + " s")

try:
    mycursor.execute("CREATE TABLE znaki (id INT NOT NULL AUTO_INCREMENT, nazwa VARCHAR(30) NOT NULL, PRIMARY KEY(id))")
except:
    print("tabela istnieje")
mydb.commit()

mycursor.execute("SELECT COUNT(*) FROM znaki")

stringsCount = mycursor.fetchall()[0][0]

sql = "INSERT INTO znaki (nazwa) VALUES (%s)"

i = 0

while i < stringsCount:
    random = random.choice(stringsTable1)[1]
    mycursor.execute("SELECT * FROM znaki WHERE nazwa = '" + random + "'")
    result = mycursor.fetchall()
    if len(result) == 0:
        mycursor.execute("INSERT INTO znaki (nazwa) VALUES ('" + random + "')")
        mydb.commit()
        i += 1
stop = perf_counter()
print("Czas wykonania: " + str(stop - start) + " s")
