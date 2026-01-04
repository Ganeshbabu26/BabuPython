def addtwonumbers(l1,l2):
    carry = 0
    result = []
    i = 0
    while i < len(l1) or i < len(l2) or carry:
        x = l1[i] if i < len(l1) else 0
        y = l2[i] if i < len(l2) else 0

        z = x + y + carry

        result.append(z%10)
        carry = z // 10

        i+=1
    return result
    
a = [1,2,3]
b = [5,6,7]

print(addtwonumbers(a,b))





# Add one

def addOne(l):
    result = []
    carry = 1
    i = len(l)-1
    while i>=0:
        x = l[i] if i >= 0 else 0
        z = x  + carry
        result.append(z%10)
        carry = z // 10

        i -= 1
    if carry:
        result.append(carry)

    return result[::-1]

a = [9,9,9]
print(addOne(a))























# class Solution:
#     def addTwoNumbers(self, l1, l2) :
#         carry = 0
#         result = []

#         i = 0
#         while i < len(l1) or i < len(l2) or carry:
#             x = l1[i] if i < len(l1) else 0
#             y = l2[i] if i < len(l2) else 0

#             total = x + y + carry
#             carry = total // 10
#             result.append(total % 10)

#             i += 1

#         return result

# s = Solution()
# a = [1,2,3]
# b = [5,6,7]
# print(s.addTwoNumbers(a,b))