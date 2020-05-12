from pymongo import MongoClient
import mysql.connector
from time import perf_counter

start = perf_counter()

mydbMariaDb = mysql.connector.connect(
  host="10.100.100.120",
  user="root",
  passwd="root",
  database="bababanych"
)

cursor = mydbMariaDb.cursor()

cursor.execute("SELECT * FROM znaki")

fetchStart = perf_counter()

stringsMariaDb = cursor.fetchall()

fetchEnd = perf_counter()

print("czas: " + str(fetchEnd - fetchStart) + " s")

client = MongoClient("10.100.100.110")

mydbMongo = client['mydb']

daneMongo = mydbMongo.strings

stringList = [{"id": string[0], "nazwa": string[1]} for string in stringsMariaDb]

result = daneMongo.insert_many(stringList)

insertEnd = perf_counter()

print(str(len(result.inserted_ids)) + " rekordow dodanych, czas: " + str(insertEnd - fetchEnd) + " s")

stop = perf_counter()

print("Czas wykonania: " + str(stop - start) + " s")
