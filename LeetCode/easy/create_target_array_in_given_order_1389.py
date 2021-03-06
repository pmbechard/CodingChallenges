"""
1389. Create Target Array in the Given Order
https://leetcode.com/problems/create-target-array-in-the-given-order/
"""


class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target
