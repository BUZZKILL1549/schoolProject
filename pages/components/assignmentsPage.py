from tkinter import *
from tkinter import ttk
import mysql.connector

def retrieveAssignments() -> list[tuple]:
    try:
        cnx = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'f00tball@143',
            database = 'school_app'
        )

        if cnx.is_connected():
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM assignments")
            records = cursor.fetchall()
            return records
    except mysql.connector.Error as error:
        print(f"Error connecting to the server: {error}")
        return []
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()

def assignments(root):
    def update():
        trv.delete(*trv.get_children())
        assignmentsRetriever = retrieveAssignments()
        
        for retrievedAssignments in assignmentsRetriever:
            trv.insert("", END, values=retrievedAssignments)
        
        assignmentsPage.after(1000, update)


    assignmentsPage = Toplevel(root)
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

    update()

    assignmentsPage.mainloop()
