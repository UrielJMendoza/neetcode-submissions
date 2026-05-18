class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_idx = i  # assume current position is the minimum

            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:  # found a new minimum
                    min_idx = j              # just track the index

            # swap AFTER the inner loop, not inside it
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        return nums