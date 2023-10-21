"""
860. Lemonade Change
https://leetcode.com/problems/lemonade-change/
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        paid = dict()
        for bill in bills:
            if bill == 5:
                paid[5] = paid.get(5, 0) + 1
            elif bill == 10:
                if paid.get(5, 0) > 0:
                    paid[5] -= 1
                    paid[10] = paid.get(10, 0) + 1
                else:
                    return False
            else:
                change = 15
                if paid.get(10, 0) > 0:
                    paid[10] -= 1
                    change -= 10
                if paid.get(5, 0) >= change // 5:
                    paid[5] -= change // 5
                else:
                    return False
        return True
