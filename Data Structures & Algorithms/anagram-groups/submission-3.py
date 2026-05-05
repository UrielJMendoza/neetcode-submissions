class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping char count of each string to list of anagram

        for s in strs: # loop through each the list  Strings of strs
            count = [0] * 26  # create a array of a...z

            for c in s: # loop through each char count each character  in s 
                count[ord(c)- ord("a")] += 1 
                #this count the character freqeuncy
                #taking aski values of count index - a starting point like a = 1 b =2 
                # so d - a = 3 from a

            res[tuple(count)].append(s) #change to tuple to be non mutable 

        return list(res.values())

        




              

