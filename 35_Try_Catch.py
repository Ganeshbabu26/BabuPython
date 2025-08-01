
try:
    a = 10/0
    print(a)
except Exception as e:
    print(e)


a = 12
b = "babu"
try:
    print(b+a) 
except Exception as e:
    print(e)
finally:
    print(b*a)


try:
    a = [2,4,5,6,7]
    print(a[2])
    print(a[100])

    for i in range(10):
        print(i)
except Exception as e:
    print(e)


