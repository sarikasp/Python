#decor operators:
#program1:
# def decor(fun):
#     def inner():
#         value = fun()  # num() --- 10
#         return value * 2 # 12  # 20
#     return inner
#
# #
# @decor
# def sub():
#     return 29
#
# print(sub())
#
#
#
#
# x = decor(num)
# print(x)
# y = x()
# print(y)

################################################
#program2:
# def decor1(fun):
#     def inner():
#         value = fun()  # num() --- 10
#         return value + 2 # 12   # 22
#     return inner
#
#
# @decor
# @decor1  # immediate will be called firstly
# def num():
#     return 10
#
# print(num())
#############################################################

#program3:
# def lis(lis):
#     def inner():
#         ty = []
#         val = lis()
#         for item in val:
#             ty.append(item+'@gmail.com')
#         return ty
#     return inner
#
#
# @lis
# def Em():
#     return ["chinmay","poorva","rasika"]
# print(Em())
#
#

##################################################################
#program5:
# import functools
# def mul(x,y):
#     return x * y
#
# lst = [1,2,3,4,5,6,7,8,9]
# print(functools.reduce(mul, lst))
#

###############################################################
#program6:

#if __name__ = '__main__':
import Day44.1
#day.display()
#day.display2()


# File Day44.1.py

# def display():
#     print("Hello I am from the another world ")
#
# def display2():
#     print('I am from the dislay two')
#
#
#
# if __name__ == '__main__':
#     print('This program runs as a python program')
# else:
#     print('This program is running as the module')






