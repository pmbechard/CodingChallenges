"""
2525. Categorize Box According to Criteria
https://leetcode.com/problems/categorize-box-according-to-criteria/
"""


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        results = []
        if max(length, width, height, mass) >= 10 ** 4 or length * width * height >= 10 ** 9:
            results.append("Bulky")
        if mass >= 100:
            results.append("Heavy")

        if len(results) == 2:
            return "Both"
        elif not results:
            return "Neither"
        else:
            return results[0]
