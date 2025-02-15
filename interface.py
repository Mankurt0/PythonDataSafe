from tkinter import *

root = Tk()
root.title('Data safe')
root.geometry("600x500")
#root.resizable(False, False)
root.iconbitmap(default="icon.ico")
root.rowconfigure(index=1, weight=1)
root.columnconfigure(index=1, weight=1)

main_menu = Menu()
create_menu = Menu(tearoff=0)
delete_menu = Menu(tearoff=0)

create_menu.add_command(label="Новая запись")
create_menu.add_command(label="Новое изображение")

delete_menu.add_command(label="Удалить запись")
delete_menu.add_command(label="Удалить изображение")

main_menu.add_command(label="Войти")
main_menu.add_cascade(label="Создать", menu=create_menu)
main_menu.add_cascade(label="Удадить", menu=delete_menu)
main_menu.add_separator()
main_menu.add_command(label="Выход", command=root.destroy)

root.config(menu=main_menu)

label = Label(root, text = 'Пройдите аутентификацию')
label.grid(row = 1, column = 1)

auth = Toplevel()
auth.title('Аутентификация')
auth.geometry("300x250")
#auth.resizable(False, False)
auth.columnconfigure(index=1, weight=1)
auth.rowconfigure(index=1, weight=1)

login = Button(auth, text = 'Войти')
login.grid(row = 1, column = 1, padx=20, pady=20, sticky=NSEW)

register = Button(auth, text = 'Зарегистрироваться')
register.grid(row = 2, column = 1)

close = Button(auth, text = 'Выход', command = root.destroy)
close.grid(row = 3, column = 1)

root.mainloop()