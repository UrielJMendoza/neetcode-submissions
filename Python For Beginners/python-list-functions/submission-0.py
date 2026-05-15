from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total

def get_min(nums: List[int]) -> int:
    smallest = nums[0]
    for i in range(len(nums)):
        if smallest == nums[i]:
            continue
        elif smallest > nums[i]:
            smallest = nums[i]
    return smallest

def get_max(nums: List[int]) -> int:
    biggest = nums[0]
    for i in range(len(nums)):
        if biggest == nums[i]:
            continue
        elif biggest < nums[i]:
            biggest = nums[i]
    return biggest


# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
