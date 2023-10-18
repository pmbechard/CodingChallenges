"""
2062. Count Vowel Substrings of a String
https://leetcode.com/problems/count-vowel-substrings-of-a-string/
"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word) < 5:
            return 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(len(word) - 4):
            j = i + 4
            while j < len(word) and word[j] in vowels:
                if set(word[i:j + 1]) == vowels:
                    count += 1
                j += 1
        return count
