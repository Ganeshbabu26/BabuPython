print("-----------------------------------Method 1-----------------------------------")
from MyPackage import A, B
A.greet()
B.greet()

print("-----------------------------------Method 2-----------------------------------")
import MyPackage as C
C.A.greet()
C.B.greet()