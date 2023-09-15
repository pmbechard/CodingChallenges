"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = dict()
        for i in range(len(nums)):
            prev_index = dic.get(nums[i], None)
            if prev_index != None and abs(prev_index - i) <= k:
                return True
            else:
                dic[nums[i]] = i
        return False
