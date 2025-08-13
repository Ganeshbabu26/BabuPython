import itertools

def multi_sum(nums, target):
    for count in range(2, len(nums) + 1):  # Try 2 numbers up to all numbers
        for combo in itertools.combinations(range(len(nums)), count):
            if sum(nums[i] for i in combo) == target:
                return list(combo)  # Return the first match
    return []  # No match found

# Example usage
print(multi_sum([2, 7, 11, 15], 9))   # [0, 1]  → 2 + 7 = 9
print(multi_sum([1, 2, 3], 6))        # [0, 1, 2] → 1 + 2 + 3 = 6
print(multi_sum([4, 5, 6, 7], 19))    # [1, 2, 3] → 5 + 6 + 7 = 18 (No, so tries other combos)
print(multi_sum([5, 5, 6, 7], 18))    # [1, 2, 3] → 5 + 6 + 7 = 18 (No, so tries other combos)