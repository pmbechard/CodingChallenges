"""
2486. Append Characters to String to Make Subsequence
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_index = 0
        for s_index in range(len(s)):
            if t_index == len(t):
                break
            if s[s_index] == t[t_index]:
                t_index += 1
        return len(t) - t_index
