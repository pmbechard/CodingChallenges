"""
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter = len(word1) if len(word1) < len(word2) else len(word2)
        result = ""
        for i in range(shorter):
            result += word1[i] + word2[i]
        if len(word1) == shorter:
            result += word2[i + 1:]
        else:
            result += word1[i + 1:]
        return result

