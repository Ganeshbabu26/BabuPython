def GCD(a,b):
    while b!=0:
        a,b = b, a%b
    return a

print(GCD(12,18))