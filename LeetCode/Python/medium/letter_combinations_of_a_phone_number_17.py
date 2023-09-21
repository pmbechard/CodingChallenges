"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        elif len(digits) == 1:
            return list(letters[digits[0]])
        digit_letters = []
        for digit in digits:
            digit_letters.append(list(letters[digit]))
        combs = list(itertools.product(*digit_letters))
        return [''.join(i) for i in combs]
