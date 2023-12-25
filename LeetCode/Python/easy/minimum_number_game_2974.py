"""
2974. Minimum Number Game
https://leetcode.com/problems/minimum-number-game/
"""


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        i = 0
        output = []
        nums.sort()
        while nums:
            min1 = nums.pop(0)
            if nums:
                min2 = nums.pop(0)
                output.append(min2)
            output.append(min1)
        return output
