#listA=["a","b","c"]
#listB=[]
#print(listA[0])#["a"]
#print(listA[1])#["b"]
#print(listA[2])#["c"]
#print(listA[:])["a","b","c"]
#print(listA[-1])#["c"]
#print(listA[1:2])#["b"]
#print(len((listA))#3
#print(listB)#[]

#tuple looks like a list but in round bracket..but it in uneditable
listTuple = ("apple","mango","pear","apples","grapes","watermelon","apple","chikoo")
print(listTuple)#('apple', 'mango', 'pear', 'apples', 'grapes', 'watermelon', 'apple', 'chikoo')

print("*"*80)

print(listTuple[0])#apple
print(listTuple[1])#mango
print(listTuple[2])#pear
print(listTuple[3])#apples
print(listTuple[-5])#apples
print(listTuple[:6])#('apple', 'mango', 'pear', 'apples', 'grapes', 'watermelon')
print(listTuple[3:7])#('apples', 'grapes', 'watermelon', 'apple')
#print(listTuple[-7:-8])#DOES NOT ITERATE FROM RIGHT TO LEFT

print("*"*80)

#Second Tuple
flower = ("rose","lily","sunflower")
#flower[1] = "jasmine"#tuple is not edited unlike lists
#solution is to convert a tuple to a list
listC = list(flower)
print(type(listC))#<class 'list'>
print(listC)#['rose', 'lily', 'sunflower']
listC[1] = "jasmine"
print(listC)#['rose', 'jasmine', 'sunflower']
newTuple = tuple(listC)
print(newTuple)#('rose', 'jasmine', 'sunflower')

print("*"*80)

#To find the length of Tuple
y = len(flower)
print(y) #3


tupleD= ('a' , "b" ,"c")  # True or flase
print(tupleD[0])#a

if 'a' in tupleD:
     print('Present in tuple')

print("*"*80)
name = "SHRADDHA POTNIS"
if "SHRADDHA" in name:
    print("Yes present")

for item in tupleD:
    print(item)# a \n  b  \n   c

for item in range(3,10):
    print(item)# prints from 3 to 9

for item in range(100):
    print(item)#prints frm 1 to 99

print(len(tupleD))# 3

for item in range(len(tupleD)):#I.E.range(3)
    print(tupleD[item])# a \n b \n c

print("*"*80)

#addition of two tuples
tupleOne = (1,2,3)
tupleTwo = ("A",3,5)
tupleThree = tupleOne + tupleTwo
print(tupleThree)#(1, 2, 3, 'A', 3, 5)

print("*"*80)

#collection inside a tuple/e.g tuple inside a tuple
tupleMix = ((1,2) ,(3,4),(4,5))
firstInnerTuple = tupleMix[1]#(3,4)
firstValueOfInnerTuple = firstInnerTuple[0]
print(firstValueOfInnerTuple)#3

print("*"*80)

tupleZ = ("Apple" ,"Apple" ,"Banana","Chiku" ,"Banana")
print(tupleZ)#('Apple', 'Apple', 'Banana', 'Chiku', 'Banana')

#.COUNT function on tuple
print(tupleZ.count("Apple"))#2
print(tupleZ.index("Banana",1,10))#2

print("*"*80)

name = "shraddha"
print(name[0])#s
print(name[1])#h

# Loops
for char in name:
     print(char)#s \n h \n r \n a \n d \n d \n h \n a

print("*" * 80)

for char in name[3:]:
     print(char)#addha

# finding the length of string

print(len(name))#8

print("*" * 80)

# range
for x in range(9):
    print(x)# prints 0 to 8


for x in range(1,8):
     print(name[x])#prints h r a d d h a

print(len(name))#8
# i.e. range(8)

for x in range(len(name)):
     print(x)
     print(name[x])








