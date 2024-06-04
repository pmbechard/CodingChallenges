"""
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_set = set()
        counter = dict()
        total = 0
        for c in s:
            counter[c] = counter.get(c, 0) + 1
            if counter[c] % 2 == 1:
                odd_set.add(c)
            else:
                odd_set.remove(c)
            total += 1
        return total - len(odd_set) + (1 if len(odd_set) else 0)
