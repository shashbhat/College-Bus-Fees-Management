from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import csv

labelfont = ('times', 20, 'bold')
labelfont2 = ('times', 14, 'bold')


def add_student():
    global student_name
    global student_usn
    global student_sem
    global bus_number
    global bus_fees
    global bus_route
    global student_screen
    global num_bus
    global num_route
    global amount_paid

    student_name = StringVar()
    student_usn = StringVar()
    student_sem = StringVar()
    bus_number = StringVar()
    bus_fees = StringVar()
    bus_route = StringVar()
    amount_paid = StringVar()
    num_bus = StringVar()
    num_route = StringVar()
    options = ['Route_1', 'Route_2', 'Route_3']

    student_screen = Toplevel(main_screen)
    student_screen.title("Add Student Details")
    student_screen.state('zoomed')
    student_screen.configure(bg='white')
    student_screen.bind('<Escape>', lambda e: student_screen.destroy())

    Label(student_screen, text='Please enter student details below', font=labelfont, bg='white').pack()
    Label(student_screen, text="", bg='white').pack()

    Label(student_screen, text='Student usn', bg='white', font=labelfont2).pack()
    Entry(student_screen, textvariable=student_usn, bg='white').pack()
    Label(student_screen, text="", bg='white').pack()

    Label(student_screen, text='Student name', font=labelfont2, bg='white').pack()
    Entry(student_screen, textvariable=student_name, bg='white').pack()
    Label(student_screen, text="", bg='white').pack()

    Label(student_screen, text='Student sem', bg='white', font=labelfont2).pack()
    Entry(student_screen, textvariable=student_sem, bg='white').pack()
    Label(student_screen, text="", bg='white').pack()

    Label(student_screen, text='Bus number', bg='white', font=labelfont2).pack()
    num_bus = ttk.Combobox(student_screen, values=list(range(1, 6)), state='readonly')
    num_bus.pack()
    num_bus.bind("<<ComboboxSelected>>", callbackfunc)
    Label(student_screen, text="", bg='white').pack()

    Label(student_screen, text='Route number', bg='white', font=labelfont2).pack()
    num_route = ttk.Combobox(student_screen, values=options, state='readonly')
    num_route.pack()
    num_route.current(0)
    num_route.bind("<<ComboboxSelected>>", callbackfunc)
    Label(student_screen, text="", bg='white').pack()

    Label(student_screen, text='Bus Fees', bg='white', font=labelfont2).pack()
    Label(student_screen, text="", bg='white').pack()
    Label(student_screen, text="", bg='white').pack()
    Label(student_screen, text="", bg='white').pack()

    Label(student_screen, text='Fees Paid', bg='white', font=labelfont2).pack()
    Entry(student_screen, textvariable=amount_paid, bg='white').pack()
    Label(student_screen, text="", bg='white').pack()
    Label(student_screen, text="", bg='white').pack()
    Button(student_screen, text='Add', command=student_add, fg='blue', font=labelfont2, relief=GROOVE,
           activebackground='green').pack()


def callbackfunc(event):
    global fees1
    fees1 = StringVar()
    num_info = num_bus.get()
    route = num_route.get()

    with open('bus.csv', 'r', newline='') as f:
        header = ['Bus_num', 'Driver_name', 'Route_1', 'Route_2', 'Route_3']
        reader = csv.DictReader(f, fieldnames=header)
        for row in reader:
            if int(num_info) == int(row['Bus_num']):
                val = row[route]
                Label(student_screen, text=val, font=labelfont2, bg='white', relief=RIDGE).place(relx=0.4855, y=450)
                fees1 = val


