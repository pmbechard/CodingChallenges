"""
3075. Maximize Happiness of Selected Children
https://leetcode.com/problems/maximize-happiness-of-selected-children
"""


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        output = 0
        for i in range(k):
            output += max(0, happiness[i] - i)
        return output
