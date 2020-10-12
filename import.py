import csv
import cs50
from sys import argv, exit
from cs50 import SQL
db = SQL("sqlite:///students.db")
db.execute("CREATE TABLE student_house_info (id INT, first_name TEXT, middle_name TEXT, last_name TEXT, house TEXT, birth NUMERIC)")
if len(argv) != 2:
    print("Wrongo")
    exit(1)
    
with open(argv[1], 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    id = 1
    for row in reader:
        student_name = row['name'].split()
        if len(student_name) == 3:
            first_name, middle_name, last_name = student_name
        else:
            first_name, last_name = student_name
            middle_name = None
        house = row['house']
        birth = row['birth']
        
        db.execute("INSERT INTO student_house_info VALUES(?, ?, ?, ?, ?, ?)", id, first_name, middle_name, last_name, house, birth)
        id += 1
   

print("done")
                
   
    
    
   
    
    
   
