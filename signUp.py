import pymysql
from tkinter import *
from tkinter import messagebox


# Functional
def email_on_enter(e):
    emailEntry.delete(0, 'end')


def email_on_leave(e):
    if emailEntry.get() == '':
        emailEntry.insert(0, 'Email')


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


def cpw_on_enter(e):
    confPasswordEntry.delete(0, 'end')


def cpw_on_leave(e):
    if confPasswordEntry.get() == '':
        confPasswordEntry.insert(0, 'Confirm Password')


def open_loginpage():
    window.destroy()
    import LOGINPAGE


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confPasswordEntry.delete(0, END)
    check.set(0)


def connectDB():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confPasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confPasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatched')
    elif check == 0:
        messagebox.showerror('Error', 'Please Accept our Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='apunda2001')
            cursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue,Please Try Again')
            return

        try:
            query = 'create database userdata'
            cursor.execute(query)
            query = 'use userdata'
            cursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            cursor.execute(query)
        except:
            query = 'use userdata'
            cursor.execute(query)

        query = 'select * from data where username = %s'
        cursor.execute(query, (usernameEntry.get()))

        row = cursor.fetchone()
        if row is not None:
            messagebox.showerror('Error', 'Username Already exists')
        else:
            query = 'insert into data(email,username,password) values (%s,%s,%s)'
            cursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            window.destroy()
            import LOGINPAGE


# GUI part
window = Tk()
window.title('Sign-Up Page')
window.geometry('925x500+300+200')
window.config(bg='#fff')
window.resizable(False, False)

img = PhotoImage(file='login.png')
Label(window, image=img, bg='white', ).place(x=50, y=50)

frame = Frame(window, width=350, height=350, bg="white")
frame.place(x=500, y=70)

heading = Label(frame, text='SIGN-UP', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

######### -------------------------------------------------------------------------------------------------------------------------------------------------
emailEntry = Entry(frame, width=25, fg='black', border=0, bg='white',
                   font=('Microsoft YaHei UI Light', 10, 'bold'))
emailEntry.place(x=30, y=50)
emailEntry.insert(0, 'Email')
emailEntry.bind('<FocusIn>', email_on_enter)
emailEntry.bind('<FocusOut>', email_on_leave)

Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=85)

######### -----------------------------------------------------------------------------------------------------------------------------------------------
usernameEntry = Entry(frame, width=25, fg='black', border=0, bg='white',
                      font=('Microsoft YaHei UI Light', 10, 'bold'))
usernameEntry.place(x=30, y=100)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', username_on_enter)
usernameEntry.bind('<FocusOut>', username_on_leave)

Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=135)

######### ----------------------------------------------------------------------------------------------------------------------------------------------
passwordEntry = Entry(frame, width=25, fg='black', border=0, bg='white',
                      font=('Microsoft YaHei UI Light', 10, 'bold'))
passwordEntry.place(x=30, y=150)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_on_enter)
passwordEntry.bind('<FocusOut>', password_on_leave)

Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=185)

######### ---------------------------------------------------------------------------------------------------------------------------------------------
confPasswordEntry = Entry(frame, width=25, fg='black', border=0, bg='white',
                          font=('Microsoft YaHei UI Light', 10, 'bold'))
confPasswordEntry.place(x=30, y=200)
confPasswordEntry.insert(0, 'Confirm Password')
confPasswordEntry.bind('<FocusIn>', cpw_on_enter)
confPasswordEntry.bind('<FocusOut>', cpw_on_leave)

Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=235)

######### --------------------------------------------------------------------------------------------------------------------------------------------
check = IntVar()
termsandconditions = Checkbutton(frame, fg='#57a1f8', bg='white', activebackground='white', activeforeground='#57a1f8',
                                 cursor='hand2', text='I agree to the Terms & Conditions',
                                 font=('Microsoft YaHei UI Light', 10, 'bold'), variable=check)
termsandconditions.place(x=30, y=245)
######### --------------------------------------------------------------------------------------------------------------------------------------------
signUpButton = Button(frame, width=39, pady=7, text='Sign-up', bg='#57a1f8', cursor='hand2',
                      fg='white', border=0, command=connectDB)
signUpButton.place(x=35, y=290)

######### --------------------------------------------------------------------------------------------------------------------------------------------
label = Label(frame, text="Already have an account?", fg='black', bg='white',
              font=('Microsoft YeHei UI Light', 9))
label.place(x=75, y=330)
log_in = Button(frame, width=5, text='Log in', border=0, bg='white', cursor='hand2',
                fg='#57a1f8', font=('Open Sans', 9, 'bold underline'), command=open_loginpage)
log_in.place(x=215, y=330)

window.mainloop()
