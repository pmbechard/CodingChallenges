"""
1304. Find N Unique Integers Sum up to Zero
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""


class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []
        if n % 2 != 0:
            output.append(0)
        for i in range(1, n // 2 + 1):
            output.append(i)
            output.append(-1 * i)
        return output
