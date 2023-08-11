"""
503. Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = []
        len_nums = len(nums)
        for i in range(len_nums):
            counter = i + 1
            while counter % len_nums != i:
                curr = nums[counter % len_nums]
                if curr > nums[i]:
                    result.append(curr)
                    break
                counter += 1
            if counter % len_nums == i:
                result.append(-1)
        return result
