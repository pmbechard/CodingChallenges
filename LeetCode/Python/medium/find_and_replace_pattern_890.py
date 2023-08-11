"""
890. Find and Replace Pattern
https://leetcode.com/problems/find-and-replace-pattern/description/
"""


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = self.getPattern(pattern)
        results = []
        for word in words:
            print(word, self.getPattern(word), pattern)
            if self.getPattern(word) == pattern:
                results.append(word)
        return results

    def getPattern(self, s):
        pattern_map = []
        pattern = []
        for i in s:
            if i in pattern_map:
                pattern.append(pattern_map.index(i))
            else:
                pattern.append(len(pattern_map))
                pattern_map.append(i)
        return pattern
