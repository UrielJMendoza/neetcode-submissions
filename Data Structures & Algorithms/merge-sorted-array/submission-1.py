class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for i in range(m+n):
            if i >= m:
                nums1.pop()

        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()


        """
        Do not return anything, modify nums1 in-place instead.
        """
        