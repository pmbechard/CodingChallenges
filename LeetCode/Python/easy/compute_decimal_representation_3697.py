"""
3697. Compute Decimal Representation
https://leetcode.com/problems/compute-decimal-representation/
"""


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        output = []
        count = 0
        while n:
            r = n % 10
            n //= 10
            if r != 0:
                output.insert(0, r * 10 ** count)
            count += 1
        return output
