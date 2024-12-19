"""

Create a CSV file “Club.csv” to store COACH_ID, COACH_NAME, AGE,SPORTS and PAY  as a tabular form:      
          Write it as a menu driven program to do the following:-							      
ADD  
DISPLAY
SEARCH (Search a coach information based on given coach_id)	


    
"""

import csv

def add():
    f1 = open("Club.csv", "w", newline="")
    f= csv.writer(f1)
    f.writerow(["COACH_ID", "COACH_NAME", "AGE", "SPORTS", "PAY"])
    u_int = int(input("How many records: "))
    for i in range(u_int):
        c_id = int(input("Enter the id: "))
        c_name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        sports = input("Enter the sports: ")
        pay = int(input("Enter the pay: "))
        f.writerow([c_id, c_name, age, sports, pay])
        print("Record added successfully")
    f1.close()

def display():
    f2 = open("Clu.csv", "r")
    club_records = csv.reader(f2)
    for j in club_records:
        print(j)
    f2.close()
    
def search(coachid):
    f3 = open("Club.csv", "r")
    club_records = csv.reader(f3)
    for i in club_records:
        if i[0] == coachid:
            print(i)
    f3.close()
    

while True:
    print("\n1. ADD\n2. DISPLAY\n3. SEARCH\n4. EXIT")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        display()
    elif choice == 3:
        coachid = input("Enter the coach id to search: ")
        search(coachid)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
    
    
"""
    
SQL QUERIESSSS

a) select * from trains where start='New Delhi';

b) select pnr, pname, gender, age from passengers where age<50;

c) select Gender, count(*) ratio from passengers group by gender;

d)  select * from passengers p, trains t where p.TNO=t.TNO and p.TNO = 12015;   
    
    
"""