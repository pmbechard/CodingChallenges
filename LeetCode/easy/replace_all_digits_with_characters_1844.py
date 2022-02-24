"""
1844. Replace All Digits with Characters
https://leetcode.com/problems/replace-all-digits-with-characters/
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            if s[i].isnumeric():
                result += chr(ord(s[i-1]) + int(s[i]))
            else:
                result += s[i]
        return result
