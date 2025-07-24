class user:
    def __init__(self,name):
        print("Call when new Instance created")
        self.name = name

    def printall(self):
        print("Name: ",self.name)

o = user("Babu Python")

o.printall()
print(o.__dict__)