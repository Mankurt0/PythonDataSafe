import sqlite3
from datetime import date
from crypto import hashpass

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

#Создание таблицы users
cursor.execute("""
CREATE TABLE IF NOT EXISTS "users" (
	"username"	TEXT NOT NULL UNIQUE,
	"password"	BLOB NOT NULL,
	PRIMARY KEY("username")
);
""")

#Создание таблицы notes
cursor.execute("""
CREATE TABLE IF NOT EXISTS "notes" (
	"id"	INTEGER NOT NULL UNIQUE,
	"owner"	TEXT NOT NULL,
	"text"	TEXT,
	"date"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("owner") REFERENCES "users"("username")
);
""")

#Создание таблицы images
cursor.execute("""
CREATE TABLE IF NOT EXISTS "images" (
	"id"	INTEGER NOT NULL UNIQUE,
	"owner"	TEXT NOT NULL,
	"image"	BLOB,
	"date"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("owner") REFERENCES "users"("username")
);
""")

def adduser(login: str, password: str):
    """Добавление пользователя в таблицу users"""
    hpassword = hashpass(password)
    cursor.execute("""
INSERT INTO "main"."users"
("username", "password")
VALUES (?, ?);
""", (login, hpassword))
    connection.commit()

def addnote(user, text):
    """Добавление записи в таблицу notes без шифрования"""
    cursor.execute("""
INSERT INTO "main"."notes"
("owner", "text", "date")
VALUES (?, ?, ?);
""", (user, text, date.today()))
    connection.commit()

def addimage(user, image):
    """Добавление изображения в таблицу images без шифрования"""
    cursor.execute("""
INSERT INTO "main"."images"
("owner", "image", "date")
VALUES (?, ?, ?);
""", (user, image, date.today()))
    connection.commit()
    
adduser("Юзерь", "Паролб")
addnote("Юзерь", "техть")
addimage("Юзерь", "ымаге")
connection.close()
