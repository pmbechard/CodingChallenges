"""
2833. Furthest Point From Origin
https://leetcode.com/problems/furthest-point-from-origin/
"""


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r_count, l_count, _count = moves.count('R'), moves.count('L'), moves.count('_')
        return r_count - l_count + _count if r_count > l_count else l_count - r_count + _count
