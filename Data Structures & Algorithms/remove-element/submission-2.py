class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 #pointer start at 0

        for i in range(len(nums)):
            #loop through index i of nums
            if nums[i] != val: #if nums at index i does not equal val

                nums[k] = nums[i] # replace nums at k with nums at i
                #k will always be in a valid spot since if dosent go only the outer index loops
                # and k will only increment and be filled with valid nums
                k += 1
#slide pointer over one
        return k # return k