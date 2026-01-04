# # # def find(decimal_str, repeating_length):
# # #     import math
# # #     # Assume decimal_str like "0.333" and repeating_length=3 for 0.333...
# # #     # Split into integer and decimal parts
# # #     if '.' in decimal_str:
# # #         integer_part, decimal_part = decimal_str.split('.')
# # #         integer = int(integer_part) if integer_part else 0
# # #         decimal = decimal_part
# # #     else:
# # #         integer = int(decimal_str)
# # #         decimal = ""
# # #         repeating_length = 0

# # #     if repeating_length == 0:
# # #         # Terminating decimal
# # #         den = 10 ** len(decimal)
# # #         num = integer * den + int(decimal)
# # #     else:
# # #         # Repeating decimal
# # #         non_repeating = len(decimal) - repeating_length
# # #         non_rep_str = decimal[:non_repeating]
# # #         rep_str = decimal[non_repeating:]
        
# # #         non_rep_num = int(non_rep_str) if non_rep_str else 0
# # #         rep_num = int(rep_str)
        
# # #         den_non_rep = 10 ** non_repeating
# # #         den_rep = 10 ** (non_repeating + repeating_length) - 10 ** non_repeating
        
# # #         num = integer * den_rep * den_non_rep + non_rep_num * den_rep + rep_num * den_non_rep
# # #         den = den_rep * den_non_rep

# # #     # Simplify
# # #     gcd = math.gcd(num, den)
# # #     num //= gcd
# # #     den //= gcd
# # #     return num, den

# # # # Example for 0.333...
# # # n, d = find("0.333", 3)
# # # print(n, "/", d)  # 1 / 3

# # # # For 1.333...
# # # n, d = find("1.333", 3)
# # # print(n, "/", d)  # 4 / 3

# # # # For terminating 1.333
# # # n, d = find("1.333", 0)
# # # print(n, "/", d)  # 1333 / 1000 -> 4 / 3 after simplify


# # def MaxSubArray(Array):
# #     currSum = Array[0]
# #     MaxSum = Array[0]

# #     start = 0
# #     end = 0
# #     temp = 0

# #     for i in range(1,len(Array)-1):
# #         # [5,-6,3,0,5,-1,3,-9]

# #         if Array[i] > currSum + Array[i]:
# #             currSum = Array[i]
# #             temp = i
        
# #         else:
# #             currSum += Array[i]

# #         if currSum > MaxSum:
# #             MaxSum = currSum
# #             start = temp
# #             end = i

# #     return start, end, MaxSum

# # a = [5,-6,3,0,5,-1,3,-9]
# # s,e,m = MaxSubArray(a)
# # print(s,e,m)


# def rev(s):
#     reverse = ""
#     for i in s:
#         reverse = i + reverse
#     return reverse

# print(rev("Babu"))

# # def filterPrime(Array):



# # def isPrime(n):
# #     if n<2:
# #         return False
# #     for i in range(2,int(n**0.5)+1):
# #         if n%i == 0:
# #             return False
# #     return True

# # def filterPrime(Array):
# #     return [i for i in Array if isPrime(i)]

# # a = [2,3,4,5,6,7,8]
# # print(filterPrime(a))  


# # def frequency(arr):
# #     freq = {}
# #     for i in arr:
# #         if i in freq:
# #             freq[i] += 1
# #         else:
# #             freq[i] = 1
# #     return freq

# # a = "babu"
# # print(frequency(a))

# # def firstNonRepetative(arr):
# #     freq =  {}

# #     for i in arr:
# #         if i in freq:
# #             freq[i] += 1
# #         else:
# #              freq[i] = 1

# #     for i in freq:
# #         if freq[i] == 1:
# #             return i
    
# # a = 'aabbdcccefg'
# # print(firstNonRepetative(a))


# # def Addition(l1, l2):
# #     result = []
# #     carry = 0
# #     i = 0

# #     while i < len(l1) or i < len(l2) or carry:
# #         x = l1[i] if i < len(l1) else 0
# #         y = l2[i] if i < len(l2) else 0

# #         z = x + y + carry

# #         result.append(z%10)
# #         carry = z//10

# #         i += 1

# #     return result

# # a = [1,2,3]
# # b = [4,6,7]

