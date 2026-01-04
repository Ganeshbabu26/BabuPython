def maxArea(height):
    left = 0
    right = len(height) - 1
    maxWater = 0

    while left < right:
        width = right - left
        water = min(height[left], height[right]) * width
        maxWater = max(maxWater, water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxWater

height = [1,8,6,2,5,4,11,22,7]
print(maxArea(height))



'''


with [1,8,6,2,5,4,11,22]
i imagine that water container program, 

iteration 1
if we have hight 1 on one end and another end has hight 22, distance (which is width = 7)

why we calculating min(height[left],height[right]) means, no matter the other end how hight is, if the other end is small, water must have filled with top level of small height, because it has no space to storage, if we try, it leaks, and top level is always the same height of (small height of the end)





'''