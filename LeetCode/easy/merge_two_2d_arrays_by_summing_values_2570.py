"""
2570. Merge Two 2D Arrays by Summing Values
https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
"""


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        results = {}
        len_1 = len(nums1)
        len_2 = len(nums2)

        for i in range(max(len_1, len_2)):
            if i < len_1:
                results[nums1[i][0]] = results.get(nums1[i][0], 0) + nums1[i][1]
            if i < len_2:
                results[nums2[i][0]] = results.get(nums2[i][0], 0) + nums2[i][1]

        output = []
        for k, v in results.items():
            output.append([k, v])

        return sorted(output, key=lambda x: x[0])
