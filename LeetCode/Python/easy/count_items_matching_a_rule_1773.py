"""
1773. Count Items Matching a Rule
https://leetcode.com/problems/count-items-matching-a-rule/
"""


class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        items_index = {'type': 0, 'color': 1, 'name': 2}
        index = items_index.get(ruleKey)
        counter = 0
        for item in items:
            if item[index] == ruleValue:
                counter += 1
        return counter
