"""
3074. Apple Redistribution into Boxes
https://leetcode.com/problems/apple-redistribution-into-boxes
"""


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        count = 0
        while apples > 0:
            apples -= capacity[count]
            count += 1
        return count
