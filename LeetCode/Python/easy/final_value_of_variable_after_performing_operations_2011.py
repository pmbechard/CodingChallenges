"""
2011. Final Value of Variable After Performing Operations
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
"""


class Solution:
    def finalValueAfterOperations(self, operations):
        return 0 - str(operations).count('-') // 2 + str(operations).count('+') // 2
