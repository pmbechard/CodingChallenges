"""
1446. Consecutive Characters
https://leetcode.com/problems/consecutive-characters/
"""


class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        letter, count, max_count = None, 0, 1
        for i in s:
            if letter != i:
                count, letter = 1, i
            else:
                count += 1
                max_count = max(count, max_count)
        return max_count
