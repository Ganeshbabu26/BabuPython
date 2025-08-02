class A:
    def abcd(self):
        print("First")

o = A()
o.abcd()

class B(A):
    def abcd(self):
        print("second")
        super().abcd()

o = B()
o.abcd()
