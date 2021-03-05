# Function or Method

##############################################################################################
#Method

# Called  with object
# Call with class name

# Function object python
##############################################################################################
#program1: a function to add two numbers
#def add():
#     """ Sum of two numbers"""
#     print(5+7)
#
# add()

##############################################################################################
#Program2: to print if the number is even or oddd
def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num,'is odd')


even_odd(12)
even_odd(24)
# Modules


###########################################################################
#program3: Passing function as paramter to another function

#age =  [21,22,23,24 ,17]

# additionAge = [31,32,33,34,27]

#above18 = [True , True,True,True,False]

#birthYear = [1999 ,1998 ,1997 ,1996]

# Generic function
#
# def printList(list , fn):
#     commonList = []
#     for item in list:
#         commonList.append(fn(item))
#     return commonList
#
# # Function 1
# def birthYear(x):
#     return 2020 - x
#
# # Function 2
#
# def isAge(x):
#     return  x > 18
#
# def addTen(x):
#     return x+10
#
# z= printList(age , addTen)
# print(z)
# x = printList(age,isAge)
# print(x)
# y = printList(age,birthYear)
# print(y)
#birthYear(age[0])

###########################################################################
#program4: factorial


#  add = 4 * 3 * 2 * 1

# def fact(n):
#     add = 1
#     while n >= 1:
#         add  = add * n
#         n = n-1
#     return add
#
#
# print(fact(4))
# print(fact(-4))
#
# for x in range(1,11):
#     print('The factorial of',x,":", fact(x))

############################################################################
#program5: prime number

# 25


#5 # 4 3 2

#25 % 5

# def prime(n):
#     flag = False
#     for x in range(2,n):
#         if n  % x == 0:
#             flag = True
#             break
#         else:
#             flag = False
#     return flag
#
# n = int(input('Please Enter the number to be checked'))
# x = prime(n)
#
# if x:
#     print('Number is not prime ')
# else:
#     print('Number is prime')


###########################################################################
#PROGRAM6: Global scope or local


# a = 10
#
# def printA():
#     print(a)
#
# printA()
# print(a)

#---------------------------------

# a = 10
# def printA():
#     x = globals()['a']
#     a = 20
#     print(a)
#     print(x)
#
# printA()
# print(a)


# a = 10
#
# def printA():
#     print(a)
#
# printA()
# print(a)


#####################################################################
#Program7:
# def prime(n):
#     flag = False
#     for x in range(2,n):
#         if n  % x == 0:
#             flag = True
#             break
#         else:
#             flag = False
#     return flag
#
# n = int(input('Please enter number of prime numbers you wish to find'))
#x = prime(n)

# if x:
#     print('Number is not prime ')
# else:
#     print('Number is prime')


# i = 2
# count = 0
#
# while True:
#     if not prime(i):
#         print(i)
#         count += 1
#     i += 1
#     if count > n:
#         break

# for x in range(2,n):
#     if not prime(x):
#         print(x)


#5 # 60
####################################################################################
#interview questions
# Encapsulation # class
#
# Abstraction
#
# Inheritance (single , multi , multilevel)
#
# Polyporphim (Overriding , overloading )

# Unix cmd (SQL )














