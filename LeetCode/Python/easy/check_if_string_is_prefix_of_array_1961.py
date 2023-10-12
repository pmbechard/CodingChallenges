"""
1961. Check If String Is a Prefix of Array
https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
"""


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ''
        i = 0
        while len(prefix) < len(s) and i < len(words):
            prefix += words[i]
            i += 1
        return prefix == s
