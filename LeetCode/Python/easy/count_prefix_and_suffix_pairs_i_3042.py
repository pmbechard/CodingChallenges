"""
3042. Count Prefix and Suffix Pairs I
https://leetcode.com/problems/count-prefix-and-suffix-pairs-i
"""


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count
