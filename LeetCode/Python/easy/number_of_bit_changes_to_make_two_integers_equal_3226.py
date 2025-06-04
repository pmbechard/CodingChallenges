"""
3226. Number of Bit Changes to Make Two Integers Equal
https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/
"""


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        binn, bink = bin(n)[2:], bin(k)[2:]
        max_len = max(len(binn), len(bink))
        binn, bink = f'{binn:0>{max_len}}', f'{bink:0>{max_len}}'
        output = 0
        for i in range(max_len):
            if binn[i] == '1' and bink[i] == '0':
                output += 1
            elif bink[i] == '1' and binn[i] == '0':
                return -1
        return output
