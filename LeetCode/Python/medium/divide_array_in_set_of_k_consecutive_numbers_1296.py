"""
1296. Divide Array in Sets of K Consecutive Numbers
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        while nums:
            for num in range(nums[0], nums[0] + k):
                try:
                    nums.remove(num)
                except ValueError:
                    return False
        return True
