def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
n = int(input("Enter a number: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    print(f"First {n} fibonacci number(s):")
    for i in range(n):
        print(fibo(i))
