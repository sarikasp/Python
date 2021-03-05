name = "shraddha"
print(len(name))#8

listNames = ["shraddha","radhaa","jayapradha","jaya"]
print(listNames[0])#shraddha
print(len(listNames))#4

for item in listNames:
    print(item)

for num in range(1,10):
    print(num)#1 to 9

# printing all list using range function

print("*" * 80)

for item in range(len(listNames)):#4
    print(listNames[item])

print("*"*80)

# adding the element to the list

listNew = []

listNew.append("radhika")
print(listNew)

y = listNew.append("krutika")
print(y)#None

#print(listNew.append("krutika"))

print("*"*80)
x = None
print(type(x))# < class 'NoneType' >
x=20
print(type(x))# <class 'int'>
x = "shraddha"
print(type(x))# <class 'str'>
print(type(listNew))#<class 'list'>

print("*"*80)
# Adding into the list with index using insert mkethod

listNew.insert(1,"Sarika")
print(listNew)



