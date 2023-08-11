"""
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/
"""


class Solution:
    def numJewelsInStones(self, jewels, stones):
        result = 0
        for stone in stones:
            if stone in jewels:
                result += 1
        return result
