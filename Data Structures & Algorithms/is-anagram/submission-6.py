class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

#declare 2 empty hash key value pair
        CountS = {}
        CountT = {}

# check if lens for strings if not same return cant be pair
        if len(s) != len(t):
            return False
         
# look through s and i for both and count freqeucny of numbers and map value with freqeucny
        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i],0)
            CountT[t[i]] = 1 + CountT.get(t[i],0)
            # so stored as key: "a" , Value: '1"
            #key 'd' ,val ' 3'


        for c in CountS:
            if CountS[c] != CountT.get(c,0):
                return False
        return True

        
        