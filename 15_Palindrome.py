def palindrome(n):
    b = ""
    for i in range(len(n)-1,-1,-1):
        b += n[i]
    return b

n = input("Enter a word: ")
if n.lower() == palindrome(n).lower():
    print(n," is palindrome")