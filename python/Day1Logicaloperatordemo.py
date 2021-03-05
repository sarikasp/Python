#logical operators
#and, or, not
#output is boolean
#true and true=true
#true and false=false
#false and true=false
#false and false=false
#true or true=true
#true or false=true
#false or true=true
#false or false=false
#not true=false
#not false=true
#print(2>4 and 7<7) #output is false
#print(7>90 or 5<60) #output is true


age=int(input("enter your age"))# here the string in input is converted to integer
swimming= input("do you know swimming?") #input function is always a string
yoga= input("do you know yoga?")

if age>30 and age<=50 and swimming=="yes":
    print("go to goa")
elif age>50 and yoga=="yes":
    print("be at home")
else:
    print("incorrect")

