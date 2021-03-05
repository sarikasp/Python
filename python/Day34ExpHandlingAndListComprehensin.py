#1: Exception Handling
class BankingException(Exception):
    def __init__(self,arg):
        self.msg = arg

class DiscountException(Exception):
    def __init__(self,arg):
        self.msg = arg

def check(dict):
    for key, val in dict.items():
        if val < 2000:
            raise BankingException("Please update your balance and it shouldn't be below 2000")
        print("name = {}, balance = {}".format(key,val))

def disc(discount):
    if discount == 10:
        print("10 percent discount given...")
    else:
        raise DiscountException("No more discount")

BankAccount = {"Hiren":5000,"Shraddha":2000,"Raj":2000}

try:
    check(BankAccount)
    disc(11)
    #withdraw()
    #confirmation()
except BankingException as x:
    print(x)
except DiscountException as y:
    print(y)

# name = Radha, balance = 5000
# name = Shraddha, balance = 2000
# Please update your balance and it shouldn't be below 2000..if BankAccount = {"Radha":5000,"Shraddha":2000,"Raj":1000}

# name = Radha, balance = 5000
# name = Shraddha, balance = 2000
# name = Raj, balance = 2000
# No more discount...if BankAccount = {"Radha":5000,"Shraddha":2000,"Raj":2000}




print("*"*80)

#List Comprehension
#Program 1:List Comprehension
list = [1,2,3,4,5,6]

for item in list:
    print(item * 2)
# 2
# 4
# 6
# 8
# 10
# 12

a = [item * 2 for item in list]
# 2
# 4
# 6
# 8
# 10
# 12

#Program2:List Comprehension
listB = [33,44,45,67,80,9]
b = [item > 40 for item in listB]
print(b)
# [False, True, True, True, True, False]


