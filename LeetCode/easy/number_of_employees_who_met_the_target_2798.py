"""
2798. Number of Employees Who Met the Target
https://leetcode.com/problems/number-of-employees-who-met-the-target/
"""


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len([i for i in hours if i >= target])
