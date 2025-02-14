from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Data safe')
root.geometry("600x500")
root.resizable(False, False)
root.iconbitmap(default="icon.ico")

label = Label(root, text = 'Пройдите аутентификацию')
label.grid(row = 1, column = 1)

auth = Toplevel()
auth.title('Аутентификация')
auth.geometry("300x250")
auth.resizable(False, False)

login = Button(auth, text = 'Войти')
login.grid(row = 1, column = 1)

register = Button(auth, text = 'Зарегистрироваться')
register.grid(row = 2, column = 1)

close = Button(auth, text = 'Выход', command = root.destroy)
close.grid(row = 4, column = 1)

root.mainloop()