#Regular Expression
import re

#program1

print("My first name is Shraddha \n my last name is Potnis")
# My first name is Shraddha
#  my last name is Potnis
print(r"My first name is Shraddha \n my last name is Potnis")
#My first name is Shraddha \n my last name is Potnis


#program2:Program to find the first occurence start m FOLLOWED BY TWO ALPHANUMERIC CHARACTERS...using \w and search
#r'm\w\w
#w==========================> a-z,A-Z,0-9
import re
# code = re.compile(r"m\w\w")
# str = "man men mew dew few"
# result = code.search(str)
# print(result)

str = "man men mew dew few"
result =  re.search(r"m\w\w",str)
print(result.group()) #man

#program3:Program to find the all the  occurences that  start with m and contains two non alphanumeric characters using \W

import re
str1 = "m@@ m## m$$ men man tat tutu"
z = re.findall(r"m\W\W",str1)
print(z)#['m@@', 'm##', 'm$$']
print(type(z))#<class 'list'>
for item in z:
    print(item)
# m@@
# m##
# m$$


#Program4:Program to find the all the  occurences that  start with m and contains two  alphanumeric characters using \w
import re
str2 = "m## cat make m##came  come"
p = re.findall(r'm\w\w', str)
print(p) #['man', 'men', 'mew']
print(type(p))#<class 'list'>
for item in p:
    print(item)
# man
# men
# mew

#program5:Program to split on non alphanumeric character.....using split and W
import re
str3 = "This: @i$s:al pha:    'Core"
result2 = re.split(r'\W+',str3)
print(result2) #['This', 'i', 's', 'al', 'pha', 'Core']

#program6: to substitute one string by other.......using sub
import re
str4 = "The capital of India is Mumbai"
result3 = re.sub(r"Mumbai","Delhi",str4)
print(result3) #The capital of India is Delhi

#program7:
import re
string6 = "Amit from India"#.....Provided the string starts with A\w\w\w

# listNew = ["Amit from India","Anna from U.K","Peter from Canada"].......cant give listNew as an arguement
result4 = re.match(r"A\w\w\w",string6)
print(result4.group())#Amit

    # str = "Ayush Jain Indore 997701900121"
    # str2 = "Ayush2 Jain Indore 997701900121"
    # str3 = "Ayush3 Jain Indore 997701900121"
    # str4 = "Ayush4 Jain Indore 997701900121"
    # str5 = "Ayush5 Jain Indore 997701900121"
    #
    # res = re.match(r'A\w\w\w\w', str)
    # print(res.group())




    # # /Z   /b  /d  /D
    #






# # module packages in python
