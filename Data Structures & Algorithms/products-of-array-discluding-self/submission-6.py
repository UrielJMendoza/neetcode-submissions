class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new = [0] * n
        prefix = 1
        for i in range(n):
            new[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            new[i] *= suffix
            suffix *= nums[i]
        return new