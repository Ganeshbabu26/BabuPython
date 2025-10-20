def sumandproducts(num):
    Sum = 0
    Product = 1

    while(num !=0):
        rem = num % 10
        Sum = Sum + rem
        Product = Product * rem
        num = num // 10
    
    return Sum, Product

n = int(input("Enter number: "))

S, P = sumandproducts(n)
print("Sum     : ",S)
print("Product  : ",P)