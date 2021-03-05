quiz={"capital of mh":"mumbai",
      "capital of mp":"bhopal",
      "capital of rj":"jaipur"
      }

print(quiz["capital of mh"])
print(quiz["capital of mp"])
print(quiz["capital of rj"])

for key in quiz:
    print("{}:{}".format(key,quiz[key]))

for item in quiz.values():
    print(item)

for keys,values in quiz.items():
    print("{}:{}".format(keys,values))