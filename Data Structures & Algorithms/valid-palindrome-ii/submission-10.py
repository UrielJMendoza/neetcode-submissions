class Solution:
    def validPalindrome(self, s: str) -> bool:

        #current = 0
        cleanArray = []
        count = 0


        for i in range(len(s)):
            if s[i].isalnum():
                cleanArray.append(s[i].lower())
            else:
                continue
        

        leftPoint = 0
        rightPoint = len(cleanArray)-1

        while leftPoint < rightPoint:
            if cleanArray[leftPoint] == cleanArray[rightPoint]:
                leftPoint += 1
                rightPoint -= 1
            else:
                skipLeft  = cleanArray[leftPoint+1 : rightPoint+1]
                skipRight = cleanArray[leftPoint   : rightPoint]
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]

        return True