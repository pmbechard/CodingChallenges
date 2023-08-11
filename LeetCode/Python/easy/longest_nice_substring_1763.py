"""
1763. Longest Nice Substring
https://leetcode.com/problems/longest-nice-substring/
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        span = len(s)
        while span >= 1:
            start = 0
            while start + span <= len(s):
                substr = s[start: start + span]
                if self.is_nice_substring(substr):
                    return substr
                start += 1
            span -= 1
        return ''

    def is_nice_substring(self, s: str) -> bool:
        set_s = set(s)
        for letter in set_s:
            if letter.isupper() and letter.lower() not in set_s:
                return False
            elif letter.islower() and letter.upper() not in set_s:
                return False
        return True
