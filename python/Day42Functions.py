#functions
#program1:Varibale length argumenent: here arguements stored in a variable of type tuple

# def add(a,*b):
#     print(type(a)) #<class 'int'>
#     print(type(b)) #<class 'tuple'>
#     sum = 0
#     for item in b:
#         sum = sum + item
#     print("The total sum of all the elements refered by a and b is {}".format(sum+a)
#     #The total sum of all the elements refered by a and b is 45
#
# add(1,2,3,4,5,6,7,8,9) #The total sum of all the elements refered by a and b is 45

###############################################################
#program2:
# def add(a,*b):
#     print(type(a))#<class 'int'>
#     print(type(b))#<class 'tuple'>
#     add1 = 0
#     for item in b:
#         add1 = add1 +item
#         print(add1)
# add(1,2,3,4,5,6,7,8,9)

###############################################################
# def add(a,*b):
#     print(a)
#     print(type(b))
#     sum = 0
#     for item in b:
#         two = a + item
#         print(two)
#         sum = sum + two
#
#     print("Addition is {}".format(sum))
# add(2,6,3,4,5,6,7,8,9,1,2,34,5,66,77)

###############################################################

#program4: Variable length argurments...here arguements stored in a key value pair in terms of a dictionary

# def  studentInformation(id,**kwargs):
#     print(id) #1
#     print(kwargs)#{'Firstname': 'Shraddha', 'Lastname': 'Potnis', 'Language': 'English'}
#     for x ,y in kwargs.items():
#         print("{}:{}".format(x,y))
#         # Firstname: Shraddha
#         # Lastname: Potnis
#         # Language: English
#
#     for item in kwargs.keys():
#         print("{}".format(item))
#     # Firstname
#     # Lastname
#     # Language
#     for item in kwargs.values():
#         print("{}".format(item))
#     # Shraddha
#     # Potnis
#     # English
#
# studentInformation(1, Firstname = "Shraddha",Lastname ="Potnis" ,Language = "English")

###################################################################################################

#program5:list comprehension... divide the elements of the list by 2
# num = [1,2,3,4,5,6,7,8,9,10]
# list= [item/2 for item in num]
# print(list) #[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]


# ###################################################################################################
# #program6: list comprehension:  print individual characters of a string in a list
# y = [item.upper() for item in "S h r a d d h a".split(" ")]
# print(y) #['S', 'H', 'R', 'A', 'D', 'D', 'H', 'A']

# ch = "S,h,r,a,d,d,h,a"
# print(ch.split(","))


#####################################################################################################

#program7: print average and sum of the elements of a list
# x = [int(item) for item in input('Enter the numbers seperated by a comma(,): ').split(',')]#1,2,3,4,5
# print(type(x)) #<class 'list'>
# print(x) #[1, 2, 3, 4, 5]
# def calculate(lst):
#     sum = 0
#     for item in lst:
#         sum += item
#     print(sum)#15
#     average = sum / len(lst)
#     return  average,sum
#
# avg,sum = calculate(x)#of type tuple
#
# print(avg,sum)#3.0 15
#
#########################################################################################

#program8: returning just one arguement ..then it is not of type tuple

# # x = [int(item) for item in input('Enter the number').split(',')]
# # def calculate(lst):
# #     sum = 0
# #     for item in lst:
# #         sum += item
# #     average = sum / len(lst)
# #     return  average
# #
# # avg = calculate(x)
# # print(avg)


















