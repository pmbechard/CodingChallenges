"""
1346. Check If N and Its Double Exist
https://leetcode.com/problems/check-if-n-and-its-double-exist/
"""


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            current = arr[:i] + arr[i + 1:]
            if arr[i] * 2 in current:
                return True
        return False
