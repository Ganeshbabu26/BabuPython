class Father:
    Fname = "Madhavan"

class Mother:
    Sname = "Punitha"

class Son(Father, Mother):
    son = "Babu"
    def __init__(self):
        print(self.Fname)
        print(self.Sname)
        print(self.son)

o = Son()