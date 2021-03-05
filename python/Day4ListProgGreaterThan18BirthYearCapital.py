# age = [12,19,2,18,22,15,65,59]
#
# #to print a list with  true where the age>=18
# # and false where age<18
#
# isGreaterThan18 = []
#
# for item in age:
#     if item >= 18:
#         isGreaterThan18.append(True)
#     else:
#         isGreaterThan18.append(False)
# print(isGreaterThan18)#[False, True, False, True, True, False, True, True]
#
# print("*"*80)
#
# #to print a list with the birth year of elements in age[]
#
# birthYear = []
# currentYear = 2020
#
# for item in age:
#     birthYear.append(currentYear - item)
# print(birthYear)#[2008, 2001, 2018, 2002, 1998, 2005, 1955, 1961]
#
# print("*"*80)
#
# # print a list with years left fr retirement
#
# ageToRetire = []
# ageOfRetirement = 65
#
# for item in age:
#     ageToRetire.append(ageOfRetirement-item)
# print(ageToRetire)#[53, 46, 63, 47, 43, 50, 0, 6]

print("*"*80)

# Refactoring the above code with function

age = [12,19,2,18,22,15,65,59]
isGreaterThan18 = []
birthYear = []
currentYear = 2020
ageToRetire = []
ageOfRetirement = 65

def printList(list,fn):
    newList = []
    for item in list:
        newList.append(fn(item))
    return newList

def ageGreaterThanEighteen(el):
    return el>=18

def birthYearAccToCurrentYear(el):
    return currentYear-el

def ageToRetirement(el):
    return ageOfRetirement-el

print(printList(age,ageGreaterThanEighteen))#[False, True, False, True, True, False, True, True]
print(printList(age,birthYearAccToCurrentYear))#[2008, 2001, 2018, 2002, 1998, 2005, 1955, 1961]
print(printList(age,ageToRetirement))#[53, 46, 63, 47, 43, 50, 0, 6]

print("*"*80)
# Removing the items from the element

capitalOfCities = ["Mumbai", "Gandhinagar","Jaipur","Bhopal","Bangalore","Chennai"]
capitalOfCities.remove("Mumbai")
print(capitalOfCities)#['Gandhinagar', 'Jaipur', 'Bhopal', 'Bangalore', 'Chennai']

print("*"*80)
# removing the element via index using pop method
capitalOfCities.pop(2)
print(capitalOfCities)#['Gandhinagar', 'Jaipur', 'Bangalore', 'Chennai']

print("*"*80)

listA = ["a", "b","a", "c", "d", "a"]
#listA.remove("a")
#print(listA)#['b', 'a', 'c', 'd', 'a'] REMOVES THE FIRTST a

listA.pop()
print(listA)#['a', 'b', 'a', 'c', 'd']removes the last element

#to remove all the "a" from listA

# Removes the removes the last element from the list

# y = capitalCity.index("Mumbai",0,10)
# for item in range((y+1),len(capitalCity)):
#     if capitalCity[item] == "Mumbai":
#         capitalCity.pop()
#     print(capitalCity)
listA = ["a", "b","a", "c", "d", "a"]
listA[:] = [item for item in listA if item !="a"]#list comprehension
print(listA)#['b', 'c', 'd']


