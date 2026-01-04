def longestSubArray(arr,k):
    seen = {}
    prefix = 0
    maxlen = 0

    for i in range(len(arr)):
        prefix += arr[i]

        if prefix == k:
            maxlen = i+1

        if prefix - k in seen:
            length = i - seen[prefix - k]
            maxlen = max(maxlen,length)

        if prefix not in seen:
            seen[prefix] = i

    return maxlen

arr = [10, 5, 2, 7, 1, 9]
k = 15

print(longestSubArray)
print(longestSubArray(arr,k))




