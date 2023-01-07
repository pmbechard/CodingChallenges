"""
2520. Count the Digits That Divide a Number
https://leetcode.com/problems/count-the-digits-that-divide-a-number
"""

class Solution:
    def countDigits(self, num: int) -> int:
        return len([i for i in list(str(num)) if num % int(i) == 0])