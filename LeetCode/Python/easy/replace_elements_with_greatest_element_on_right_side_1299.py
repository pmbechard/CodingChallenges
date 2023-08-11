"""
1299. Replace Elements with Greatest Element on Right Side
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(1, len(arr)):
            result.append(max(arr[i:]))
        result.append(-1)
        return result
