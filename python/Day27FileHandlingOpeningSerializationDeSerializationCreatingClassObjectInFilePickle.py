#program 1
#Practice program for interview
#to convert the string  e.g"book" into a dictionary e.g {b:1,o:2,k:1}
# so that the characters are the keys and their count is the value

name = "shraddha"
dict = {}
for char in name:
    #print(char)# s /n h /n r /n a /n d /n d /n h /n a
    dict[char]=dict.get(char,0)+1
print(dict)#{'s': 1, 'h': 2, 'r': 1, 'a': 2, 'd': 2}

print("*"*80)

#program 2
#Another way of opening a file in python
with open('sample.txt','w') as f:
    f.write("Shraddha Potnis")
    #no need to write close file ..its already closed now

#program 3
#Serialization ...writing in file...creating objects f a file and write in a file(data stred in file is in terms of bytes)
import Employee,pickle

f = open('emp.dat','wb')
Num = int(input("Please enter the number of employees: "))

for item in range(Num):
    id = int(input("Please enter the id of the employee: "))
    name = input("Please enter the name of the employee: ")
    salary = int(input("Please enter the salary of the employee: "))
    x = Employee.Emp(id,name,salary)
    pickle.dump(x,f)#creates objects in the file
f.close()

# Please enter the number of employees: 2
# Please enter the id of the employee: 1
# Please enter the name of the employee: Shradz
# Please enter the salary of the employee: 100000
# Please enter the id of the employee: 2
# Please enter the name of the employee: Shraddu
# Please enter the salary of the employee: 200000

#Program 3
#De-Serialization...reading the data written in the file... converting the binary data into readable data
import Employee,pickle
f1 = open('emp.dat','rb')
print("Details")
while True:
    try:
        obj = pickle.load(f1)
        obj.display()
    except EOFError:
        print("End of all bjects")
        break

# Details
# The employee names 1 has Id as Shradz and earns 100000 in salary
# The employee names 2 has Id as Shaddu and earns 200000 in salary
# End of all bjects