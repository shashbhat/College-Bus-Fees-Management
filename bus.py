from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
import os

labelfont = ('times', 20, 'bold')
labelfont2 = ('times', 14, 'bold')


def bus_add():
    global bus_number
    global num_entry
    global driver_name
    global name_entry
    global bus_screen
    global route_1
    global route_2
    global route_3
    bus_screen = Toplevel(main_screen)
    bus_screen.title("Add Bus Details")
    bus_screen.state('zoomed')
    bus_screen.configure(bg='white')
    bus_screen.bind('<Escape>', lambda e: bus_screen.destroy())
    bus_number = StringVar()
    driver_name = StringVar()
    route_1 = StringVar()
    route_2 = StringVar()
    route_3 = StringVar()

    Label(bus_screen, text='Please enter bus details below', bg='white', font=labelfont).pack()
    Label(bus_screen, text="", bg='white').pack()
    Label(bus_screen, text='Bus number', bg='white', font=labelfont2).pack()
    num_entry = Entry(bus_screen, textvariable=bus_number, bg='white').pack()
    Label(bus_screen, text="", bg='white',).pack()
    Label(bus_screen, text='Driver Name', bg='white', font=labelfont2).pack()
    name_entry = Entry(bus_screen, textvariable=driver_name, bg='white').pack()

    Label(bus_screen, text='Route 1', bg='white', font=labelfont2).pack()
    Entry(bus_screen, textvariable=route_1, bg='white').pack()
    Label(bus_screen, text='Route 2', bg='white', font=labelfont2).pack()
    Entry(bus_screen, textvariable=route_2, bg='white').pack()
    Label(bus_screen, text='Route 3', bg='white', font=labelfont2).pack()
    Entry(bus_screen, textvariable=route_3, bg='white').pack()

    Button(bus_screen, text='Add', command=add_bus,  width=10, height=1, font='bold', fg='blue', bg='white',
           relief=GROOVE, activebackground='green').place(relx=0.475, rely=0.6)


def callback():
    main_screen.destroy()
    os.system('python menu.py')


