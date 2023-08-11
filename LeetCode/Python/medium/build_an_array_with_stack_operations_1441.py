"""
1441. Build an Array With Stack Operations
https://leetcode.com/problems/build-an-array-with-stack-operations/
"""


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stream = list(range(1, n+1))
        target_i = 0
        ops = []
        for i in stream:
            if target_i == len(target):
                break
            elif i == target[target_i]:
                ops.append('Push')
                target_i += 1
            else:
                ops.append('Push')
                ops.append('Pop')
        return ops