def student_add():
    name_info = student_name.get()
    usn_info = student_usn.get()
    sem_info = student_sem.get()
    num_info = num_bus.get()
    route = num_route.get()
    amount = amount_paid.get()
    balance = int(fees1) - int(amount)

    file_exists = os.path.isfile('student.csv')
    if file_exists:
        with open('student.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if usn_info == row[0]:
                    messagebox.showerror('Error', 'USN already exists')
                    return

    with open('student.csv', 'a', newline='') as f:
        header = ['student_usn', 'student_name', 'student_sem', 'bus_number', 'bus_route', 'bus_fees', 'fees_paid',
                  'balance']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writerow({'student_usn': usn_info, 'student_name': name_info, 'student_sem': sem_info,
                         'bus_number': num_info, 'bus_route': route, 'bus_fees': fees1, 'fees_paid': amount,
                         'balance': balance})
        messagebox.showinfo('Success', "Details added successfully")


def student_display():
    global display_student

    display_student = Toplevel(main_screen)
    display_student.title("Student Details")
    display_student.state('zoomed')
    display_student.configure(bg='white')
    display_student.bind('<Escape>', lambda e: display_student.destroy())

    Label(display_student, text='USN', width=10, height=2, relief=RIDGE, font=labelfont2, bg='white')\
        .grid(row=0, column=0)
    Label(display_student, text='Name', width=10, height=2, relief=RIDGE, font=labelfont2, bg='white')\
        .grid(row=0, column=1)
    Label(display_student, text='SEM', width=10, height=2, relief=RIDGE, font=labelfont2, bg='white')\
        .grid(row=0, column=2)
    Label(display_student, text='Bus Number', width=10, height=2, relief=RIDGE, font=labelfont2, bg='white')\
        .grid(row=0, column=3)
    Label(display_student, text='Route', width=10, height=2, relief=RIDGE, font=labelfont2, bg='white')\
        .grid(row=0, column=4)
    Label(display_student, text='Bus Fees', width=10, height=2, relief=RIDGE, font=labelfont2, bg='white')\
        .grid(row=0, column=5)
    Label(display_student, text='Fees Paid', width=10, height=2, relief=RIDGE, font=labelfont2, bg='white')\
        .grid(row=0, column=6)
    Label(display_student, text='Balance', width=10, height=2, relief=RIDGE, font=labelfont2, bg='white')\
        .grid(row=0, column=7)

    file_exists = os.path.isfile('student.csv')
    if file_exists:
        with open("student.csv", newline="") as file:
            reader = csv.reader(file)
            r = 0
            for col in reader:
                c = 0
                for row in col:
                    Label(display_student, width=10, height=2, text=row, relief=RIDGE, font=labelfont2, bg='white')\
                        .grid(row=r+1, column=c)
                    c += 1
                r += 1


def search_student():
    global search_screen
    global student_search

    student_search = StringVar()

    search_screen = Toplevel(main_screen)
    search_screen.title('Search Student')
    search_screen.state('zoomed')
    search_screen.configure(bg='white')
    search_screen.bind('<Escape>', lambda e: search_screen.destroy())

    Label(search_screen, text='Search for student', bg='white', font=labelfont).pack()
    Label(search_screen, text="", bg='white').pack()
    Label(search_screen, text='Enter Student USN', bg='white', font=labelfont2).pack()
    ent = Entry(search_screen, textvariable=student_search, bg='white')
    ent.pack()
    ent.focus()

    Label(search_screen, text="", bg='white').pack()
    Label(search_screen, text="", bg='white').pack()
    Button(search_screen, text='Search', command=display_searched, fg='blue', bg='white', font=labelfont2,
           relief=GROOVE, activebackground='green').pack()


def display_searched():
    global search1_screen
    global p_amount
    p_amount = StringVar(0)
    student_text = student_search.get()
    flag = 0

    with open("student.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if student_text == row[0]:

                search1_screen = Tk()
                search1_screen.title('Display Student')
                search1_screen.configure(bg='white')
                search1_screen.state('zoomed')
                search1_screen.bind('<Escape>', lambda e: search1_screen.destroy())
                Label(search1_screen, text='Name', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                    .grid(row=0, column=0)
                Label(search1_screen, text='USN', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                    .grid(row=0, column=1)
                Label(search1_screen, text='SEM', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                    .grid(row=0, column=2)
                Label(search1_screen, text='Bus Number', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                    .grid(row=0, column=3)
                Label(search1_screen, text='Route', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                    .grid(row=0, column=4)
                Label(search1_screen, text='Bus Fees', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                    .grid(row=0, column=5)
                Label(search1_screen, text='Fees Paid', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                    .grid(row=0, column=6)
                Label(search1_screen, text='Balance', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                    .grid(row=0, column=7)
                flag = 1
                i = 0
                for field in row:
                    Label(search1_screen, text=row[i], relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                        .grid(row=1, column=i)
                    i += 1

                if int(row[7]) is not 0:
                    Label(search1_screen, text='Amount Paid', font=labelfont2, bg='white').place(relx=0.48, rely=0.45)
                    p_amount = Entry(search1_screen, bg='white')
                    p_amount.place(relx=0.478, rely=0.5)
                    Button(search1_screen, text='Pay', command=update_fees, fg='blue', bg='white', font=labelfont2,
                           relief=GROOVE, activebackground='green').place(relx=0.491, rely=0.55)

        if flag == 0:
            messagebox.showerror('Error', 'USN not available')


def update_fees():
    flag = 0
    amount = p_amount.get()
    student_text = student_search.get()

    with open('student.csv', 'r', newline='') as file, open('temp.csv', 'a', newline='') as tempfile:
        header = ['student_usn', 'student_name', 'student_sem', 'bus_number', 'bus_route', 'bus_fees', 'fees_paid',
                  'balance']
        reader = csv.DictReader(file, fieldnames=header)
        writer = csv.DictWriter(tempfile, fieldnames=header)
        for row in reader:
            if int(row['student_usn']) == int(student_text):
                row['fees_paid'] = int(row['fees_paid']) + int(amount)
                row['balance'] = int(row['balance']) - int(amount)
                flag = 1
            writer.writerow(row)

        file.close()
        tempfile.close()
        os.replace('temp.csv', 'student.csv')
        if flag == 0:
            messagebox.showerror('Error', 'Cannot update')
        else:
            search_screen.destroy()
            search1_screen.destroy()
            messagebox.showinfo('Success', 'Successfully Paid')


def delete_student():
    global delete_screen
    global student_delete
    student_delete = StringVar()

    delete_screen = Toplevel(main_screen)
    delete_screen.configure(bg='white')
    delete_screen.title('Delete Student')
    delete_screen.state('zoomed')
    delete_screen.bind('<Escape>', lambda e: delete_screen.destroy())

    Label(delete_screen, text='Delete student', bg='white', font=labelfont).pack()
    Label(delete_screen, text="", bg='white').pack()
    Label(delete_screen, text='Enter USN',  bg='white', font=labelfont2).pack()
    Entry(delete_screen, textvariable=student_delete, bg='white').pack()
    Label(delete_screen, text="", bg='white').pack()
    Label(delete_screen, text="", bg='white').pack()
    Button(delete_screen, text='Delete', command=delete, fg='blue', font=labelfont2, relief=GROOVE,
           activebackground='green').pack()


def delete():
    flag = 0
    delete_info = student_delete.get()
    rem = [delete_info]
    with open('student.csv', 'r', newline='') as infile, open('temp.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for row in csv.reader(infile):
            if row[0] == delete_info:
                flag = 1
            if not any(remove_word in row for remove_word in rem):
                writer.writerow(row)
        infile.close()
        outfile.close()
        os.replace('temp.csv', 'student.csv')
        if flag == 0:
            messagebox.showerror('Error', 'Cannot Delete')
        else:
            messagebox.showinfo('Success', 'Successfully Deleted')


def update_student():
    global update_screen
    global student_update
    global option_info
    global choice

    choice = StringVar()
    option_info = StringVar()
    student_update = StringVar()
    options = ['Student Name', 'Sem', 'Bus Num', 'Route']

    update_screen = Toplevel(main_screen)
    update_screen.configure(bg='white')
    update_screen.title('Update')
    update_screen.state('zoomed')
    update_screen.bind('<Escape>', lambda e: update_screen.destroy())

    Label(update_screen, text='Update Student', bg='white', font=labelfont).pack()
    Label(update_screen, text="", bg='white').pack()

    Label(update_screen, text='Enter USN', font=labelfont2, bg='white').pack()
    Label(update_screen, text="", bg='white').pack()
    Entry(update_screen, textvariable=student_update, bg='white').pack()
    Label(update_screen, text="", bg='white').pack()

    Label(update_screen, text='Choose to update', font=labelfont2, bg='white').pack()
    Label(update_screen, text="", bg='white').pack()
    choice = ttk.Combobox(update_screen, values=options, state='readonly')
    choice.pack()
    Label(update_screen, text="", bg='white').pack()

    Label(update_screen, text='Enter New Value', font=labelfont2, bg='white').pack()
    Entry(update_screen, textvariable=option_info, bg='white').pack()
    Label(update_screen, text="", bg='white').pack()

    Label(update_screen, text="", bg='white').pack()
    Label(update_screen, text="", bg='white').pack()
    Button(update_screen, text='Update', command=update, width=10, height=1, font='bold', fg='blue', bg='white',
           relief=GROOVE, activebackground='green').pack()


def update():
    flag = 0
    usn = student_update.get()
    option = choice.get()
    val = option_info.get()

    with open('student.csv', 'r', newline='') as file, open('temp.csv', 'a', newline='') as tempfile:
        header = ['student_usn', 'student_name', 'student_sem', 'bus_number', 'bus_route', 'bus_fees', 'fees_paid',
                  'balance']
        reader = csv.DictReader(file, fieldnames=header)
        writer = csv.DictWriter(tempfile, fieldnames=header)

        if option == 'Student Name':
            for row in reader:
                if int(row['student_usn']) == int(usn):
                    row['student_name'] = val
                    flag = 1
                writer.writerow(row)

        if option == 'Sem':
            for row in reader:
                if int(row['student_usn']) == int(usn):
                    row['student_sem'] = val
                    flag = 1
                writer.writerow(row)

        if option == 'Bus Num':
            for row in reader:
                if int(row['student_usn']) == int(usn):
                    row['bus_number'] = val
                    with open('bus.csv', 'r') as f:
                        header1 = ['Bus_num', 'Driver_name', 'Route_1', 'Route_2', 'Route_3']
                        reader1 = csv.DictReader(f, fieldnames=header1)
                        for col in reader1:
                            if int(row['bus_number']) == int(col['Bus_num']):
                                row['bus_fees'] = col[row['bus_route']]
                    flag = 1
                writer.writerow(row)

        if option == 'Route':
            for row in reader:
                if int(row['student_usn']) == int(usn):
                    row['bus_route'] = val
                    with open('bus.csv', 'r') as f:
                        header1 = ['Bus_num', 'Driver_name', 'Route_1', 'Route_2', 'Route_3']
                        reader1 = csv.DictReader(f, fieldnames=header1)
                        for col in reader1:
                            if int(row['bus_number']) == int(col['Bus_num']):
                                row['bus_fees'] = col[val]
                    flag = 1
                writer.writerow(row)

        file.close()
        tempfile.close()
        os.replace('temp.csv', 'student.csv')
        if flag == 0:
            messagebox.showerror('Error', 'Cannot Update')
        else:
            messagebox.showinfo('Success', 'Successfully Deleted')


def callback():
    main_screen.destroy()
    os.system('python menu.py')


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.state('zoomed')
    main_screen.configure(bg='white')
    main_screen.bind('<Escape>', lambda e: main_screen.destroy())
    main_screen.title('Student details')

    Label(text="Welcome to College Bus Fees Management", bg='white', fg='green', width="512", height="2",
          font=labelfont).pack()
    Label(text='', bg='white').pack()

    Button(text='Add Student Details', height='2', width='30', command=add_student, fg='blue', font='bold',
           relief=GROOVE, activebackground='green').pack()
    Label(text='', bg='white').pack()

    Button(text='Display Student Details', height='2', width='30', command=student_display, fg='blue', font='bold',
           relief=GROOVE, activebackground='green').pack()
    Label(text='', bg='white').pack()

    Button(text='Search for student', height='2', width='30', command=search_student, fg='blue', font='bold',
           relief=GROOVE, activebackground='green').pack()
    Label(text='', bg='white').pack()

    Button(text='Delete student', height='2', width='30', command=delete_student, fg='blue', font='bold', relief=GROOVE,
           activebackground='green').pack()
    Label(text='', bg='white').pack()

    Button(text='Update student', height='2', width='30', command=update_student, fg='blue', font='bold', relief=GROOVE,
           activebackground='green').pack()

    Button(main_screen, text='Back', command=callback, fg='blue', font='bold', relief=GROOVE,
           activebackground='green').place(x=10, y=40)

    main_screen.mainloop()


main_page()
