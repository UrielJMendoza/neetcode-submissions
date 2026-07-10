class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        SeenNums = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in SeenNums:
                return [SeenNums[complement], i]
            SeenNums[nums[i]] = i




        