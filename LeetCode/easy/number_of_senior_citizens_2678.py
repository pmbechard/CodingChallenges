"""
2678. Number of Senior Citizens
https://leetcode.com/problems/number-of-senior-citizens/
"""


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([i for i in details if int(i[-4: -2]) > 60])
