class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        Frequency = {}
        threshold = len(nums) / 3
        majorElement = []

        for i in range(len(nums)):
            if nums[i] not in Frequency:
                Frequency[nums[i]] = 1
            else:
                Frequency[nums[i]] += 1
        #have freqency in hash map and created threshold value
        for key in Frequency:
            if Frequency[key] > threshold:
                majorElement.append(key)
        return majorElement

        
        