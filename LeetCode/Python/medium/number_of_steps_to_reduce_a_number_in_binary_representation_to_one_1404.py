"""
1404. Number of Steps to Reduce a Number in Binary Representation to One
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
"""


class Solution:
    def numSteps(self, s: str) -> int:
        n = int(f'0b{s}', 2)
        steps = 0
        while n > 1:
            print(n)
            if n % 2 == 0:
                n //= 2
            else:
                n += 1
            steps += 1
        return steps
