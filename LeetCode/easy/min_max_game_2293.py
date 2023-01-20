"""
2293. Min Max Game
https://leetcode.com/problems/min-max-game/
"""


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            temp = []
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    temp.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    temp.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = temp
        return nums[0]
