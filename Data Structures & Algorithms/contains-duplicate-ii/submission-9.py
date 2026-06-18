class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 1
        # i is the anchor, j sweeps the window in front of it

        while i < len(nums):

            # j ran off the end OR left the window → advance i, reset j
            if j == len(nums) or abs(i - j) > k:
                i += 1
                j = i + 1
                continue

            # same value within distance k → found it
            if nums[i] == nums[j]:
                return True

            # window still valid, keep sweeping j
            j += 1

        return False