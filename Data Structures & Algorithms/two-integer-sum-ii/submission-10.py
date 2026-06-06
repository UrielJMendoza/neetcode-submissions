class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:



        ##loop through nums
        ## them 1 - target = new target 
        ## if we dont find target 2 -  target = new target 
        k=1
        for i in range(len(numbers)):
            for k in range(len(numbers)):
                missing = target - numbers[i]
                if numbers[k] == missing and numbers[i] < numbers[k]:
                    return [i+1, k+1]
                

            
        