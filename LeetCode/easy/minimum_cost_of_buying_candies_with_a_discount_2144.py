"""
2144. Minimum Cost of Buying Candies With Discount
https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
"""


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        result = 0
        while len(cost) >= 3:
            result += cost[-1] + cost[-2]
            cost = cost[:-3]
        if cost:
            result += sum(cost)
        return result
