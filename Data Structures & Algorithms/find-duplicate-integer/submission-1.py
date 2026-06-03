class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
                if hashMap[nums[i]] > 1:
                    return nums[i]
        