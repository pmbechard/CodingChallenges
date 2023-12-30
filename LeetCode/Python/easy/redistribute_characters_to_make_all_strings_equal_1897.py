"""
1897. Redistribute Characters to Make All Strings Equal
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
"""


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        num_words = len(words)
        freqs = Counter(''.join(words))
        for freq in freqs.values():
            if freq % num_words != 0:
                return False
        return True
