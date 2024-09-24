"""
3280. Convert Date to Binary
https://leetcode.com/problems/convert-date-to-binary/description/
"""


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join([bin(int(i))[2:] for i in date.split('-')])
