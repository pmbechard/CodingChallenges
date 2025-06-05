"""
2027. Minimum Moves to Convert String
https://leetcode.com/problems/minimum-moves-to-convert-string/
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        s = list(s)
        output = 0
        for i in range(len(s)):
            if s[i] == 'X':
                for j in range(i, min(len(s), i + 3)):
                    s[j] = 'O'
                output += 1
        return output
