class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ##
        left = 0
        arraylens = []
        counter = 0


        for right in range(len(nums)):
            
            counter += nums[right]

            while counter >= target:
                arraylens.append(right-left+1)
                counter -= nums[left]
                left += 1
                


        if not arraylens:
            return 0


        return min(arraylens)

        
        