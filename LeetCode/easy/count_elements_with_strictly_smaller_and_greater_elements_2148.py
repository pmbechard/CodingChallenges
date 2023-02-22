"""
2148. Count Elements With Strictly Smaller and Greater Elements
https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/
"""


class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(set(nums)) <= 2: return 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        while True:
            change = 0
            if nums[l] == nums[l + 1]:
                l += 1
                change += 1
            if nums[r] == nums[r - 1]:
                r -= 1
                change += 1
            if change == 0:
                break
        return max(0, r - l - 1)
