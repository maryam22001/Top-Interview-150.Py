1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        m + n = length of nums1
5        nums1 contains m valid elements + extra zeros
6        nums2 contains n elements
7        """
8
9        nums1[:] = sorted(nums1[:m] + nums2)