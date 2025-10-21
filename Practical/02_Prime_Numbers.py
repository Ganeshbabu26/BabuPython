def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

nums = list(map(int,input("Enter all numbers (Seperated by space): ").split()))

prime = [i for i in nums if isPrime(i)]
print("Only prime in given list: ",prime)