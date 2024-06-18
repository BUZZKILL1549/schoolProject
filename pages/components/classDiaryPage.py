from tkinter import *
from tkinter import ttk

import mysql_connection.mysqlConnection as mysqlConnection

def classDiary():
    classDiaryRetriever = mysqlConnection.retrieveClassDiary()

    classDiaryPage = Toplevel()
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

    trv.delete(*trv.get_children())

    for retrievedClassDiary in classDiaryRetriever:
        trv.insert("", END, values = retrievedClassDiary)

    classDiaryPage.mainloop()

if __name__ == "__main__":
    classDiaryRetriever = mysqlConnection.retrieveClassDiary()

    classDiaryPage = Tk()
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

    trv.delete(*trv.get_children())

    for retrievedClassDiary in classDiaryRetriever:
        trv.insert("", END, values = retrievedClassDiary)

    classDiaryPage.mainloop()