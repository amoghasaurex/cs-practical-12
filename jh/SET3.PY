"""


Write a program to create a 'Book.dat' file to store the following records.  [Bookid, Name, Quantity, Price].														  8
Create
show(): display all records:
Count(): Display the count of records in the file.       
Delete(): Accept book Id and delete the record    

    
"""

import pickle as pikol

def create():
    with open("Book.dat", "ab") as f:
        book_id = int(input("Enter the book id: "))
        name = input("Name of the book: ")
        quantity = int(input("Quantity of the book: "))
        price = int(input("Price of the book: "))
        data = [book_id, name, quantity, price]
        pikol.dump(data, f)
        
def show():
    with open("Book.dat", "rb") as f:
        while True:
            try:
                R = []
                R = pikol.load(f)
                print(R)
            except:
                print("No records...")
                break

def count():
    count = 0
    with open("Book.dat", "rb") as f:
        while True:
            try:
                R = []
                R = pikol.load(f)
                count += 1
            except:
                print("No records...")
                break
        print("Count of the records: ", count)

def delete():
    book_id_to_delete = int(input("Enter the book ID to delete: "))
    found = False
    records = []

    try:
        with open("Book.dat", "rb") as f:
            while True:
                record = pikol.load(f)
                if record[0] == book_id_to_delete:
                    found = True
                else:
                    records.append(record)
    except EOFError:
        pass

    if found:
        with open("Book.dat", "wb") as f:
            for record in records:
                pikol.dump(record, f)
        print("Record deleted successfully.")
    else:
        print("Record with the specified book ID not found.")
        

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


b) select tname, designation from teacher t, admin a where t.code=a.code;

c) select tname, subject from teacher t, admin a where t.code = a.code and gender='f';

d)  select * from teacher t, admin a where t.code=a.code;

    
"""