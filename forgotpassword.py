from tkinter import *
import pymysql
from tkinter import messagebox

window = Toplevel()
window.title('Change Password')

# bgPic = ImageTk.PhotoImage(file='resetpassBg.jpg')
# bglabel = Label(window, image=bgPic)
# bglabel.grid()

heading_label = Label(window, text='RESET PASSWORD', font=('arial', '18', 'bold'), bg='white', fg='magenta2')
heading_label.place(x=480, y=60)

userLabel = Label(window, text='Username', font=('arial', '12', 'bold'), bg='white', fg='orchid1')
userLabel.place(x=470, y=130)
user_entry = Entry(window, width=25, font=('arial', '11', 'bold'), bd=0, fg='magenta2')
user_entry.place(x=470, y=160)
Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

passwordLabel = Label(window, text='New Password', font=('arial', '12', 'bold'), bg='white', fg='orchid1')
passwordLabel.place(x=470, y=210)
newpass_entry = Entry(window, width=25, font=('arial', '11', 'bold'), bd=0, fg='magenta2')
newpass_entry.place(x=470, y=240)
Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=268)

confirmpassLabel = Label(window, text='Username', font=('arial', '12', 'bold'), bg='white', fg='orchid1')
confirmpassLabel.place(x=470, y=290)
confirmpass_entry = Entry(window, width=25, font=('arial', '11', 'bold'), bd=0, fg='magenta2')
confirmpass_entry.place(x=470, y=320)
Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

window.mainloop()
