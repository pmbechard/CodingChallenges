"""
1652. Defuse the Bomb
https://leetcode.com/problems/defuse-the-bomb/
"""


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0] * len(code)
        code = code * 3
        results = []
        length = len(code)
        for i in range(length//3, length-length//3):
            if k < 0: results.append(sum(code[i-abs(k):i]))
            if k > 0: results.append(sum(code[i+1:i+k+1]))
        return results
