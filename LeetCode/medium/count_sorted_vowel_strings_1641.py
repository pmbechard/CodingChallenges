"""
1641. Count Sorted Vowel Strings
https://leetcode.com/problems/count-sorted-vowel-strings
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        nums = [n+x for x in range(1, 5)]
        prod = 1
        for num in nums:
            prod *= num
        return prod // 24
