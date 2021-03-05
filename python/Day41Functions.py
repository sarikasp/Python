#functions
#program1:Returning more than one value
# def add_sub(x,y):# parameters # Formal arguments
#     c = x+y
#     d = x-y
#     return c,d
#
# z = add_sub(9,5)
# print(type(z)) #<class 'tuple'>
# print(z) #(14, 4)
# add ,sub = add_sub(9,5)
# print(add)#14
# print(sub)#4
# print(z[0])#14
# print(z[1])#4

#################################################################################

#program2:
# def cal(x,y):
#     add = x+y
#     sub = x-y
#     mul = x*y
#     div = x/y
#     return add , sub ,mul,div
# x = cal(10,2)
# print(type(x)) #<class 'tuple'>
#
# for item in x:
#     print(item)
#12
# 8
# 20
# 5.0

###################################################################################
#program3: Function as a parameter to another function

# def display():
#     return 'Hey'
# result = display()+" Shraddha"
# print(result) #Hey Shraddha

###################################################################################
#program4: giving function as a parameter

# def  display(fun):
#     return 'Hi ' + fun
#
# def message():
#     return 'How are you?'
#
#
# print(display(message())) #Hi How are you?

######################################################################################
#program5: Function chaining

# def display():
#     def message():
#         return 'How are you?'
#
#     return message
#
# x= display()()
# print(x) #How are you?
# x = display()
# y = x()
# print(y) #How are you?
######################################################################################
# # Everything in python is object
# # Function as object
# # Separate address
###################################################################################

#program6:Interger are immutable in python

x = 10
print(id(x)) #4565941184 #4340935616 #4446944192

b = 10
print(id(b))#4340935616
#
# def f():
#     a = 10
#     b = 10
#     print("************")
#     print(id(a))#4483566528
#     print(id(b))#4483566528
#
#
# f() #10
# print(b) # 10
# print("************")
# print(id(b)) #4483566528

########################################################################
#program7:same reference

# y = 1000
# f = y
#
# print(id(y)) #140233728115888
# print(id(f)) #140233728115888

#######################################################################

#program8: integers are immutable..unchangeble
# x = 10
# print(id(x)) #4328917952
#
# x = 15
# print(id(x)) #4328918112

#######################################################################

#program9:
# b = 10
# print(id(b)) #4405369792
# a = 10
# print(id(a)) #4405369792
#
# def add(a):
#     a = 19
#     print(id(a)) #4405370080
#
# add(a)
# print(id(a)) #4405369792

########################################################################
#program10:

# y = (10,20)
# print(id(y)) #140239699520640
# y = (20,30,40)

# print(id(y)) #140239699581632
##########################################################################

#program 11:
# listA = ["Shraddha" ,"Potnis"]
# print(id(listA))#140718965887680
# listB = listA
#
# listB.append("Shanbhag")
# print(listA)#['Shraddha', 'Potnis', 'Shanbhag']
# print(listB)#['Shraddha', 'Potnis', 'Shanbhag']
# print(id(listA))#140718965887680
# print(id(listB))#140718965887680

###################################################################

#PROGRAM12.1:LISTS ARE MUTABLE
# listC = ["A","B","C"]
# def list(lst):
#
#     lst.append("D")
#     print(id(lst))#140379152814784
#
# list(listC)
# print(id(listC))#140379152814784


#PROGRAM12.2:LISTS ARE MUTABLE
# listD = ["A", "B", "C"]
# def list2(lst):
#     lst = ["A" ,"B" ,"C"] #A NEW MEMORY IS CREATED HERE
#     print(id(lst)) #140443553206720
# list2(listD)
# print(id(listD))#140443553206976

##########################################################################

#PROGRAM13:Key Arguments

# def printNameAge(age,name):
#     print(age,name)#Shraddha 29
#     print(type(name)) #<class 'str'>
#     print(type(age))#<class 'int'>
# printNameAge("Shraddha",29)
#
# print(type(printNameAge))#<class 'function'>
######################################################################

#program14:
# name  = "chinmay"
# print(type(name)) #<class 'str'>
#
# x = "chinmay"
# print(type(x)) #<class 'str'>
#
# x = 10
# print(type(x)) #<class 'int'>

##########################################################################

#program15:Default arguments

# def func(name = "Shraddha",age = 29):
#     print(name)
#     print(age)
# func()
#Shraddha
#29
# func("Radha" ,15)
# Radha
# 15




