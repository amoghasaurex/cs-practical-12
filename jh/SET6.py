"""

Q1.    Creating a Python program named “Mycsv.py” to store the details of Empno, Name and Salary in “Emp.csv”  
          and search for an Empno entered by the user. If found, display the details of the Employee else display 
          Empno is not present.


"""


import csv

def add():
    f = open("Emp.csv", "a")
    writer = csv.writer(f)
    writer.writerow(["Empno","Name","salary"])
    u_int = int(input("How many records: "))
    for i in range(u_int):
        Empno = int(input("Enter Empno: "))
        Name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))
        writer.writerow([Empno,Name,salary])
        f.close()


def search(Empno):
    f = open("Emp.csv", "r")
    reader = csv.reader(f)
    found = False
    for i in reader():
        if i[0] == Empno:
            print(i)
            found = True
            break
    if not found:
        print("nopee not present")
    f.close()
    

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


b) select gender, count(*) from coaches group by gender;

c) select coachname, pay, age, pay * 0.15 bonus from coaches;

d) select * from coaches where coachid in (1,2,7,8) and pay>5000;

    
"""