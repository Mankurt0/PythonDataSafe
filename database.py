import sqlite3
from datetime import date

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

#Создание таблицы users
cursor.execute("""
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"login"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
""")

#Создание таблицы notes
cursor.execute("""
CREATE TABLE IF NOT EXISTS "notes" (
	"id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"text"	TEXT NOT NULL,
	"date"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
""")

#Создание таблицы images
cursor.execute("""
CREATE TABLE IF NOT EXISTS"images" (
	"id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"image"	TEXT NOT NULL,
	"date"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
""")

def adduser(login: str, password: str):
    """Добавление пользователя в таблицу users без шифрования"""
    
    cursor.execute("""
INSERT INTO "main"."users"
("login", "password")
VALUES (?, ?);
""", (login, password))
    connection.commit()

def addnote(user_id, text):
    """Добавление записи в таблицу notes без шифрования"""
    cursor.execute("""
INSERT INTO "main"."notes"
("user_id", "text", "date")
VALUES (?, ?, ?);
""", (user_id, text, date.today()))
    connection.commit()

def addimage(user_id, image):
    """Добавление изображения в таблицу images без шифрования"""
    cursor.execute("""
INSERT INTO "main"."images"
("user_id", "image", "date")
VALUES (?, ?, ?);
""", (user_id, image, date.today()))
    connection.commit()
    
adduser("Юзерь", "Паролб")
addnote(1, "техть")
addimage(1, "ымаге")
connection.close()
