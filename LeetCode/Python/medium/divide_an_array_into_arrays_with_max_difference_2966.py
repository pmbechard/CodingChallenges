"""
2966. Divide Array Into Arrays With Max Difference
https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
"""


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0
        while i < len(nums):
            sub = nums[i: i + 3]
            if sub[2] - sub[0] > k:
                return []
            output.append(sub)
            i += 3
        return output
