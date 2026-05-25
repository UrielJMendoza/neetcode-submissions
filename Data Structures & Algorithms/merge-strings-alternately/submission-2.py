class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:


        new = ""

        lens1 = len(word1)
        lens2 = len(word2)


        short = 0
        


        if lens1 >= lens2:
            short = lens2
            
        else:
            short = lens1
            

        

        for i in range(short):
            new += word1[i]
            new += word2[i]

        if lens1 >= lens2:
            for i in range(short, lens1):
                new += word1[i]
        else:
            for i in range(short, lens2):
                new += word2[i]



        return new


        