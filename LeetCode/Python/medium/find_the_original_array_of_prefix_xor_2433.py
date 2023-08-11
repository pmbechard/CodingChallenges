"""
2433. Find The Original Array of Prefix Xor
https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
"""


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i] ^ pref[i+1] for i in range(len(pref)-1)]
