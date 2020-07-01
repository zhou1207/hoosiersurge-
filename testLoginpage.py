from tkinter import *
from functools import partial

def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    return

#window structure
tkWindow = Tk()
tkWindow.geometry('500x300')
tkWindow.title('Remote learning login window')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=2, column=5)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=2, column=6)

#password label and text entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=4, column=5)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password).grid(row=4, column=6)

validatelogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=8, column=5)

tkWindow.mainloop()
