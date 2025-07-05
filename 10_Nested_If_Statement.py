a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>=b and a>=c:
    if a==b and a>c:
        print("a and b are greatest")
    elif a==c and a>b:
        print("a and c are greatest")
    elif a == b == c:
        print("All are equal")
    else:
        print("a is greatest")
elif b>=a and b>=c:
    if b==c and b>a:
        print("b and c are greatest")
    else:
        print("b is greatest")
else:
    print("c is greatest")