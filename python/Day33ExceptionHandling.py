#1: synatx error are complie type errors
# def add(x):
#  if  x == 2:
#     #print('hello')
# add(2)
    # add(2)
    #^
#IndentationError: expected an indented block




#2: Logical error

# def addFifteenPercentBonus(x):
#     return (0.15 * x )  #+ x
# x = addFifteenPercentBonus(1000)
# print(x)
#150.0...should return 150+1000=1150

#3: Run type errors

# x = [1,2,3,4,5,6]
# print(x[7])
# print('hello')
#    print(x[7])
#IndexError: list index out of range

print("*"*80)
#when i can manage the error --- exception


#4:Exception Handling

# import os
# f = open('myfile.txt','r')
# print(os.getcwd())
# f.write(10/0)
# f.close()

# f.write(10/0)
# ZeroDivisionError: division by zero



# try:
#     f = open('myFile.txt', 'w+')
#
# except ZeroDivisionError:
#     print('you cannot divide by zero')# Handler
# except IOError:
#     print('File not found')
# except:
#     print('Some exception occur')
# else:
#     try:
#         f.write(10/0)
#     except ZeroDivisionError:
#         print('Division error')
# finally:
#     f.close()

print("*"*80)

#5.Exception Handling
# def divE(x,y,z):
#     try:
#         f = open(x, 'r+')
#
#     except ZeroDivisionError:
#         print('you cannot divide by zero')  # Handler
#     except IOError:
#         print('File not found')
#     except:
#         print('Some exception occur')
#     else:
#         try:
#             c = int(y/z)
#             f.write(str(c))
#         except ZeroDivisionError:
#             print('Division error')
#     finally:
#         print('No file found')
#
# divE("minole.txt",10,0)


#---------------------------------------
#6.Exception Handling
# try:
#   print("name" + 4)
# except TypeError:
#   print("Please enter the correct")
#
# # hanlding the AssertionError
#
# try:
#     assert  10
# except AssertionError:
#     print('please pass condition to be true')


# try:
#     if null:
#         print('Hi')
# except NameError :
#     print("Please Enter the valid input")






