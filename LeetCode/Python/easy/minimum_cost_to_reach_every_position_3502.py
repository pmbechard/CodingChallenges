"""
3502. Minimum Cost to Reach Every Position
https://leetcode.com/problems/minimum-cost-to-reach-every-position/
"""


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        prev_min = cost[0]
        i = 0
        while i < len(cost):
            if cost[i] > prev_min:
                cost[i] = prev_min
            else:
                prev_min = cost[i]
            i += 1
        return cost
