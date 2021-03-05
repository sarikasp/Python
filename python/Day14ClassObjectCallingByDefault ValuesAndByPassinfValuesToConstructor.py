# class Students:
# #
# #      language = "English"
# #      # name = None
# #      # age = None
# #      # marks = None
# #
# #      # def __init__(self):
# #      #    self.name = "Vishnu"
# #      #    self.age = 20
# #      #    self.marks = 900
# #
# #      def __init__(self ,nm = "John" ,age =56 ,marks = 700):
# #          self.name = nm
# #          self.age = age
# #          self.marks = marks
# #
# #      # constructor overloading
# #
# #      def talk(self):
# #         print("Hello I am {}".format(self.name))
# #         print("My age is  {}".format(self.age))
# #         print("I got marks {}".format(self.marks))
# #
# #
# #
# #      def setAgeMarksName(self , nm ,ag ,mkr):
# #         self.name = nm
# #         self.age = ag
# #         self.marks = mkr
# #
# #
# # # Calling with all default values
# # chinmay = Students()
# # chinmay.talk()
# #
# #
# #
# # # By passing all values to the contructor
# #
# # #chinmay = Students("Ravi" , 34,44)
# # #chinmay.talk()
# #
# #
# #
# #
# # #
# # # chinmay = Students()
# # # #
# # # # chinmay.name = "chinmay"
# # # # chinmay.age = 100
# # # # chinmay.marks = 900
# # #
# # # chinmay.setAgeMarksName("chinmay",34,900)
# # #
# # # chinmay.talk()
# # #
# # #
#
#
#
# # Types of varibales
#
# # Instance varible
#
# # Class variables



# Instance variables
#
# class Sample:
#
#     def __init__(self,y):
#         self.y = y;
#
#     def modify(self,y):
#         self.y = y
#
#
# #abc = Sample()
#
#
# a = Sample(9)
# print(a.y)
# a.modify(89)
# print(a.y)
#
#
# b= Sample(999)
# print(b.y)
# b.modify(89999)
# print(b.y)



# Program 3


class Sample2:

    x = 10

    # this is classMethod
    @classmethod
    def modify(cls,yc):
        cls.x += yc



# a = Sample2()

b = Sample2()
print(b.x)
b.x = 100

print("----------------------------------")

print(b.x)
print(Sample2.x)

print("---------------------------------")


Sample2.modify()
print(Sample2.x)

Sample2.x = 67
print(Sample2.x)







