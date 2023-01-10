"""
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        for num in nums1:
            index = nums2.index(num)
            sub = [x for x in nums2[index + 1:] if x > num]
            if len(sub) == 0:
                results.append(-1)
            else:
                results.append(sub[0])
        return results

