"""
2053. Kth Distinct String in an Array
https://leetcode.com/problems/kth-distinct-string-in-an-array/
"""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = 0
        for i in arr:
            if arr.count(i) == 1:
                counter += 1
                if counter == k:
                    return i
        return ''
