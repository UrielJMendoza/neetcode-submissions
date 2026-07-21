class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #ok so we we need two pointers
        #we need to find max wTER FOR LEFT AND RIGHT 
        #probably have sum that has all the total values added up that are less than bo
        #both left and right 
        ## so calculate sum and compare max value 
        ## only update max and indices if greater than

        maxValue = 0

        left = 0 
        right = len(heights) - 1

        while left <= right:
            water = (right - left) * min(heights[left], heights[right])

            if water >= maxValue:
                maxValue = water

            if heights[left] <= heights[right]:
                left +=1

            elif heights[left] > heights[right]:
                right -=1
        return maxValue



        
        