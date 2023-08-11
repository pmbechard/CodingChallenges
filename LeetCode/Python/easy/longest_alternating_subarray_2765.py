"""
2765. Longest Alternating Subarray
https://leetcode.com/problems/longest-alternating-subarray/
"""


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        longest = -1
        for i in range(len(nums) - 1):
            num1, num2 = nums[i], nums[i + 1]
            if num2 - num1 != 1:
                continue
            current = 2
            index = i + 2
            while index < len(nums):
                if nums[index] == num1:
                    current += 1
                else:
                    break
                if index + 1 <= len(nums) - 1 and nums[index + 1] == num2:
                    current += 1
                else:
                    break
                index += 2
            if current > longest:
                longest = current
        return longest
