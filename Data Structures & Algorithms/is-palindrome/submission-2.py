class Solution:
    def isPalindrome(self, s: str) -> bool:
        real_aplpha_num = []

        for i in range(len(s)):
            if s[i].isalnum():
                real_aplpha_num.append(s[i].lower())
            else:
                continue

#get rid of not aplha num char and puts it into new list 
#create left pointer and will make right pointer and converge to see if they equal
        leftPointer = 0
        rightPointer = len(real_aplpha_num)-1

        while leftPointer < rightPointer:
            if real_aplpha_num[leftPointer] == real_aplpha_num[rightPointer]:
                leftPointer +=1
                rightPointer -= 1
            else:
                return False
        return True


        
        
        
        