a = [[i+j*3+1 for i in range(3)] for j in range(3)]
b = [[i+j*3+1 for i in range(3)] for j in range(3)]

result = [[0 for i in range(len(a[0]))] for j in range(len(b))]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]

for i in result:
    for j in i:
        print(f"{j:3}",end="   ")
    print()


# Explanation:

#     j goes from 0 to 2 (for each row),
#     i goes from 0 to 2 (for each element in the row),
#     Formula: i + j*3 + 1 generates:

#         Row 0: 0+0+1, 1+0+1, 2+0+1 → [1, 2, 3]

#         Row 1: 0+3+1, 1+3+1, 2+3+1 → [4, 5, 6]

#         Row 2: 0+6+1, 1+6+1, 2+6+1 → [7, 8, 9]