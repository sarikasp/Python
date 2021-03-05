#Dictionaries

person={"firstName":"shraddha",
        "lastName":"potnis",
        "age":"29",
        "pin":"1234"
}#key and value...key:value

print(person["firstName"])
print(person["lastName"])
print(person["age"])
print(person["pin"])

print("*"*80)
#could also be printed as:

for key in person:
    print("{}:{}".format(key,person[key]))

print("*"*80)

for item in person.values():
    print(item)

print("*"*80)

for keys,values in person.items():
    print("{}:{}".format(keys, values))


