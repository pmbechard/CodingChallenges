"""
2785. Sort Vowels in a String
https://leetcode.com/problems/sort-vowels-in-a-string/
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        found, indices = [], []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                found.append(s[i])
                indices.append(i)
        found.sort()
        for i in range(len(found)):
            s = s[:indices[i]] + found[i] + s[indices[i] + 1:]
        return s
