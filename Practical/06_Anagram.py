print("---------------------------------------Method 1---------------------------------------")

def bsort(arr):
    if type(arr) == str:
        list = []
        for i in arr:
            list.append(i)
        arr = list
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def is_anagram(s1,s2):
    return bsort(s1) == bsort(s2)

m = input("Enter a word 1: ")
n = input("Enter a word 2: ")

if is_anagram(m,n):
    print("Strings are anagram")
else:
    print("Strings are not anagram")



print("---------------------------------------Method 2---------------------------------------")

def is_Anagram(s1,s2):
    return sorted(s1) == sorted(s2)

m = input("Enter a word 1: ")
n = input("Enter a word 2: ")

if is_Anagram(m,n):
    print("Strings are anagram")
else:
    print("Strings are not anagrams")