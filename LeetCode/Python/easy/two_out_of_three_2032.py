"""
2032. Two Out of Three
https://leetcode.com/problems/two-out-of-three/
"""

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = []
        all_nums = set(nums1 + nums2 + nums3)
        for i in all_nums:
            count = 0
            if i in nums1:
                count += 1
            if i in nums2:
                count += 1
            if i in nums3:
                count += 1
            if count > 1:
                result.append(i)
        return result
