n = int(input("Enter a number: "))
Sum = 0
Product = 1
while(n!=0):
    Sum = Sum + (n%10)
    Product = Product * (n%10)
    n = n//10
print("Sum of digits: ",Sum)
print("Product of digits: ",Product)
