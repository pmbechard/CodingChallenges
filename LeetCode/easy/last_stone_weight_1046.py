"""
1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones[-2]
            y = stones[-1]
            if x == y:
                stones = stones[:-2]
            else:
                stones = stones[:-1]
                stones[-1] = y - x
        return stones[0] if len(stones) > 0 else 0
