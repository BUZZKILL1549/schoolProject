from tkinter import *
from tkinter import ttk

import mysql_connection.mysqlConnection as mysqlConnection

def assignments():
    assignmentsRetriever = mysqlConnection.retrieveAssignments()

    assignmentsPage = Toplevel()
    assignmentsPage.title("Assignments")

    # Appbar area
    appBarFrame = ttk.Frame(assignmentsPage)
    appBarFrame.pack()
    ttk.Label(appBarFrame, text = "ASSIGNMENTS").pack(side = TOP, pady = 20)

    # Rest of the page
    assignmentsFrame = ttk.Frame(assignmentsPage)
    assignmentsFrame.pack(fill = BOTH, expand = 1)

    assignmentsCanvas = Canvas(assignmentsFrame)
    assignmentsCanvas.pack(side = BOTTOM, fill = BOTH, expand = 1)

    scrlbar = ttk.Scrollbar(assignmentsFrame, orient = HORIZONTAL, command = assignmentsCanvas.xview)
    scrlbar.pack(side = BOTTOM, fill = X)

    assignmentsCanvas.configure(xscrollcommand = scrlbar.set)
    assignmentsCanvas.bind('<Configure>', lambda e: assignmentsCanvas.configure(scrollregion = assignmentsCanvas.bbox("all")))

    treeviewFrame = ttk.Frame(assignmentsCanvas)
    assignmentsCanvas.create_window((0, 0), window = treeviewFrame, anchor = S)

    trv = ttk.Treeview(treeviewFrame, selectmode = BROWSE)
    trv.pack(padx = 20, pady = 20, ipadx = 100)
    trv["columns"] = ("1", "2")
    trv['show'] = 'headings'

    trv.column("1", width = 80, anchor = 'c')
    trv.column("2", width = 200, anchor = 'c')

    trv.heading("1", text = "Title")
    trv.heading("2", text = "Description")

    trv.delete(*trv.get_children())

    for retrievedAssignments in assignmentsRetriever:
        trv.insert("", END, values = retrievedAssignments)

    assignmentsPage.mainloop()

if __name__ == "__main__":
    assignmentsRetriever = mysqlConnection.retrieveAssignments()

    assignmentsPage = Tk()
    assignmentsPage.title("Assignments")

    # Appbar area
    appBarFrame = ttk.Frame(assignmentsPage)
    appBarFrame.pack()
    ttk.Label(appBarFrame, text = "ASSIGNMENTS").pack(side = TOP, pady = 20)

    # Rest of the page
    assignmentsFrame = ttk.Frame(assignmentsPage)
    assignmentsFrame.pack(fill = BOTH, expand = 1)

    assignmentsCanvas = Canvas(assignmentsFrame)
    assignmentsCanvas.pack(side = BOTTOM, fill = BOTH, expand = 1)

    scrlbar = ttk.Scrollbar(assignmentsFrame, orient = HORIZONTAL, command = assignmentsCanvas.xview)
    scrlbar.pack(side = BOTTOM, fill = X)

    assignmentsCanvas.configure(xscrollcommand = scrlbar.set)
    assignmentsCanvas.bind('<Configure>', lambda e: assignmentsCanvas.configure(scrollregion = assignmentsCanvas.bbox("all")))

    treeviewFrame = ttk.Frame(assignmentsCanvas)
    assignmentsCanvas.create_window((0, 0), window = treeviewFrame, anchor = S)

    trv = ttk.Treeview(treeviewFrame, selectmode = BROWSE)
    trv.pack(padx = 20, pady = 20, ipadx = 100)
    trv["columns"] = ("1", "2")
    trv['show'] = 'headings'

    trv.column("1", width = 80, anchor = 'c')
    trv.column("2", width = 200, anchor = 'c')

    trv.heading("1", text = "Title")
    trv.heading("2", text = "Description")

    trv.delete(*trv.get_children())

    for retrievedAssignments in assignmentsRetriever:
        trv.insert("", END, values = retrievedAssignments)

    assignmentsPage.mainloop()