#list

flowers = ["rose","lilly","jasmine","tulip","lotus","marygold"]
print(flowers[:])
print(flowers[:6])
flowers[1] = "orchid"
print(flowers)#orchid replaces lilly

x=0
for flower in flowers:
    print(flower)
    print(" The flower at index {} is {}".format(x,flower))
    x +=1


print("*"*80)

if "rose" in flowers:
    print("rose is available")

print("*"*80)

#search engine
a = input("Please enter the flower you wish to buy: ").casefold()#casefolds the captital to lower
if a in flowers:
    print("{} is available in the list".format(a))
else:
    print("{} is not available in the list ".format(a))

print("*"*80)

listA = [["a","b","c"],["A","B",["1","2","3"]],["c","d","e"]]
print(listA[1][2][2])#print 3

print("*"*80)

#TO PRINT INDIVIDUAL ITEMS OF THE ABOVE LIST
for item1 in listA:
    for item2 in item1:
        print(item2)
