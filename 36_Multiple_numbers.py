def sort(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
    return s

def total(s):
    total = 0
    for i in s:
        total = total + i
    return total

def product(s):
    product = 1
    for i in s:
        product = product * i
    return product

def array():
    s = []
    while True:
        n = input("Enter number (leave black to stop): ")
        if n == "":
            break
        s.append(int(n))
    print("Original: ",s)
    print("Sorted: ",sort(s))
    print("Total: ",total(s))
    print("Product: ",product(s))

array()
