print("---------------------------------------Method 1---------------------------------------")
class Product:
    def __init__(self, name, price=None):
        self.name = name
        self.price = price
    
    def Bill(self,qty=None):
        if qty is None:
            print("Product name: ", self.name)
            print("Total product: ", 1 )
            print(f"Price: ${self.price if self.price is not None else 0}")
        else:
            print("Product name: ", self.name)
            print("Total product: ",qty)
            print(f"Price: ${self.price*qty if self.price is not None else 0}")

o1 = Product("Diary Milk",299)
o1.Bill(8)
o1.Bill(5)
o1.Bill()


print("---------------------------------------Method 2---------------------------------------")
class Product:
    def __init__(self,a):
        self.a = a

    def bill(self,b=None):
        if b is None:
            print(self.a, "count: ", 1)
            print("total price = ", 299)
        else:
            print(self.a, "count: ", b)
            print("Total price = ",b*299)

o2 = Product("goodday")
o2.bill(10)
o2.bill()