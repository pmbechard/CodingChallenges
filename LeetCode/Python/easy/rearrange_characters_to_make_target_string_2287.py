"""
2287. Rearrange Characters to Make Target String
https://leetcode.com/problems/rearrange-characters-to-make-target-string/
"""


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        min_occ = None
        for letter in set(target):
            occ = max(0, s.count(letter) // target.count(letter))
            if min_occ is None or occ < min_occ:
                min_occ = occ
        return min_occ
