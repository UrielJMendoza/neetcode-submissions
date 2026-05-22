class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        #so we wanna remove all in place duplicates right
        # problem when we remove them that value become nulls right so we might need three pointers 
        #probably 2 pointers checking nums[0] and nums[1] since its ascending order we can just check i f
        # they are not equal then increment both pointers
        # else we would have to remove pointer at nums[1] then move nums[1] over again and compare 
        # the only problem i can see hapening is a index problem as removing in place might mess up looping

        left = 0

        for right in range(len(nums)):
            if nums[left] == nums[right]:
                continue
            else:
                nums[left+1] = nums[right]
                left += 1
                
           
        return left + 1
                


        

            
