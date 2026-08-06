class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1

        current = 1
        nums.sort()

        if not nums:
            return 0

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] + 1 == nums[i+1]:
                current += 1
            else:
                if current > longest:
                    longest = current
                current = 1
                
        if current > longest:
            longest = current
        


        return longest