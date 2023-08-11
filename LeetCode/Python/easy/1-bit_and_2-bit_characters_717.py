"""
717. 1-bit and 2-bit Characters
https://leetcode.com/problems/1-bit-and-2-bit-characters/
"""


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if i == len(bits) - 1 and bits[i] == 0:
                return True
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return False
