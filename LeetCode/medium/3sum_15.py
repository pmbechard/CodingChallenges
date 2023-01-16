"""
15. 3Sum
https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                num_sum = nums[i] + nums[l] + nums[r]
                if num_sum == 0 and [nums[i], nums[l], nums[r]] not in results:
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif num_sum > 0:
                    r -= 1
                else:
                    l += 1
        return results
