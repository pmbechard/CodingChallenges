"""
2760. Longest Even Odd Subarray With Threshold
https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/
"""


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        curr_count = max_count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                curr_count = 1
                prev_is_even = True
                for j in range(i + 1, len(nums)):
                    if prev_is_even and nums[j] % 2 != 0 and nums[j] <= threshold:
                        curr_count += 1
                        prev_is_even = False
                    elif not prev_is_even and nums[j] % 2 == 0 and nums[j] <= threshold:
                        curr_count += 1
                        prev_is_even = True
                    else:
                        break
                if curr_count > max_count:
                    max_count = curr_count
        return max_count
