"""
1200. Minimum Absolute Difference
https://leetcode.com/problems/minimum-absolute-difference/
"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        results = []
        lowest_diff = arr[-1]
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            if diff < lowest_diff:
                results = [[arr[i - 1], arr[i]]]
                lowest_diff = diff
            elif diff == lowest_diff:
                results.append([arr[i - 1], arr[i]])
        return results
