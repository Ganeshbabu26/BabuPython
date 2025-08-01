my_list = [1,2,3,4,5]
my_list.append(6)
my_list.insert(2,2.5)
my_list.extend([7,8,9,10])
print(my_list)

a = [1,[2,3],[4,5,6],7,8,9,[10,[11,12,13],14],15]
print(a)

a[1].append(3.5)
a[2].append(6.3)
print(a)

a[6][1].append(13.345)
print(a)

a = sum(a[1]+a[2]+a[6][1])
print(a)

print(sum([i for i in range(1,101)]))