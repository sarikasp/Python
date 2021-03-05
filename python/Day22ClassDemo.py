#program 1
#overloading without using constructor
class Operations():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum of the three numbers is : {}".format(a+b+c))
        elif a!=None and b!=None:
            print("The sum of two numbers is : {}".format(a+b))
        else:
            print("Please enter atleast two numbers...")
o = Operations()
o.sum(12,24,36)#The sum of the three numbers is : 72   #......this is overloading
o.sum(33,55)#The sum of two numbers is : 88   #......this is overloading
o.sum(2)#Please enter atleast two numbers...   #......this is overloading

#program2
#overloading with using a constructr
class COperations():
     def __init__(self,A,B,C):
         self.A= A
         self.B= B
         self.C= C

     def addition(self, A=None,B=None,C=None):
         if A != None and B != None and C != None:
             print("The sum of the three numbers is : {}".format(A + B + C))
         elif A!=None and B!=None:
             print("The sum of two numbers is : {}".format(A+B))
         else:
             print('please enter more then one variables for sum')

o2 = COperations(1,2,3)
o2.addition(o2.A,o2.B,o2.C)#The sum of the three numbers is : 6
o2.addition(o2.A,o2.B)#The sum of two numbers is : 3
o2.addition(o2.C)#please enter more then one variables for sum

#program 3
#overriding...diff class same method same signature
class Square():
    def op(self,x):
        print(x*x)

class Cube(Square):
    def op(self,x):
        print(x*x*x)
        super().op(x)

c = Cube()
c.op(7)
#343
#49

