def sort(n):
    n = n.copy()  
    for i in range(len(n)):
        for j in range(0, len(n)-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

def mean(n):
    return sum(n) / len(n)

def median(n):
    n = sort(n)
    mid = len(n) // 2
    if len(n) % 2 == 0:
        return (n[mid - 1] + n[mid]) / 2
    else:
        return n[mid]
