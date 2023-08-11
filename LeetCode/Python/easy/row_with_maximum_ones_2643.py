"""
2643. Row With Maximum Ones
https://leetcode.com/problems/row-with-maximum-ones/
"""


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        output = None
        for i, v in enumerate(mat):
            if output == None or sum(v) > output[1]:
                output = [i, sum(v)]
        return output
