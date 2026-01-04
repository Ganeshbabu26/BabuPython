
def Add(l1,l2):
    result = []
    carry = 0
    i = len(l1) -1
    j = len(l2) - 1

    while i > -1 or j > -1 or carry:
        x = l1[i] if i > -1 else 0
        y = l2[j] if j > -1 else 0

        z = x + y + carry

        result.append(z%10)
        carry = z//10

        i -= 1
        j -= 1

    return result[::-1]

a = [1,2,3]
b = [8,7,7]
print(Add(a,b))