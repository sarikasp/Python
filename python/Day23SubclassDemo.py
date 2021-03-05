from Day23ClassDemo import WorldBank
class BOI(WorldBank):
    def save(self,y):
        print('Save account BOI',y)
    def loan(self,x):
        print('Loan account BOI',x)
class SBI(WorldBank):
    def save(self,y):
        print('Save account SBI',y)
    def loan(self,x):
        print('Loan account SBI',x)


x = SBI()
x.logo()#Logo
x.loan(4)#Loan account SBI 4
x.save(5)#Save account SBI 5


x = SBI()
x.loan(2)#Loan account SBI 2
x.save(3)#Save account SBI 3