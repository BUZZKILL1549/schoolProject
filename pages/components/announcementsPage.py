from tkinter import *
from tkinter import ttk
import mysql.connector

def retrieveAnnouncements() -> list[tuple]:
    try:
        cnx = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'f00tball@143',
            database = 'school_app'
        )

        if cnx.is_connected():
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM announcements")
            records = cursor.fetchall()
            return records
    except mysql.connector.Error as error:
        print(f"Error connecting to the server: {error}")
        return []
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()

def announcements(root):
    def update():
        trv.delete(*trv.get_children())
        announcementsRetriever = retrieveAnnouncements()
        for retrievedAnnouncements in announcementsRetriever:
            trv.insert("", END, values=retrievedAnnouncements)
        announcementsPage.after(1000, update)

    announcementsPage = Toplevel(root)
    announcementsPage.title("Announcements")

    # Appbar area
    appBarFrame = ttk.Frame(announcementsPage)
    appBarFrame.pack()
    ttk.Label(appBarFrame, text="ANNOUNCEMENTS").pack(side="top", pady=20)

    # Rest of the page
    announcementsFrame = ttk.Frame(announcementsPage)
    announcementsFrame.pack(fill=BOTH, expand=1)

    announcementsCanvas = Canvas(announcementsFrame)
    announcementsCanvas.pack(side=BOTTOM, fill=BOTH, expand=1)

    scrlbar = ttk.Scrollbar(announcementsFrame, orient=HORIZONTAL, command=announcementsCanvas.xview)
    scrlbar.pack(side=BOTTOM, fill=X)

    announcementsCanvas.configure(xscrollcommand=scrlbar.set)
    announcementsCanvas.bind('<Configure>', lambda e: announcementsCanvas.configure(scrollregion=announcementsCanvas.bbox("all")))

    treeviewFrame = ttk.Frame(announcementsCanvas)
    announcementsCanvas.create_window((0, 0), window=treeviewFrame, anchor=S)

    trv = ttk.Treeview(treeviewFrame, selectmode=BROWSE)
    trv.pack(padx=20, pady=20, ipadx=100)
    trv["columns"] = ("1", "2")
    trv['show'] = 'headings'

    trv.column("1", width=80, anchor='c')
    trv.column("2", width=200, anchor='c')

    trv.heading("1", text="Title")
    trv.heading("2", text="Description")

    update()
    
    announcementsPage.mainloop()