def add_bus():
    num_info = bus_number.get()
    name_info = driver_name.get()
    route_info1 = route_1.get()
    route_info2 = route_2.get()
    route_info3 = route_3.get()

    file_exists = os.path.isfile('bus.csv')
    if file_exists:
        with open('bus.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if num_info == row[0]:
                    messagebox.showerror('Error', 'Bus Number already exists')
                    return
    with open('bus.csv', 'a', newline='') as f:
        header = ['Bus_num', 'Driver_name', 'Route_1', 'Route_2', 'Route_3']
        writer = csv.DictWriter(f, fieldnames=header)

        writer.writerow({'Bus_num': num_info, 'Driver_name': name_info, 'Route_1': route_info1, 'Route_2': route_info2,
                         'Route_3': route_info3})
        messagebox.showinfo('Success', "Details added successfully")


def bus_display():
    global display_bus
    display_bus = Toplevel(main_screen)
    display_bus.configure(bg='white')
    display_bus.title("Display Bus Details")
    display_bus.state('zoomed')
    display_bus.bind('<Escape>', lambda e: display_bus.destroy())
    Label(display_bus, text='Bus Number', relief=RIDGE, width=10, height=2,  font=labelfont2, bg='white')\
        .grid(row=0, column=0)
    Label(display_bus, text='Driver Name', relief=RIDGE, width=10, height=2,  font=labelfont2, bg='white')\
        .grid(row=0, column=1)
    Label(display_bus, text='Route 1', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white') \
        .grid(row=0, column=2)
    Label(display_bus, text='Route 2', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white') \
        .grid(row=0, column=3)
    Label(display_bus, text='Route 3', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white') \
        .grid(row=0, column=4)
    with open("bus.csv", newline="") as file:
        reader = csv.reader(file)
        r = 0
        for col in reader:
            c = 0
            for row in col:
                Label(display_bus, width=10, height=2, text=row, relief=RIDGE, font=labelfont2, bg='white')\
                    .grid(row=r+1, column=c)
                c += 1
            r += 1


def search_bus():
    global search_screen
    search_screen = Toplevel(main_screen)
    search_screen.configure(bg='white')
    global bus_search
    bus_search = StringVar()
    search_screen.title('Search bus')
    search_screen.state('zoomed')
    search_screen.bind('<Escape>', lambda e: search_screen.destroy())
    Label(search_screen, text='Search for bus', bg='white', font=labelfont).pack()
    Label(search_screen, text="", bg='white').pack()
    Label(search_screen, text='Enter Bus num', font=labelfont2, bg='white').pack()
    Label(search_screen, text="", bg='white').pack()
    ent = Entry(search_screen, textvariable=bus_search, bg='white')
    ent.pack()
    ent.focus()
    Label(search_screen, text="", bg='white').pack()
    Label(search_screen, text="", bg='white').pack()
    Button(search_screen, text='Search', command=search, width=10, height=1, font='bold', fg='blue', bg='white',
           relief=GROOVE, activebackground='green').pack()


def search():
    global search1_screen
    flag = 0
    bus_text = bus_search.get()
    with open('bus.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if bus_text == row[0]:

                search1_screen = Tk()
                search1_screen.title('Display Student')
                search1_screen.configure(bg='white')
                search1_screen.state('zoomed')
                search1_screen.bind('<Escape>', lambda e: search1_screen.destroy())
                Label(search1_screen, text='Bus Number', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white')\
                    .grid(row=0, column=0)
                Label(search1_screen, text='Driver Name', relief=RIDGE, width=10, height=2, font=labelfont2,
                      bg='white').grid(row=0, column=1)
                Label(search1_screen, text='Route 1', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white') \
                    .grid(row=0, column=2)
                Label(search1_screen, text='Route 2', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white') \
                    .grid(row=0, column=3)
                Label(search1_screen, text='Route 3', relief=RIDGE, width=10, height=2, font=labelfont2, bg='white') \
                    .grid(row=0, column=4)
                i = 0
                flag = 1
                for field in row:
                    Label(search1_screen, width=10, height=2, text=row[i], relief=RIDGE, font=labelfont2, bg='white')\
                        .grid(row=1, column=i)
                    i += 1
        if flag == 0:
            messagebox.showerror('Error', 'Bus not available')


def delete_bus():
    global delete_screen
    delete_screen = Toplevel(main_screen)
    delete_screen.configure(bg='white')
    global bus_delete
    bus_delete = StringVar()
    delete_screen.title('Delete bus')
    delete_screen.state('zoomed')
    delete_screen.bind('<Escape>', lambda e: delete_screen.destroy())
    Label(delete_screen, text='Delete Bus', bg='white', font=labelfont).pack()
    Label(delete_screen, text="", bg='white').pack()
    Label(delete_screen, text='Enter Bus num', font=labelfont2, bg='white').pack()
    Label(delete_screen, text="", bg='white').pack()
    Entry(delete_screen, textvariable=bus_delete, bg='white').pack()
    Label(delete_screen, text="", bg='white').pack()
    Label(delete_screen, text="", bg='white').pack()
    Button(delete_screen, text='Delete', command=delete, width=10, height=1, font='bold', fg='blue', bg='white',
           relief=GROOVE, activebackground='green').pack()


def delete():
    flag = 0
    delete_info = bus_delete.get()
    rem = [delete_info]
    with open('bus.csv', 'r', newline='') as infile, open('temp.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for row in csv.reader(infile):
            if row[0] == delete_info:
                flag = 1
            if not any(remove_word in row for remove_word in rem):
                writer.writerow(row)
        infile.close()
        outfile.close()
        os.replace('temp.csv', 'bus.csv')
        if flag == 0:
            messagebox.showerror('Error', 'Cannot Delete')
        else:
            messagebox.showinfo('Success', 'Successfully Deleted')


def update_bus():
    global update_screen
    global bus_update
    global driver_update
    global num_route
    global option_info
    options = ['Driver Name', 'Route 1', 'Route 2', 'Route 3']
    num_route = StringVar()
    option_info = StringVar()
    driver_update = StringVar()
    bus_update = StringVar()
    update_screen = Toplevel(main_screen)
    update_screen.configure(bg='white')
    update_screen.title('Update')
    update_screen.state('zoomed')
    update_screen.bind('<Escape>', lambda e: update_screen.destroy())
    Label(update_screen, text='Update Bus', bg='white', font=labelfont).pack()
    Label(update_screen, text="", bg='white').pack()
    Label(update_screen, text='Enter Bus Number', font=labelfont2, bg='white').pack()
    Label(update_screen, text="", bg='white').pack()
    Entry(update_screen, textvariable=bus_update, bg='white').pack()
    Label(update_screen, text="", bg='white').pack()

    Label(update_screen, text='Choose to update', font=labelfont2, bg='white').pack()
    Label(update_screen, text="", bg='white').pack()
    num_route = ttk.Combobox(update_screen, values=options, state='readonly')
    num_route.pack()
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
    num = bus_update.get()
    val = option_info.get()
    option = num_route.get()
    with open('bus.csv', 'r', newline='') as file, open('temp.csv', 'a', newline='') as tempfile:
        header = ['Bus_num', 'Driver_name', 'Route_1', 'Route_2', 'Route_3']
        reader = csv.DictReader(file, fieldnames=header)
        writer = csv.DictWriter(tempfile, fieldnames=header)

        if option == 'Driver Name':
            for row in reader:
                if int(row['Bus_num']) == int(num):
                    row['Driver_name'] = val
                    flag = 1
                writer.writerow(row)

        elif option == 'Route 1':
            for row in reader:
                if int(row['Bus_num']) == int(num):
                    row['Route_1'] = val
                    flag = 1
                writer.writerow(row)

        elif option == 'Route 2':
            for row in reader:
                if int(row['Bus_num']) == int(num):
                    row['Route_2'] = val
                    flag = 1
                writer.writerow(row)

        elif option == 'Route 3':
            for row in reader:
                if int(row['Bus_num']) == int(num):
                    row['Route_3'] = val
                    flag = 1
                writer.writerow(row)

        file.close()
        tempfile.close()
        os.replace('temp.csv', 'bus.csv')
        if flag == 0:
            messagebox.showerror('Error', 'Cannot update')
        else:
            messagebox.showinfo('Success', 'Successfully Updated')


def student():
    os.system('python student.py')


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.state('zoomed')
    main_screen.configure(bg='white')
    main_screen.bind('<Escape>', lambda e: main_screen.destroy())
    main_screen.title('Details')
    Label(text="Welcome to College Bus Fees Management", bg='white', fg='green', width="512", height="2",
          font=labelfont).pack()
    Label(text='', bg='white').pack()
    Button(text='Add Bus Details', height='2', width='30', command=bus_add, fg='blue', font='bold', relief=GROOVE,
           activebackground='green').pack()
    Label(text='', bg='white').pack()
    Button(text='Display Bus Details', height='2', width='30', command=bus_display, fg='blue', font='bold',
           relief=GROOVE, activebackground='green').pack()
    Label(text='', bg='white').pack()
    Button(text='Search for Bus', height='2', width='30', command=search_bus, fg='blue', font='bold', relief=GROOVE,
           activebackground='green').pack()
    Label(text='', bg='white').pack()
    Button(text='Delete Bus', height='2', width='30', command=delete_bus, fg='blue', font='bold', relief=GROOVE,
           activebackground='green').pack()
    Label(text='', bg='white').pack()
    Button(text='Update Bus', height='2', width='30', command=update_bus, fg='blue', font='bold', relief=GROOVE,
           activebackground='green').pack()
    Label(text='', bg='white').pack()

    btn = Button(main_screen, text='Back', command=callback,  fg='blue', font='bold', relief=GROOVE,
                 activebackground='green')
    btn.place(x=10, y=40)

    main_screen.mainloop()


main_page()
