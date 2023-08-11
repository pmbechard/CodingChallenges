"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums):
        count = 0
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue
            nums[count] = nums[i]
            count += 1
        return count

    def removeDuplicates2(self, nums):
        """ Same output but not accepted on leetcode """
        nums_set = set(nums)
        k = len(nums_set)
        l = len(nums)
        nums = list(nums_set)
        for i in range(l - k):
            nums.append('')
        return k


solution = Solution()
print(solution.removeDuplicates([1, 1, 2]))                 # 2, [1, 2, _]
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))     # 5, [0,1,2,3,4,_,_,_,_,_]

print(solution.removeDuplicates2([1, 1, 2]))                 # 2, [1, 2, _]
print(solution.removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))     # 5, [0,1,2,3,4,_,_,_,_,_]
