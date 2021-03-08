from tkinter import *
from tkinter import messagebox

# here we working with Tkinter
root = Tk()
root.geometry('300x200')
root.title('Social Media')
root.wm_attributes('-alpha', 0.99)
root['bg'] = '#282828'


""" Check function """

# check Function
def check(event):
    Login = login.get()
    Password = password.get()

    if Login and Password:
        messagebox.showinfo('Success', 'Авторизация прошла успешно')
    elif not Login and Password:
        messagebox.showerror('Error 0002bх251', 'Необходимо ввести логин')
    elif not Password and Login:
        messagebox.showerror('Error 00032bx750', 'Необходимо ввести пароль')
    if not Login and not Password:
        messagebox.showerror('Critical Error 000x571', 'Введите логин и пароля для авторизации')


""" Главная часть """
text_login = Label(text='Login',
                   font='Roboto 15',
                   fg='#FF9C09',
                   pady='2',
                   bg='#282828')
login = Entry(root, font='Consolas 15',
              fg='white',
              bg='#48494f',
              relief='solid',
              justify='center')

text_password = Label(text='Password',
                      font='Roboto 15',  # Label - это текст, а Entry - это функция input()
                      fg='#FF9C09',
                      pady='2',
                      bg='#282828')
password = Entry(root, font='Consolas 15',
                 fg='white',
                 bg='#48494f',
                 relief='solid',
                 justify='center',
                 show='*')

check_status = Checkbutton(text='Запомнить меня',
                           font='Roboto 13',
                           bg='#282828',
                           fg='white',
                           activebackground='#282828',
                           activeforeground='#282828')

enter = Button(text='Войти в аккаунт',
               font='Roboto 12',
               bg='#FF9C09',
               width='20',
               height='1')

""" Упаковка """
text_login.pack()
login.pack()

text_password.pack()
password.pack()

check_status.pack()

enter.pack()

enter.bind('<Button-1>', check)

root.mainloop()
