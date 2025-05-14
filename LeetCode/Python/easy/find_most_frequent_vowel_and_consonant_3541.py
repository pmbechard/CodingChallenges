"""
3541. Find Most Frequent Vowel and Consonant
https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
"""


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        chars = dict()
        max_con = max_vow = 0
        for c in s:
            chars[c] = chars.get(c, 0) + 1
            if c in vowels:
                max_vow = max(max_vow, chars[c])
            else:
                max_con = max(max_con, chars[c])
        return max_vow + max_con
