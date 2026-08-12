class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #sorted array and a tarrget value return index if found else return where it would be 
        ## we can return where the pointers end up +1 or -1 where the missing value would be


        high = len(nums) - 1
        low = 0 

        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return mid
            


            elif nums[mid] < target:
                low = mid + 1



            elif nums[mid] > target:
                high = mid -1 
        return low 

        
        