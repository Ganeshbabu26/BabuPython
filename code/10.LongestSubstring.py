def longest(string):
    left = 0
    Max = 0
    Set = set()
    start = 0

    for right in range(len(string)):
        while string[right] in Set:
            Set.remove(string[left])
            left += 1

        Set.add(string[right])

        if right - left + 1 > Max:
            Max = right - left + 1
            start = left
            end = Max

    return string[start:start+end]

a = "fwefree"
print(longest(a))