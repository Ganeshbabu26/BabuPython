
# 1. Static method 
# a. method overloading

class addition:
    def add(a,b,c=0):
        return a+b+c
    
obj = addition
print(obj.add(4,5,6))
print(obj.add(4,5))


# b.operator overloading

class A:
    def __init__(self,x):
        self.x = x
    
    def __add__(self,other):
        return A(self.x + other.x )
    
obj1 = A(10)
obj2 = A(20)

result = obj1 + obj2

print(result.x)

# 2. Dynamic method (Run time polymorphism)
# a.Method overriding

class Animal:
    def show(self):
        print("Animal makes sound")

class Dog(Animal):
    def show(self):
        print("Dog barking")

class Cat(Animal):
    def show(self):
        print("Cat makes sound")

for i in [Animal(), Dog(), Cat()]:
    i.show()

# b.Duck typing

class dog:
    def show(self):
        print("new Dog makes sound")

class cat:
    def show(self):
        print("new Cat makes sound")

def abcd(obj):
    obj.show()

abcd(dog())
abcd(cat())