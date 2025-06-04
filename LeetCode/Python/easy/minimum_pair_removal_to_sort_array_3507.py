"""
3507. Minimum Pair Removal to Sort Array I
https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
"""


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        output = 0
        while not self.is_sorted(nums):
            nums = self.update(nums)
            output += 1
        return output

    def update(self, nums: List[int]) -> List[int]:
        min_sum = None
        idx = None
        for i in range(len(nums) - 1):
            curr = nums[i] + nums[i + 1]
            if min_sum == None or curr < min_sum:
                min_sum = curr
                idx = i
        return nums[:idx] + [min_sum] + nums[idx + 2:]

    def is_sorted(self, nums: List[int]) -> bool:
        prev = None
        for num in nums:
            if prev == None or prev <= num:
                prev = num
            else:
                return False
        return True
