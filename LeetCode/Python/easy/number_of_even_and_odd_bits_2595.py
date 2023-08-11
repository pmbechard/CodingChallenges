"""
2595. Number of Even and Odd Bits
https://leetcode.com/problems/number-of-even-and-odd-bits/
"""


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bin_n = bin(n)[2:][::-1]
        output = [0, 0]
        for n in range(len(bin_n)):
            if bin_n[n] == '1':
                if n % 2 == 0:
                    output[0] += 1
                else:
                    output[1] += 1
        return output
