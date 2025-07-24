class Student:
    name = "Ganeshbabu"
    age = 20

    def printall():
        print("Name   : ",Student.name)
        print("Age    : ",Student.age)
    
    def printAll(self,gender):
        print("Name     : ",Student.name)
        print("Age      : ",Student.age)
        print("Gender   :  ",gender)
    

Student.printall()
print(Student.__dict__)

print(getattr(Student,"printall"))
getattr(Student,"printall")()
print(Student.__dict__['printall'])

o = Student()
o.printAll("Male")