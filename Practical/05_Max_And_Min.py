def MinAndMax(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[0], arr[-1]

arr = []
while True:
    n = input("Enter a number (click without numbers to stop):  ")
    if n=="":
        break
    arr.append(int(n))

min, max = MinAndMax(arr)

print("Min = ", min)
print("Max = ", max)