"""
1694. Reformat Phone Number
https://leetcode.com/problems/reformat-phone-number/
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        result = ''
        index = 0
        length = len(number)
        while index < length:
            if length - index > 4:
                result += '-' + number[index:index + 3]
                index += 3
            elif length - index == 4:
                result += '-' + number[index:index + 2] + '-' + number[index + 2:]
                index += 4
            else:
                result += '-' + number[index:]
                index += length - index
        return result[1:]
