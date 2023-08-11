"""
2446. Determine if Two Events Have Conflict
https://leetcode.com/problems/determine-if-two-events-have-conflict/
"""


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        times = [self.convert(x) for x in event1 + event2]
        return (times[2] >= times[0] and times[2] <= times[1]) or (times[3] >= times[0] and times[3] <= times[1]) or (
                times[0] >= times[2] and times[0] <= times[3]) or (times[1] >= times[2] and times[1] <= times[3])

    def convert(self, s):
        return float(f'{s[:2]}.{s[3:]}')
