a = {}
b = {1:4,2:6,3:8,9:7}
c = {1,2,3,4,5}

print(type(a))
print(type(b))
print(type(c))

for i in b:
    print(i," : ",b[i])

s = set()
while True:
    a = input("Enter anything: ")
    if a=="":
        break
    s.add(a)
print(s)

s = {}
while True:
    a = input("Enter a key (leave blank to stop: )")
    if a=="":
        break
    b = input("Enter value: ")
    s[a] = b
print(s)