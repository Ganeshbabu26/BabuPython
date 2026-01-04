def productnextnum(nums):
    n = len(nums)
    res = [0]*n
    for i in range(n):
            res[i] = nums[i] * nums[(i+1)%n]
    return res

a = [1,2,3,4]
print(productnextnum(a))

b = [4,6,0,2]
print(productnextnum(b))

'''

nums = [1,2,3,4]

n = 4
res = [1,1,1,1]

num = 1
for i in 4:

res[0] = nums[0]*nums[num] = 1*2 = 2
num = 2

res[1] = nums[1]*nums[num] = 2*3 = 6
num = 3

res[2] = nums[2]*nums[num] = 3*4 = 12
num = 4

res[3] = nums[3]*nums[0] = 4*1 = 4



...

'''