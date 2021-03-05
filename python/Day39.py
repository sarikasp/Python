# operator overloading

print("*"*80)
#Operator Overloading

#program 1:
class BookX:
    def __init__(self,pages):
        self.pages = pages


class BookY:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, others):
        return self.pages + others.pages


b = BookX(60)
z = BookY(70)
print('Total pages ',z+b)

#Total pages  130

#program 2:

class classA(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

def passObj(obj):
    print(obj.name)
    print(obj.age)

a = classA("chinmay" ,23)
b= classA("tejaswi" ,24)
passObj(a)
passObj(b)

# chinmay
# 23
# tejaswi
# 24

#program 3:

class A():
    def __init__(self, pages):
       self.pages = pages


class B():

    def __init__(self, pages):
        self.pages = pages

    def __gt__(self, other):
        return self.pages > other.pages


b1 = A(100)
b2 = B(200)


if b2 > b1:
    print('b2 has more values')
else:
    print('b1 has more pages')


#b2 has more values

#program 4:

class Employee:
    def __init__(self,salary):
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days


class Days():
    def __init__(self,days):
        self.days = days


x = Employee(1000)
x2 = Days(2)

print("Total salary", x * x2)


#Total salary 2000


