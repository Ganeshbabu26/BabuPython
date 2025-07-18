def bs(arr, target, low, high):
    mid = (low+high)//2
    if low > high:
        if high < 0:
            return -1, arr[0],0
        elif low > len(arr) -1:
            return -1, len(arr)-1, -1
        elif abs(arr[high]-target) > abs(arr[low]-target):
            return -1,arr[low],low
        else:
            return -1, arr[high],high
    elif arr[mid] > target:
        return bs(arr,target,low,mid-1)
    elif arr[mid] < target:
        return bs(arr,target,mid+1,high)
    else:
        return mid, arr[mid], mid
arr = list(map(lambda x: x*x,range(101)))
n = int(input("Enter a number to find: "))
index, value, pos = bs(arr,n,0,len(arr)-1)

if index != -1:
    print(f"{n} is located at index: {index}")
else:
    print(f"{n} is not found in given list")
    print(f"Closest number near {n} is {value} at index {pos}")