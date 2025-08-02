class student:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.count += 1
    def printDetails(self):
        print("Name: ",self.name,"   Age:  ",self.age)

    @classmethod
    def total(cls):
        return cls.count

o = student("Babu",21)
o.printDetails()

a = student("Ganesh",20)
a.printDetails()

print("Total Admission: ", a.total())