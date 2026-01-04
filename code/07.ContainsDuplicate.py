# What if we want ALL duplicates?

# 👉 Modify logic to collect results

def duplicates(nums):
    Myset = set()
    List = []
    for num in nums:
        if num in Myset:
            List.append(num)
        Myset.add(num)
    return List if len(List) > 0 else None

a = [3,1,4,2,1,3]
print(duplicates(a))
a = [1,2,3]
print(duplicates(a))