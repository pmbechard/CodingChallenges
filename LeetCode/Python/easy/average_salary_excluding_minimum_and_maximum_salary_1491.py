"""
1491. Average Salary Excluding the Minimum and Maximum Salary
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""


class Solution:
    def average(self, salary: List[int]) -> float:
        min_s = min(salary)
        max_s = max(salary)
        salaries = [i for i in salary if i != min_s and i != max_s]
        return sum(salaries) / len(salaries)
