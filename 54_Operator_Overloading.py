class Addition:
    def __init__(self,a):
        self.a = a
    def __add__(o1,o2):
        return o1.a + o2.a

    def __sub__(o1,o2):
        return o1.a - o2.a
    
o1 = Addition(10)
o2 = Addition(20)
print(o1+o2)
print(o1-o2)


def add(*n):
    Sum = 0
    for i in n:
        Sum += i
    return Sum

print(add(4,5,6,7,8))