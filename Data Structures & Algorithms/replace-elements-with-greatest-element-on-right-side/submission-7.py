class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:


        



        for i in range(len(arr)):
            currentMax = 0
            for k in range(i + 1, len(arr)):
               if arr[k] > currentMax:
                currentMax = arr[k]

                 
            arr[i] = currentMax



            

        arr[len(arr)-1] = -1

        return arr
            

                

        
        