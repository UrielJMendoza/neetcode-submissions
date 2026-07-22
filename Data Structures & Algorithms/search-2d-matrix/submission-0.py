class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use binary search
        #we will look and make mid the middle of all arrays
        #low 0 high end of final array
        # move low or high if no return return false else return true

        lowArray = 0 
        highArray = len(matrix) - 1

        while lowArray <= highArray:
            ##use binary search 
            midArray = lowArray + (highArray-lowArray) // 2
            ## get mid array

            LowValue = 0
            HighValue = len(matrix[midArray]) - 1
            ##calc high val based on the array its in

            while LowValue <= HighValue:
                midIdx = LowValue + (HighValue-LowValue) // 2
                midValue = matrix[midArray][midIdx]
                if midValue == target:
                    return True

                elif midValue < target:
                    LowValue = midIdx + 1 
                
                elif midValue > target:
                    HighValue = midIdx - 1


            if matrix[midArray][0] < target:
                lowArray = midArray + 1


            else:
                highArray = midArray - 1



        return False