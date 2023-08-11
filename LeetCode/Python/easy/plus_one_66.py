"""
66. Plus One
https://leetcode.com/problems/plus-one/
"""


class Solution:
    def plusOne(self, digits):
        str_digits = ""
        for digit in digits:
            str_digits += str(digit)
        int_digits = int(str_digits)
        int_digits += 1
        return list(str(int_digits))


solution = Solution()
solution.plusOne([1, 2, 3])         # [1, 2, 4]
solution.plusOne([4, 3, 2, 1])      # [4, 3, 2, 2]
solution.plusOne([9])               # [1, 0]