# # print(Addition(a,b))



# def Add(l1,l2):
#     result = []
#     carry = 0
#     i = len(l1) -1
#     j = len(l2) - 1

#     while i > -1 or j > -1 or carry:
#         x = l1[i] if i > -1 else 0
#         y = l2[j] if j > -1 else 0

#         z = x + y + carry

#         result.append(z%10)
#         carry = z//10

#         i -= 1
#         j -= 1

#     return result[::-1]

# a = [1,2,3]
# b = [8,7,7]
# print(Add(a,b))


# def Sub(l1,l2):
#     result = []
#     i = len(l1) -1
#     j = len(l2) -1

#     while i > -1 :
#         x = l1[i]
#         y = l2[j] if j > -1 else 0

#         if x < y:
#             x = x + 10
#             l1[i-1] -= 1

#         result.append(x-y)

#         i -= 1
#         j -= 1

#     return result[::-1]

# a = [9,9,9,9]
# b = [1,2,3,4]

# print(Sub(a,b))



# def Missing(arr):
#     Total = (arr[len(arr)-1] * (arr[len(arr)-1] +1) ) //2
#     Sum = sum(arr)
#     return Total - Sum

# a = [1,2,3,5]
# print(Missing(a))         max_val = max(arr)


# def MissingNat(arr):
#     Set = set()
#     for i in range(1,max(arr)+1):
#         Set.add(i)
#     List = []
#     for i in Set:
#         if i not in arr:
#             List.append(i)
#     return List

# a = [1,2,3,7,23,10,16,4,10]
# print(MissingNat(a))


# def firstrepeat(arr):
#     Set = set()
#     for i in arr:
#         if i in Set:
#             return i
#         Set.add(i)
#     return -1

# arr = [10, 5, 3, 4, 3, 5, 6]
# print(firstrepeat(arr))

# def rightRotation(arr,k):
#     n = len(arr)
#     k = k%n

#     return arr[-k:] + arr[:-k]

# arr = [1,2,3,4,5]
# k = 2
# print(rightRotation(arr,k))


# def palindrome(n):
#     temp = n
#     rem = 0
#     reverse = 0

#     while n!=0:
#         rem = n%10
#         reverse = rem + reverse*10
#         n = n//10

#     return reverse == temp

# print(palindrome(123454321))

# arr = [1,2,2,3,1,4,3]
# # Output: [1,2,3,4]


# def removeDuplicates(arr):
#     seen = set()
#     result = []
#     for i in arr:
#         if i not in seen:
#             seen.add(i)
#             result.append(i)
#     return result

# arr = [1,2,2,3,1,4,3]
# print(removeDuplicates(arr))


# arr = [10, 5, 8, 20, 3]
# Output: 10

# def secondHigh(arr):
#     first = second = -float('inf')

#     for x in arr:
#         if x > first:
#             second = first
#             first = x
#         elif first > x > second:
#             second = x
#     return second if second != -float('inf') else None

# arr = [12,98,76,45,89,34,12]
# print(secondHigh(arr))


# def twoNum(arr, target):
#     seen = {}

#     for i, num in enumerate(arr):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement],i]
#         seen[num] = i
#     return []

# a = [2,7,8,10]
# target = 9

# print(twoNum(a,target))


# List = []
# for i in range(2,36):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         List.append(i)

# print(List,len(List))


def palindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if not s[left].isalnum():
            left += 1 
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True

a = 'Racecar'
print(palindrome(a))



# def MaxSubArray(arr, k):
#     left = 0
#     right = k
#     high = 0

#     while right < len(arr):
#         high = max(high,sum(arr[left:right]))
#         left += 1
#         right += 1
#     return high


# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# print(MaxSubArray(arr,k))
# # Output: 9   (subarray [5,1,3])


# a = [1,2,3,4,5]

# a += [6]
# print(a)

# print(a[-6])

# def maxSubArray(arr,k):
#     Window = sum(arr[:k])
#     MaxSum = 0

#     for i in range(k,len(arr)):
#         Window += arr[i]
#         Window -= arr[i-k]

#         MaxSum = max(MaxSum,Window)
#     return MaxSum

# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# print(maxSubArray(arr,k))
# Output: 9   (subarray [5,1,3])



