class A:
    def display(self):
        print("I am display of class A")

class B(A):
    def display(self):
        print("I am display of class B")

class C(A):
    def display(self):
        print("I am display of class C")

class D(B,C):
    def display(self):
        print("I am display of class D")

o = D()
o.display()