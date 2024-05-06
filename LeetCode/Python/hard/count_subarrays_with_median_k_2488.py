"""
2488. Count Subarrays With Median K
https://leetcode.com/problems/count-subarrays-with-median-k
"""


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        li = ri = nums.index(k)
        lv = rv = 0
        vals = {}
        count = 1

        while li > 0:
            li -= 1
            lv += 1 if nums[li] > k else -1
            vals[lv] = vals.get(lv, []) + [li]
            if 0 <= lv <= 1:
                count += 1

        while ri < len(nums) - 1:
            ri += 1
            rv += 1 if nums[ri] > k else -1
            if -rv in vals:
                count += len(vals[-rv])
            if -rv + 1 in vals:
                count += len(vals[-rv + 1])
            if 0 <= rv <= 1:
                count += 1

        return count
