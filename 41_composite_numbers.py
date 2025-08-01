def isComposite(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return True
    return False

count = 0
s = int(input("Enter start: "))
l = int(input("Enter end: "))
for i in range(s,l+1):
    if isComposite(i):
        print(i)
        count +=1

print("There are",count,"composite numbers between",s,"and",l)