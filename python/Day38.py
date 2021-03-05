# function inside inside function

z = 35
def Hello():
    print('Hello World!')
    a = 10

    return def sayHello():
        print('sayHello')
        print(a)
        c = 10
        print(c)
        print(z)

# Hello()`

# def ga():
#     print('Good Moring')
#     def a():
#         print('Hello')
#     return a
#
# def hello():
#     print('Print hello')
# def sayHello(fun):
#     fun() # calling function inside another
#
# sayHello(hello)
# sayHello(ga)()

# def greeting():
#     print('Hello Greeting ........!')
#
#     def Evening():
#         print('Hello Event')
#
#     return Evening
#
# xy = greeting()
# xy()


str = 'anil akhil anant arun arundhati abhjit ankur aunty'
result  = re.findall(r'a[nku][\w]*',str)
print(result)

print(re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}','Neha 20-11-1991 , Poorva 29-10-1993 , Reshma 2-2-1990'))

# starting the string with the sub string ...


