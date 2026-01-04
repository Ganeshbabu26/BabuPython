def maxSubArray(array):
    currSum = array[0]
    MaxSum = array[0]

    for i in range(1, len(array)):

        currSum = max(array[i], currSum+ array[i])
        MaxSum = max(MaxSum, currSum)

    return MaxSum

a = [1,-3,-5,5,-1,0,4,-3]
print(maxSubArray(a))


def MaxSubArray(Array):
    currSum = Array[0]
    maxSum = Array[0]

    temp = 0
    start = 0
    end =  0

    for i in range(1, len(Array)-1):
        if Array[i] > currSum + Array[i] :
            currSum = Array[i]
            temp = i

        else:
            currSum += Array[i]

        if currSum > maxSum:                     
            maxSum = currSum
            start = temp
            end = i

    return start, end, maxSum
    
a = [1,-3,-5,5,-1,0,4,-3]
print("Length: ",len(a))
start, end, maxsum = MaxSubArray(a)
print(start, end, maxsum)


           