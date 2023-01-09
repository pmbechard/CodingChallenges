"""
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        sorted_set = set(sorted(arr))
        count = []
        for num in sorted_set:
            current_count = arr.count(num)
            if current_count in count:
                return False
            count.append(current_count)
        return True
