#list = ["apple","mango"]
#dict = {"name" : "Shraddha",
       #  "age" : 29,
       #  "country" : ["India","Denmark"],
       #  "skills" : ("python", "java", "sql")
       #  "marriage details" : {"maidenname": "Shraddha", "hobby" : "Singing"}
       # }
#str = "Shraddha"

#set

flowers = {"lilly","orchid"}
print(type(flowers))#<class 'set'>
print(flowers)#{'orchid', 'lilly'}

#to print all the  elements of a set

for item in flowers:
    print((item))# lilly /n orchid

print("*"*80)

# is available in the set
if "lilly" in flowers:
     print("Available")#Available

print("*"*80)
# to add an item to a set

print(flowers.add("jasmine"))#returns None
print(flowers)#{'lilly', 'jasmine', 'orchid'}# A new element can be added anywhere

print("*"*80)

def add(x,y):
    return x + y
z = add(22,33)
print(z)#55

print("*"*80)
#adding multiple values to the set
flowers.update(["rose","sunflower","tulip","lotus"])
print(flowers)#{'jasmine', 'lilly', 'sunflower', 'rose', 'orchid', 'lotus', 'tulip'}

print("*"*80)
#to find the length

print(len(flowers))#7

print("*"*80)
#to remove an element
flowers.remove("lotus")#removes lotus{'rose', 'sunflower', 'tulip', 'lilly', 'jasmine', 'orchid'}
print(flowers)
#flowers.remove("lotus")#if i do it again it gives me a keyerror
#to remove an element using a discard function
print(flowers.discard("sunflower"))#returns None
print(flowers)#{'tulip', 'jasmine', 'lilly', 'rose', 'orchid'}
print(flowers.discard("sunflower"))#returns None without giving an error unlilke remove

print("*"*80)
print(flowers.pop())# it pops randomly
print(flowers)#{'tulip', 'lilly', 'rose', 'orchid'}

print("*"*80)
# name = {"Shraddha" ,"Roshani" , "Neha"}
# person = input("Please Enter the name to be removed :")
# name.discard(person)
# print(name)

#using the remove function
#
# name = {"Shraddha" ,"Roshani" , "Neha"}
# person = input("Please Enter the name to be removed :")#Neha
# if person in name:
#     name.remove(person)
#     print(name)#{'Shraddha', 'Roshani'}
# else:
#     print(("Not in the list"))
#     print(name)

print("*"*80)
cities = {"Mumbai", "Pune", "Kolkata"}
cities.clear()
print(cities)#set()# maintains the schema

list = ["a","b"]
list.clear()
print(list)#[]# maintains the schema

dict = { "name" : "shraddha",
         "age" : 29
}
dict.clear()
print(dict)#{}# maintains the schema

#no clear method on a string

print("*"*80)

# del cities
# print(cities)#gives error name 'cities' is not defined# does not maintain the schema

#join operatoins on sets
#1.unios()
setOne = {"a","b","c","d"}
setTwo = {"c","d",1,2,3,4}
setThree = setOne.union(setTwo)
print(type(setThree))#<class 'set'>
print(setThree)#{1, 2, 3, 4, 'c', 'a', 'b', 'd'}
#union() and update() adds by removing the duplicate elements

#2.difference()
print(setOne.difference(setTwo))#{'b', 'a'}
print(setTwo.difference(setOne))#{1, 2, 3, 4}

print("*"*80)
#call by reference
set1 = {"A", "B"}
set2 = set1#set2 is refereing to the same memory as that of set1..no new memory formed
set2.pop()
print(set2)#{'A'}
print(set1)#{'A'}


print("*"*80)
set3 = set1.copy()#now new memory is formed for set3
set3.pop()
print(set3)#set()
print(set1)#{'A'}
