"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return
        elif n == len(nums1) or all(num != 0 for num in nums1):
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return

        nums1_copy = nums1[:][:m]
        nums1_index = 0
        nums1_copy_index = 0
        nums2_index = 0

        for i in range(m + n):
            if not nums1_copy_index < len(nums1_copy):
                nums1[nums1_index] = nums2[nums2_index]
                nums1_index += 1
                nums2_index += 1
            elif not nums2_index < len(nums2):
                nums1[nums1_index] = nums1_copy[nums1_copy_index]
                nums1_index += 1
                nums1_copy_index += 1
            else:
                if nums1_copy[nums1_copy_index] < nums2[nums2_index]:
                    nums1[nums1_index] = nums1_copy[nums1_copy_index]
                    nums1_index += 1
                    nums1_copy_index += 1
                else:
                    nums1[nums1_index] = nums2[nums2_index]
                    nums1_index += 1
                    nums2_index += 1
