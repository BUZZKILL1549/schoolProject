from tkinter import *
from tkinter import ttk
import mysql.connector

def retrieveClassDiary() -> list[tuple]:
    try:
        cnx = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'f00tball@143',
            database = 'school_app'
        )

        if cnx.is_connected():
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM class_diary")
            records = cursor.fetchall()
            return records
    except mysql.connector.Error as error:
        print(f"Error connecting to the server: {error}")
        return []
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()

def classDiary(root):
    def update():
        trv.delete(*trv.get_children())
        classDIaryRetriever = retrieveClassDiary()
        
        for retrievedAnnouncements in classDIaryRetriever:
            trv.insert("", END, values=retrievedAnnouncements)
        
        classDiaryPage.after(1000, update)

    classDiaryPage = Toplevel(root)
    classDiaryPage.title("Class Diary")

    # Appbar area
    appBarFrame = ttk.Frame(classDiaryPage)
    appBarFrame.pack()
    ttk.Label(appBarFrame, text = "CLASS DIARY").pack(side = "top", pady = 20)

    # Rest of the page
    classDiaryFrame = ttk.Frame(classDiaryPage)
    classDiaryFrame.pack(fill = BOTH, expand = 1)

    classDiaryCanvas = Canvas(classDiaryFrame)
    classDiaryCanvas.pack(side = BOTTOM, fill = BOTH, expand = 1)

    scrlbar = ttk.Scrollbar(classDiaryFrame, orient = HORIZONTAL, command = classDiaryCanvas.xview)
    scrlbar.pack(side = BOTTOM, fill = X)

    classDiaryCanvas.configure(xscrollcommand = scrlbar.set)
    classDiaryCanvas.bind('<Configure>', lambda e: classDiaryCanvas.configure(scrollregion = classDiaryCanvas.bbox("all")))

    treeviewFrame = ttk.Frame(classDiaryCanvas)
    classDiaryCanvas.create_window((0, 0), window = treeviewFrame, anchor = S)

    trv = ttk.Treeview(treeviewFrame, selectmode = BROWSE)
    trv.pack(padx = 20, pady = 20, ipadx = 100)
    trv["columns"] = ("1", "2")
    trv['show'] = 'headings'

    trv.column("1", width = 80, anchor = 'c')
    trv.column("2", width = 200, anchor = 'c')

    trv.heading("1", text = "Title")
    trv.heading("2", text = "Description")

    update()

    classDiaryPage.mainloop()
