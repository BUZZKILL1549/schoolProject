# School Project

Title: Alternate School App (I'm working on it ok?)

# Introduction
Currently, the school has an app for mobile and a web app for desktop.
This is completely fine; if they work properly, at least.
But they don't. They are often faulty and there are a lot of issues.
It's also very expensive because they have to pay MyClassBoard for using their framework.

This project is made with GNU GPL 3.0, completely open-source and developed in-house.
I think you can imagine that it's a lot better than having to pay for a service that
only works half of the time.

# Project components
This project will utilize the following:
- Python 3.12
- MySQL 8.0

I initially wanted to make the app for mobile and use Flutter/Dart to accomplish that.
But I ran into some issues that led me to not being able to complete it in the
required time. I also have some project constraints that insist that I must only
use Python and its modules and MySQL. It's unfortunate, but I think it still
works as a good concept.

# Project requirements
This project has the following requirements:
- mysql-connector-python==8.4.0
- MySQL database details file

They can be installed in two ways:
## Automatic setup using the automate.ps1 file:
Run the following command in Powershell:
~~~
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\automate.ps1
~~~

## Manual setup:
### mysql-connector-python==8.4.0:
~~~
pip install -r requirements.txt
~~~

### MySQL database details file:
From MySQL Workbench, open:
~~~
initializeDatabase.sql
~~~
This script is present in the root directory of the project.

Run the script in MySQL Workbench to create the database and tables.