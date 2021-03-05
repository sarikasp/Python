# data structures
# collection list

fruits = ["apple", " chikoo", "banana", "mango", "stawberry", "peach", "grapes"]

fruits.append("cherry")
print(fruits) #output is ["apple", " chikoo", "banana", "mango", "stawberry", "peach", "grapes", "cherry"]
x=fruits.count("mango")
print(x) #output is 1
#fruits.clear()
fruits.insert(2,"papaya")
print(fruits)#output is ["apple", " chikoo", "papaya", "banana", "mango", "stawberry", "peach", "grapes","cherry"]
fruits.reverse()
print(fruits) #output is ["cherry","grapes","peach","stawberry","mango","banana","papaya"," chikoo","apple"]
fruits.reverse() #output is ["apple", " chikoo", "papaya", "banana", "mango", "stawberry", "peach", "grapes", "cherry"]
fruits.pop(2)
print(fruits)#output is ["apple", " chikoo","banana", "mango", "stawberry", "peach", "grapes","cherry"]
#print(fruits[0]) #output is "apple"
#print(fruits[1])#output is "chikoo"
#print(fruits[2])#output is "banana"


#print(fruits[0:7])#output is ["apple", " chikoo", "banana", "mango", "stawberry", "peach","grapes","cherry"]
#print(fruits[1:])#output is [ " chikoo","banana", "mango", "stawberry", "peach", "grapes","cherry"]
#print(fruits[:])#output is ["apple", " chikoo","banana", "mango", "stawberry", "peach", "grapes","cherry"]
#print(fruits[0:])#output is[ "apple", " chikoo","banana", "mango", "stawberry", "peach", "grapes","cherry"]
#print(fruits[:2])#output is ["apple", " chikoo"]
#print(fruits[-1])#output is no. of elements=8 -1 =7 and 7 index is of cherry, so output is cherry
#print(fruits[-2:])#output is ["grapes","cherry"]
#print(fruits[-8:3])#output is ["apple", " chikoo", "banana"]

#for item in fruits:
    #print(item)
    #output is
    #apple
    #chikoo
    #banana
    #mango
    #starawberry
    #peach
    #grapes
    #cherry
    #print("mango" in fruits)# true

search=input("please enter the items you wish to buy")
if search in fruits:
    print("{} is available in stock".format(search))
else:
    print("{} is notavailable in stock".format(search))

fruits.remove("mango")
print(fruits)

alp=["a","b","c","d"]
alpB=alp
alpB.remove("d")
print(alpB)
print(alp)
alpB.insert(3,"d")
print(alp)
alpC=alpB.copy()
alpC.remove("a")
print(alpC)
print(alpB)

listNum1=[1,2,3,4]
listNum2=[5,6,7,8]
listNum3=listNum1+listNum2
print(listNum3)

names=["abbey","crabby","shaggy"]

def printList(list):
    for item in list:
        print(item)

printList(names)

names.insert(1,"baggy")
print(names)

#+InInsertCopyRemovePop=SlicingReverseCountAppend