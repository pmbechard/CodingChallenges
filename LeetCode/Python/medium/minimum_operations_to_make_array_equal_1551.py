"""
1551. Minimum Operations to Make Array Equal
https://leetcode.com/problems/minimum-operations-to-make-array-equal/
"""


class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            centre = n - 1
        else:
            centre = n
        arr = [2 * i + 1 for i in range(centre)]
        l = 0
        r = 0
        for i in range(len(arr)):
            if i <= len(arr)//2:
                l += n - arr[i]
            else:
                r += arr[i] - n
        return l if l >= r else r
