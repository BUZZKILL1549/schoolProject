from tkinter import *
from tkinter import ttk

import mysql_connection.mysqlConnection as mysqlConnection

def send() -> bool:
        try:
            subject = subjectEntry.get()
            description = descriptionEntry.get("1.0", END)

            mysqlConnection.sendConcern(subject, description)

            success.configure(text = "Your concern has been delivered.")
        except:
            success.configure(text = "Our services do not currently work. Please try later.")

def parentConcern():
    parentConcernPage = Toplevel()
    parentConcernPage.title("Parent Concern")

    # Appbar area
    appBarFrame = ttk.Frame(parentConcernPage)
    appBarFrame.pack()
    ttk.Label(appBarFrame, text = "PARENT CONCERN").pack(side = "top", pady = 20)

    # Rest of the app
    entryFrame = ttk.Frame(parentConcernPage)
    entryFrame.pack()

    ttk.Label(entryFrame, text = "Subject: ").grid(row = 0, column = 0, padx = 20, sticky = W)
    subjectEntry = ttk.Entry(entryFrame)
    subjectEntry.grid(row = 0, column = 1, pady = 20, ipadx = 180)

    ttk.Label(entryFrame, text = "Detailed Description: ").grid(row = 1, column = 0, padx = 20)
    descriptionEntry = Text(entryFrame)
    descriptionEntry.grid(row = 1, column = 1, pady = 20, padx = 20, sticky = W)

    success = ttk.Label(entryFrame, text = "")
    success.grid(row = 2, column = 1)

    sendButton = ttk.Button(entryFrame, text = "Send", command = send)
    sendButton.grid(row = 3, column = 1, pady = 20)

    parentConcernPage.mainloop()

if __name__ == "__main__":
    def send() -> bool:
        try:
            subject = subjectEntry.get()
            description = descriptionEntry.get("1.0", END)

            mysqlConnection.sendConcern(subject, description)

            success.configure(text = "Your concern has been delivered.")
        except:
            success.configure(text = "Our services do not currently work. Please try later.")


    parentConcernPage = Tk()
    parentConcernPage.title("Parent Concern")

    # Appbar area
    appBarFrame = ttk.Frame(parentConcernPage)
    appBarFrame.pack()
    ttk.Label(appBarFrame, text = "PARENT CONCERN").pack(side = "top", pady = 20)

    # Rest of the app
    entryFrame = ttk.Frame(parentConcernPage)
    entryFrame.pack()

    ttk.Label(entryFrame, text = "Subject: ").grid(row = 0, column = 0, padx = 20, sticky = W)
    subjectEntry = ttk.Entry(entryFrame)
    subjectEntry.grid(row = 0, column = 1, pady = 20, ipadx = 180)

    ttk.Label(entryFrame, text = "Detailed Description: ").grid(row = 1, column = 0, padx = 20)
    descriptionEntry = Text(entryFrame)
    descriptionEntry.grid(row = 1, column = 1, pady = 20, padx = 20, sticky = W)

    success = ttk.Label(entryFrame, text = "")
    success.grid(row = 2, column = 1)

    sendButton = ttk.Button(entryFrame, text = "Send", command = send)
    sendButton.grid(row = 3, column = 1, pady = 20)

    parentConcernPage.mainloop()