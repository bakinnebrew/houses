import csv
import cs50
from sys import argv, exit
from cs50 import SQL
db = SQL("sqlite:///students.db")

#TODO create function to clickly input house name

if(argv[-1]) == "Gryffindor": 
    house_students_g = db.execute("SELECT * FROM student_house_info WHERE house = 'Gryffindor' ORDER BY last_name");
    
    for row in house_students_g:
                first_name, middle_name, last_name, birth = row["first_name"], row["middle_name"], row["last_name"], row["birth"]
                if middle_name == None:
                     print(f"{first_name} {last_name}, born {birth}")
                else:
                     print(f"{first_name} {middle_name} {last_name}, born {birth}")
            
if(argv[-1]) == "Ravenclaw":
    house_students_g = db.execute("SELECT * FROM student_house_info WHERE house = 'Ravenclaw' ORDER BY last_name");
    
    for row in house_students_g:
                first_name, middle_name, last_name, birth = row["first_name"], row["middle_name"], row["last_name"], row["birth"]
                if middle_name == None:
                     print(f"{first_name} {last_name}, born {birth}")
                else:
                     print(f"{first_name} {middle_name} {last_name}, born {birth}")       
if(argv[-1]) == "Slytherin":
    house_students_g = db.execute("SELECT * FROM student_house_info WHERE house = 'Slytherin' ORDER BY last_name");
    
    for row in house_students_g:
                first_name, middle_name, last_name, birth = row["first_name"], row["middle_name"], row["last_name"], row["birth"]
                if middle_name == None:
                     print(f"{first_name} {last_name}, born {birth}")
                else:
                     print(f"{first_name} {middle_name} {last_name}, born {birth}")

if(argv[-1]) == "Hufflepuff":
    house_students_g = db.execute("SELECT * FROM student_house_info WHERE house = 'Hufflepuff' ORDER BY last_name");
    
    for row in house_students_g:
                first_name, middle_name, last_name, birth = row["first_name"], row["middle_name"], row["last_name"], row["birth"]
                if middle_name == None:
                     print(f"{first_name} {last_name}, born {birth}")
                else:
                     print(f"{first_name} {middle_name} {last_name}, born {birth}")
    