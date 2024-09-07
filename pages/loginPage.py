from tkinter import *
from tkinter import ttk
import mysql_connection.mysqlConnection as mysqlConnection
import homePage as homePage

def tryLogin():
    username = nameEntry.get()
    password = pwdEntry.get()
    if mysqlConnection.login(username, password):
        passReport.configure(text="Login Successful")
        root.after(500, openHomePage)  
    else:
        passReport.configure(text="Try Again")

def openHomePage():
    root.destroy()
    homePage.home()

if __name__ == "__main__":
    root = Tk()
    root.title("Login")

    rootFrame = ttk.Frame(root)
    rootFrame.grid(padx=40, pady=40)

    ttk.Label(rootFrame, text="Username: ").grid(row=0, column=0, padx=40, pady=40)
    nameEntry = ttk.Entry(rootFrame)
    nameEntry.grid(row=0, column=1, pady=40)

    ttk.Label(rootFrame, text="Password: ").grid(row=1, column=0)
    pwdEntry = ttk.Entry(rootFrame, show="*")  # Mask password entry
    pwdEntry.grid(row=1, column=1, padx=40)

    passReport = ttk.Label(rootFrame, text="")
    passReport.grid(row=2, column=1)

    loginButton = ttk.Button(rootFrame, text="Log in", command=tryLogin)
    loginButton.grid(row=3, column=1, pady=20)

    root.mainloop()
