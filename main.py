""" 
Шифрование
"""
import sqlite3
import bcrypt
from datetime import datetime
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo
from cryptography.fernet import Fernet
from PIL import Image
from os import path, remove

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
    """, (user, text, datetime.now()))
    connection.commit()
    update()
def addimage(user, image, imagename):
    """Добавление изображения в таблицу images без шифрования"""
    cursor.execute("""
    INSERT INTO "main"."images"
    ("owner", "image", "date", "imagename")
    VALUES (?, ?, ?, ?);
    """, (user, image, datetime.now(), imagename))
    connection.commit()
    update()

def getnotes(user):
    """Получение данных об записях для таблицы из БД"""
    cursor.execute("SELECT text,  date FROM notes WHERE owner = ?", (user,))
    return cursor.fetchall()
def getimages(user):
    """Получение данных об изображениях для таблицы из БД"""
    cursor.execute("SELECT imagename,  date FROM images WHERE owner = ?", (user,))
    return cursor.fetchall()
def update():
    """Обновление данных таблиц"""
    texttable.delete(*texttable.get_children())
    for row in getnotes(currentuser):
        texttable.insert("", END, values=row)
    imagetable.delete(*imagetable.get_children())
    for row in getimages(currentuser):
        imagetable.insert("", END, values=row)

def opensignin():
    """Открыть окно выхода"""
    def getinfo():
        global entlogin
        global entpassword
        entlogin = loginentry.get()
        entpassword = passwordentry.get()
        cursor.execute("SELECT password FROM users WHERE username = ?", (entlogin,))
        try:
            hashedpassword = cursor.fetchall()[0][0]
            if checkhash(entpassword, hashedpassword):
                window.destroy()
                global currentuser
                currentuser = entlogin
                update()
            else:
                showinfo(message="Неверный пароль")
                passwordentry.delete(0, END)
        except IndexError:
            showinfo(message="Неверный логин")
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

    loginlabel = Label(window, text = 'Логин:')
    loginlabel.grid(row = 0, column = 0)
    passwordlabel = Label(window, text = 'Пароль:')
    passwordlabel.grid(row = 1, column = 0)
    loginentry = Entry(window)
    loginentry.grid(row = 0, column = 1, padx=10, pady=10, sticky=EW)
    passwordentry = Entry(window)
    passwordentry.grid(row = 1, column = 1, padx=10, pady=10, sticky=EW)
    loginbutton = Button(window, text = 'Войти', command=getinfo)
    loginbutton.grid(row = 0, column = 2, rowspan=2, padx=10, pady=10, ipadx=30, sticky=NSEW)
def opensignup():
    """Открыть окно регистрации"""
    def getinfo():
        global entlogin
        global entpassword
        entlogin = loginentry.get()
        entpassword = passwordentry.get()
        try:
            adduser(entlogin, entpassword)
            window.destroy()
        except sqlite3.IntegrityError:
            showinfo(message="Такой логин уже существует")
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

    loginlabel = Label(window, text = 'Логин:')
    loginlabel.grid(row = 0, column = 0)
    passwordlabel = Label(window, text = 'Пароль:')
    passwordlabel.grid(row = 1, column = 0)
    loginentry = Entry(window)
    loginentry.grid(row = 0, column = 1, padx=10, pady=10, sticky=EW)
    passwordentry = Entry(window)
    passwordentry.grid(row = 1, column = 1, padx=10, pady=10, sticky=EW)
    loginbutton = Button(window, text = 'Создать аккаунт', command=getinfo)
    loginbutton.grid(row = 0, column = 2, rowspan=2, padx=10, pady=10, ipadx=5, sticky=NSEW)
def signout():
    """Выход из учетной записи"""
    global currentuser
    currentuser = "testuser"
    update()

def openaddnote():
    if currentuser == "testuser":
        showinfo(message="Выход не выполнен")
    else:
        window = Toplevel()
        window.title("Добавление записи")
        window.geometry("300x80")
        window.minsize(300, 80)
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)
        window.resizable(True, False)

        textentry = Entry(window)
        textentry.grid(column=0, row=0, sticky=EW, padx=10, pady=10)
        addnotebtn = Button(window, text="Добавить запись", command=lambda: addnote(currentuser, textentry.get()))
        addnotebtn.grid(column=0, row=1, sticky=NSEW, padx=10, pady=10)
def openaddimage():
    if currentuser == "testuser":
        showinfo(message="Выход не выполнен")
    else:
        imagepath = filedialog.askopenfilename()
        imagename = path.basename(imagepath).split('/')[-1]
        with open(imagepath, 'rb') as file:
            blobdata = file.read()
        addimage(currentuser, blobdata, imagename)

def textselected(event):
    """Выбор выделенных записей"""
    global textvalues
    textvalues = []
    for selecteditem in texttable.selection():
        item = texttable.item(selecteditem)
        textvalues = item["values"]
def imageselected(event):
    """Выбор выделенных изображений"""
    global imagevalues
    imagevalues = []
    for selecteditem in imagetable.selection():
        item = imagetable.item(selecteditem)
        imagevalues = item["values"]
def viewimage():
    """Просмотр изображения"""
    cursor.execute("SELECT image FROM images WHERE owner = ? AND imagename = ? AND date = ?", (currentuser, imagevalues[0], imagevalues[1]))
    with open("tempimage", 'wb') as file:
        file.write(cursor.fetchall()[0][0])
    tempimage = Image.open("tempimage")
    tempimage.show()
    remove("tempimage")
def deletenote():
    """Удаление выбранной записи"""
    cursor.execute("DELETE FROM notes WHERE owner = ? AND text = ? AND date = ?", (currentuser, textvalues[0], textvalues[1]))
    connection.commit()
    update()
def deleteimage():
    """Удаление выбранного изображения"""
    cursor.execute("DELETE FROM images WHERE owner = ? AND imagename = ? AND date = ?", (currentuser, imagevalues[0], imagevalues[1]))
    connection.commit()
    update()

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
        "imagename"	TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT),
        FOREIGN KEY("owner") REFERENCES "users"("username")
    );
    """)

