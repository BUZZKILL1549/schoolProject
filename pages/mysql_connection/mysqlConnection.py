import mysql.connector

cnx = mysql.connector.connect(
    host = "localhost",
    user = "buzzkill",
    password = "f00tball@143",
    database = "school_app"
)
cursor = cnx.cursor()

def login(name: str, pwd: str) -> bool:
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()

    for row in records:
        if row[1] == name:
            if row[2] == pwd:
                return True

def retrieveAnnouncements() -> list[tuple]:
    cursor.execute("SELECT * FROM announcements")
    announcementsRetriever = cursor.fetchall()

    return announcementsRetriever

def retrieveAssignments() -> list[tuple]:
    cursor.execute("SELECT * FROM assignments")
    assignmentsRetriever = cursor.fetchall()

    return assignmentsRetriever

def retrieveClassDiary() -> list[tuple]:
    cursor.execute("SELECT * FROM class_diary")
    classDiaryRetriever = cursor.fetchall()

    return classDiaryRetriever

def sendConcern(subject: str, description: str) -> None:
    query = f'''INSERT INTO parent_concern (Subject, Description) VALUES (%s, %s);'''
    values = (subject, description)

    try:
        cursor.execute(query, values)
        cnx.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table: {}".format(error))
    
