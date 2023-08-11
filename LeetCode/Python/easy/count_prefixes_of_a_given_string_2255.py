"""
2255. Count Prefixes of a Given String
https://leetcode.com/problems/count-prefixes-of-a-given-string/
"""


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if s.find(word) == 0:
                count += 1
        return count
