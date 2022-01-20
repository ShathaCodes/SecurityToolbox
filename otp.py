import random
import smtplib
from tkinter import *
from tkinter.messagebox import *
import pymysql
import getpass
from login import otp


def login():
    if otpentry.get() == '':
        showerror('Error', 'All Fields Are Required')
    elif otpentry.get() != otp:
        showerror('Error', 'Invalid OTP')

    else:
        showinfo('Success', 'Welcome')


def login_window():
    root.destroy()
    import login


root = Tk()
root.geometry('600x200+50+50')
root.title('OTP Page')

frame = Frame(root, bg='white', width=560, height=320)
frame.place(x=10, y=10)

otpLabel = Label(frame, text='otp', font=(
    'arial', 22, 'bold'), bg='white', fg='black')
otpLabel.place(x=50, y=32)
otpentry = Entry(frame, font=('arial', 22,), bg='white', fg='black')
otpentry.place(x=50, y=70)
logbutton = Button(frame, text='Return to Login form?', font=('arial', 12,), bd=0, fg='gray20', bg='white',
                   cursor='hand2', command=login_window,
                   activebackground='white', activeforeground='gray20')
logbutton.place(x=150, y=120)
loginbutton = Button(frame, text='Login', font=('arial', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                     activebackground='gray20', activeforeground='white', command=login)
loginbutton.place(x=50, y=120)
root.mainloop()
