from tkinter import *
import os


def bus():
    os.system('python add_bus.py')


def student():
    os.system('python student.py')


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.title('MENU')
    main_screen.state('zoomed')
    main_screen.bind('<Escape>', lambda e: main_screen.destroy())
    Label(text="Welcome to College Bus Fees Management", bg='white', width="512", height="2").pack()
    Label(text='').pack()
    Button(text='Bus Details', height='2', width='30', command=bus).pack()
    Label(text='').pack()
    Button(text='Student Details', height='2', width='30', command=student).pack()
    Label(text='').pack()

    main_screen.mainloop()


main_page()