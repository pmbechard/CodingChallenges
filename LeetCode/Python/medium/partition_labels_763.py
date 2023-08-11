"""
763. Partition Labels
https://leetcode.com/problems/partition-labels/
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        checked = []
        left = 0
        while left < len(s):
            right = self.last_index_of(s, left)
            i = left
            while i < right:
                if s[i] not in checked:
                    current_last = self.last_index_of(s, i)
                    checked.append(s[i])
                    if current_last > right:
                        right = current_last
                i += 1
            result.append(len(s[left:right + 1]))
            left = right + 1
        return result

    def last_index_of(self, s, i):
        return len(s) - 1 - s[::-1].index(s[i])
