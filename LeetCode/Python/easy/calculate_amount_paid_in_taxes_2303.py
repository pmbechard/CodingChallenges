"""
2303. Calculate Amount Paid in Taxes
https://leetcode.com/problems/calculate-amount-paid-in-taxes/
"""


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = prev_bracket = 0
        for bracket in brackets:
            mini = min(bracket[0] - prev_bracket, income)
            taxes += mini * bracket[1] / 100
            income -= mini
            prev_bracket = bracket[0]
            if not income:
                break
        return taxes
