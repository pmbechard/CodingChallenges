"""
1662. Check If Two String Arrays are Equivalent
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
"""


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_str = ""
        word2_str = ""
        longest_arr = max(len(word1), len(word2))
        for i in range(longest_arr):
            if i < len(word1):
                word1_str += word1[i]
            if i < len(word2):
                word2_str += word2[i]
        return word1_str == word2_str
