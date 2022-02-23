from tkinter import *
from Createwindow import *
from functools import partial
import os


def click():
    window = Tk()
    window.geometry("600x500")
    frame = Frame(window, bg="#161853", width=600, height=500)
    row_ = 0
    column_ = 0

    list = []
    with open("Passwords.txt", 'r') as data_file:
        data = data_file.read().splitlines()
        for i in data:
            names = i.split("|")
            list.append(names[0])

    if len(list) == 0:
        Error_Message = Label(frame, text="There are no saved passwords.", font=("Helvetica", 16), fg="white", bg="red")
        Error_Message.place(relx=0.5, rely=0.5, anchor="center")

    else:
        for i in range(len(list)):

            name = list[i]
            button_ = Button(frame, text=name, font=("Helvetica", 12), width=16, bg="white", fg="black",
                             command=partial(create_win, name))
            button_.grid(row=row_, column=column_, padx=(25, 0), pady=(25, 0))

            column_ += 1
            if column_ == 3:
                row_ += 1
                column_ = 0

    frame.pack(fill="both", expand=True)
    window.mainloop()


def create_win(name):
    def fill_fields():

        with open("Passwords.txt", 'r') as data_file:
            data = data_file.readlines()

            for i in data:
                names = i.split("|")
                if names[0] == name:
                    Website_.insert(0, names[0])
                    Username_.insert(0, names[1])
                    Password_.insert(0, names[2])

    def update_password():
        if Website_.get() == "" or Username_.get() == "" or Password_.get() == "":
            window = Tk()
            Error_Message = Label(window, text="Error! Please fill all the above fields.", bg="red", fg="white",
                                  font=("Arial", 16))

            Error_Message.pack()
            window.mainloop()

        else:
            passwords = []
            with open("Passwords.txt", 'r') as file:
                data = file.readlines()
                
                for i in data:
                   savedPasswords =  i.split("|")
                   
                   if savedPasswords[0] == name:
                       savedPasswords[2] = Password_.get()
                       passwords.append("|".join(savedPasswords))

                   else:
                       passwords.append(i)
            
            
            with  open("Passwords.txt", 'w') as file:     
                file.truncate()
                for i in passwords:
                    file.write(i + "\n")

            
                    
            
            

    window = Tk()
    window.geometry("600x500")
    window.configure(bg="#161853")

    window.minsize(600, 500)

    frame = Frame(window, bg="#161853")
    frame.rowconfigure(2, weight=1)
    frame.columnconfigure([0, 1, 2], weight=1)
    Text = Label(frame, text="Save your password here", font=("Helvetica", 14), fg="white", bg="#161853")
    Text.grid(row=0, column=1, pady=(0, 25))
    Website = Label(frame, text="Website:", font=("Helvetica", 14), fg="white", bg="#161853")
    Website.grid(row=1, column=0, padx=(0, 15), pady=(0, 20))
    Website_ = Entry(frame, width=25)
    Website_.grid(row=1, column=1, pady=(0, 20))
    Username = Label(frame, text="Username/Email:", font=("Helvetica", 14), fg="white", bg="#161853")
    Username.grid(row=2, column=0, padx=(0, 15), pady=(0, 20))
    Username_ = Entry(frame, width=25)
    Username_.grid(row=2, column=1, pady=(0, 20))

    Password = Label(frame, text="Password:", font=("Helvetica", 14), fg="white", bg="#161853")
    Password.grid(row=3, column=0, padx=(0, 15), sticky="s")
    Password_ = Entry(frame, width=25)
    Password_.grid(row=3, column=1, pady=(0, 30), sticky="s")
   

    Save = Button(frame, text="Update Password", font=("Helvetica", 12), width=14, command=update_password)
    Save.grid(row=4, column=1)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    fill_fields()

    window.mainloop()
