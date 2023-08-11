"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        elif target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        start = 0
        end = len(nums) -1
        while True:
            mid = (start + end) // 2
            if start == end - 1 and nums[start] < target < nums[end]:
                return end
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))      # 2
print(solution.searchInsert([1, 3, 5, 6], 2))      # 1
print(solution.searchInsert([1, 3, 5, 6], 7))      # 4
