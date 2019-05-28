from tkinter import *
import os

labelfont = ('times', 20, 'bold')
labelfont2 = ('times', 14, 'bold')


def bus():
    main_screen.destroy()
    os.system('python bus.py')


def student():
    main_screen.destroy()
    os.system('python student.py')


def logout():
        main_screen.destroy()
        os.system('python login.py')


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.title('MENU')
    main_screen.state('zoomed')
    main_screen.configure(bg='white')
    main_screen.bind('<Escape>', lambda e: main_screen.destroy())
    Label(text="Welcome to College Bus Fees Management", bg='white', fg='green', width="512", height="2",
          font=labelfont).pack()
    Label(text='', bg='white').pack()
    Button(text='Bus Details', height='2', width='30', command=bus, fg='blue', font=labelfont2, relief=GROOVE,
           activebackground='green').pack()
    Label(text='', bg='white').pack()
    Button(text='Student Details', height='2', width='30', command=student, fg='blue', font=labelfont2, relief=GROOVE,
           activebackground='green').pack()
    Label(text='', bg='white').pack()

    btn = Button(main_screen, text='Logout', command=logout, fg='blue', font='bold', relief=GROOVE,
                 activebackground='green')
    btn.place(x=10, y=40)

    main_screen.mainloop()


main_page()

