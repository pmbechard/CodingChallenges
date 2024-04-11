"""
3090. Maximum Length Substring With Two Occurrences
https://leetcode.com/problems/maximum-length-substring-with-two-occurrences
"""


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = r = max_len = 0
        freqs = {s[l]: 1}

        while r < len(s) - 1:
            r += 1
            freqs[s[r]] = freqs.get(s[r], 0) + 1

            if freqs[s[r]] <= 2 and r - l + 1 > max_len:
                max_len = r - l + 1

            while freqs[s[r]] == 3:
                freqs[s[l]] -= 1
                if freqs[s[l]] == 0:
                    del freqs[s[l]]
                l += 1

        return max_len
