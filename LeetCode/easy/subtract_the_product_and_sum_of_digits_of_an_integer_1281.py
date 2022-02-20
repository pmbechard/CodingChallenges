"""
1281. Subtract the Product and Sum of Digits of an Integer
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""


class Solution:
    def subtractProductAndSum(self, n):
        n_sum = 0
        n_product = 1
        for i in [int(i) for i in str(n)]:
            n_sum += i
            n_product *= i
        return n_product - n_sum
