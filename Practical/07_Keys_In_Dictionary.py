print("---------------------------------------Method 1---------------------------------------")
a = {1:'a', 2:'b', '3':'c', "Ganesh":"Babu" }

keys = input("Enter all keys: ").split()

for k in keys:
    if k.isdigit() and int(k) in a:
        print(f"key {k} is found with value {a[int(k)]}")
    elif k in a:
        print(f"Key {k} is found with value {a[k]}")
    else:
        print(f"Key {k} is not found")



print("---------------------------------------Method 2---------------------------------------")
a = {'a':1, 'b':2, 'c':3}

keys = input("Enter all keys: ").split(" ")

for k in keys:
    if k in a:
        print(f"key {k} is found with value {a[k]}")
    else:
        print("Not found")