class Father():

    education = "BE"

    def __init__(self, name= None , lastname = None):
        self.name = name
        self.lastname = lastname
        self.age = 34


    def display(self):
        print(self.education)

    def displayN(self):
        print("My name is {} and lastName {} ".format(self.name,self.lastname))

class  Child(Father):
    def __init__(self,name,lastname ,age,childName):
            super().__init__(name ,lastname)
            self.name = childName
            self.age = age
            self.education = "BSC"

    def display(self):
            print("My name is {} and lastName {} and age is {} ".format(self.name, self.lastname ,self.age))

    def displayP(self):
        super().display()


# sanjay = Father("sanjay","kumar")
# sanjay.display()

sanjayjr = Child("sanjay","dutt",23 ,"sanjayjr")
sanjayjr.display()#My name is sanjayjr and lastName dutt and age is 23
sanjayjr.displayP()#BSC


