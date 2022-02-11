"""
27. Remove Element
https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums, val):
        if not nums or all(num == val for num in nums):
            return 0
        nums.sort(key=lambda x: x == val)
        print(nums)
        return len(nums) - nums.count(val)


solution = Solution()
print(solution.removeElement([3, 2, 2, 3], 3))          # 2, [2,2,_,_]
print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))     # 5, [0,1,4,0,3,_,_,_]
print(solution.removeElement([1], 1))                   # 0, []
print(solution.removeElement([3, 3], 3))                # 0, []
print(solution.removeElement([4, 5], 5))                # 1, [4]
