"""
1208. Get Equal Substrings Within Budget
https://leetcode.com/problems/get-equal-substrings-within-budget/
"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        max_len = l = r = cost = 0
        while l < len(diffs):
            if cost <= maxCost:
                max_len = max(max_len, r - l)
                if r < len(diffs):
                    cost += diffs[r]
                    r += 1
                else:
                    cost -= diffs[l]
                    l += 1
            else:
                cost -= diffs[l]
                l += 1
        return max_len
