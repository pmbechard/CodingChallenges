"""
398. Random Pick Index
https://leetcode.com/problems/random-pick-index/
"""


from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_map = {}
        for v, k in enumerate(nums):
            if self.nums_map.get(k):
                self.nums_map[k].append(v)
            else:
                self.nums_map[k] = [v]

    def pick(self, target: int) -> int:
        return self.nums_map[target][randint(0, len(self.nums_map[target]) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
