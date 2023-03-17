"""
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        set_s = set(s)
        has_odd = False
        for i in set_s:
            curr_count = s.count(i)
            if curr_count % 2 == 0:
                count += curr_count
            elif not has_odd:
                count += curr_count
                has_odd = True
            else:
                count += curr_count - 1
        return count
