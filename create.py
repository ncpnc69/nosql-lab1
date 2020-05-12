from time import perf_counter
from random import choice
import mysql.connector
from string import ascii_uppercase, digits

N = int(input("Enter N value: "))

def id_generator(size=20, chars=ascii_uppercase + digits):
    return ''.join(choice(chars) for _ in range(size))
start = perf_counter()

try:
    mydb = mysql.connector.connect(
      host="10.100.100.120",
      user="root",
      passwd="root",
      database="bababanych"
    )
except:
    mydb = mysql.connector.connect(
      host="10.100.100.120",
      user="root",
      passwd="root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE bababanych")
    mydb.commit()
    mydb = mysql.connector.connect(
      host="10.100.100.120",
      user="root",
      passwd="root",
      database="bababanych"
    )

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE TABLE znaki (id INT NOT NULL AUTO_INCREMENT, nazwa VARCHAR(30) NOT NULL, PRIMARY KEY(id))")
except:
    print("tabela istnieje")

mydb.commit()

sql = "INSERT INTO znaki (nazwa) VALUES (%s)"

randomDict = {}

while len(randomDict) < (10 ** N):
    randomDict[id_generator()] = 1

items = []

for car in randomDict:
    items.append((car,))

if N > 5:
    step = (N-5) ** 10
    for i in range(step):
        start = (10 ** 5) * i
        stop = (10 ** 5) * (i+1)
        mycursor.executemany(sql, items[start:stop])
        mydb.commit()
        print("step " + str(i) + " done")
else:
    mycursor.executemany(sql, items)
    mydb.commit()

stop = perf_counter()
print(str(mycursor.rowcount) + " dodanych rekordow.")
print("Czas wykonania: " + str(stop - start) + " s")
