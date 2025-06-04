"""
3483. Unique 3-Digit Even Numbers
https://leetcode.com/problems/unique-3-digit-even-numbers/
"""
import itertools


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        return len(set(i[0] * 100 + i[1] * 10 + i[2] for i in itertools.permutations(digits, 3) if
                       (i[0] * 100 + i[1] * 10 + i[2]) % 2 == 0 and 100 <= (i[0] * 100 + i[1] * 10 + i[2]) <= 999))

    # def __init__(self):
    #     self.combs = set()

    # def totalNumbers(self, digits: List[int]) -> int:
    #     self.traverse(digits, None)
    #     return len(self.combs)

    # def traverse(self, nums, num):
    #     if num and 100 <= int(num) <= 999:
    #         self.combs.add(num)
    #         return
    #     elif num and int(num) > 999:
    #         return

    #     for i in range(len(nums)):
    #         if num == None and nums[i] % 2 == 0:
    #             self.traverse(nums[:i] + nums[i + 1:],f'{nums[i]}')
    #         elif num != None:
    #             self.traverse(nums[:i] + nums[i + 1:], f'{nums[i]}{num}')
