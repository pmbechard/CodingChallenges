"""
2389. Longest Subsequence With Limited Sum
https://leetcode.com/problems/longest-subsequence-with-limited-sum/
"""


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        result = []
        nums.sort()
        for query in queries:
            count, index = 0, 0
            while True:
                count += nums[index]
                index += 1
                if count > query:
                    result.append(index - 1)
                    break
                elif index == len(nums):
                    result.append(index)
                    break
        return result
