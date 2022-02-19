from tkinter import *

import string

from random import *

LENGTH = 12


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
special_characters = string.punctuation
digits = string.digits

temp_password = lowercase + uppercase + special_characters + digits

def generate_password():

    g_password = ""
    for _ in range(LENGTH):
        g_password += temp_password[randint(0, len(temp_password)-1)]

    return g_password



def create_window():


    def fill_password():
        Password_.delete(0)
        Password_.insert(0, generate_password())





    def save_password():
        if Website_.get() == "" or Username_.get() == "" or Password_.get() == "":
            window = Tk()
            Error_Message = Label(window, text = "Error! Please fill all the above fields.", bg = "red", fg = "white", font = ("Arial", 16))

            Error_Message.pack()
            window.mainloop()

        else:

            with open("Passwords.txt" , 'a') as file:
                file.write(Website_.get() + "|" + Username_.get() + "|" + Password_.get() + "\n")


            window = Tk()
            Message = Label(window, text = "Password successfully saved.", bg = "green", fg = "white", font = ("Arial", 16))

            Message.pack()
            window.mainloop()






    window = Tk()
    window.geometry("600x500")
    window.configure(bg =  "#161853")


    window.minsize(600,500)


    frame = Frame(window, bg = "#161853")

    Text = Label(frame, text = "Save your password here",  font = ("Helvetica", 14), fg = "white", bg = "#161853")
    Text.grid(row = 0, column =1, pady= (0,25))
    Website = Label(frame , text = "Website:", font = ("Helvetica", 14), fg = "white", bg = "#161853")
    Website.grid(row = 1, column = 0, padx = (0, 15), pady= (0,20) )
    Website_ = Entry(frame, width = 25 )
    Website_.grid(row = 1, column =1, pady = (0, 20))
    Username = Label(frame, text = "Username/Email:", font = ("Helvetica", 14), fg = "white", bg = "#161853")
    Username.grid(row = 2, column =0, padx = (0, 15), pady = (0,20))
    Username_ = Entry(frame, width = 25)
    Username_.grid(row = 2, column =1, pady = (0,20))

    Password = Label(frame , text = "Password:", font = ("Helvetica", 14), fg = "white", bg = "#161853" )
    Password.grid(row = 3, column =0, padx = (0,15), sticky = "s")
    Password_ = Entry(frame ,width = 25)
    Password_.grid(row = 3, column =1, pady = (0,30), sticky = "s")
    Generate = Button(frame,text = "Generate Password", font = ("Helvetica", 12), width = 16, command = fill_password)
    Generate.grid(row = 3, column =2, sticky = "s")

    Save = Button(frame,text = "Save Password", font = ("Helvetica", 12), width = 14, command = save_password)
    Save.grid(row = 4, column =1)
    frame.place(relx = 0.5, rely = 0.5, anchor = "center")

    
    window.mainloop()






