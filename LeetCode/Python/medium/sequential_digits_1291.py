"""
1291. Sequential Digits
https://leetcode.com/problems/sequential-digits/
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num_digits = len(str(low))
        current = self.get_start(num_digits)

        while current < low:
            current, num_digits = self.get_next(current, num_digits)

        output = []
        while current <= high:
            output.append(current)
            current, num_digits = self.get_next(current, num_digits)
        return output

    def get_start(self, num_digits: int) -> int:
        start = 0
        for i in range(1, num_digits + 1):
            start += i * (10 ** (num_digits - i))
        return start

    def get_next(self, num: int, num_digits: int) -> int:
        num += int('1' * num_digits)
        if len(str(num)) > num_digits or '0' in str(num):
            num_digits += 1
            num = self.get_start(num_digits)
        return [num, num_digits]
