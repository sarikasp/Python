#Program One  # Multi- level
# class Grandfather(object):
#     def __init__(self,lastName ,name):
#         self.gname = name;
#         self.lastName = lastName
#     def displayGP(self):
#         print(self.gname,self.lastName)
#
# class Father(Grandfather):
#     def __init__(self,lastName ,name, gpname):
#         super().__init__(lastName,gpname)
#         self.fname = name
#     def displayFN(self):
#         print(self.fname , self.lastName)
#         super().displayGP()
# class Son(Father):
#     def __init__(self,name ,lastName ,fname, gpname):
#         super().__init__(lastName,fname ,gpname)
#         self.name = name
#     def displaySN(self):
#         print(self.name, self.lastName)
#     def displayFN(self):
#         super().displayFN()
# raju = Son("Raju", "Deshpande" ,"Ram" ,"Sai Ram")
# raju.displaySN()
# raju.displayFN()
#
#
# class Father(object):
#     def __init__(self,lastName):
#         self.lastName = lastName
#     def displayName(self):
#         print(self.lastName)
# class Son(Father):
#     def __init__(self,name):
#         super().__init__('deshpande')
#         self.name = name
#     def fName(self):
#         print(self.name)
#         print(self.lastName)
# class Daughter(Father):
#     def __init__(self, name,lastName):
#         super().__init__(lastName)
#         self.middlename = name
#     def fName(self):
#         print(self.name)
#         print(self.lastName)
# class GrandChild(Daughter):
#     def __init__(self,name, lastname, middlename):
#        super().__init__(middlename ,lastname)
#        self.name = name
#     def dispPlay(self):
#         print(self.name,self.middlename, self.lastName)
#
# arna = GrandChild('arna' ,'kanhe','gauri')
# arna.dispPlay()
#
# # Multiple inheritance
# class A():
#     def __init__(self,name):
#         print('Father constructor called ')
#         self.fname = name
# class B():
#     def __init__(self,mname):
#         print('mother constructor called ')
#         self.mname = mname
# class Son(A,B):
#     def __init__(self,name,mname):
#         super().__init__(mname)
#         self.name = name
#     def display(self):
#         print('The name of mother is {} and child {}'.format(self.fname ,self.name))
# chinmay = Son("chinmay" ,"shirish")
# chinmay.display()
#
#
#
# # chinmay = Son("Chinmay")
# # chinmay.fName()
# #
# # gauri = Daughter("Gauri","Deshpande")
# #
# # print(gauri.name)
# # gauri.fName()
#
#
#


# class Father(object):
#     def __init__(self,lastName,name):
#         self.lastname = lastName
#         self.gname = name
#         self.sai = "sairam"
#
#     def displayName(self):
#         print("{}:{}".format(self.gname, self.lastname))
#
# class SonOne(Father):
#     def __init__(self, lastName, fname, name):
#         super().__init__(lastName, fname)
#         self.name = name
#         self.sai = "sairam2"
#
#     def displayName(self):
#         print("{}:{}".format(self.name ,self.lastname))
#         super().displayName()
#
#
# class SonTwo(Father):
#     def __init__(self,lastName,fname,name):
#         super().__init__(lastName,fname)
#         self.name = name
#
#     def displayName(self):
#         print("{}:{}".format(self.name ,self.lastname))
#         super().displayName()
#
#
# ramesh = SonTwo("Deshpande","Balasaheh","Ramesh")
# suresh = SonOne("Deshpande","Balasaheh","Suresh")
#
#
# ramesh.displayName()
# suresh.displayName()
#
#
# # Multiple
#
#
# class Mother(object):
#
#     def __init__(self ,mName ,lastName):
#         self.mname = mName
#         self.lastName = lastName
#         #print(mName,lastName)
#
#     def displayName(self):
#         print("Mother method called")
#         print(self.mname,self.lastName)
#
#
# class Father(object):
#
#     def __init__(self, fName, lastName):
#         self.fname = fName
#         self.lastName = lastName
#         #print(mName, lastName)
#
#     def displayName(self):
#         print("Father method called")
#         print(self.fname, self.lastName)
#
#
# class Child(Mother,Father):
#     def __init__(self, pname, lastName ,name):
#         super().__init__(pname,lastName)
#         self.name = name
#
#     def displayName(self):
#         print(self.name, self.lastName)
#         super().displayName()
#
# childOne = Child("Sarika" ,"Deshpande","Chinmay")
# childOne.displayName()
#






