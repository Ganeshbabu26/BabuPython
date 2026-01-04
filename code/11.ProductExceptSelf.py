def productExceptSelf(nums):
    n = len(nums)
    res = [1]*n

    left = 1

    ''' nums = [1,2,3,4]

        res = [1,1,1,1]
        res[0] = 1
        left = 1*nums[0] = 1*1 = 1

        res = [1,1,1,1]
        res[1] = 1
        left = 1*nums[1] = 1*2 = 2

        res = [1,1,1,1]
        res[2] = 2
        left = 2*nums[2] = 2*3 = 6

        res = [1,1,2,1]
        res[3] = 6
        left = 6*nums[3] = 6*4 = 24

        res = [1,1,2,6]

        right = 1

        res[3] = res[3]*right = 6*1 = 6
        right = 1*nums[3] = 1*4 = 4

        res = [1,1,2,6]
        res[2] = res[2]*right = 2*4 = 8
        right = 4*nums[2] = 4*3 = 12

        res = [1,1,8,6]
        res[1] = res[1]*right = 1*12
        right = 12*nums[1] = 12*2 = 24

        res = [1,12,8,6]
        res[0] = res[0]*right = 1*24
        right = 24*right = 24*24

    '''

    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1

    for i in range(n-1,-1,-1):
        res[i] *= right
        right *= nums[i]

    return res

a = [1,2,3,4]      #[24,12,8,4]
print(productExceptSelf(a))

b = [0,8,9,1]       #[72,0,0,0]
print(productExceptSelf(b))

