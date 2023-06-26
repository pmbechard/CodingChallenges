"""
2744. Find Maximum Number of String Pairs
https://leetcode.com/problems/find-maximum-number-of-string-pairs/
"""


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        found = []
        for i in range(len(words)):
            if words[i][::-1] in words[:i] + words[i + 1:] and words[i] not in found:
                found += [words[i], words[i][::-1]]
        return len(found) // 2
