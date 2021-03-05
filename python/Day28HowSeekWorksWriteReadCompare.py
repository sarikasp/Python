# #Program1
# #To see how seek() works
# with open('file3.txt','w+b') as f: #w+b enables write and read the binary using encode and decode respectively
#     strA = "Denmark is beautiful"#this is a binary file
#     strA = strA.encode()
#     f.write(strA)
#     print(f.tell())#20 ...returns the length of the string
#     f.seek(0,0)# the cursor is on the 0th byte of line 0
#     print(f.tell())#0 ...as now the cursor is to the extreme left of the top
#     f.seek(3,0)# the cursor is on the 3rd byte of line 0
#     print(f.tell())#3...first 3 bytes
#     print(f.read().decode())#mark is beautiful
#     f.seek(0,0)#0
#     print(f.read().decode())#Denmark is beautiful
#     f.seek(-3,2) #   2 -------> move to end of the string and can use  negative indexing
#     print(f.read().decode())#ful
#

print("*"*80)

#Program2
#To add/write a  few city records to a binary file and using seek to find the desired city
#the trick is to assign same size bytes to an individual city
#for e.g. Mumbai(20bytes)       Pune(20bytes)          Copenhagen(20bytes)
# f.seek(0,0) cursor is in the begininning
# f.seek(20) cursor is at the end of mumbai ...if i print read..i ll get pune
# f.seek(20) cursor is at the end of pune...if i read i ll get copenhagen
# f.seek(20) cursor is at the end of copenhagen...i will need to use seek(0,0) to read further

lenC = 20 #length of characters

with open('city.bin','wb')as f:
    n = int(input("Please enter the number of cities: "))#Please enter the number of cities: 3

    for item in range(n):
        city = input("Please enter the city: ")
        #Please enter the city: Mumbai
        #Please enter the city: Pune
        #Please enter the city: Copenhagen
        city = city + (lenC - len(city)) * " " #adding length to the city...e.g. pune + (20-4) * " "
        city = city.encode()
        f.write(city)#this is written in the file city.bin: Mumbai              Pune                Copenhagen


print("*"*80)

# #Program 3
# #To read from the above binary file city.bin
# recordLength = 20
#
# with open('city.bin','rb')as f:
#     n = int(input('Enter the record to the end '))#seek should be 2
#     f.seek(recordLength * (n-1))
#     #strB= f.read().decode()
#     strC = f.read(20).decode()
# #print(strB)
# print(strC)
#Enter the record to the end 1 ...if f.read().decode() and i print strB
#Mumbai              Pune                Copenhagen

#Enter the record to the end 1 ...if f.read(20).decode() and i print strC
#Mumbai

#Enter the record to the end 2 ...if f.read().decode() and i print strB
#Pune                Copenhagen

#Enter the record to the end 2 ...if f.read(20).decode() and i print strC
#Pune


#Enter the record to the end 3...if f.read().decode() and i print strB
#Copenhagen

#Enter the record to the end 3...if f.read(20).decode() and i print strC
#Copenhagen


print("*"*80)

#Program 4
# import os
#
# reclen = 20
# size = os.path.getsize('city.bin')#gets the total length of the bytes in the binary file
# n = int(size/reclen) # gives me the number of records
# position = 0
# found = False#flag
# print('The total number of records {}'.format(n))
#
# with open('city.bin','rb') as f:
#     city = input('Please Enter the city')
#     city = city.encode()
#     found = False
#
#
#     for i in range(n):
#         f.seek(position)
#         str = f.read(20)
#         if city in str:
#             print('city found')
#             found = True
#
#         position += reclen #to go to the next record
#
#     if not found:
#         print('City not found')

#The total number of records 3
# Please Enter the cityCopenhagen
# city found

#to see how seek works,write ,read,compare