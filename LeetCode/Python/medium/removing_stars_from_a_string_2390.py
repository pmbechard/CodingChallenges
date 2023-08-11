"""
2390. Removing Stars From a String
https://leetcode.com/problems/removing-stars-from-a-string/
"""


class Solution:
    def removeStars(self, s: str) -> str:
        result = ""
        for i in s:
            if i == '*':
                result = result[:-1]
            else:
                result += i
        return result
