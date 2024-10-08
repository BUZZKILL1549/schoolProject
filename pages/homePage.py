from tkinter import *
from tkinter import ttk
import components.announcementsPage as announcementsPage
import components.assignmentsPage as assignmentsPage
import components.classDiaryPage as classDiaryPage
import components.parentConcernPage as parentConcernPage

def home():
    homePage = Tk()
    homePage.title("Home Page")

    # Appbar area
    appBarFrame = ttk.Frame(homePage)
    appBarFrame.grid(padx=10, pady=10)
    ttk.Label(appBarFrame, text="BVM GLOBAL").grid(row=0, column=0)

    homeFrame = ttk.Frame(homePage)
    homeFrame.grid(padx=10, pady=10)

    # Rest of the app
    announcementButton = ttk.Button(homeFrame, text="Announcements", command=lambda: announcementsPage.announcements(homePage))
    announcementButton.grid(row=1, column=0, padx=10, pady=20)

    assignmentsButton = ttk.Button(homeFrame, text="Assignments", command=lambda: assignmentsPage.assignments(homePage))
    assignmentsButton.grid(row=1, column=2, padx=10, pady=20)

    classDiaryButton = ttk.Button(homeFrame, text="Class Diary", command=lambda: classDiaryPage.classDiary(homePage))
    classDiaryButton.grid(row=1, column=1, padx=10, pady=20)

    parentConcernButton = ttk.Button(homeFrame, text="Parent Concern", command=lambda: parentConcernPage.parentConcern(homePage))
    parentConcernButton.grid(row=2, column=1, padx=10, pady=30, sticky=E)

    homePage.mainloop()
