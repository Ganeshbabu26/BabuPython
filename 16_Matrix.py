a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Matrix a: ")
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()

print("Transpose of matrix a: ")
for i in range(3):
    for j in range(3):
        print(a[j][i],end=" ")
    print()
