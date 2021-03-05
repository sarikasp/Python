#program1: Function as a parameter to another function

# listA = ['A','B','C','D']
# listB = ['C','D','E','F','G']
# def printList(list):
#     for item in list:
#         print(item)
# printList(listA)
# printList(listB)

##########################################################################################################################
#program2:Function as a parameter to another function

# def add():
#     print(7+8)
#
#
# def cal(fn):
#     fn()
#
# cal(add)#15
#
############################################################################################################################
#program3:
# def add():
#     return 7+8
#
#
#
# print(add)#<function add at 0x7fb84b901820>
# print(add())#15

##########################################################################################################################
#program4:recursive functions in python

# def factorial(n):
#
#     if n == 0:
#         result = 1
#     else:
#         result = n * factorial(n-1)
#         # *  factorial(n-1) * factorial() * factorial() * factorial(0)
#         print(result)
#
#     return result
#
# r = factorial(5)
#
# print(r)
#1
#2
#6
#24
#120

#factorial(4)*factorial(3)*factorial(2)*factorial(1)

##########################################################################################################
#program5: lamda function

# def square(x):
#     return x*x

#syntax for lambda  is lamda argument_list : expression

# q = lambda x : x*x
# print(q(5))#25

##################################################################################################

#program6: lamda function

# c = lambda x,y: x + y
# print(c(3,4)) #7

###############################################################################################

#program7: reduce function
#from functools import *
# # import functools

# #
# import  functools
#
# #from functools import *
#
# print(functools.reduce())
#
#
# lst = [1,2,3,4,5]
# result = functools.reduce(lambda x,y:x+y ,[1,2,3,4,5,6])#if i import * i dont need to mention the keyword functools
# print(result)
#
#

#######################################################################################

#PROGRAM8:
# def isEven(x):
#     if x % 2 ==0:
#         return True
#     else:
#         return False
#
#
# lst = [1,2,3,45,556]
# x = list(filter(isEven,lst)) ## filter object can be convert in to sequence data type only (tuple , tuple)
# print(x) #[2, 556]



###########################################################################################

#PROGRAM9:
# lst = [1,2,3,45,556]
# lst = tuple(filter(lambda x: x % 2 == 0,lst))
# print(lst) #(2, 556)

#######################################################################################

#PROGRAM10: map() function
# lst = [1,2,3,45,556]
#
# def pr(x):
#     return x + 2#
#
# lst = list(map(pr,lst))
# print(lst)#[3, 4, 5, 47, 558]
#
# lst = list(map(lambda x:x * 2,lst))
# print(lst)#[6, 8, 10, 94, 1116]

#####################################################################################

# filter, map  AND reduce   :  sequence data type



#################################################################
#PROGRAM11:#strings


# from functools import *
#
# lst = ["Shraddha" , " Potnis"]
# result = reduce(lambda x,y:x+y ,lst)
# print(result) #Shraddha Potnis


##############################################################

#program12:

# lst = [" Shraddha" ," Potnis"]
# result = list(map(lambda x: 'Welcome'+ x ,lst))
# print(result) #['Welcome Shraddha', 'Welcome Potnis']

###############################################################

#PROGRMAM13:
#
# lst = ["luckyshradz08@gmail.com " ," sh@gmail.com"]
# result = list(filter(lambda x:len(x) <= 14 ,lst))
# print(result) #['sh@gmail.com']

################################################################

#PROGRAM14:

# # Numbers
#
# from functools import *
#
# result = reduce(lambda x,y:x+y ,[1,2,3,4])
# print(result)#10                  1+2=3,3+3=6,6+4=10

##################################################################

#program15:
# result = list(map(lambda x: x+2 ,[1,2,3,4,5,6,7]))
# print(result)#[3, 4, 5, 6, 7, 8, 9]

##############################################################################

#program16:

# result = list(filter(lambda x: x > 2 ,[12,34,45,45,565,777,899,000]))
# print(result) #[12, 34, 45, 45, 565, 777, 899]

####################################################################################


# decorator
# lst = list(map(pr,lst))
# print(lst)








