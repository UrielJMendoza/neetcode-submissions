# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        high = n
        
        mid = (l+high)//2

        result = guess(mid)

     


        while l <= high:
        
            mid = (l+high)//2
            result = guess(mid)

            if result == 0:
                return mid


            elif result == -1:
                high = mid -1

            elif result == 1:
                l = mid +1

        return mid

        