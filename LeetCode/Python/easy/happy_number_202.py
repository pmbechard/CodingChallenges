"""
202. Happy Number
https://leetcode.com/problems/happy-number/
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        answers = []
        str_n = str(n)
        while True:
            list_n = [int(n) ** 2 for n in str_n]
            answer = sum(list_n)
            if answer == 1:
                return True
            elif answer in answers:
                return False
            else:
                answers.append(answer)
                str_n = str(answer)
