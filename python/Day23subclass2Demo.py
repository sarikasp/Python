from Day23class2Demo import Car
class Audi(Car):

    def steering(self):
        print('steering from Audi')

    def company(self):
        print('company name Audi')


y = Audi(1000)
y.fuelTank()#Fill the fuel into the tank /t For the car with rb 1000
y.company()#company name Audi
y.steering()#steering from Audi
