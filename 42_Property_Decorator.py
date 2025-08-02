class user:
    def __init__(self,Name,Age):
        self.Name= Name
        self.Age = Age
        self.msg = self.Name + " is " + str(self.Age) +" years old "
    @property
    def Msg(self):
        return self.Name + " is " + str(self.Age) +" years old "


o = user("Babu",21)
print(o.Name)
print(o.Age)
print(o.msg)
o.Age = 20
print(o.msg)
print()

o = user("Babu",21)
print(o.Name)
print(o.Age)
print(o.Msg)
o.Age = 20
print(o.Msg)
print(type(o.Msg))