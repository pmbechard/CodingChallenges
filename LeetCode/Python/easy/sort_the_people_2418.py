"""
2418. Sort the People
https://leetcode.com/problems/sort-the-people
"""

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = []
        while heights:
            i = heights.index(max(heights))
            result.append(names[i])
            del heights[i]
            del names[i]
        return result
