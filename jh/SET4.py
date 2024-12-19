"""


Write a function in python to count the number of  digits,alphabets, uppercase, lowercase, lines, spaces and words in a text file “Quotes.txt”. If the file contents are as follows:
Be Good Do Good
Welcome 2 all brothers and sisters
Thank you 2 all brothers and sisters


"""

f = open("Quotes.txt","w")
f.writelines(["Be Good Do Good",'\n','Welcome 2 all brothers and sisters','\n','Thank you 2 all brother and sisters'])
f.close()

f2=open("Quote.txt","r")
qotes = f2.read()

alpha=digits=upper=lower=spaces = 0

for i in qotes:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digits+=1
    elif i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isspace():
        spaces+=1

f3 = open("Quote.txt","r")
a = f3.realines()
lines = len(a)
l=qotes.split()
words = len(l)

print("Number of digits:",digits)

print("Number of alphabets:",alpha)

print("Number of uppercase letters:",upper)

print("Number of lowercase letters:",lower)

print("Number of lines:",lines)

print("Number of spaces:",spaces)

print("Number of words:",words)

f2.close()

f3.close()


"""

b) select distinct dept_id from employee;

c)  select * from employee e, department d where e.dept_id = d.dept_id;

d) select count(emp_name) count_of_employee, dept_id from employee group by dept_id;

"""