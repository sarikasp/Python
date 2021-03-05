# compile type error

#syntax erroe

# def add ()
#     print('Hello')
#
# add()
# PVM
#Run time error (ZeroDivisionError)
# print('Hello , I am working')
# print(10/0)                       #
# print('Hello I am still working ')


# Run time error 2 (Type Error)
# def add(a,b):
#     print(a+b)
#
# add(2,4)
# add(2,"hello")


# Run time (IndexError)

# listA = [1,2,3,4]
# print(listA[4])


# ----  salary    1000   -- 10  --- total salary

# def totalSal(sal):
#     return 0.10 * sal + sal
# print(totalSal(2000))

# BaseException
# Exception ---

try:
    #print(10/0)

    # listA = [1,2,3,4]
    # print(listA[4])

    #print('Hello'+8)
    print('Hello')

# except ZeroDivisionError:
#     print('please input the correct value')

except IndexError:
    print('Please add additional elements to the list')

except TypeError:
    print('You cannot add string to the interger directly')

else: # optional block
    try:
        print('Nexted block')
        print(12/0)
    except:
        print('Nexted exception')

finally:
    print('I am running at the end of the file')



# program 2 for the multiple blocks


try:
    #print(10/0)

    listA = [1,2,3,4]
    print(listA[4])

    #print('Hello'+8)
    print('Hello')

except (ZeroDivisionError,IndexError):
    print('please input the correct value')
    print('Please add additional elements to the list')

# except IndexError:
#     print('Please add additional elements to the list')

# except TypeError:
#     print('You cannot add string to the interger directly')

else: # optional block
    try:
        print('Nexted block')
        print(12/0)
    except:
        print('Nexted exception')

finally:
    print('I am running at the end of the file')

#------------------------------------------------

# Assertion block

try:
    x = int(input("Please Enter the value between 10 to 100"))
    assert x > 10 and x <= 100
    print("The number is{}".format(x))
except AssertionError:
    print('The condition is not fullfilled')


try:
    x = int(input("Please Enter the value between 10 to 100"))
    assert x > 10 and x <= 100 ,"The condition is not fullfilled"
    print("The number is{}".format(x))
except AssertionError as obj:
    print(obj)



# tuple block
# try:
#     x = int(input("Please Enter the value between 10 to 100"))
#     assert (x > 10 and x <= 100 ,"The condition is not fullfilled")
#     print("The number is{}".format(x))
# except AssertionError as obj:
#     print(obj)