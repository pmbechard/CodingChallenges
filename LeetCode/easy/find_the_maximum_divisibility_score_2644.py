"""
2644. Find the Maximum Divisibility Score
https://leetcode.com/problems/find-the-maximum-divisibility-score/
"""


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # max_div = [val, count]
        max_div = None
        for div in divisors:
            count = 0
            for num in nums:
                if num % div == 0:
                    count += 1
            if not max_div or count > max_div[1] or (count == max_div[1] and div < max_div[0]):
                max_div = [div, count]
        return max_div[0]
