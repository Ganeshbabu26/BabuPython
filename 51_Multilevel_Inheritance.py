class GrandFather:
    def ownHouse(self):
        print("Grandpa House")

class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike")

class Son(Father):
    def ownBook(self):
        print("Son have a book")

o = Son()
o.ownHouse()
o.ownBike()
o.ownBook()