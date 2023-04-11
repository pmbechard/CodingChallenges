"""
2404. Most Frequent Even Element
https://leetcode.com/problems/most-frequent-even-element/
"""


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        min_num = min_count = -1
        for num in set(nums):
            if num % 2 == 0:
                num_count = nums.count(num)
                if min_count == -1 or num_count > min_count:
                    min_num = num
                    min_count = num_count
                elif num_count == min_count and num < min_num:
                    min_num = num
        return min_num
