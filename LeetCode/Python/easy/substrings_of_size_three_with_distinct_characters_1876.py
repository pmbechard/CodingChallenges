"""
1876. Substrings of Size Three with Distinct Characters
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            sub = s[i:i+3]
            if sub[0] != sub[1] and sub[1] != sub[2] and sub[0] != sub[2]:
                count += 1
        return count
