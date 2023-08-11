"""
2125. Number of Laser Beams in a Bank
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
"""


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        operand_1 = 0
        operand_2 = 0
        for i in bank:
            if operand_1 == 0:
                operand_1 = i.count("1")
            elif operand_2 == 0:
                operand_2 = i.count("1")
            if operand_1 != 0 and operand_2 != 0:
                result += operand_1 * operand_2
                operand_1 = operand_2
                operand_2 = 0
        return result
