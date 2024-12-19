"""

 Write a menu-based program to add, delete and display the record of the hostel using list and stack structure in Python. The record of the hostel contains the field : hostel number, Total students and total rooms. 

"""

l=[]
def push():
    hno=int(input("Enter hostel no: "))
    students=int(input("Enter total number of students: "))
    rooms=int(input("Enter number of rooms: "))
    l.append([hno,students,rooms])
def pop():
    if l==[]:
        print("Stack is underflow")
    else:
        print("Popped node: ",l.pop())
        print("New stack: ",l)
def display():
    if l==[]:
        print("Stack is underflow")
    else:
        for i in range(-1,-(len(l)+1),-1):
            print(l[i])
            
            
print("Choose one of the following:")
print("1. Add a record")
print("2. Delete a record")
print("3. Display records")
print("4. Exit")

while True:
  choice = int(input("Enter your choice: "))
  if choice == 1:
      push()
  elif choice == 2:
      pop()
  elif choice == 3:
      display()
  elif choice == 4:
      break
  else:
      print("Wrong input :/..... Try Again...")


"""
SQL QUERIESSSS


b) select d.ecode, firstname, d.depname from employee e, department d where e.ECode = d.ECode and budget > 18000;

c) select * from employee where lastname like 's%' and depname='sales';

d) update department set depname = 'marketing' where depname = 'sales';
    

"""