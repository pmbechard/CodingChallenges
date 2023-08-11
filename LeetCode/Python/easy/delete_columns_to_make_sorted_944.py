"""
944. Delete Columns to Make Sorted
https://leetcode.com/problems/delete-columns-to-make-sorted/
"""


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        cols = [[] for i in strs[0]]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                cols[j].append(strs[i][j])
        return len([i for i in range(len(cols)) if cols[i] != sorted(cols[i])])
