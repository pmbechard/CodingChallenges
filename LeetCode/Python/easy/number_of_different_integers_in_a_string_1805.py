"""
1805. Number of Different Integers in a String
https://leetcode.com/problems/number-of-different-integers-in-a-string/
"""


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num = ''
        num_set = set()
        for i in word:
            if i.isnumeric():
                num += i
            elif num:
                num_set.add(int(num))
                num = ''
        if num:
            num_set.add(int(num))
        return len(num_set)
