"""
2185. Counting Words With a Given Prefix
https://leetcode.com/problems/counting-words-with-a-given-prefix/
"""


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for word in words:
            if word[:len(pref)] == pref:
                result += 1
        return result
