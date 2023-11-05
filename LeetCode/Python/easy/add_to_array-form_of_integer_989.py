"""
989. Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/
"""


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        while k:
            current = k % 10
            k //= 10
            if i < 0:
                num.insert(0, 0)
                i = 0
            num[i] = num[i] + current
            if num[i] > 9:
                k += 1
                num[i] -= 10
            i -= 1
        return num
