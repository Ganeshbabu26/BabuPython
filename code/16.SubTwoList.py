def smaller(a,b):
    if len(a) != len(b):
        return len(a) < len(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return a[i] < b[i]
    return False

def Sub(l1,l2):
    negative = smaller(l1,l2)
    if negative:
        l1,l2 = l2,l1

    result = []
    i = len(l1) -1
    j = len(l2) -1
    borrow = 0

    while i > -1 :
        x = l1[i]-borrow
        y = l2[j] if j > -1 else 0

        if x < y:
            x = x + 10
            borrow = 1
        else:
            borrow = 0

        result.append(x-y)

        i -= 1
        j -= 1
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    result = result[::-1] 
    return result if not negative else ['-']+result

l1= [1,0,0]
l2 = [1,2,9]

print(Sub(l1,l2))

