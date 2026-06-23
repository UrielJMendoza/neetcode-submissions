class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        low = max(weights)
        #get low and high from weight value 
        high = sum(weights)

        #binary search

        while low < high:
            mid = low + (high-low) // 2
            ##calc mid no int overflow

            daysUsed = 1
            load = 0
            for w in weights:
                if load + w > mid:
                    daysUsed +=1
                    load = 0
                load += w
            if daysUsed <= days:
                high = mid
            else:
                low = mid + 1
        return low
                    




        