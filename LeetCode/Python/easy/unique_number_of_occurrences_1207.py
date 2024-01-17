"""
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(set(counter.values())) == len(counter)
