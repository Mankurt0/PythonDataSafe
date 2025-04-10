import sqlite3
from datetime import date
from tkinter import *
from tkinter import ttk
from cryptography.fernet import Fernet
import bcrypt

def hashpass(password: str) -> bytes:
    """Хэширование пароля"""
    encpassword = password.encode()
    hashedpassword = bcrypt.hashpw(encpassword, bcrypt.gensalt())
    return hashedpassword

def checkhash(password, hashedpassword) -> bool:
    """Сравнение хэша и пароля"""
    encpassword = password.encode()
    if bcrypt.checkpw(encpassword, hashedpassword):
        return True
    else:
        return False



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

def getnotes(user):
    cursor.execute("SELECT text,  date FROM notes WHERE owner = ?", (user,))
    return cursor.fetchall()

def getimages(user):
    cursor.execute("SELECT image,  date FROM images WHERE owner = ?", (user,))
    return cursor.fetchall()



def openmain():
    """Открыть главное окно"""
    currentuser = "testuser"
    root = Tk()
    root.title('Data safe')
    root.geometry("600x500")
    root.minsize(600, 500)
    root.iconbitmap(default="icon.ico")
    """ root.rowconfigure(index=1, weight=1)
    root.columnconfigure(index=1, weight=1) """

    main_menu = Menu()
    auth_menu = Menu(tearoff=0)

    main_menu.add_cascade(label="Аутентификация", menu=auth_menu)
    auth_menu.add_command(label="Войти", command=opensignin)
    auth_menu.add_command(label="Зарегистрироваться", command=opensignup)
    auth_menu.add_separator()
    auth_menu.add_command(label="Выйти")

    root.config(menu=main_menu)

    notebook = ttk.Notebook()
    notebook.grid(row = 0, column = 0, sticky=NSEW)
    textframe = ttk.Frame(notebook)
    imageframe = ttk.Frame(notebook)
    textframe.grid(row = 0, column = 0, sticky=NSEW)
    imageframe.grid(row = 0, column = 0, sticky=NSEW)
    notebook.add(textframe, text="Текст")
    notebook.add(imageframe, text="Изображения")

    texttable = ttk.Treeview(textframe,columns=("text", "date"), show="headings")
    texttable.grid(sticky=NSEW)
    texttable.heading("text", text="Текст")
    texttable.heading("date", text="Дата создания")
    for row in getnotes(currentuser):
        texttable.insert("", END, values=row)

    imagetable = ttk.Treeview(imageframe,columns=("image", "date"), show="headings")
    imagetable.grid(sticky=NSEW)
    imagetable.heading("image", text="Изображение")
    imagetable.heading("date", text="Дата создания")
    for row in getimages(currentuser):
        imagetable.insert("", END, values=row)
    root.mainloop()

def opensignin():
    """Открыть окно выхода"""
    def getinfo():
        global entlogin
        global entpassword
        entlogin = login_entry.get()
        entpassword = password_entry.get()
        cursor.execute("SELECT password FROM users WHERE username = ?", (entlogin,))
        try:
            hashedpassword = cursor.fetchall()[0][0]
            if checkhash(entpassword, hashedpassword):
                print("Правильный пароль") #ВХОД
                window.destroy()
                global currentuser
                currentuser = entlogin
            else:
                print("Неверный пароль")
                password_entry.delete(0, END)
        except IndexError:
            print("Неверный логин")
    window = Toplevel()
    window.title('Вход')
    window.geometry("400x100")
    window.minsize(400, 100)
    window.resizable(True, False)
    window.columnconfigure(index=0, weight=0)
    window.columnconfigure(index=1, weight=1)
    window.columnconfigure(index=2, weight=0)
    window.rowconfigure(index=0, weight=1)
    window.rowconfigure(index=1, weight=1)

    login_label = Label(window, text = 'Логин:')
    login_label.grid(row = 0, column = 0)

    password_label = Label(window, text = 'Пароль:')
    password_label.grid(row = 1, column = 0)

    login_entry = Entry(window)
    login_entry.grid(row = 0, column = 1, padx=10, pady=10, sticky=EW)

    password_entry = Entry(window)
    password_entry.grid(row = 1, column = 1, padx=10, pady=10, sticky=EW)

    login_button = Button(window, text = 'Войти', command=getinfo)
    login_button.grid(row = 0, column = 2, rowspan=2, padx=10, pady=10, ipadx=30, sticky=NSEW)

def opensignup():
    """Открыть окно регистрации"""
    def getinfo():
        global entlogin
        global entpassword
        entlogin = login_entry.get()
        entpassword = password_entry.get()
        try:
            adduser(entlogin, entpassword)
            window.destroy()
        except sqlite3.IntegrityError:
            print("Такой логин уже существует")
    window = Toplevel()
    window.title('Регистрация')
    window.geometry("400x100")
    window.minsize(400, 100)
    window.resizable(True, False)
    window.columnconfigure(index=0, weight=0)
    window.columnconfigure(index=1, weight=1)
    window.columnconfigure(index=2, weight=0)
    window.rowconfigure(index=0, weight=1)
    window.rowconfigure(index=1, weight=1)

    login_label = Label(window, text = 'Логин:')
    login_label.grid(row = 0, column = 0)

    password_label = Label(window, text = 'Пароль:')
    password_label.grid(row = 1, column = 0)

    login_entry = Entry(window)
    login_entry.grid(row = 0, column = 1, padx=10, pady=10, sticky=EW)

    password_entry = Entry(window)
    password_entry.grid(row = 1, column = 1, padx=10, pady=10, sticky=EW)

    login_button = Button(window, text = 'Создать аккаунт', command=getinfo)
    login_button.grid(row = 0, column = 2, rowspan=2, padx=10, pady=10, ipadx=5, sticky=NSEW)



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

openmain()

connection.close()