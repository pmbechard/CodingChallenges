"""
1217. Minimum Cost to Move Chips to The Same Position
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
"""


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = len([i for i in position if i % 2 == 0])
        return min(evens, len(position) - evens)
