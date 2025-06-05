"""
2269. Find the K-Beauty of a Number
https://leetcode.com/problems/find-the-k-beauty-of-a-number/
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        snum = str(num)
        result = 0
        for i in range(0, len(snum) - k + 1):
            div = int(snum[i:i + k])
            if div != 0 and num % div == 0:
                result += 1
        return result
