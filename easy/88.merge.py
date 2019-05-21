class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[n + m - 1] = nums1[m - 1]
                m = m - 1
            else:
                nums1[n + m - 1] = nums2[n - 1]
                n = n - 1
        if n > 0:
            nums1[:n] = nums2[:n]

# pythonic的做法就不写了，把两个列表加起来排序，在切片赋值回去
class Solution1:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2[0:n]
        nums1.sort()