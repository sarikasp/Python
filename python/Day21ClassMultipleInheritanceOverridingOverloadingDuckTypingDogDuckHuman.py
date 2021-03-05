#Multiple inheritance
#Program..also called Method resolution order

class A():
    def method(self):
        print("A class method called")#3 A class method called
        super().method() #every class has a super as object class

class B():
    def method(self):
        print("B class method called")#5 B class method called
        super().method()

class C():
    def method(self):
        print("C class method called") #6 C class method called
        super().method()

class D():
    def method(self):
        print("D class method called")#7 D class method called


class X(A,B):
    def method(self):
        print("X class method called")#2 X class method called
        super().method()

class Y(B,C):
    def method(self):
        print("Y class method called")#4 Y class method called
        super().method()

class Z(X,Y,C,D):
    def method(self):
        print("output is: ")
        print("Z class method called") #1 Z class method called
# X class method called
        super().method()

z = Z()
z.method()
# output is :
# Z class method called
# X class method called
# A class method called
# Y class method called
# B class method called
# C class method called
# D class method called

print("*"*100)

# Single , Multilevel , Multiple (Interface)
# Encapsulation # Inheritance


# same class , same method name with signature (It will work in java) overloading

# Different class same method name with same signature  # overriding

# Run time polymorphism

# Compiler time polymorphism

# Poly - Forms





print("*"*100)

#Program 2....overriding and overloading
class A():
    def sample(self):
        print("I am from class A")
    def sub(self):
        print("I am from class parent")
class B(A):
    def sample1(self):
        print("I am from class B")
    def sub(self):
        print("I am child")


b = B()
b.sample()#I am from class A...overriding
b.sample1()#I am from class B...overriding
b.sub()#I am child..overloading


print("*"*100)
# 1) duck typing
# 2) Overriding
# 3) Over loading (Operator overloading)

#program 3
class Duck():
    def sound(self):
        print('Quack!')

class Human():
    def sound(self):
        print("Hi")

def test_sound(obj): #this is a function
    obj.sound()

d = Duck()
test_sound(d)#Quack!


h = Human()
test_sound(h)#Hi

print("---------------------*----------------------------"*4)

class Dog():
    def barks(self):
        print('Bow')

class Duck():
    def sounds(self):
        print('Quack!')

class Human():
    def sounds(self):
        print("Hi")

def test_method(obj):
    if hasattr(obj,'sounds'):
        obj.sounds()
    elif hasattr(obj,'barks'):
        obj.barks()
    else:
        print('Wrong object passed....')


bulldog = Dog()
test_method(bulldog)# Bow

Shraddha = Human()
test_method(Shraddha)#Hi

donald = Duck()
test_method(donald)#Quack!

