"""
1624. Largest Substring Between Two Equal Characters
https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        largest = -1
        for i in range(len(s)):
            last = len(s) - s[::-1].find(s[i]) - 1
            if i != last and last - i - 1 > largest:
                largest = last - i - 1
        return largest
