"""
697. Degree of an Array
https://leetcode.com/problems/degree-of-an-array/
"""


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freqs = dict()
        max_count = 0
        min_diff = 50_000
        for i in range(len(nums)):
            if nums[i] in freqs:
                current = freqs[nums[i]]
                current[0] += 1
                current[1][1] = i
            else:
                freqs[nums[i]] = current = [1, [i, i]]
            if current[0] > max_count:
                max_count = current[0]
                min_diff = current[1][1] - current[1][0] + 1
            elif current[0] == max_count:
                min_diff = min(min_diff, current[1][1] - current[1][0] + 1)
        return min_diff

        # freqs = dict()
        # maxes = [0, -1]
        # for num in nums:
        #     freqs[num] = freqs.get(num, 0) + 1
        #     if freqs[num] > maxes[0]:
        #         maxes[0] = freqs[num]
        #         maxes[1:] = [num]
        #     elif freqs[num] == maxes[0]:
        #         maxes.append(num)
        # min_diff = len(nums)
        # for num in maxes[1:]:
        #     left = nums.index(num)
        #     right = len(nums) - nums[::-1].index(num)
        #     min_diff = min(min_diff, right - left)
        # return min_diff

        # diff = len(nums)
        # max_count = 0
        # for num in set(nums):
        #     count = nums.count(num)
        #     if count > max_count:
        #         diff = (len(nums) - nums[::-1].index(num)) - nums.index(num)
        #         max_count = count
        #     elif count == max_count:
        #         diff = min(diff, (len(nums) - nums[::-1].index(num)) - nums.index(num))
        # return diff
