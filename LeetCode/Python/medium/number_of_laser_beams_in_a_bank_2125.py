"""
2125. Number of Laser Beams in a Bank
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
"""


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # result = 0
        # operand_1 = 0
        # operand_2 = 0
        # for i in bank:
        #     if operand_1 == 0:
        #         operand_1 = i.count("1")
        #     elif operand_2 == 0:
        #         operand_2 = i.count("1")
        #     if operand_1 != 0 and operand_2 != 0:
        #         result += operand_1 * operand_2
        #         operand_1 = operand_2
        #         operand_2 = 0
        # return result

        prev = result = 0
        for row in bank:
            curr = row.count('1')
            if curr == 0:
                continue
            elif prev == 0:
                prev = curr
            else:
                result += row.count('1') * prev
                prev = curr
        return result
