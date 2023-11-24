"""
696. Count Binary Substrings
https://leetcode.com/problems/count-binary-substrings/
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        digit = None
        output = 0
        for i in range(len(s)):
            if s[i] == digit:
                count += 1
            else:
                digit = s[i]
                count = 1
            for j in range(i + 1, min(len(s), i + count + 1)):
                if s[j] == digit:
                    break
                output += 1
        return output
