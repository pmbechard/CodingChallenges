"""
2965. Find Missing and Repeated Values
https://leetcode.com/problems/find-missing-and-repeated-values/
"""


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freqs = Counter([col for row in grid for col in row])
        return [freqs.most_common(1)[0][0], set(range(1, len(freqs) + 2)).difference(freqs).pop()]
