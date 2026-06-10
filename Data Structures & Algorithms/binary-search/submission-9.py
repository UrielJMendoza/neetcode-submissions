class Solution:
    def search(self, nums: List[int], target: int) -> int:

        mid =  (len(nums)//2)
        ## get mid of ordered list
        low = 0
        ##low to 0

        high = len(nums)-1

        ## high end of list
        while low <= high:
            if nums[mid] == target:
            #check if mid is target
                return mid
            elif target < nums[mid]:
            # if target is less then mid
            # mid is now high
                high = mid-1
                mid = (low + high)//2


            elif target > nums[mid]:
                low = mid +1
                mid = (high+low)//2
        return -1
            
        



        
        