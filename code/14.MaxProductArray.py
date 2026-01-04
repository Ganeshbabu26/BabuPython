def maxProduct(nums):
    maxProd = nums[0]
    currMax = nums[0]
    currMin = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            currMax, currMin = currMin, currMax

        currMax = max(nums[i], currMax * nums[i])
        currMin = min(nums[i], currMin * nums[i])

        maxProd = max(maxProd, currMax)

    return maxProd

a = [1, -3, -5, 5, -1, 0, 4, 2, -3]
print(maxProduct(a))