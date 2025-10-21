print("\n------------------------------------------1. First Method------------------------------------------\n")
def fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b

n = int(input("Enter a number: "))
fibo(n)

print("\n------------------------------------------2. Second Method------------------------------------------\n")

t1 = 0
t2 = 1

count = 1

for i in range(n):
    t = t1 + t2
    print("Fibo(",count,") = ",t1)
    t1 = t2
    t2 = t
    count+=1

print("\n------------------------------------------3. Third Method------------------------------------------\n")

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(n):
    print(fibo(i),end=" ")