currentuser = "testuser"
root = Tk()
root.title('Data safe')
root.geometry("600x500")
root.minsize(600, 500)
root.grid_columnconfigure(index=0, weight=1)
root.grid_rowconfigure(index=0, weight=1)

mainmenu = Menu()
authmenu = Menu(tearoff=0)
mainmenu.add_cascade(label="Аутентификация", menu=authmenu)
authmenu.add_command(label="Войти", command=opensignin)
authmenu.add_command(label="Зарегистрироваться", command=opensignup)
authmenu.add_separator()
authmenu.add_command(label="Выйти", command=signout)
root.config(menu=mainmenu)

notebook = ttk.Notebook()
notebook.grid(row = 0, column = 0, sticky=NSEW)
texttab = ttk.Frame(notebook)
imagetab = ttk.Frame(notebook)
notebook.add(texttab, text="Текст")
notebook.add(imagetab, text="Изображения")

texttab.grid_columnconfigure(index=0, weight=1)
texttab.grid_columnconfigure(index=1, weight=1)
texttab.grid_columnconfigure(index=2, weight=1)
texttab.grid_rowconfigure(index=0, weight=1)
texttab.grid_rowconfigure(index=1, weight=0)

imagetab.grid_columnconfigure(index=0, weight=1)
imagetab.grid_columnconfigure(index=1, weight=1)
imagetab.grid_columnconfigure(index=2, weight=1)
imagetab.grid_rowconfigure(index=0, weight=1)
imagetab.grid_rowconfigure(index=1, weight=0)

texttable = ttk.Treeview(texttab,columns=("text", "date"), show="headings")
texttable.grid(row=0, column=0, columnspan=3, sticky=NSEW)
texttable.heading("text", text="Текст")
texttable.heading("date", text="Время создания")
texttable.bind("<<TreeviewSelect>>", textselected)

imagetable = ttk.Treeview(imagetab,columns=("image", "date"), show="headings")
imagetable.grid(row=0, column=0, columnspan=3, sticky=NSEW)
imagetable.heading("image", text="Изображение")
imagetable.heading("date", text="Время создания")
imagetable.bind("<<TreeviewSelect>>", imageselected)

addtextbtn = Button(texttab, text="Добавить", command=openaddnote)
addtextbtn.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)
viewtextbtn = Button(texttab, text="Открыть")
viewtextbtn.grid(row= 1, column=1, padx=10, pady=10, sticky=NSEW)
deltextbtn = Button(texttab, text="Удалить", command=deletenote)
deltextbtn.grid(row=1, column=2, padx=10, pady=10, sticky=NSEW)

addimagebtn = Button(imagetab, text="Добавить", command=openaddimage)
addimagebtn.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)
viewimagebtn = Button(imagetab, text="Открыть", command=viewimage)
viewimagebtn.grid(row= 1, column=1, padx=10, pady=10, sticky=NSEW)
delimagebtn = Button(imagetab, text="Удалить", command=deleteimage)
delimagebtn.grid(row=1, column=2, padx=10, pady=10, sticky=NSEW)

root.mainloop()
connection.close()