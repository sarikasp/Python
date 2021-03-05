import sys
#program1
class Student:
    #mutator method or setter method
    def setName(self,n):
        self.name=n

    #accesor method or getter method
    def getName(self):
        return self.name

    def setMarks(self,m):
        self.marks=m

    def getMarks(self):
        return self.marks

nos = int(input("Enter the number of students"))#2

i = 0
ListOfObjectsStudents = []

while(i<nos):
    s = Student()
    nameOfObject = input("Enter the name : ")#SHRADDHA #SAMIKSHA
    s.setName(nameOfObject)
    marksOfObject = int(input("Enter the marks : "))#100 #100
    s.setMarks(marksOfObject)
    ListOfObjectsStudents.append(s)
    print(ListOfObjectsStudents)#[<__main__.Student object at 0x106d97cd0>, <__main__.Student object at 0x106dc6f10>]
    i +=1
    print("*"*80)

for item in ListOfObjectsStudents:
    print("The student named ",item.getName(),"scored ",item.getMarks())
    #The student named  Shraddha scored  100
    #The student named  Samiksha scored  100


#program2
#Static Methods

class Myclass:
    n = 0 #class variable
    def __init__(self,name):
        Myclass.n = Myclass.n + 1 #accessing class variable inside a constructor
        self.name= name

    #creating static method to tell the number of instances created

    @staticmethod
    def numOfObjectsCreated():
        print("The number of objects/class variables are {}".format(Myclass.n))
        return Myclass.n

#now creating objects
x = Myclass("Shraddha")
y = Myclass("Samiksha")
z = Myclass("Kalyani")

print(x.numOfObjectsCreated())
print(Myclass.numOfObjectsCreated())

# The number of objects/class variables are 3
# 3
# The number of objects/class variables are 3
# 3


#Program 3
#user-----> Account---0.0, deposit, withdraw, printBlance()

class Bank:
    nOfUser = 0

    def __init__(self,name,balance=0):
        Bank.nOfUser += 1
        self.name = name
        self.balance = balance

    #deposit
    def depositAmount(self,amount):
        self.balance += amount
        return self.balance
    #withdraw
    def withdrawAmount(self,amount):
        if amount > self.balance:
            print("Insufficient balance to withdraw ", amount)
        else:
            self.balance -=amount
        return self.balance
    #check balance
    def getBalance(self):
        return self.balance

    @staticmethod
    def numberOfAccounts():
        print("The total number of accounts ",Bank.nOfUser)


nameOfObject = input("Please enter your name :")
b = Bank(nameOfObject)

while(True):
    print("d=deposit","w=withdraw","bal=balance","e=exit")
    choiceOfTransaction = input("Please enter your choice of transaction: ")
    if choiceOfTransaction =="d":
        amount = int(input("Please enter the amount to be deposited: "))
        print(b.depositAmount(amount))
    elif choiceOfTransaction =="w":
        amount = int(input("Please enter the amount to be withdrawed : "))
        print(b.withdrawAmount(amount))
    elif choiceOfTransaction == "bal":
        print(b.getBalance())
    elif choiceOfTransaction =="e":
        break
    else:
        print("Select a valid option...")


# Please enter your name :shraddha
# d=deposit w=withdraw bal=balance e=exit
# Please enter your choice of transaction: ba
# Select a valid option...
# d=deposit w=withdraw bal=balance e=exit
# Please enter your choice of transaction: bal
# 0
# d=deposit w=withdraw bal=balance e=exit
# Please enter your choice of transaction: d
# Please enter the amount to be deposited: 10000000
# 10000000
# d=deposit w=withdraw bal=balance e=exit
# Please enter your choice of transaction: bal
# 10000000
# d=deposit w=withdraw bal=balance e=exit
# Please enter your choice of transaction: w
# Please enter the amount to be withdrawed : 0
# 10000000
# d=deposit w=withdraw bal=balance e=exit
# Please enter your choice of transaction: bal
# 10000000
# d=deposit w=withdraw bal=balance e=exit
# Please enter your choice of transaction: e
