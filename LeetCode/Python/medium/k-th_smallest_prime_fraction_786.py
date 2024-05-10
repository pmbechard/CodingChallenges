"""
786. K-th Smallest Prime Fraction
https://leetcode.com/problems/k-th-smallest-prime-fraction/
"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        dic = {}
        for n in range(len(arr) - 1):
            for d in range(n + 1, len(arr)):
                dic[arr[n] / arr[d]] = [arr[n], arr[d]]
        return dic[sorted(dic.keys())[k - 1]]
