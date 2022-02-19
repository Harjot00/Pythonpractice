from tkinter import *
from Createwindow import *
from Saved_password import *
window = Tk()
window.geometry("600x500")
frame = Frame(window, bg = "#161853")
center = Frame(window, bg = "#161853")
text = Label(center, text = "Welcome to the password Manager\nChoose any one option", font = ("Helvetica", 12) , fg = "white", bg = "#161853")
text.pack(pady = (0 , 20))
SavedPasswords = Button(center,text = "Saved Passwords", font = ("Helvetica", 12), width = 16, command = click)
SavedPasswords.pack(pady = (0, 15))
Savepassword = Button(center,text = "Save Password", font = ("Helvetica", 12), width = 16, command = create_window(name))
Savepassword.pack()
center.place(relx = 0.5, rely = 0.5, anchor = "center")
frame.pack(fill = "both", expand = True)
window.minsize(600,500)
window.mainloop()

