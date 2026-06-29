class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ##thinking using sliding window
        ## have a extra array that we return sorted

        left = 0
        right = len(arr) - 1

        ## loop through vals
        ## use two pointers to narrow down the window to size k
        while right - left >= k:
            # compare distances to x from both ends
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
        
        # the window [left, right] now contains the k closest elements
        closeToValue = arr[left:right + 1]
        return closeToValue