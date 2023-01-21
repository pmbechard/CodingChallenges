"""
1507. Reformat Date
https://leetcode.com/problems/reformat-date/
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        date = date.split(' ')
        return '{}-{:02d}-{:02d}'.format(date[2], MONTHS.index(date[1]) + 1, int(date[0][:-2]))
