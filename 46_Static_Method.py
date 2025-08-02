class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name: ",self.name,"   Age:  ",self.age)
    
    @staticmethod
    def welcome():
        print("Welcome to our Institutuion")

s1 = student("Babu",21)
s1.printDetail()
s1.welcome()