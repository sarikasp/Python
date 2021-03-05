#dict

# Shraddha = { "firstName":"shraddha", "age":29, "rollNumber":1, "maidenName":"Shraddha"}
# print(Shraddha["firstName"])
# print(Shraddha["age"])
# print(Shraddha["rollNumber"])
# print(Shraddha["maidenName"]

print("*"*80)

person = {"name":"shraddha", "rollNum":34}

for item in person:
    print(item)
    print(person[item])
    print(" {} : {}".format(item,person[item]))

print("*"*80)

for item in person.keys():
    print(item)

for item in person.values():
    print(item)

for key , values in person.items():
    print(" {} : {}".format(key , values))

print("*"*80)

questionsDict = {
    "capital Of MH" : "Mumbai",
    "capital Of MP" : "Bhopal",
    "capital of AP" : "Hyderabad"
}
#print(len(questionsDict))#3

i = 0
correctAnswers = 0

while i < len(questionsDict):
    for item in questionsDict:
        answer = input("Enter the {} :".format(item)).capitalize()#.upper(),.lower()
        i += 1
        if questionsDict[item] == answer:
            correctAnswers += 1

if correctAnswers ==3:
    print("Gold")
elif correctAnswers ==2:
    print("Silver")
elif correctAnswers ==1:
    print("Bronze")
else:
    print("Please try again")

print("*"*80)

newDict = {
    "name":"shraddha",
    "age":29,
    "skills": ["python","java","sql"],
    "address": {"city":"Honalulu", "pinCode":1234}
}

print(newDict["name"])
print(newDict["age"])
print(newDict["skills"][1])
print(newDict["address"]["pinCode"])

print("*"*80)

studentsDict = [
{
    "name":"shraddha",
    "age":29,
    "skills": ["python","java","sql"],
    "address": {"city":"Honalulu", "pinCode":1234}},
{
    "name":"Tintin",
    "age":13,
    "skills": ["python","java","sql"," datascience"],
    "address": {"city":"Mumbai", "pinCode":400000}},
{
    "name":"Brian",
    "age":20,
    "skills": ["Analyst","sql","excel"],
    "address": {"city":"Morocco", "pinCode":3000}}
]

#count number of shraddha

count = 0

for item in studentsDict:
    if item["name"] == "shraddha":
        count += 1
print(count)

#count the skills of excel

count1 = 0

for item in studentsDict:
    if "excel" in item["skills"]:
        count1 += 1

print(count1)

