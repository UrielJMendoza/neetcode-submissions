class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        #we make k = 0 to have are starting pointer 
        #we loop through len of nums 

        for i in range(len(nums)):
            #checking if nums at index i is not equal to var
            #finding all nums we want to stay
            if nums[i] != val:

                nums[k] = nums[i]
                k+=1
                #then if we want it to stay  we put it at nums[k] pointer
                # then we slide k over one
        return k
        # then we return k
        