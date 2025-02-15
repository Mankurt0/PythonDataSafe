from tkinter import *

def opensignin():
    def get():
        login = login_entry.get()
        password = password_entry.get()
        window.destroy()
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

    login_button = Button(window, text = 'Войти', command=get)
    login_button.grid(row = 0, column = 2, rowspan=2, padx=10, pady=10, ipadx=30, sticky=NSEW)

def opensignup():
    def get():
        login = login_entry.get()
        password = password_entry.get()
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

    login_button = Button(window, text = 'Создать аккаунт', command=get)
    login_button.grid(row = 0, column = 2, rowspan=2, padx=10, pady=10, ipadx=5, sticky=NSEW)



root = Tk()
root.title('Data safe')
root.geometry("600x500")
root.minsize(600, 500)
root.iconbitmap(default="icon.ico")
root.rowconfigure(index=1, weight=1)
root.columnconfigure(index=1, weight=1)

main_menu = Menu()
auth_menu = Menu(tearoff=0)

main_menu.add_cascade(label="Аутентификация", menu=auth_menu)
auth_menu.add_command(label="Войти", command=opensignin)
auth_menu.add_command(label="Зарегистрироваться", command=opensignup)
auth_menu.add_separator()
auth_menu.add_command(label="Выйти")
main_menu.add_separator()
main_menu.add_command(label="Закрыть", command=root.destroy)

root.config(menu=main_menu)

label = Label(root, text = 'Пройдите аутентификацию')
label.grid(row = 1, column = 1)

root.mainloop()