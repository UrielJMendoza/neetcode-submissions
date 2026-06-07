from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        my_deque = deque(nums)

        for i in range(k):

            right = my_deque.pop()
            my_deque.appendleft(right)
        
        nums[:] = my_deque
        """
        Do not return anything, modify nums in-place instead.
        """
        