# def longest(string):
#     left = 0
#     Max = 0
#     seen = set()
#     for right in range(len(string)):
#         while string[right] in seen:
#             seen.remove(string[left])
#             left += 1
#         seen.add(string[right])

#         Max = max(right - left + 1 , Max)
#     return Max

# a  = "abcabcbb"
# print(longest(a))

# stack = []
# print(not stack)

# 
# def balanced(brackets):
#     stack = []
#     pairs = {']':'[','}':'{',')':'('}
#     for i in brackets:
#         if i in pairs:
#             if not stack or stack.pop() != pairs[i]:
#                 return False
#         else:
#             stack.append(i)
#     return True


# def same(arr):
#     pass


# a = [1,2,3,4,5]

# astrs = ["flower", "flow", "flight"]
# Output: "fl"

# def longsub(arr):
#     left = 0
#     Max = 0
#     seen = set()
#     for right in range(len(arr)-1):
#         while arr[right] in seen:
#             seen.remove(arr[left])
#             left += 1
#         seen.add(arr[right])
#         Max = max(right-left+1,Max)

#     return Max

# strs = ["flower", "flow", "flight"]
# # Output: "fl"
# print(strs)
# print(sorted(strs))

def longestSubString(words):
    if not words:
        return ""
    
    words.sort()

    first = words[0]
    last = words[-1]

    seen = ""

    for i in range(len(first)):
        if i < len(last) and first[i]==last[i]:
            seen += first[i]
    return seen

strs = ["flower", "flow", "flight"]
print(longestSubString(strs))


def count(string):
    seen = {}
    for i in string:
        if i in seen:
            seen[i] +=1
        else:
            seen[i] = 1
    result =""
    for item,freq in seen.items():
        result += f"{item}{freq}"
    return result
s = 'aaabbc'
print(count(s))


def Sum(arr,start,end):
    return sum(arr[start:end+1])
arr = [1, 2, 3, 4, 5]
print(Sum(arr,1,3))


# ----------------

def buildPrefix(arr):
    prefix = [0]
    for x in arr:
        prefix.append(prefix[-1] + x)
    return prefix

arr = [1,2,3,4,5]
prefix = buildPrefix(arr)
print(prefix)

def rangeSum(prefix, l, r):
    return prefix[r+1] - prefix[l]

print(rangeSum(prefix,1,3))  # 9


def sumExceptSelf(arr):
    n = len(arr)
    res = [0]*n
    left = 0
    right = 0
    '''
    res = [0,0,0,0]

    res[i] = 0
    left = 0 + 1

    res = [0,0,0,0]

    res[i] = 1
    left = 1 + 2 = 3

    res = [0,1,0,0]

    i = 2
    res[i] = 3
    left = 3 + 3 = 6

    res = [0,1,3,0]

    res[i] = 6
    left = 6 + 4 = 10

    res = [0,1,3,6]

    res[3] = 6 + 0 = 6
    right = 0 + 4 = 4
    res = [0,1,3,6]

    res[2] = 3 + 4 = 7
    right = 4 + 3 = 7
    res = [0,1,7,6]

    res[1] = 1 + 7 = 8
    right = 7 + 2 = 9
    res = [0, 8,7,6]

    res[0] = 0 + 9 = 9
    right = 9 + 1 = 10
    res = [9,8,7,6]

    '''

    for i in range(n):
        res[i] = left 
        left += arr[i]

    for i in range(n-1,-1,-1):
        res[i] += right
        right += arr[i]

    return res

a = [1,2,3,4]
print(sumExceptSelf(a))



def findWithTwoPointer(arr,find):
    left = 0
    right = len(arr)-1

    while left <= right:
        if arr[left] == find: 
            return left
        left += 1
        if arr[right]==find:
            return right
        right -= 1
    return None

a = [56,78,12,77,100,34,98,23,90]
find = 100
print(findWithTwoPointer(a,find))


# move zeros to end

a = [0,12,45,0,0,56]

def moveZerosToEnd(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[pos] = arr[pos],arr[i]
            pos += 1            
    return arr

print(moveZerosToEnd(a))


def binarySearch(arr,target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] <  target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [2, 5, 8, 12, 16, 23, 38]
print(binarySearch(arr, 16))


