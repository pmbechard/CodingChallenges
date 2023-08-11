"""
2243. Calculate Digit Sum of a String
https://leetcode.com/problems/calculate-digit-sum-of-a-string/
"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s_list = []
            for i in range(0, len(s), k):
                s_list.append(s[i:i + k])
            for j in range(len(s_list)):
                s_list[j] = str(sum([int(x) for x in s_list[j]]))
            s = ''.join(s_list)
        return s
