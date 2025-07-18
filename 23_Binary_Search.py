def bs(arr,target,low,high):
    mid = (low+high)//2
    if low>high:
        return -1
    elif arr[mid]<target:
        return bs(arr,target,mid+1,high)
    elif arr[mid]>target:
        return bs(arr,target,low,mid-1)
    else:
        return mid
    
arr = list(map(lambda x: x*x,range(101)))
n = int(input("Enter a number: "))
index= bs(arr,n,0,len(arr)-1)

if index!=-1:
    print(n," is located at the index", index)
else:
    print(f"{n} is not found")
