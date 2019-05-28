from tkinter import *
import os
from tkinter import messagebox
import csv

labelfont = ('times', 20, 'bold')
labelfont2 = ('times', 14, 'bold')


def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    main_screen.destroy()

    login_screen = Tk()
    login_screen.title('Login')
    login_screen.state('zoomed')
    login_screen.configure(bg='white')
    login_screen.bind('<Escape>', lambda e: login_screen.destroy())

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text='Please Enter details below to login', fg='green', bg='white', font=labelfont).pack()
    Label(login_screen, text="", bg='white').pack()
    Label(login_screen, text='Username', fg='green', bg='white', font=labelfont2).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, bg='white')
    username_login_entry.pack()
    username_login_entry.focus()
    Label(login_screen, text="", bg='white').pack()
    Label(login_screen, text='Password', fg='green', bg='white', font=labelfont2).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*', bg='white')
    password_login_entry.pack()
    Label(login_screen, text='', fg='green', bg='white', font='bold').pack()
    Button(login_screen, text='Login', width=10, height=1, font=labelfont2, fg='blue', bg='white', relief=GROOVE,
           command=login_verify, activebackground='green').pack()


def login_verify():
    username = username_verify.get()
    password = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    with open('users.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if username == row[0] and password == row[1]:
                callback()
                return TRUE

        messagebox.showerror('Invalid Information', 'Invalid Username or Password')


def callback():
    login_screen.destroy()
    os.system('python menu.py')


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.state('zoomed')
    main_screen.bind('<Escape>', lambda e: main_screen.destroy())
    main_screen.title('Account Login')
    main_screen.configure(bg='white')
    Label(text="Welcome to College Bus Fees Management", bg='white', width="512", height="2", font=labelfont,
          fg='green').pack()
    Label(text='', font='bold', bg='white').pack()
    Button(text='Login', height='2', width='30', command=login, fg='blue', font=labelfont2, relief=GROOVE,
           activebackground='green').pack()
    Label(text='', bg='white').pack()

    main_screen.mainloop()


main_page()

