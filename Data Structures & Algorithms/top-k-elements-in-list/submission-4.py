class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        #we mapped freq with counted appearance values
        #how do we loop through to find k highest elements
        arraycounter = [] #create array of k spaces to store
        
        for i in range(k):
            highestfreq = 0 
            for key in freq:
                if freq[key] > highestfreq:
                    highestfreq = freq[key]
                    highestKey = key
                    
            # found first highest element now put in spot 
            arraycounter.append(highestKey)
            del freq[highestKey]
        return arraycounter
                
