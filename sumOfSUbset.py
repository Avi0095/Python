def find_subsets(nums, target, subset=[], index=0):
    # If target becomes 0, print the found subset
    if target == 0: # when sumofSUbset equal to target
        print(subset)
        return

    # If we go out of range or target becomes negative, stop
    if index == len(nums) or target < 0:
        return

    # Include current number
    find_subsets(nums, target - nums[index], subset + [nums[index]], index + 1)

    # Exclude current number
    find_subsets(nums, target, subset, index + 1)


# Main part
nums = [5, 10, 12, 13, 15, 18]
target = 30

print(f"Given set: {nums}")
print(f"Target sum: {target}")
print("Subsets that sum to target:")

find_subsets(nums, target)

