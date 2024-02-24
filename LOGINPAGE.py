from tkinter import *
import pymysql
from tkinter import messagebox


# Functional
def username_on_enter(e):
    usernameEntry.delete(0, 'end')


def username_on_leave(e):
    if usernameEntry.get() == '':
        usernameEntry.insert(0, 'Username')


def password_on_enter(e):
    passwordEntry.delete(0, 'end')


def password_on_leave(e):
    if passwordEntry.get() == '':
        passwordEntry.insert(0, 'Password')


def hide():
    pass


# openEye.config(file='closEye.png')
# passwordEntry.config(show='*')
# eyeButton.config(command=show)


def show():
    pass


# openEye.config(file='openEye.png')
# passwordEntry.config(show='')
# eyeButton.config(command=hide)

def open_signuppage():
    window.destroy()
    import signUp


def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='apunda2001')
            cursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue,Please Try Again')
            return

        query = 'use userdata'
        cursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        cursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            messagebox.showinfo('Success', 'Login is successful')


def forget_pass():
    import forgotpassword


# GUI part
window = Tk()
window.title('Login Page')
window.geometry('925x500+300+200')
window.config(bg='#fff')
window.resizable(False, False)

img = PhotoImage(file='login.png')
Label(window, image=img, bg='white', ).place(x=50, y=50)

frame = Frame(window, width=350, height=350, bg="white")
frame.place(x=500, y=70)

heading = Label(frame, text='USER LOGIN', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
######### --------------------------------------------------------------------------------
usernameEntry = Entry(frame, width=25, fg='black', border=0, bg='white',
                      font=('Microsoft YaHei UI Light', 11))
usernameEntry.place(x=30, y=80)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', username_on_enter)
usernameEntry.bind('<FocusOut>', username_on_leave)

Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=107)
######### --------------------------------------------------------------------------------
passwordEntry = Entry(frame, width=25, fg='black', border=0, bg='white',
                      font=('MMicrosoft YaHei UI Light', 11))
passwordEntry.place(x=30, y=150)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_on_enter)
passwordEntry.bind('<FocusOut>', password_on_leave)
######### --------------------------------------------------------------------------------
# openEye = PhotoImage(file='open_eye.png')
# eyeButton = Button(frame, image=openEye, bd=0, bg="white", activebackground='white',
# cursor='hand2', command=hide)
# eyeButton.place(x=300, y=250)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
######### --------------------------------------------------------------------------------
forgetButton = Button(frame, text='Forget Password?', bd=0, bg="white", activebackground='white',
                      cursor='hand2', font=('Microsoft YaHei UI Light', 9, 'bold'), fg='#57a1f8',
                      activeforeground='#57a1f8', command=forget_pass)
forgetButton.place(x=210, y=183)
######### --------------------------------------------------------------------------------
loginButton = Button(frame, width=39, pady=7, text='Log in', bg='#57a1f8', cursor='hand2',
                     fg='white', border=0, command=login_user)
loginButton.place(x=35, y=222)
######### --------------------------------------------------------------------------------
label = Label(frame, text="Don't have an account?", fg='black', bg='white',
              font=('Microsoft YeHei UI Light', 9))
label.place(x=75, y=270)
sign_up = Button(frame, width=5, text='Sign up', border=0, bg='white', cursor='hand2',
                 fg='#57a1f8', font=('Open Sans', 9, 'bold underline'), command=open_signuppage)
sign_up.place(x=215, y=270)
######### --------------------------------------------------------------------------------
window.mainloop()
