"""
1640. Check Array Formation Through Concatenation
https://leetcode.com/problems/check-array-formation-through-concatenation/
"""


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {v: i for i, v in enumerate(arr)}
        for piece in pieces:
            prev = None
            for p in piece:
                if prev is None and p in dic:
                    prev = dic[p] - 1
                if p not in dic or dic[p] - prev != 1:
                    return False
                prev = dic[p]
        return True
