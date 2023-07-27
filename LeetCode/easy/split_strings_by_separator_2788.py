"""
2788. Split Strings by Separator
https://leetcode.com/problems/split-strings-by-separator/
"""


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            split_words = word.split(separator)
            for split_word in split_words:
                if split_word:
                    result.append(split_word)
        return result
