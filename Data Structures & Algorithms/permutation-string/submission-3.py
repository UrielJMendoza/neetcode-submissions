class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #create a limit for our sliding window of length s1
        limit = len(s1)
        # make a set to check if s2[i] in the set and within the range limit 
        hashcount = {}
        for i in range(len(s1)):
            if s1[i] not in hashcount:
                hashcount[s1[i]] = 1
            else:
                hashcount[s1[i]] += 1
        

        left = 0 
        window = {}

# if len s1 greater than lens2 then cannot be true

        if len(s1) > len(s2):
            return False

        #create a for loop to go through s2
        for right in range(len(s2)):

            
            if s2[right] not in window:
                window[s2[right]] = 1
            else:
                window[s2[right]] += 1 


            if right - left + 1 > limit:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left +=1

            if window == hashcount:
                return True
            


        return False


        