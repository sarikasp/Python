#Dynamically typed
age=2
name="shraddha"
isGirl=True
height=2.5
print(age)
print(type(age))
print(name)
print(type(name))
print(isGirl)
print(type(isGirl))
print(height)
print(type(height))
#following rules not applicable in python
#int+int=int(not applicable)
#string+int=string(not applicable)
#int+string=string(not applicable)
#string+string=string(not applicable)

#print(age+name) gives error as int+str is not supported
print(name+str(age))
print(age+int(height))
#print(age+int(name)) cant be executed as character cant be converted to interger

