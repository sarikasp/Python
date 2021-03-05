#Program 1
class Employee():

    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("The person with name {} has employee id as {} and salary as {}".format(self.name,self.id,self.salary))

# class DisplayInfo():

    @staticmethod
    def disp(e):
        print(e.id)
        print(e.name)
        print(e.salary)
        e.salary = 200000

Shraddha = Employee(1,"Shraddha",100000)
Shraddha.display() #The person with name Shraddha has employee id as 1 and salary as 100000

Employee.disp(Shraddha) #The person with name Shraddha has employee id as 1 and salary as 200000
#1
# Shraddha
# 100000

Shraddha.display() #The person with name Shraddha has employee id as 1 and salary as 200000

print("*"*80)

#program 2
class PowerCal():

     @staticmethod
     def powercal(x,y):
         print(x ** y)

PowerCal.powercal(2,3)#8

print("*"*80)

#program3.....encapsulation
class Person():
     def __init__(self):
         self.name = "Shraddha"
         self.dateOfBirth = self.Dob()

     def display(self):
         print("The name of the person is : " ,self.name)

     class Dob():
         def __init__(self):
             self.date = 9
             self.month = 11
             self.year = 1990

         def display(self):
            print("This person was born on {}th/st of {}th/st month of the year {} ".format(self.date,self.month,self.year))

ShraddhaPotnis = Person()
ShraddhaPotnis.display()#The name of the person is :  Shraddha
d = ShraddhaPotnis.dateOfBirth
d.display() #This person was born on 9th/st of 11th/st month of the year 1990

