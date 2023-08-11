"""
1684. Count the Number of Consistent Strings
https://leetcode.com/problems/count-the-number-of-consistent-strings/
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        allowed_list = list(allowed)
        for word in words:
            for allowed in allowed_list:
                word = word.replace(allowed, '')
            if not word:
                result += 1
        return result
