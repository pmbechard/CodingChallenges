"""
2586. Count the Number of Vowel Strings in Range
https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/
"""


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = 'aeiou'
        count = 0
        for word in words[left: right + 1]:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
        return count
