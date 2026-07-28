class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        count = 1
        current = nums[0]


        for i in range(len(nums)):

            if count < 0:
                current = nums[i]


            if current == nums[i]:
                count += 1

            else:
                count -= 1

        return current