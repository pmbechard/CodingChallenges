"""
2176. Count Equal and Divisible Pairs in an Array
https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
"""

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] == nums[j] and (i * j) % k == 0:
                    if sorted([i, j]) not in result:
                        result.append(sorted([i, j]))
        return len(result)
