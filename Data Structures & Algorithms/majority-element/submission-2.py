class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        HighestCount = 0

        number = nums[0]
    
        for i in range(len(nums)):
            if HighestCount == 0:
                number = nums[i]
                
            if nums[i] == number:
                HighestCount +=1
            else:
                HighestCount -=1


        return number
                



        #