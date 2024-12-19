"""

Each node of a STACK contains the following information:
        a) pincode of the city
        b) name of the city
        c) name of the state
        
 Write a menu driven program to implement the PUSH, POP and Display operations in above code using  
    list.


"""

emp_list = []

def push():
    pincode = int(input("Enter the pincode of the city: "))
    name = input("Enter the name of the city: ")
    state = input("Enter the name of the state: ")
    emp_list.append([pincode,name,state])
    print("WOWW successfully pushed")
    
def pop():
    if emp_list ==[]:
        print("Stack empty.")
    else:
        print("Poped node: ",emp_list.pop())
        print("New stack: ", emp_list)

def display():
    if emp_list == []:
        print("Stack empty.")
    else:
         for i in range(len(emp_list) -1,-1,-1):
            print(emp_list[i])
        
while True:
  print("\nEnter the operation you want to perform: \n 1: PUSH AN ENTRY\n 2: POP AN ELEMENT\n 3: DISPLAY THE STACK\n 4: quit")
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

b) select name from client where name like '%van%';

c) select * from client where city!='Bombay';

d) select city, count(*) no_of_clients from client group by city;   
    
    
"""

