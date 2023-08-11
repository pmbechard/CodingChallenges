"""
2138. Divide a String Into Groups of Size k
https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
"""


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s_list = [s[i:i+k] for i in range(0, len(s), k)]
        if len(s_list[-1]) < k:
            s_list[-1] += fill * (k - len(s_list[-1]))
        return s_list
