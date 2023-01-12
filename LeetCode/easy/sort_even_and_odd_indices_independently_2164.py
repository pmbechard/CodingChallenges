"""
2164. Sort Even and Odd Indices Independently
https://leetcode.com/problems/sort-even-and-odd-indices-independently/
"""


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted([nums[x] for x in range(len(nums)) if x % 2 == 0])
        odd = sorted([nums[x] for x in range(len(nums)) if x % 2 == 1], reverse=True)
        longer = even if len(even) > len(odd) else odd
        result = []
        for i in range(len(longer)):
            if i < len(even):
                result.append(even[i])
            if i < len(odd):
                result.append(odd[i])
        return result

