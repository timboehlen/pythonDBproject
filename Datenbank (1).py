from ast import While
import mysql.connector
from mysql.connector import Error
import pandas as pd
import re

pattern_name = '[A-Z][a-z]{3,20}'
pattern_duration = '[0-10][[:upper:]]'
pattern_gender = '[Male][Female]'
pattern_doc = '{0-2022][.upper.]'


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythonproject"
)


mycursor = mydb.cursor()

print("Herzlich Willkommen zu unserer Musikapplikation. Bitte wählen Sie mit 1 oder 2 aus, welches Objekt Sie erstellen wollen. Die 1 ist für einen Song und die 2 für einen Artist.")

objectchoice = input("Bitte geben Sie eine Zahl ein: ")

if objectchoice == "1": 
    print("Sie wollen einen Song erstellen")

    namesong = input("Bitte geben Sie den Namen des Songs ein: ")
    durationsong = input("Bitte geben Sie die Dauer des Songs ein: ")
    genresong = input("Bitte geben Sie das Genre des Songs ein: ")

    val = (namesong, durationsong, genresong)

    re.match(pattern_name, namesong)
    re.match(pattern_name, genresong)
    re.match(pattern_duration, str(durationsong)
    )

    sql = "INSERT INTO song (name, duration, genre) VALUES (%s, %s, %s)"
else:
    print("Sie wollen einen Artist erstellen")

    nameartist = input("Bitte geben Sie den Namen des Artisten ein: ")
    genderartist = input("Bitte geben Sie das Geschlecht des Artisten ein(Male, Female): ")
    docartist = input("Bitte geben Sie das Erstellungsdatum des Artisten ein: ")

    val = (nameartist, genderartist, docartist)

    re.match(pattern_name, nameartist)
    re.match(pattern_gender, genderartist)
    re.match(pattern_doc, docartist)

    sql = "INSERT INTO artist (name, gender, date_of_creation) VALUES (%s, %s, %s)"

mycursor.execute(sql, val)

mydb.commit()

