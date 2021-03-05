# #/Z   /b  /d  /D

#* o more than *

#/b added for space

# /w [A-Z] [a-z] [0-9]
import re
#Program1: to sprint the workds that start with an a
str = "an apple a day keeps doctor away"
result1=re.findall(r"\ba[\w]*\b",str)
for item in result1:
    print(item)
# an
# apple
# a
# away
# result2=re.findall(r"a[\w]*",str)
#
# for item in result2:
#     print(item)
# an
# apple
# a
# ay
# away

# result3=re.findall(r"a[\w]*\b",str)
# for item in result3:
#     print(item)
# an
# apple
# a
# ay
# away


print("*"*80)
#Program2:
#str = "an apple a day keeps doctor away"
result4 = re.findall(r'\ba[\w]*\b',str)
for item in result4:
    print(item)
# an
# apple
# a
# away

#program 3: i need to print number 1st and 21st
str2 = 'The meeting will be conducted on 1st and 21st of every month'
result5 = re.findall(r"\d[w]*",str2)
for item in result5:
    print(item)

# 1
# 2
# 1

result6 = re.findall(r"\d\d[w]*",str2)
for item in result6:
    print(item)
#21
print("*"*80)
result7 = re.findall(r"\d+[w]*",str2)
for item in result7:
    print(item)

# 1
# 21
print("*"*80)

#program 4:
str3 = "one two three four five six seven  asdsadasd 8 9 10"
result8 = re.findall(r"\b\w{5}\b",str3)
for item in result8:
    print(item)
# three
# seven

print("*"*80)
#str3 = "one two three four five six seven  asdsadasd 8 9 10"
result9 = re.findall(r'\b\w{5,}\b',str3)
for item in result9:
    print(item)
# three
# seven
# asdsadasd

print("*"*80)
#str3 = "one two three four five six seven  asdsadasd 8 9 10"
result10 = re.findall(r'\b\w{4}\b',str3)
for item in result10:
    print(item)
# four
# five


print("*"*80)
#str3 = "one two three four five six seven  asdsadasd 8 9 10"
result11 = re.findall(r'\b\w{4,}\b',str3)
for item in result11:
    print(item)
# three
# four
# five
# seven
# asdsadasd

print("*"*80)
#str3 = "one two three four five six seven  asdsadasd 8 9 10"
result12 = re.findall(r'[\d]*',str3)
for item in result12:
    print(item)

#
#
#
# 8
#
# 9
#
# 10


print("*"*80)
#program5:

str4 = "one two three four five six seven three"
result13 = re.findall(r't[\w]*\Z',str4)
for item in result13:
    print(item)
#three

print("*"*80)
# str4 = "one two three four five six seven three"
result14 = re.search(r't[\w]*\Z',str4)
print(result14)
print(result14.group())

#\b['']\b

print("*"*80)
#program 6:
str5 = 'ChinmayDeshpande 770919244ee'

result15 = re.search(r'\d[\d]*',str5)
print(result15.group())

#770919244

print("*"*80)

#program 7:
str6 = 'Chinmay Deshpande 7709192441'
result16 = re.search(r'\d+',str6)
print(result16.group())

#7709192441

print("*"*80)
#program 8:
str7 = 'Chinmay Deshpande: 7709192441'
result17 = re.search(r'\D+',str)
print(result17.group())
#an apple a day keeps doctor away