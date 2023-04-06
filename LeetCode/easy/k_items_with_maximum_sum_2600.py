"""
2600. K Items With the Maximum Sum
https://leetcode.com/problems/k-items-with-the-maximum-sum/
"""


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        result = min(k, numOnes)
        k -= numOnes
        if k > 0:
            k -= numZeros
        if k > 0:
            result -= min(k, numNegOnes)
        return result
