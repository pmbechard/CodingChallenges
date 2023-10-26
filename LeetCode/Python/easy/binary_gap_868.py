"""
868. Binary Gap
https://leetcode.com/problems/binary-gap/
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]
        gap = 0
        for i in range(len(n)):
            if n[i] == '1':
                j = i + 1
                while j < len(n):
                    if n[j] == '1':
                        gap = max(j - i, gap)
                        break
                    j += 1
        return gap
