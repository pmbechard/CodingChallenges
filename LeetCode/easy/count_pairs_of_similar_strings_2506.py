"""
2506. Count Pairs Of Similar Strings
https://leetcode.com/problems/count-pairs-of-similar-strings/
"""


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = [set(x) for x in words]
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    count += 1
        return count
